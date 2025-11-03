import unittest
import requests
import sys
import io


def get_currencies(currency_codes: list, url: str = "https://www.cbr-xml-daily.ru/daily_json.js",
                   handle=sys.stdout) -> dict:
    """
    Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list): Список символьных кодов валют (например, ['USD', 'EUR']).

    Returns:
        dict: Словарь, где ключи - символьные коды валют, а значения - их курсы.
              Возвращает None в случае ошибки запроса.
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
        handle.write(f"Ошибка при запросе к API: {e}")
        raise ValueError('Упали с исключением')


currency_list = ['USD', 'EUR', 'GBP', 'NNZ']
currency_data = get_currencies(currency_list)


def main():
    currency_list = ['USD', 'EUR', 'GBP', 'NNZ']
    currency_data = get_currencies(currency_list)
    if currency_data:
        print(currency_data)


if __name__ == "__main__":
    main()

MAX_R_VALUE = 1000


class TestGetCurrencies(unittest.TestCase):

    def test_currency_usd(self):
        """
          Проверяет наличие ключа в словаре и значения этого ключа
        """
        currency_list = ['USD']
        currency_data = get_currencies(currency_list)

        self.assertIn(currency_list[0], currency_data)
        self.assertIsInstance(currency_data['USD'], float)
        self.assertGreaterEqual(currency_data['USD'], 0)
        self.assertLessEqual(currency_data['USD'], MAX_R_VALUE)

    def test_nonexist_code(self):
        self.assertIn("Код валюты", get_currencies(['XYZ'])['XYZ'])
        self.assertIn("XYZ", get_currencies(['XYZ'])['XYZ'])
        self.assertIn("не найден", get_currencies(['XYZ'])['XYZ'])

    def test_get_currency_error(self):
        error_phrase_regex = "Ошибка при запросе к API"
        with self.assertRaises(ValueError):
            with io.StringIO() as fake_handle:
                get_currencies(['USD'], url="https://www.cbr-xml-daily.1ru/daily_json.js", handle=fake_handle)
                output = fake_handle.getvalue()


if __name__ == "__main__":
    unittest.main()
