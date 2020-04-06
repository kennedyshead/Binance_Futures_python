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
        _LOGGER.debug("Event Type: ", event.eventType)
        _LOGGER.debug("Event Time: ", event.eventTime)
        _LOGGER.debug("transaction time: ", event.transactionTime)
        _LOGGER.debug("Symbol: ", event.symbol)
        _LOGGER.debug("first update Id from last stream: ",
                      event.firstUpdateId)
        _LOGGER.debug("last update Id from last stream: ", event.finalUpdateId)
        _LOGGER.debug("last update Id in last stream: ",
                      event.lastUpdateIdInlastStream)
        _LOGGER.debug("=== Bids to be updated ===")
        PrintMix.print_data(event.bids)
        _LOGGER.debug("==========================")
        _LOGGER.debug("=== Asks to be updated ===")
        PrintMix.print_data(event.asks)
        _LOGGER.debug("==========================")
        sub_client.unsubscribe_all()
    else:
        _LOGGER.debug("Unknown Data:")


def error(e: 'BinanceApiException'):
    _LOGGER.debug(e.error_code + e.error_message)


sub_client.subscribe_diff_depth_event("btcusdt", callback, error,
                                      update_time=UpdateTime.REALTIME)
