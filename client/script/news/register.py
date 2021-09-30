
from common import RegisterEvent
class CNewsManger():
    
    def __init__(self) -> None:
        self.RegisterNews()
        RegisterEvent("E_PlayerMove", self.GiveNews)
                
    def GiveNews(self, iPlayerID):
        print(f"触发了事件 {self.m_Title}, {self.m_Text}")

    def RegisterNews(self):
        import 