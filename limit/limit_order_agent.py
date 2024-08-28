from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener


class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        self.execution_client = execution_client
        self.orders = []
        super().__init__()

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        if product_id.upper() == "IBM" and price < 100:
            return self.execution_client.buy(product_id.upper(), 1000, price)

    
    def add_order(self,action: str, product_id: str, amount: int, limit: float):
        order = {
            "action" : action,
            "product_id": product_id,
            "amount": amount,
            "limit" : limit
        }
        print("Order added with product id :- " + str(order))
        self.orders.append(order)
        return self.orders
    
    def execute_held_orders(self,product_id: str, price: float):
        for order in self.orders:
            if order["product_id"] == product_id:
                if order["action"].lower() == "buy" and price <= order["limit"]:
                    self.execution_client.buy(product_id.upper(), order["amount"], price)
                elif order["action"] == "sell" and price >= order["limit"]:
                    self.execution_client.sell(product_id.upper(), order["amount"], price)
