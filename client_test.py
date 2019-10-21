import unittest
from client import getDataPoint
from client import getRatio

class ClientTest(unittest.TestCase):

	def test_getDataPoint_calculatePrice(self):
		quotes = [
		{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
		{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
	]
	# ------------ Add the assertion below ------------ 
		self.assertEqual(getDataPoint(quotes[0])[-1],120.48)
		self.assertEqual(getDataPoint(quotes[1])[-1],117.87)
		
	def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
		quotes = [
		{'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
		{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
	# ------------ Add the assertion below ------------ 
		self.assertEqual(getDataPoint(quotes[0])[-1],119.2)
		self.assertEqual(getDataPoint(quotes[1])[-1],117.87)
	
	# ------------ Add more unit tests ------------ 
	
	def test_div_zero_values(self):
		quotes = [
		{'top_ask': {'price': 10.5, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 10.4, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
		{'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
	# ------------ Add the assertion below ------------  
		self.assertEqual(getRatio(getDataPoint(quotes[0])[-1],getDataPoint(quotes[1])[-1]),0)
	

  
if __name__ == '__main__':
    unittest.main()
