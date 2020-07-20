<center> 
<font color="red" size="8">
 CITEX 项目方API文档
</font>
</center>

## 请求地址(base)：

```
https://apiproject.citex.me/
```

## 限流
所有API请求为600次/min。如果请求过多会导致失败。建议每次请求确认请求成功状态。

apikey 为限流凭证

## API-KEY填写规则
API-KEY:apikey



## 公用接口

```
1.获取所有交易对
2.获取所有币种信息
3.获取系统时间戳
4.获取单个交易对orderbook
5.获取所有交易对行情
6.获取K线数据
```


## 认证接口
```
1.查询用户币币账户余额
2.委托下单
3.撤单
4.获取订单信息
5.获取委托记录
6.获取已成交记录
```

## 公用接口

### 1.获取系统时间戳

- 调用方法

``` 
GET:v1/common/timestamp
```
-  Headers

``` 
API-KEY:*******************************
```

-  返回成功示例：

```
{
    "code": 0,
    "msg": "success",
    "data": 1588059429693
}
```


-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
 code       |    int   |  返回状态
 message    | string    |   返回状态说明
 data       | object    |   时间戳（微秒）


<br>

### 2.获取所有交易对

- 调用方法

``` 
GET:v1/common/symbols
```
-  Headers

``` 
API-KEY:*******************************
```

-  返回成功示例：

```
{
    "code": 0,
    "msg": "success",
    "data": [
        {
            "contractId": 1,
            "symbol": "ETH-BTC",
            "minOrderAmt": "0.001",
            "priceTick": "0.000001",
            "lotSize": "0.001",
            "takerFeeRatio": "0.002",
            "makerFeeRatio": "0.002"
        },
        {
            "contractId": 3,
            "symbol": "ETH-USDT",
            "minOrderAmt": "10",
            "priceTick": "0.01",
            "lotSize": "0.00001",
            "takerFeeRatio": "0.002",
            "makerFeeRatio": "0.002"
        }
    ]
}
```


-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
 code       |    int   |  返回状态
 message    | string    |   返回状态说明
 data       | object    |   返回数据对象(List类型)
&#8195;&#8195; contractId       |    Integer   |  交易对ID
&#8195;&#8195; symbol       |    string   |  交易对名称
&#8195;&#8195; minOrderAmt       |    string   |  最小下单额
&#8195;&#8195; priceTick       |    string   |  最小报价单位
&#8195;&#8195; lotSize       |    string   |  最小交易量单位
&#8195;&#8195; takerFeeRatio       |    string   |  taker 手续费
&#8195;&#8195; makerFeeRatio       |    string   |  maker 手续费


<br>

### 3.获取所有币种信息

- 调用方法

``` 
GET:v1/common/currencys
```
-  Headers

``` 
API-KEY:*******************************
```

-  返回成功示例：

```
{
    "code": 0,
    "msg": "success",
    "data": [
        {
            "symbol": "ETH",
            "enabled": 0
        },
        {
            "symbol": "BTC",
            "enabled": 0
        }
    ]
}
```


-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
 code       |    int   |  返回状态
 message    | string    |   返回状态说明
 data       | object    |   返回数据对象(List类型)
&#8195;&#8195; symbol       |    string   |  币种名称
&#8195;&#8195; enabled       |    Integer   |  0：已开启  1：已关闭


<br>

### 4.获取单个交易对out book

- 调用方法

``` 
GET:v1/common/snapshot/{symbol}
```
-  Headers

``` 
API-KEY:*******************************
```

- 请求参数

 参数   |   必填   |   类型        |        描述   
 ------------ | ------------ |-------------|-----------
symbol       |  必选    |    String   |  交易对名称

- 请求示例

```
v1/common/snapshot/ETH-BTC
```

-  返回成功示例：

```
{
    "code": 0,
    "msg": "success",
    "data": {
        "symbol": "ETH-BTC",
        "bids": [
            {
                "price": "0.025218",
                "quantity": "0.587"
            }
        ],
        "asks": [
            {
                "price": "0.02525",
                "quantity": "0.5"
            }
        ]
    }
}
```


-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
code       |    int   |  返回状态
message    | string    |   返回状态说明
data       | object    |   返回数据对象(Object类型)
&#8195;&#8195;symbol       |    string   |  交易对名称
&#8195;&#8195;bids       |    List   |  最大50单
&#8195;&#8195;&#8195;&#8195; price       |    String   |  价格
&#8195;&#8195;&#8195;&#8195; quantity       |    String   |  数量
&#8195;&#8195;asks       |    List   |  最大50单
&#8195;&#8195;&#8195;&#8195; price       |    String   |  价格
&#8195;&#8195;&#8195;&#8195; quantity       |    String   |  数量


<br>

### 5.获取所有交易对行情

- 调用方法

``` 
GET:v1/common/allticker
```
-  Headers

``` 
API-KEY:*******************************
```

- 请求参数

 参数   |   必填   |   类型        |        描述   
 ------------ | ------------ |-------------|-----------
symbol       |  可选     |    String   |  交易对名称

- 请求示例

```
v1/common/allticker?symbol=ETH_BTC
```



-  返回成功示例：

```
{
    "code": 0,
    "msg": "success",
    "data": {
        "date": 1588060727755,
        "ticker": [
            {
                "symbol": "eth_btc",
                "high": "0.025251",
                "vol": "8346.23",
                "last": "0.025218",
                "low": "0.025005",
                "buy": "0.025186",
                "sell": "0.02525",
                "change": "0.0046"
            }
        ]
    }
}
```


-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
code       |    int   |  返回状态
message    | string    |   返回状态说明
data       | object    |   返回数据对象(Object类型)
&#8195;&#8195;date       |    long   |  时间(微妙)
&#8195;&#8195;ticker       |    List   |  
&#8195;&#8195;&#8195;&#8195; symbol       |    String   |  交易名称
&#8195;&#8195;&#8195;&#8195; high       |    String   |  最高价
&#8195;&#8195;&#8195;&#8195; vol       |    String   |  成交量（最近24H成交）
&#8195;&#8195;&#8195;&#8195; last       |    String   |  最新成交价
&#8195;&#8195;&#8195;&#8195; low       |    String   |  最低价
&#8195;&#8195;&#8195;&#8195; buy       |    String   |  买一价
&#8195;&#8195;&#8195;&#8195; sell       |    String   |  卖一价
&#8195;&#8195;&#8195;&#8195; change       |    String   |  涨跌幅



<br>

### 6.获取K线数据

- 调用方法

``` 
GET:v1/common/candlestick
```
-  Headers

``` 
API-KEY:*******************************
```

- 请求参数

 参数   |   必填   |   类型        |        描述   
 ------------ | ------------ |-------------|-----------
symbol       |   必填    |    String   |  交易对名称
type       |  可选     |    Integer   |  默认 1(1min). (1,3,5,15,30,60,120,240,360,1440)
size       |  可选     |    Integer   |  默认10条记录

- 请求示例

```
v1/common/candlestick?symbol=ETH_BTC
```



-  返回成功示例：

```
[
    [
        1588061580000,
        "0.025202",
        "0.025205",
        "0.025201",
        "0.025205",
        "3.752"
    ]
    ...
]
```


-  返回说明

 类型        |        描述   
 -------------|-----------
long   |  时间戳(微秒)
String    |   开盘价
String    |  最高价
String    |  最低价
String    |  收盘价
String    |  成交量 

<br/>

## 认证接口


### 1.委托下单

- 调用方法

``` 
POST:v1/order/orders/place
```
-  Headers

``` 
API-KEY:*******************************
```

- Body请求参数

 参数   |   必填   |   类型        |        描述   
 ------------ | ------------ |-------------|-----------
contractId       |   必填    |    String   |  合约ID
side       | 必填     |    String   |  委托方向 1：买  -1：卖
price       |  必填     |    String   |  委托价格
quantity       |  必填     |    String   |  委托数量
orderType       |  必填     |    String   |  委托类型 1：限价单 3：市价单
timeInForce       |  必填     |    String   |  订单有效时期类型 默认：2

- 请求示例

```
{
	"orderType": "1",
	"side": "1",
	"quantity": "1000",
	"price": "0.00963",
	"contractId": "15",
	"timeInForce": "2"
}
```



-  返回成功示例：

```
{
	"code": 0,
	"msg": "success",
	"data": "1587348404927348"
}
```

-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
code       |    int   |  返回状态
message    | string    |   返回状态说明
data       | object    |   委托号

<br/>

### 2.撤单

- 调用方法

``` 
POST:v1/order/orders/cancel
```
-  Headers

``` 
API-KEY:*******************************
```

- Body请求参数

 参数   |   必填   |   类型        |        描述   
 ------------ | ------------ |-------------|-----------
contractId       |   必填    |    String   |  合于ID
orderId       |  必填     |    String   |  委托号

- 请求示例

```
{
	"contractId": "15",
	"orderId": "1587348404927348"
}
```



-  返回成功示例：

```
{
	"code": 0,
	"msg": "success",
	"data": null
}
```

-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
code       |    int   |  返回状态
message    | string    |   返回状态说明
data       | object    |   



<br/>

### 3.查询用户币币账户余额

- 调用方法

``` 
GET:v1/account/balance
```
-  Headers

``` 
API-KEY:*******************************
```




-  返回成功示例：

```
{
    "code": 0,
    "msg": "success",
    "data": [
        {
            "currencyName": "ETH",
            "totalBalance": "563.216"
            "available": "563.216"
            "frozenForTrade": "0", 
        }
        ...
    ]
}
```

-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
code       |    int   |  返回状态
message    | string    |   返回状态说明
data       | list    |   余额对象
&#8195;&#8195; currencyName       |    String   |  币种名称
&#8195;&#8195; totalBalance       |    String   |  币种总数量
&#8195;&#8195; available       |    String   |  币种可用数量
&#8195;&#8195; frozenForTrade       |    String   |   币种冻结数量


<br/>

### 4.获取订单信息

- 调用方法

``` 
GET:v1/order/orders/{orderId}
```
-  Headers

``` 
API-KEY:*******************************
```

- 请求参数

 参数   |   必填   |   类型        |        描述   
 ------------ | ------------ |-------------|-----------
orderId       |   必填    |    String   |  委托号


- 请求示例

```
v1/order/orders/1587348404927348
```



-  返回成功示例：

```
{
	"code": 0,
	"msg": "success",
	"data": {
		"timestamp": 1588062955351066,
		"contractId": 15,
		"symbol": "CTT-USDT",
		"side": 1,
		"price": "0.00963",
		"quantity": "1000",
		"orderType": 1,
		"timeInForce": 1,
		"orderStatus": 6,
		"filledQuantity": "0",
		"makerFeeRatio": "0.002",
		"takerFeeRatio": "0.002"
	}
}
```

-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
code       |    int   |  返回状态
message    | string    |   返回状态说明
data       | Object    |   订单对象
&#8195;&#8195; timestamp       |    Long   |  时间戳（微秒）
&#8195;&#8195; contractId       |    Integer   |  合于ID
&#8195;&#8195; symbol       |    String   |  交易对名称
&#8195;&#8195; side       |    Integer   |   买卖方向 1：买  -1：卖
&#8195;&#8195; price       |    String   |   委托价
&#8195;&#8195; quantity       |    String   |   委托数量
&#8195;&#8195; orderType       |    Integer   |   委托类型 1：限价单 3：市价单
&#8195;&#8195; timeInForce       |    Integer   |   订单有效时期类型
&#8195;&#8195; orderStatus       |    Integer   |   委托状态<br/>0为未申报<br/>1为正在申报<br/>2为未成交<br/>3为部分成交<br/>4为完全成交<br/> 5为部分成交部分撤单<br/>6为已撤<br/>7为撤单<br/>8为失效
&#8195;&#8195; filledQuantity       |    String   |   已成交数量
&#8195;&#8195; makerFeeRatio       |    String   |   maker 手续费
&#8195;&#8195; takerFeeRatio       |    String   |   taker 手续费


<br/>

### 5.获取委托记录

- 调用方法

``` 
GET:v1/order/list
```
-  Headers

``` 
API-KEY:*******************************
```



-  返回成功示例：

```
{
	"code": 0,
	"msg": "success",
	"data": [{
		"symbol": "CTT-USDT",
		"orderId": "1587348399596427",
		"price": "0.00963",
		"quantity": "1000",
		"executedQty": "0",
		"matchStatus": "1",
		"orderType": "1",
		"side": "1",
		"orderTime": "1588055843017297"
	}]
}
```

-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
code       |    int   |  返回状态
message    | string    |   返回状态说明
data       | Object    |   订单对象
&#8195;&#8195; symbol       |    String   |  交易对名称
&#8195;&#8195; orderId       |    String   |   委托号
&#8195;&#8195; price       |    String   |   委托价
&#8195;&#8195; quantity       |    String   |   委托数量
&#8195;&#8195; executedQty       |    String   |   已成交数量
&#8195;&#8195; matchStatus       |    String   |   订单状态<br/>0为未申报<br/>1为未成交<br/>3为部分成交<br/>4为完全成交<br/>5为部分成交部分撤单<br/>6为已撤<br/>7为撤单中<br/>8为失效。
&#8195;&#8195; orderType       |    String   |  委托类型 1：限价单 3：市价单
&#8195;&#8195; side       |    String   |  买卖方向 1：买  -1：卖
&#8195;&#8195; orderTime       |    String   |  委托时间


<br/>

### 6.获取已成交记录

- 调用方法

``` 
GET:/order/{contractId}/history
```
-  Headers

``` 
API-KEY:*******************************
```

- 请求参数

 参数   |   必填   |   类型        |        描述   
 ------------ | ------------ |-------------|-----------
contractId       |   必填    |    String   |  合约ID


- 请求示例

```
/order/15/history
```


-  返回成功示例：

```
{
    "code": 0,
    "msg": "success",
    "data":[
        {
	        "orderId": "134584156458", 
            "symbol": "LTC-BTC",
		    "matchPrice": "0.1",
		    "matchQty": "1.0",
		    "fee": "0.5",
		    "feeCurrency": "BTC",
		    "matchTime": "15489419849",
		    "side": "1",
		    "orderType":”1”,
	    }
	]
}
```

-  返回说明

 参数                      |     类型        |        描述   
 ------------ |-------------|-----------
code       |    int   |  返回状态
message    | string    |   返回状态说明
data       | List    |   订单对象
&#8195;&#8195; orderId       |    String   |   委托号
&#8195;&#8195; symbol       |    String   |  交易对名称
&#8195;&#8195; matchPrice       |    String   |   成交价
&#8195;&#8195; matchQty       |    String   |   成交数量
&#8195;&#8195; fee       |    String   |   手续费
&#8195;&#8195; feeCurrency       |    String   |  手续费币种名称
&#8195;&#8195; matchTime       |    String   |  成交时间(微秒)
&#8195;&#8195; side       |    String   |  买卖方向 1：买  -1：卖
&#8195;&#8195; orderType       |    String   |  委托类型 1：限价单 3：市价单

<br>

## 错误码

错误码     |        描述   
---------- |  ---------
0      | 成功
2001   | 参数错误
2002   | 时间戳格式错误
2003   | accesskey 无效
2004   | accesskey 没有权限
2005   | 签名非法
2006   | ip地址错误
3001   | 委托类型错误
3002   | 委托方向错误
3003   | time in force 错误
3004   | 交易对错误
3005   | 委托号错误
3006   | 委托号为空

<br>

## 安全认证

目前关于apikey申请和修改，请联系CITEX工作人员。其中AccessKey为API 访问密钥，SecretKey为用户对请求进行签名的密钥（仅申请成功后邮件可见）。

<font color="red">
重要提示：这两个密钥与账号安全紧密相关，无论何时都请勿向其它人透露
</font>

### 合法请求结构

基于安全考虑，除行情API 外的 API请求都必须进行签名运算。一个合法的请求由以下几部分组成：

•	加密请求地址：'api.citex.io' 后面跟上方法名，比如'api.citex.io' + /v1/order/orders/15485146161498。

•	API 访问密钥（AccessKeyId） 您申请的 APIKEY 中的AccessKey。

•	签名方法（Signature Method） 用户计算签名的基于哈希的协议，此处使用 HmacSHA256。

•	签名版本（Signature Version） 签名协议的版本，此处使用2。

•	时间戳（Timestamp） 您发出请求的时间 (UTC 时区) (UTC 时区) (UTC 时区) 。在查询请求中包含此值有助于防止第三方截取您的请求。如：2017-05-11T16:22:06。再次强调是 (UTC 时区) 。

•	必选和可选参数 每个方法都有一组用于定义 API 调用的必需参数和可选参数。可以在每个方法的说明中查看这些参数及其含义。 请一定注意：对于GET请求，每个方法自带的参数都需要进行签名运算； 对于POST请求，每个方法自带的参数不进行签名认证，即POST请求中需要进行签名运算的只有AccessKeyId、SignatureMethod、SignatureVersion、Timestamp四个参数，其它参数放在body中, 传body参数请转换json格式。

•	签名 签名计算得出的值，用于确保签名有效和未被篡改。

<br/>
请求示例

```
api.citex.io/v1/order/orders/15485146161498?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06&Signature=41OKsrDrG%2BizHgziwi00RbXjV3KURYXXp//7HqpciOc%3D
```

并且添加API-KEY到请求头headers中


### 签名运算
API请求在通过Internet发送的过程中极有可能被篡改。为了确保请求未被更改，我们会要求用户在每个请求中带上签名（行情API除外），来校验参数或参数值在传输途中是否发生了更改。

#### 计算签名所需的步骤
<br>
1.规范要计算签名的请求 因为使用 HMAC进行签名计算时，使用不同内容计算得到的结果会完全不同。所以在进行签名计算前，请先对请求进行规范化处理。下面以查询某订单详情请求为例进行说明


```
https://api.citex.io/v1/order/orders/15485146161498?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06&Signature=41OKsrDrG%2BizHgziwi00RbXjV3KURYXXp//7HqpciOc%3D
```
请求方法（GET或POST），后面添加换行符\n


```
GET\n
```


2.	添加小写的访问地址，后面添加换行符\n。
	

```
api.citex.io\n
```


3.	访问方法的路径，后面添加换行符\n。


```
/v1/order/orders/15485146161498\n
```


4.	按照ASCII码的顺序对参数名进行排序(使用 UTF-8 编码，且进行了 URLENCODE 编码，十六进制字符必须大写，如‘:’会被编码为'%3A'，空格被编码为'%20')。 例如，下面是请求参数的原始顺序，进行过编码后。


```
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx
SignatureMethod=HmacSHA256
SignatureVersion=2
Timestamp=2019-06-20T09%3A38%3A06
```

这些参数会被排序为：

```
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx
SignatureMethod=HmacSHA256
SignatureVersion=2
Timestamp=2019-06-20T09%3A38%3A06
```

按照以上顺序，将各参数使用字符'&'连接。

```
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06
```

组成最终的要进行签名计算的字符串如下：

```
GET\n
api.citex.io\n
/v1/order/orders/15485146161498\n
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06
```

5.	使用HmacSHA256计算签名，将以下两个参数传入加密哈希函数：

a.要进行签名计算的字符串


```
GET\n
api.citex.io\n
/v1/order/orders/15485146161498\n
AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06
```

b. 进行签名的密钥（SecretKey）
    
```
b0xxxxxx-c6xxxxxx-94xxxxxx-dxxxx
```

得到签名计算结果并进行 Base64编码并且进行URLENCODE 编码

```
41OKsrDrG%2BizHgziwi00RbXjV3KURYXXp//7HqpciOc%3D
```

将此参数添加到请求前，必须将该值进行 URLENCODE 编码。然后将上述值作为参数Signature的取值添加到 API 请求中。

6.	最终，发送到服务器的 API 请求应该为：

```
https://apiproject.citex.me/v1/order/orders/15485146161498?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06&Signature=41OKsrDrG%2BizHgziwi00RbXjV3KURYXXp//7HqpciOc%3D
```

以上边参数为例，如请求BALANCE余额(不包含order id)，请求链接如下：

```
https://apiproject.citex.me/v1/account/balance?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-06-20T09%3A38%3A06&Signature=ydOk2DwcpAcujVnfPmsJDXn8b7Wl9HCDay98Bs82pa0%3D
```

