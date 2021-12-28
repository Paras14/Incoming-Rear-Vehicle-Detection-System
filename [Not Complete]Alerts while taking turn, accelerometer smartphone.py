from flask import Flask
from flask_sockets import Sockets
import socket
import time

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

hostname = socket.gethostname()
IPAddr = get_ip()

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/accelerometer')
def echo_socket(ws):
    while True:
        message = ws.receive()
        tupinfo = eval(message)
        #print(tupinfo[0])
        xstr = str(tupinfo[0])
        x_acc = float(xstr)
        if x_acc > 1.5:
            print("turned RIGHT")
            time.sleep(0.5)
        elif x_acc < -1.5:
            print("turned LEFT")
            time.sleep(0.5)
        else:
            pass
            


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(
        ('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
