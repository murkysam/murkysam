
class CMap():
	
	def __init__(self):
		self.m_Map = [[0]*5]*5

	def GetMapMatrix(self):
		return self.m_Map


if "g_Map" not in globals():
	g_Map = CMap()

def GetMap():
	return g_Map

if __name__ == "__main__":
	print(GetMap().GetMapMatrix())
