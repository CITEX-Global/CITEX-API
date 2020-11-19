import websocket
import time
import gzip
import zlib
import json
import io
import base64

class test_ws_client:
    def __init__(self, base_url):
        self.url = base_url
        self.ws = websocket.create_connection(self.url)

    def recv(self):

        topic1 = '42["subscribe",{"args":[{"topic":"snapshot","params":{"contractId":1,"depth":30}}]}]'#订阅深度
        # topic2 = '42["subscribe",{"args":[{"topic":"tick","params":{"contractId":1}}]}]'#订阅tick
        self.ws.send(topic1)
        while True:
            try:
                compress_data = self.ws.recv()
                if type(compress_data) == bytes:

                    msg = json.loads(zlib.decompress(compress_data[1:], zlib.MAX_WBITS|32))

                    print(msg)
            except Exception as e:
                print(e)


if __name__ == '__main__':

    base_url = "wss://socket.citex.me/socket.io/?EIO=3&transport=websocket"

    test_ws_client(base_url).recv()
