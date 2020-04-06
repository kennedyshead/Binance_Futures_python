import logging

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

_LOGGER = logging.getLogger(__name__)

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_exchange_information()
_LOGGER.debug("======= Exchange Information =======")
_LOGGER.debug("timezone: ", result.timezone)
_LOGGER.debug("serverTime: ", result.serverTime)
_LOGGER.debug("=== Rate Limits ===")
PrintMix.print_data(result.rateLimits)
_LOGGER.debug("===================")
_LOGGER.debug("=== Exchange Filters ===")
PrintMix.print_data(result.exchangeFilters)
_LOGGER.debug("===================")
_LOGGER.debug("=== Symbols ===")
PrintMix.print_data(result.symbols)
_LOGGER.debug("===================")
_LOGGER.debug("====================================")
