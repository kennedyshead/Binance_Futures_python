import logging

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

_LOGGER = logging.getLogger(__name__)

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_recent_trades_list(symbol="BTCUSDT", limit=10)

_LOGGER.debug("======= Recent Trades List =======")
PrintMix.print_data(result)
_LOGGER.debug("==================================")
