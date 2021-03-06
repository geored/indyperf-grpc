# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg-struct.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg-struct.proto',
  package='broute',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10msg-struct.proto\x12\x06\x62route\"\x19\n\tRequestor\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"L\n\tResponsor\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x0f\n\x07headers\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\t2;\n\x07\x43hannel\x12\x30\n\nServerCall\x12\r.broute.Empty\x1a\x11.broute.Responsor\"\x00\x62\x06proto3')
)




_REQUESTOR = _descriptor.Descriptor(
  name='Requestor',
  full_name='broute.Requestor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='broute.Requestor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=53,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='broute.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=62,
)


_RESPONSOR = _descriptor.Descriptor(
  name='Responsor',
  full_name='broute.Responsor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='broute.Responsor.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='broute.Responsor.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headers', full_name='broute.Responsor.headers', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='broute.Responsor.payload', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['Requestor'] = _REQUESTOR
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Responsor'] = _RESPONSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Requestor = _reflection.GeneratedProtocolMessageType('Requestor', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTOR,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:broute.Requestor)
  ))
_sym_db.RegisterMessage(Requestor)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:broute.Empty)
  ))
_sym_db.RegisterMessage(Empty)

Responsor = _reflection.GeneratedProtocolMessageType('Responsor', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSOR,
  __module__ = 'msg_struct_pb2'
  # @@protoc_insertion_point(class_scope:broute.Responsor)
  ))
_sym_db.RegisterMessage(Responsor)



_CHANNEL = _descriptor.ServiceDescriptor(
  name='Channel',
  full_name='broute.Channel',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=142,
  serialized_end=201,
  methods=[
  _descriptor.MethodDescriptor(
    name='ServerCall',
    full_name='broute.Channel.ServerCall',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_RESPONSOR,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHANNEL)

DESCRIPTOR.services_by_name['Channel'] = _CHANNEL

# @@protoc_insertion_point(module_scope)
