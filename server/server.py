
import uuid
import grpc
from concurrent import futures
import msg_struct_pb2_grpc as msg_grpc
import msg_struct_pb2 as msg
import time
import random
from http.server import BaseHTTPRequestHandler,HTTPServer
import json


from google import auth as google_auth
from google.auth import jwt as google_auth_jwt
from google.auth.transport import grpc as google_auth_transport_grpc

_HOST = "localhost"
_GRPC_PORT = 50051
_HTTP_PORT = 8081
_ONE_DAY_IN_SECONDS = 60*60*24
_HEALTH = {'status': 'OK'}
_HEADER_CONTENT_LENGTH = "Content-Length"
_HEADER_CONTENT_TYPE = "Content-Type"
_HEADER_APP_JSON = "application/json"

_GIT_WEBHOOK_LIST = []
_HEADERS = str()
_PAYLOAD = str()

class ChannelServicerProvider(msg_grpc.ChannelServicer):
    """ this is implementation class for generated Channel Servicer"""
    def ServerCall(self,request,context):
        print("Client: " + request.data + "Registered")
        while True:
            time.sleep(1)
            if len(_GIT_WEBHOOK_LIST) == 0:
                pass
            else:
                yield _GIT_WEBHOOK_LIST.pop(0)

class Server(BaseHTTPRequestHandler):

    """ HTTP GET METHOD """
    def do_GET(self):
        print("LOG:GET@ "+str(time.time()))
        self.send_response(200)
        self.send_header(_HEADER_CONTENT_TYPE, _HEADER_APP_JSON)
        self.end_headers()
        self.wfile.write(bytes(json.dumps(_HEALTH), 'UTF-8'))

    """ HTTP POST METHOD """
    def do_POST(self):
        print("LOG:POST@ "+str(time.time()) + " Headers: " + str(self.headers))
        _HEADERS = str(self.headers)
        content_length = int(self.headers[_HEADER_CONTENT_LENGTH])
        post_data = self.rfile.read(content_length)
        data = post_data.decode("utf-8")
        _PAYLOAD = data
        responsor = msg.Responsor(
            id=str(uuid.uuid4()),
            timestamp=str(time.time()*1000),
            headers=_HEADERS,
            payload=_PAYLOAD
        )
        _GIT_WEBHOOK_LIST.append(responsor)

        self.send_response(200)
        self.send_header(_HEADER_CONTENT_TYPE, _HEADER_APP_JSON)
        self.end_headers()
        self.wfile.write(bytes(data,'UTF-8'))


def serve():
    print("Starting GRPC server...")
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        options=(
            ('grpc.keepalive_time_ms', 10000),
            ('grpc.keepalive_timeout_ms', 5000),
            ('grpc.keepalive_permit_without_calls', True),
            ('grpc.http2.max_pings_without_data', 0),
            ('grpc.http2.min_time_between_pings_ms', 10000),
            ('grpc.http2.min_ping_interval_without_data_ms',  5000),
        )
    )
    msg_grpc.add_ChannelServicer_to_server(ChannelServicerProvider() , server)

    # server.add_secure_port(_HOST + ":" + str(_GRPC_PORT),creds)
    server.add_insecure_port(_HOST + ":" + str(_GRPC_PORT))
    server.start()
    """ Start serving http content on port 8081 """
    http_server = HTTPServer((_HOST,_HTTP_PORT),Server)
    http_server.serve_forever()
    """ Start serving grpc content on port 50051 """
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()