#from typing import Protocol
from typing_extensions import Protocol

class ExecutionException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ExecutionClient(Protocol):

    def buy(product_id: str, amount: int, price:float):
        """
        Execute a buy order, throws ExecutionException on failure
        :param product_id: the product to buy
        :param amount: the amount to buy
        :return: None
        """
        try:
            buy_order = {
                "action": "buy",
                "product_id": product_id,
                "amount": amount,
                "price": price
            }
            print("Buy order placed for " + str(amount) + " shares of " + str(product_id) + " at " + str(price))
        except Exception as e:
            raise ExecutionException("Error Buying Order------" + str(e))

    def sell(product_id: str, amount: int, price:float):
        """
        Execute a sell order, throws ExecutionException on failure
        :param product_id: the product to sell
        :param amount: the amount to sell
        :return: None
        """
        try:
            sell_order = {
                "action": "sell",
                "product_id": product_id,
                "amount": amount,
                "price": price
            }
            print("Sell order placed for " + str(amount) + " shares of " + str(product_id) + " at " + str(price))
        except Exception as e:
            raise ExecutionException("Error Selling Order------" + str(e))
