import logging
from binance_f import SubscriptionClient
from binance_f.constant.test import *
from binance_f.model import *
from binance_f.exception.binanceapiexception import BinanceApiException

from binance_f.base.printobject import *

_LOGGER = logging.getLogger(__name__)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    if data_type == SubscribeMessageType.RESPONSE:
        _LOGGER.debug("Event ID: ", event)
    elif data_type == SubscribeMessageType.PAYLOAD:
        PrintBasic.print_obj(event)
        sub_client.unsubscribe_all()
    else:
        _LOGGER.debug("Unknown Data:")


def error(e: 'BinanceApiException'):
    _LOGGER.debug(e.error_code + e.error_message)


sub_client.subscribe_mark_price_event("btcusdt", callback, error)
