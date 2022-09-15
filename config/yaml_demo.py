from utils.YamlUtil import YamlReader
res = YamlReader("../data/testlogin.yml").data_all()
print(res)
print(type(res))
for i in res:
    print(i)