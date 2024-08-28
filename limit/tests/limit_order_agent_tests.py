import unittest
from limit.limit_order_agent import LimitOrderAgent
from trading_framework.execution_client import ExecutionClient

class LimitOrderAgentTest(unittest.TestCase):

    # def test_something(self):
    #     self.fail("not implemented")

    def test_ibm_buy_order_execution_price_under_100(self):
        print("-----test_ibm_buy_order_execution_price_under_100------")
        '''Implement LimitOrderAgent such that it buys 1000 shares of IBM when the price drops below $100'''
        limit_agent = LimitOrderAgent(ExecutionClient)
        limit_agent.on_price_tick('IBM', 99)
        
    def test_add_order(self):
        print("-----test_add_order------")
        limit_agent = LimitOrderAgent(ExecutionClient)
        orders = limit_agent.add_order('buy', 'BBM', 100, 150)
        self.assertEqual(len(orders), 1)
        order = orders[0]
        self.assertEqual(order['action'], 'buy')
        self.assertEqual(order['product_id'], 'BBM')
        self.assertEqual(order['amount'], 100)
        self.assertEqual(order['limit'], 150)

    def test_exceute_held_orders(self):
        print("-----test_exceute_held_orders------")
        limit_agent = LimitOrderAgent(ExecutionClient)
        limit_agent.add_order('buy', 'HCL', 50, 2000)
        limit_agent.add_order('sell', 'BPCL', 200, 3000)
        limit_agent.add_order('buy', 'BST', 100, 250)
        limit_agent.add_order('sell', 'TATA', 200, 1000)
        changeList = [
            {"product_id":"HCL", "price":1500},
            {"product_id":"BPCL", "price":3100},
            {"product_id":"BST", "price":260},
            {"product_id":"TATA", "price":1100}
        ]
        for change in changeList:
            limit_agent.execute_held_orders(change["product_id"], change["price"])
            
        
