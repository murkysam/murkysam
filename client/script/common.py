import time
import random
from collections import defaultdict
# 事件系统   通过事件解耦合
class CEvent():

	def __init__(self) -> None:
		self.m_Index = 0
		self.m_Event = defaultdict()

	def RegisterEvent(self, sEvent, funcCallback):
		print(f"RegisterEvent -> {sEvent}")
		self.m_Index +=1
		if not self.m_Event[sEvent]:
			self.m_Event[sEvent] = {}
		self.m_Event[sEvent].update({self.m_Index:funcCallback})
		return self.m_Index

	def UnregisterEvent(self, iIndex):
		for v in self.m_Event.values():
			if iIndex in v:
				del v[iIndex]
		
	def FireEvent(self, sEvent, *args, **kwargs):
		print(f"FireEvent ->{sEvent}")
		if sEvent in self.m_Event:
			self.m_Event[sEvent](args, kwargs)

if "g_Event" not in globals():
	g_Event = CEvent()

def RegisterEvent(sEvent, funcCallback):
	return g_Event.RegisterEvent(sEvent, funcCallback)

def UnregisterEvent(iIndex):
	return g_Event.UnregisterEvent(iIndex)

def FireEvent(sEvent, *args, **kwargs):
	return g_Event.FireEvent(sEvent, *args, **kwargs)

# 资源管理器
class CResManager():

	def __init__(self) -> None:
		self.m_Res = {}

	def Register(self, obj):
		self.m_Res[obj.__name__] = obj

	def CallFunc(self, sResName, sFunc, *args, **kwargs):
		pass

if "g_ResManager" not in globals():
	g_ResManager = CResManager()

def singleton(cls):
	_instance = {}
	def inner():
		if cls not in _instance:
			_instance[cls] = cls()
			g_ResManager.Register(_instance[cls])
		return _instance[cls]
	return inner

def Init():
	global g_Seed	
	random.seed(time.time())
	g_Seed = random.randint(0, 1<<31)
	print(g_Seed)

def Log(sText):
	global g_Seed
	with open(f"log.txt{g_Seed}", "a", encoding='utf-8') as f:
		f.write(sText+"\n")
	print(sText)

Init()