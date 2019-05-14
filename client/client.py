

import grpc
import msg_struct_pb2 as msg_
import msg_struct_pb2_grpc as msg_grpc
import os
import time
import logging


def gen():
    for i in range(1,100):
        time.sleep(1)
        yield msg_.Empty()

def run():
    logging.warning("Establishing connection with server...")

    with open('server.crt', 'rb') as f:
        trusted_certs = f.read()
        credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
        channel = grpc.secure_channel(os.getenv("GRPC_SERVER","[::]:50051"), credentials)

        stub = msg_grpc.ChannelStub(channel)
        message = stub.ServerCall(msg_.Empty())
        try:
            logging.warning("Server Payload: {}".format(message))
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    run()
