# -- coding: utf-8 --
# 需求：做一个通讯录，人的姓名、电话、地址，支持增删改
import pickle


class address_book:

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def getDetail(self):
        return self.name + ',' + self.phone + ',' + self.address


addressFile = 'addressFile.data'
address_list = {}
f = open(addressFile, 'rb')
address_list = pickle.load(f)
print(address_list)
f.close()
while True:
    ctr = str(input('add?del?'))
    if ctr == 'add':
        name = str(input('please add name:'))
        phone = str(input('please add phone:'))
        address = str(input('please add address:'))
        a = address_book(name, phone, address)
        address_list[a.name] = a.getDetail()
        print('new:', address_list)
        f = open(addressFile, 'wb')
        pickle.dump(address_list, f)
        f.close()
        with open(addressFile, 'rb') as f:
            print(pickle.load(f))

    elif ctr == 'del':
        print('....')
    elif ctr =='exit':
        print('bye~')
        break
    else:
        with open(addressFile, 'rb') as f:
            print(pickle.load(f))
