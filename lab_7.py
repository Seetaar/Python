import unittest
import requests
import sys
import io
import functools
from unittest.mock import patch, Mock


def logger(func=None, *, handle=sys.stdout):
    """
    декоратор logger
    """
    if func is None:
        return lambda f: logger(f, handle=handle)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        handle.write("Вызов функции\n")
        try:
            result = func(*args, **kwargs)
            handle.write(f"Результат: {result}\n")
            return result
        except Exception as e:
            handle.write(f"Ошибка: {e}\n")
            raise ValueError(str(e))

    return wrapper


@logger(handle=sys.stdout)
def get_currencies(currency_codes: list, url: str = "https://www.cbr-xml-daily.ru/daily_json.js",
                   handle=sys.stdout) -> dict:
    """
    Получает курсы валют с API Центробанка России.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        currencies = {}

        if "Valute" in data:
            for code in currency_codes:
                if code in data["Valute"]:
                    currencies[code] = data["Valute"][code]["Value"]
                else:
                    currencies[code] = f"Код валюты '{code}' не найден."
        return currencies

    except requests.exceptions.RequestException as e:
        handle.write(f"Ошибка при запросе к API: {e}\n")
        raise ValueError(f"Ошибка запроса: {e}")
    except ValueError as e:
        handle.write(f"Некорректный JSON: {e}\n")
        raise ValueError(f"Некорректный JSON: {e}")


MAX_R_VALUE = 1000


class TestGetCurrencies(unittest.TestCase):

    def setUp(self):
        self.stream = io.StringIO()
        @logger(handle=self.stream)
        def wrapped_get_currencies(currency_codes, url="https://www.cbr-xml-daily.ru/daily_json.js"):
            return get_currencies(currency_codes, url, handle=self.stream)
        self.wrapped = wrapped_get_currencies

    @patch('requests.get')
    def test_currency(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 75.5}
            }
        }
        mock_get.return_value = mock_response
        currency_list = ['USD']
        currency_data = self.wrapped(currency_list)
        self.assertIn('USD', currency_data)
        self.assertIsInstance(currency_data['USD'], float)
        self.assertGreaterEqual(currency_data['USD'], 0)
        self.assertLessEqual(currency_data['USD'], MAX_R_VALUE)
        logs = self.stream.getvalue()
        self.assertIn("Вызов функции", logs)
        self.assertIn("USD", logs)

    @patch('requests.get')
    def test_code(self, mock_get):
        # Мокаем ответ API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 75.5}
            }
        }
        mock_get.return_value = mock_response
        result = self.wrapped(['XYZ'])
        self.assertIn('XYZ', result)
        self.assertIn("Код валюты", result['XYZ'])
        self.assertIn("XYZ", result['XYZ'])
        self.assertIn("не найден", result['XYZ'])

    @patch('requests.get')
    def test_ValueError(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Ошибка соединения")
        with self.assertRaises(ValueError):
            self.wrapped(['USD'])
        logs = self.stream.getvalue()
        self.assertIn("Вызов функции", logs)
        self.assertIn("Ошибка", logs)

    @patch('requests.get')
    def test_json(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response
        with self.assertRaises(ValueError) as context:
            self.wrapped(['USD'])
        self.assertIn("JSON", str(context.exception))
        logs = self.stream.getvalue()
        self.assertIn("Вызов функции", logs)
        self.assertIn("Ошибка", logs)

    @patch('requests.get')
    def test_logging_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 75.5}
            }
        }
        mock_get.return_value = mock_response
        result = self.wrapped(['USD'])
        logs = self.stream.getvalue()
        self.assertIn("Вызов функции", logs)  # Первый вызов из wrapper
        self.assertIn("USD", logs)
        self.assertIn("Результат", logs)
        self.assertIsInstance(result['USD'], float)

    @patch('requests.get')
    def test_logging_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError("Сервер недоступен")
        with self.assertRaises(ValueError):
            self.wrapped(['USD'])
        logs = self.stream.getvalue()
        self.assertIn("Вызов функции", logs)
        self.assertIn("Ошибка", logs)
        self.assertIn("Ошибка при запросе к API", logs)

    @patch('requests.get')
    def test_logging_key_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 75.5}
            }
        }
        mock_get.return_value = mock_response
        result = self.wrapped(['XYZ'])
        self.assertEqual(result['XYZ'], "Код валюты 'XYZ' не найден.")
        logs = self.stream.getvalue()
        self.assertIn("Вызов функции", logs)
        self.assertIn("Результат", logs)
        self.assertIn("XYZ", logs)


if __name__ == "__main__":
    unittest.main()
