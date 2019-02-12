# _*_ coding : utf -8 _*_
class DataBase():
    '''Python 3 中的类'''

    def __init__(self):
        '''初始化方法'''
        self.id = id
        #self.address = address
        self.d = {self.id: 1,
                  #self.address: "192.168.1.1",
                  }

    def __getitem__(self, key):
        return self.d.get(key, "default")



data = DataBase()
print(data["hi"])
#print(data[data.address])
print(data.id)
#print(data.address)
print(data["item"])