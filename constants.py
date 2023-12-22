from pathlib import Path

# https://api.privatbank.ua/#p24/exchangeArchive
BANK_URL = 'https://api.privatbank.ua/p24api/exchange_rates?date='

ROOT_DIR = Path()
STORAGE_DIR = ROOT_DIR.joinpath('storage')
STORAGE_DATA_FILE = STORAGE_DIR.joinpath('data.txt')
BASE_CURRENCIES = ('EUR', 'USD')
ALL_CURRENCIES = ('EUR', 'USD', 'CHF', 'CZK', 'GBP', 'PLN')
