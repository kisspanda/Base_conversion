def any_to_dec(num_type, num_str):
    num_type = int(num_type)
    #print("输入的",num_type,"进制数是：",num_str)
    i = 0
    num = 0
    num_str = num_str[::-1]
    dict1={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
           'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    for each in num_str :       
        num += num_type**i*int(dict1[each.lower()])
        i += 1
    #print("输入的十进制数是：",num)
    return num    
 
def dec_to_any(num_type, num_dec):
    num_type = int(num_type)
    #print("输入的十进制数是：",num_dec,"要转换成",num_type,"进制的数")
    num_dec = int(num_dec)
    num_str = ''
    while num_dec != 0 :
        num_str += hex(num_dec % num_type)[2] 
        num_dec = num_dec //num_type
    num_str = num_str[::-1]
    return num_str

nottrue=False
while not nottrue:
    print("最高16进制，再多没写")
    print("使用完毕，直接关闭窗口就可以")
    print("")
    print("\n")
    num_type = input("请输入源数值进制：")
    num = input( "请输入源数值u：")
    dec = any_to_dec(num_type,num)
    num_type = input("请输入目标数值进制：")
    num_str = dec_to_any(num_type, dec)
    print("转换后的数值是：",num_str)
    print("\n")
