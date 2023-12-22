import asyncio
import logging
import os
import platform
import sys
from time import time

import aiohttp

from DateHandler import DateHandler
from constants import BANK_URL, STORAGE_DIR, STORAGE_DATA_FILE
from utils import check_all_currencies, check_days, create_storage_dir, save_data_to_file


class HttpGetError(Exception):
    ...


async def get_exchange_rate(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, ) as response:
                if response.status == 200:
                    result = await response.json(content_type='application/json')
                    return result
                else:
                    raise HttpGetError(f'Error when opening URL: {url}, Error: {response.status}')
        except (
                aiohttp.ClientError, aiohttp.ClientConnectionError, aiohttp.ClientResponseError,
                aiohttp.InvalidURL) as e:
            raise HttpGetError(f'Connection error when opening URL: {url}, Error: {e}')


async def process_response_data(data: dict, currencies: tuple) -> dict:
    date_key = data['date']
    currency_dict = {
        currency['currency']: {
            'sale': currency['saleRate'],
            'purchase': currency['purchaseRate']
        }
        for currency in data['exchangeRate']
        if currency['currency'] in currencies  # ('EUR', 'USD')
    }
    day_dict = {date_key: currency_dict}
    logging.debug(f'Parsed data: {day_dict}')
    return day_dict


async def get_data(days, currencies):
    date_handler = DateHandler()
    output_list = []
    current_day = 0
    async for day in date_handler.dates_list(days):  # Use async for loop
        try:
            current_day += 1
            logger.info(f"Getting data for {day} ({current_day}/{days + 1})")
            response = await get_exchange_rate(BANK_URL + day)
            # logger.debug(response)
            result = await process_response_data(response, currencies)
            output_list.append(result)
        except HttpGetError as e:
            logger.error(f'Error: {e}')
    return output_list


async def main():
    days = check_days(sys.argv[1]) if len(sys.argv) > 1 else 0

    cur = check_all_currencies(sys.argv[-1])

    start_time = time()
    logger.debug(f"Start time: {start_time}")

    result = await get_data(days, cur)

    logger.debug(f"Result data: {result}")

    end_time = time()
    logger.debug(f"End time: {end_time}")
    logger.info(f"Time elapsed: {end_time - start_time}")

    create_storage_dir(STORAGE_DIR)
    save_data_to_file(result, STORAGE_DATA_FILE)
    logger.info(f"Data saved to file: {STORAGE_DATA_FILE}")


if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dir_name = os.path.dirname(abspath)
    os.chdir(dir_name)

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s - %(message)s')

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Exiting after Control+C...")
        sys.exit(0)
