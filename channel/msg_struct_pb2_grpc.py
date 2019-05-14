# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import msg_struct_pb2 as msg__struct__pb2


class ChannelStub(object):
  """Channel Service for comminication between client and server
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ServerCall = channel.unary_unary(
        '/broute.Channel/ServerCall',
        request_serializer=msg__struct__pb2.Empty.SerializeToString,
        response_deserializer=msg__struct__pb2.Responsor.FromString,
        )


class ChannelServicer(object):
  """Channel Service for comminication between client and server
  """

  def ServerCall(self, request, context):
    """Server Call connection
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChannelServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ServerCall': grpc.unary_unary_rpc_method_handler(
          servicer.ServerCall,
          request_deserializer=msg__struct__pb2.Empty.FromString,
          response_serializer=msg__struct__pb2.Responsor.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'broute.Channel', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
