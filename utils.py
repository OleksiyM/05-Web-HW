import json
import logging

from constants import BASE_CURRENCIES, ALL_CURRENCIES

logger = logging.getLogger(__name__)


def check_all_currencies(param: str) -> list:
    if param.lower() == 'all':
        logger.debug(f"Using all currencies for exchange rate data retrieval: {ALL_CURRENCIES}")
        return ALL_CURRENCIES
    else:
        logger.debug(f"Using base currencies for exchange rate data retrieval: {BASE_CURRENCIES}")
        return BASE_CURRENCIES


def check_days(days: str) -> int:
    try:
        days = int(days)
    except ValueError:
        logger.info("Invalid input for days. Using default value (0).")
        return 0

    days = min(max(days, 0), 10)  # valid range (0-10)

    if days != 0:
        logger.debug(f"Using {days} days for exchange rate data retrieval.")
    else:
        logger.debug("Using current day for exchange rate data.")

    return days


def create_storage_dir(storage_dir):
    if not storage_dir.exists():
        storage_dir.mkdir()


def save_data_to_file(r, filename):
    with open(filename, 'w') as file:
        json.dump(r, file, ensure_ascii=False, indent=4)
        # file.write(str(r))
