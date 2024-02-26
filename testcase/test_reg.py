import re

def func(address_instruction):
    address = "详细地址是"+"("+address_instruction+")"
    reg0="\\s?\\("+address_instruction+"\\)$"
    reg=re.compile(reg0)
    # reg1 = reg0.ecape(reg0)
    print(address,reg0,reg)
    print(address.replace(reg0,''))


func("ab")



