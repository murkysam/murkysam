

class CGoods():
	
	def __init__(self):
		self.m_Name = ""
		self.m_ID = 0
		self.m_Price = 1<<31

	def GetPrice(self):
		return self.m_Price

	def SetPrice(self, iPrice):
		self.m_Price = iPrice