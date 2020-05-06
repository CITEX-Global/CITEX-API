import requests
import hmac
import hashlib
from datetime import datetime
import base64
from urllib.parse import quote

# Please enter the base url first
base = 'https://api2.citex.io'

# And enter access key and secret key if want request private API
akey = " "
skey = " "

headers = {'API-KEY': akey}


def get_symbols():
    url = base + '/v1/common/symbols'
    r = requests.get(url, headers=headers)
    detail = r.json()
    return detail

print(get_symbols())


def get_currencys():
    url = base + '/v1/common/currencys'
    r = requests.get(url, headers=headers)
    detail = r.json()
    return detail

print(get_currencys())


def get_server_time():
    url = base + '/v1/common/timestamp'
    r = requests.get(url, headers=headers)
    detail = r.json()
    return detail

print(get_server_time())


def get_order_book(symbol):
    url = base + '/v1/common/snapshot/%s' % symbol
    r = requests.get(url=url, headers=headers)
    detail = r.json()
    return detail

print(get_order_book('ETH-USDT'))


def get_tickers():
    url = base + '/v1/common/allticker'
    r = requests.get(url, headers=headers)
    detail = r.json()
    return detail

print(get_tickers())


def get_candlestick(symbol, type, size):
    url = base + '/v1/common/candlestick'
    r = requests.get(url, params={'symbol': symbol, 'type': type, 'size': size}, headers=headers)
    detail = r.json()
    return detail

print(get_candlestick('eth_btc', 15, 20))


# Need verification
def createHash(dataJsonStr):
    key = bytes(skey, 'utf-8')
    jsonBytes = bytes(dataJsonStr, 'utf-8')
    hmac_result = hmac.new(key, jsonBytes, hashlib.sha256).digest()
    return base64.b64encode(hmac_result).decode()


def get_balance():
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/account/balance'
    dataJsonStr = 'GET\n' + 'api.citex.io' + '\n' + '/v1/account/balance\n'
    add_data = 'AccessKeyId=%s' % akey + '\n' + 'SignatureMethod=HmacSHA256' + '\n' + 'SignatureVersion=2' + '\n' + 'Timestamp=%s' % timestamp
    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + \
                 add_data.split('\n')[3]
    dataJsonStr = dataJsonStr + added_data
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature, headers=headers)
    detail = r.json()
    return detail

print(get_balance())


def place_order(contractId, price, quantity, side, orderType):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/orders/place'
    dataJsonStr = 'POST\n' + 'api.citex.io' + '\n' + '/v1/order/orders/place' + '\n'
    add_data = 'AccessKeyId=%s' % akey + '\n' + 'SignatureMethod=HmacSHA256' + '\n' + 'SignatureVersion=2' + '\n' + 'Timestamp=%s' % timestamp

    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + \
                 add_data.split('\n')[3]
    dataJsonStr = dataJsonStr + added_data
    signature = quote(createHash(dataJsonStr=dataJsonStr))

    data = {"orderType": orderType, "side": side, "quantity": quantity, "price": price, "contractId": contractId,
            "timeInForce": "1"}
    r = requests.post(url=url + '?' + added_data + '&' + 'Signature=' + signature, json=data, headers=headers)
    detail = r.json()
    return detail

print(place_order('2', '7000', '0.001', '1', '1'))


def cancel_order(contractId, orderId):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/orders/cancel'
    dataJsonStr = 'POST\n' + 'api.citex.io' + '\n' + '/v1/order/orders/cancel' + '\n'
    add_data = 'AccessKeyId=%s' % akey + '\n' + 'SignatureMethod=HmacSHA256' + '\n' + 'SignatureVersion=2' + '\n' + 'Timestamp=%s' % timestamp
    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + \
                 add_data.split('\n')[3]
    dataJsonStr = dataJsonStr + added_data
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    data = {"contractId": contractId, "orderId": orderId}
    r = requests.post(url=url + '?' + added_data + '&' + 'Signature=' + signature, json=data, headers=headers)
    detail = r.json()
    return detail

print(cancel_order('2', '1588748621241869'))


def list_orders(orderId):
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/orders/%s' % int(orderId)

    dataJsonStr = 'GET\n' + 'api.citex.io' + '\n' + '/v1/order/orders/%s' % int(orderId) + '\n'
    add_data = 'AccessKeyId=%s' % akey + '\n' + 'SignatureMethod=HmacSHA256' + '\n' + 'SignatureVersion=2' + '\n' + 'Timestamp=%s' % timestamp
    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + \
                 add_data.split('\n')[3]
    dataJsonStr = dataJsonStr + added_data
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature, headers=headers)
    detail = r.json()
    return detail

print(list_orders("1588748621241869"))


def open_orders():
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/list'
    dataJsonStr = 'GET\n' + 'api.citex.io' + '\n' + '/v1/order/list' + '\n'
    add_data = 'AccessKeyId=%s' % akey + '\n' + 'SignatureMethod=HmacSHA256' + '\n' + 'SignatureVersion=2' + '\n' + 'Timestamp=%s' % timestamp
    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + \
                 add_data.split('\n')[3]
    dataJsonStr = dataJsonStr + added_data
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature, headers=headers)
    detail = r.json()
    return detail

print(open_orders())


def order_history(contractId):
    contId = str(contractId)
    timestamp = str(quote(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')))
    url = base + '/v1/order/%s/history' % contId
    dataJsonStr = 'GET\n' + 'api.citex.io' + '\n' + '/v1/order/%s/history' % contId + '\n'
    add_data = 'AccessKeyId=%s' % akey + '\n' + 'SignatureMethod=HmacSHA256' + '\n' + 'SignatureVersion=2' + '\n' + 'Timestamp=%s' % timestamp
    added_data = add_data.split('\n')[0] + '&' + add_data.split('\n')[1] + '&' + add_data.split('\n')[2] + '&' + \
                 add_data.split('\n')[3]
    dataJsonStr = dataJsonStr + added_data
    signature = quote(createHash(dataJsonStr=dataJsonStr))
    r = requests.get(url=url + '?' + added_data + '&' + 'Signature=' + signature, headers=headers)
    detail = r.json()
    return detail

print(order_history(15))

