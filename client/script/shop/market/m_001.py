from .base import CMarket as CCustomMarket

class CMarket(CCustomMarket):

	def __init__(self):
		self.m_Name = "水果市场"
		self.m_ID = 1
		self.m_Goods = []