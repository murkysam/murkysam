import json

class CCSVParser():
    def Csv2Json(self, sCsv):
        lstJson = []
        try:
            f = open(sCsv, 'r', encoding="GBK")
        except:
            f = open(sCsv, 'r', encoding="utf-8")
        keys = f.readline().strip('\n').split(',')
        for line in f.readlines():
            values = line.strip('\n').split(',')
            lstJson.append(dict(zip(keys, values)))
        f.close()
        ret = json.dumps(lstJson, indent=1)
        return ret

    def ParseCsv(self, sCsv):
        sJson = sCsv
        if sCsv.find("/") != -1:
            sJson = sCsv.split('/')[-1]
        sJson = sJson.split('.')[0] + ".json"
        print(sJson)
        with open(sJson, 'w', encoding='UTF-8') as f:
            f.write(self.Csv2Json(sCsv))

MyCSVParser = CCSVParser()
MyCSVParser.ParseCsv("./design/kv工具/城市数据.csv")