import logging

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

_LOGGER = logging.getLogger(__name__)

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

aggregate_trades_list = request_client.get_aggregate_trades_list(symbol="BTCUSDT", fromId=None,
												startTime=None, endTime=None, limit=10)

_LOGGER.debug("======= Compressed/Aggregate Trades List =======")
PrintMix.print_data(aggregate_trades_list)
_LOGGER.debug("================================================")
