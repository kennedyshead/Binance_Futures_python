import logging

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

_LOGGER = logging.getLogger(__name__)

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_mark_price(symbol="BTCUSDT")

_LOGGER.debug("======= Mark Price =======")
PrintBasic.print_obj(result)
_LOGGER.debug("==========================")
