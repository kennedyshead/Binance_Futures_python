import logging

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

_LOGGER = logging.getLogger(__name__)

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_order_book(symbol = "BTCUSDT", limit = 10)
_LOGGER.debug("======= Order Book =======")
_LOGGER.debug("lastUpdateId: ", result.lastUpdateId)
_LOGGER.debug("=== Bids ===")
PrintMix.print_data(result.bids)
_LOGGER.debug("===================")
_LOGGER.debug("=== Asks ===")
PrintMix.print_data(result.asks)
_LOGGER.debug("===================")
_LOGGER.debug("====================================")
