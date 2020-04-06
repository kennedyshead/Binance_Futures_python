import logging

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

_LOGGER = logging.getLogger(__name__)

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_account_information()
_LOGGER.debug("canDeposit: ", result.canDeposit)
_LOGGER.debug("canWithdraw: ", result.canWithdraw)
_LOGGER.debug("feeTier: ", result.feeTier)
_LOGGER.debug("maxWithdrawAmount: ", result.maxWithdrawAmount)
_LOGGER.debug("totalInitialMargin: ", result.totalInitialMargin)
_LOGGER.debug("totalMaintMargin: ", result.totalMaintMargin)
_LOGGER.debug("totalMarginBalance: ", result.totalMarginBalance)
_LOGGER.debug("totalOpenOrderInitialMargin: ", result.totalOpenOrderInitialMargin)
_LOGGER.debug("totalPositionInitialMargin: ", result.totalPositionInitialMargin)
_LOGGER.debug("totalUnrealizedProfit: ", result.totalUnrealizedProfit)
_LOGGER.debug("totalWalletBalance: ", result.totalWalletBalance)
_LOGGER.debug("updateTime: ", result.updateTime)
_LOGGER.debug("=== Assets ===")
PrintMix.print_data(result.assets)
_LOGGER.debug("==============")
_LOGGER.debug("=== Positions ===")
PrintMix.print_data(result.positions)
_LOGGER.debug("==============")
