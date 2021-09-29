from . import container
from common import Log, FireEvent, singleton


@singleton
class CPlayer():
	
	def __init__(self):
		self.m_ID = "0"
		self.m_Money = 0
		self.m_Pack = container.CPackContainer()
		self.m_Inventory = container.CInventoryContainer()
		self.m_Positon = [0,0]
	
	def Move(self, iDiretion, iNum):
		Log(f"player Move {iDiretion} {iNum}")
		FireEvent("E_PlayerMove", self.m_ID)

	def Buy(self, iITemID, iNum):
		pass