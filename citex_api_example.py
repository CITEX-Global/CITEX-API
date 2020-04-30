import requests
import hmac
import hashlib
from datetime import datetime
import base64
from urllib.parse import quote
import sys
import urllib
import urllib.parse
import urllib.request


#Please enter the base url first

#And enter access key and secret key if want request private API

base = 'https://apiproject.citex.io/'
akey = ""
skey = ""


u = 'api.citex.io'
headers = {'API-KEY':akey}

def get_symbols():
    url = base + 'v1/common/symbols'
    r = requests.get(url, headers = headers)
    detail = r.json()
    return detail
# print(get_symbols())



def get_currencys():
    url = base + '/v1/common/currencys'
    r = requests.get(url, headers = headers)
    detail = r.json()
    return detail
# print(get_currencys())



def get_server_time():
    url = base + '/v1/common/timestamp'
    r = requests.get(url, headers = headers)
    detail = r.json()
    return detail
# print(get_server_time())


#symbol ETH-USDT
def get_order_book(symbol):
    url = base + '/v1/common/snapshot/%s'%symbol
    r = requests.get(url=url, headers = headers)
    detail = r.json()
    return detail
# print(get_order_book('ETH-USDT'))

def get_tickers():
    url = base + '/v1/common/allticker'
    r = requests.get(url, headers = headers)
    detail = r.json()
    return detail
# print(get_tickers())

#
def get_candlestick(symbol, type, size):
    url = base + '/v1/common/candlestick'
    r = requests.get(url, params={'symbol':symbol, 'type':type, 'size':size}, headers=headers)
    detail = r.json()
    return detail
# print(get_candlestick('eth_btc', 15, 20))


#Need verification
def createHash(dataJsonStr):
    key = bytes(skey, 'utf-8')
    # print(key)
    jsonBytes = bytes(dataJsonStr, 'utf-8')
    # print(jsonBytes)
    hmac_result = hmac.new(key, jsonBytes, hashlib.sha256).digest()
    return base64.b64encode(hmac_result).decode()
    #hmac_result = hmac.new(key, jsonBytes, digestmod=hashlib.sha256).hexdigest()
    #return hmac_result
   

def get_balance():
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    # timestamp = '2019-06-20T09%3A38%3A06'
    url = base + '/v1/account/balance'
    # print(timestamp)
    dataJsonStr = 'GET\n'+ u +'\n'+ '/v1/account/balance\n'

    add_data = 'AccessKeyId=%s'%akey + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    #print(add_data)

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    #print(added_data)
    dataJsonStr = dataJsonStr + added_data
    #print("签名字符串：",dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    #print('signature:',signature)
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature, headers = headers)

    #print("sendurl:",url + '?' + added_data + '&' + 'Signature=' + signature)

    detail = r.json()
    return detail

print(get_balance())




def place_order(contractId, price, quantity, side, orderType):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))

    # timestamp = '2019-06-20T09%3A38%3A06'
    url = base + '/v1/order/orders/place'

    dataJsonStr = 'POST\n'+ u +'\n'+ '/v1/order/orders/place' +'\n'
    add_data = 'AccessKeyId=%s'%akey + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)

    data = {"orderType":orderType,"side":side,"quantity":quantity,"price":price,"contractId":contractId,"timeInForce":"1"}
    # print(data)
    r = requests.post(url=url + '?' + added_data + '&' + 'Signature=' + signature, json = data, headers = headers)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail


#print(place_order('15','0.01','1','-1','1'))
#sys.exit()

def cancel_order(contractId, orderId):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/orders/cancel'

    dataJsonStr = 'POST\n'+ u +'\n'+ '/v1/order/orders/cancel' +'\n'
    add_data = 'AccessKeyId=%s'%akey + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    data = {"contractId":contractId,"orderId":orderId}
    r = requests.post(url=url + '?' + added_data + '&' + 'Signature=' + signature, json = data, headers = headers)

    detail = r.json()
    return detail
#print(cancel_order('15', '1587348529485470'))


#查询订单消息
def list_orders(orderId):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/orders/%s'%int(orderId)

    dataJsonStr = 'GET\n'+ u +'\n'+ '/v1/order/orders/%s'%int(orderId) +'\n'
    add_data = 'AccessKeyId=%s'%akey + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature, headers = headers)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail
#print(list_orders("1587348529485470"))


def open_orders():
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/list'

    dataJsonStr = 'GET\n'+ u +'\n'+ '/v1/order/list' +'\n'
    add_data = 'AccessKeyId=%s'%akey + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature, headers = headers)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail
#print(open_orders())


def order_history(contractId):
    contId = str(contractId)
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/%s/history'%contId

    dataJsonStr = 'GET\n'+ u +'\n'+ '/v1/order/%s/history'%contId +'\n'
    add_data = 'AccessKeyId=%s'%akey + '\n' + 'SignatureMethod=HmacSHA256'+ '\n' + 'SignatureVersion=2'+ '\n' + 'Timestamp=%s'%timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + add_data.split('\n')[3]
    # print(added_data)
    dataJsonStr = dataJsonStr + added_data
    # print(dataJsonStr)
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    # print(signature)
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature, headers = headers)
    # print(url + '?' + added_data + '&' + 'Signature=' + signature)
    detail = r.json()
    return detail
print(order_history(15))