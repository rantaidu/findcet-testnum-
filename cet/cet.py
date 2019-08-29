import requests
import random
import socket
import struct

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Referer': 'http://www.chsi.com.cn/cet',
    'X-FORWARDED-FOR':'',
	'CLIENT-IP':''
}

param={
        'zkzh':'',
        'xm':''}

xxdm = input("输入学校代码：")
type = input("输入四六级编号：")
zkzh = int(xxdm+type+'00101') 

param['zkzh']=zkzh
param['xm'] = input("请输入考生姓名：")

while 1:
    IP = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    HEADERS['X-FORWARDED-FOR'] = IP
    HEADERS['CLIENT-IP'] = IP
    try:
        rsp = requests.get('http://www.chsi.com.cn/cet/query',params=param, headers=HEADERS)
    except requests.exceptions.ConnectionError:
        continue
    except requests.exceptions.HTTPError:
        continue
    if '写作和翻译' in rsp.text:
        print(param, '查询成功')
        # print(rsp.text)
        break
    else:
        print(param, '查询中')
        zkzh += 1
        temp = zkzh - 31
        if temp % 100 == 0:
            zkzh = zkzh + 70
        param['zkzh'] = zkzh

print("准考证号位",param['zkzh'])	
	
input("Please Enter:")		
