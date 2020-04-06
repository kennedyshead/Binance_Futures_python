import logging
from binance_f import RequestClient
from binance_f import SubscriptionClient
from binance_f.constant.test import *
from binance_f.model import *
from binance_f.exception.binanceapiexception import BinanceApiException

from binance_f.base.printobject import *

_LOGGER = logging.getLogger(__name__)

# Start user data stream
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
listen_key = request_client.start_user_data_stream()
_LOGGER.debug("listenKey: ", listen_key)

# Keep user data stream
result = request_client.keep_user_data_stream()
_LOGGER.debug("Result: ", result)

# Close user data stream
# result = request_client.close_user_data_stream()
# _LOGGER.debug("Result: ", result)

logger = logging.getLogger("binance-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    if data_type == SubscribeMessageType.RESPONSE:
        _LOGGER.debug("Event ID: ", event)
    elif  data_type == SubscribeMessageType.PAYLOAD:
        if(event.eventType == "ACCOUNT_UPDATE"):
            _LOGGER.debug("Event Type: ", event.eventType)
            _LOGGER.debug("Event time: ", event.eventTime)
            _LOGGER.debug("Transaction time: ", event.transactionTime)
            _LOGGER.debug("=== Balances ===")
            PrintMix.print_data(event.balances)
            _LOGGER.debug("================")
            _LOGGER.debug("=== Positions ===")
            PrintMix.print_data(event.positions)
            _LOGGER.debug("================")
        elif(event.eventType == "ORDER_TRADE_UPDATE"):
            _LOGGER.debug("Event Type: ", event.eventType)
            _LOGGER.debug("Event time: ", event.eventTime)
            _LOGGER.debug("Transaction Time: ", event.transactionTime)
            _LOGGER.debug("Symbol: ", event.symbol)
            _LOGGER.debug("Client Order Id: ", event.clientOrderId)
            _LOGGER.debug("Side: ", event.side)
            _LOGGER.debug("Order Type: ", event.type)
            _LOGGER.debug("Time in Force: ", event.timeInForce)
            _LOGGER.debug("Original Quantity: ", event.origQty)
            _LOGGER.debug("Price: ", event.price)
            _LOGGER.debug("Average Price: ", event.avgPrice)
            _LOGGER.debug("Stop Price: ", event.stopPrice)
            _LOGGER.debug("Execution Type: ", event.executionType)
            _LOGGER.debug("Order Status: ", event.orderStatus)
            _LOGGER.debug("Order Id: ", event.orderId)
            _LOGGER.debug("Order Last Filled Quantity: ", event.lastFilledQty)
            _LOGGER.debug("Order Filled Accumulated Quantity: ", event.cumulativeFilledQty)
            _LOGGER.debug("Last Filled Price: ", event.lastFilledPrice)
            _LOGGER.debug("Commission Asset: ", event.commissionAsset)
            _LOGGER.debug("Commissions: ", event.commissionAmount)
            _LOGGER.debug("Order Trade Time: ", event.orderTradeTime)
            _LOGGER.debug("Trade Id: ", event.tradeID)
            _LOGGER.debug("Bids Notional: ", event.bidsNotional)
            _LOGGER.debug("Ask Notional: ", event.asksNotional)
            _LOGGER.debug("Is this trade the maker side?: ", event.isMarkerSide)
            _LOGGER.debug("Is this reduce only: ", event.isReduceOnly)
            _LOGGER.debug("stop price working type: ", event.workingType)
        elif(event.eventType == "listenKeyExpired"):
            _LOGGER.debug("Event: ", event.eventType)
            _LOGGER.debug("Event time: ", event.eventTime)
            _LOGGER.warning("CAUTION: YOUR LISTEN-KEY HAS BEEN EXPIRED!!!")
            _LOGGER.warning("CAUTION: YOUR LISTEN-KEY HAS BEEN EXPIRED!!!")
            _LOGGER.warning("CAUTION: YOUR LISTEN-KEY HAS BEEN EXPIRED!!!")
    else:
        _LOGGER.debug("Unknown Data:")



def error(e: 'BinanceApiException'):
    _LOGGER.debug(e.error_code + e.error_message)

sub_client.subscribe_user_data_event(listen_key, callback, error)
