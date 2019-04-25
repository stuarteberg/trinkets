# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: neuclease/dvid/keyvalue/ingest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='neuclease/dvid/keyvalue/ingest.proto',
  package='keyvalue',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$neuclease/dvid/keyvalue/ingest.proto\x12\x08keyvalue\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\x14\n\x04Keys\x12\x0c\n\x04keys\x18\x01 \x03(\t\",\n\tKeyValues\x12\x1f\n\x03kvs\x18\x01 \x03(\x0b\x32\x12.keyvalue.KeyValueb\x06proto3')
)




_KEYVALUE = _descriptor.Descriptor(
  name='KeyValue',
  full_name='keyvalue.KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='keyvalue.KeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='keyvalue.KeyValue.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=50,
  serialized_end=88,
)


_KEYS = _descriptor.Descriptor(
  name='Keys',
  full_name='keyvalue.Keys',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='keyvalue.Keys.keys', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=90,
  serialized_end=110,
)


_KEYVALUES = _descriptor.Descriptor(
  name='KeyValues',
  full_name='keyvalue.KeyValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kvs', full_name='keyvalue.KeyValues.kvs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=112,
  serialized_end=156,
)

_KEYVALUES.fields_by_name['kvs'].message_type = _KEYVALUE
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['Keys'] = _KEYS
DESCRIPTOR.message_types_by_name['KeyValues'] = _KEYVALUES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUE,
  __module__ = 'neuclease.dvid.keyvalue.ingest_pb2'
  # @@protoc_insertion_point(class_scope:keyvalue.KeyValue)
  ))
_sym_db.RegisterMessage(KeyValue)

Keys = _reflection.GeneratedProtocolMessageType('Keys', (_message.Message,), dict(
  DESCRIPTOR = _KEYS,
  __module__ = 'neuclease.dvid.keyvalue.ingest_pb2'
  # @@protoc_insertion_point(class_scope:keyvalue.Keys)
  ))
_sym_db.RegisterMessage(Keys)

KeyValues = _reflection.GeneratedProtocolMessageType('KeyValues', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUES,
  __module__ = 'neuclease.dvid.keyvalue.ingest_pb2'
  # @@protoc_insertion_point(class_scope:keyvalue.KeyValues)
  ))
_sym_db.RegisterMessage(KeyValues)


# @@protoc_insertion_point(module_scope)
