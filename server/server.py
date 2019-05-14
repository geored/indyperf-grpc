
import grpc
from concurrent import futures
import msg_struct_pb2_grpc as msg_grpc
import msg_struct_pb2 as msg_
import time
import logging

_ONE_DAY_IN_SECONDS = 60*60*24

with open('server.key', 'rb') as f:
    private_key = f.read()

with open('server.crt', 'rb') as f:
    certificate_chain = f.read()


class ChannelServicerProvider(msg_grpc.ChannelServicer):
    """ this is implementation class for generated Channel Servicer"""
    def ServerCall(self,request,context):
        return msg_.Responsor(id='1',timestamp='2',headers='3',payload='test')


def serve():
    logging.warning("Starting GRPC server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    msg_grpc.add_ChannelServicer_to_server(ChannelServicerProvider() , server)
    creds = grpc.ssl_server_credentials(((private_key, certificate_chain,),))

    server.add_secure_port("localhost:50051",creds)
    # server.add_insecure_port(_HOST + ":" + str(_GRPC_PORT))
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()