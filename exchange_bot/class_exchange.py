import requests
import json
from config import keys


class ConversionException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Невозможно обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Невозможно обработать валюту{base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Неправильно введено количество {amount}')

        currency = f'{quote_ticker}_{base_ticker}'
        r = requests.get(f'https://free.currconv.com/api/v7/convert?q={currency}'
                         f'&compact=ultra&apiKey=af3d80b1a3c65157a1ae')
        res = json.loads(r.content)

        text = f'Курс: 1 {quote} стоит {res[currency]:.2f} {base}\n\n' \
               f'{amount} {quote} стоит {float(amount) * float(res[currency]):.2f} {base}'

        return text
