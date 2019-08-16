# -- coding: utf-8 --
# 需求：做一个通讯录，人的姓名、电话、地址，支持增删改
import os
import pickle


class address_book:

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def getDetail(self):
        return self.name + ',' + self.phone + ',' + self.address


def isNotEmpty(s):
    return bool(s and s.strip())

addressFile = 'addressFile.data'
address_list = {}
if os.path.exists(addressFile):
    with open(addressFile, 'rb') as f:
        address_list = pickle.load(f)
        for name, address in address_list.items():
            print('联系人： {} 通讯信息： {}'.format(name, address))
else:
    os.system(r'touch {}'.format(addressFile))

while True:
    ctr = str(input('add?del?exit?'))
    if ctr == 'add':
        name = str(input('please add name:'))
        phone = str(input('please add phone:'))
        address = str(input('please add address:'))
        a = address_book(name, phone, address)
        address_list[a.name] = a.getDetail()
        with open(addressFile, 'wb') as f:
            pickle.dump(address_list, f)
            for name, address in address_list.items():
                print('联系人： {} 通讯信息： {}'.format(name, address))

    elif ctr == 'del':
        del_item = str(input('del name:'))
        if isNotEmpty(del_item):
            del address_list[del_item]
            for name, address in address_list.items():
                print('联系人： {} 通讯信息： {}'.format(name, address))
    elif ctr == 'exit':
        print('bye~')
        break
    else:
        with open(addressFile, 'rb') as f:
            list = pickle.load(f)
            for name, address in list.items():
                print('联系人： {} 通讯信息： {}'.format(name, address))
