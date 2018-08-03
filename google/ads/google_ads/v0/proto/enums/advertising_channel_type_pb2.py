# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/advertising_channel_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/advertising_channel_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\nBgoogle/ads/googleads_v0/proto/enums/advertising_channel_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"k\n\x1a\x41\x64vertisingChannelTypeEnum\"M\n\x16\x41\x64vertisingChannelType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06SEARCH\x10\x02\x12\t\n\x05HOTEL\x10\x05\x42\xcc\x01\n!com.google.ads.googleads.v0.enumsB\x1b\x41\x64vertisingChannelTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_ADVERTISINGCHANNELTYPEENUM_ADVERTISINGCHANNELTYPE = _descriptor.EnumDescriptor(
  name='AdvertisingChannelType',
  full_name='google.ads.googleads.v0.enums.AdvertisingChannelTypeEnum.AdvertisingChannelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOTEL', index=3, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=131,
  serialized_end=208,
)
_sym_db.RegisterEnumDescriptor(_ADVERTISINGCHANNELTYPEENUM_ADVERTISINGCHANNELTYPE)


_ADVERTISINGCHANNELTYPEENUM = _descriptor.Descriptor(
  name='AdvertisingChannelTypeEnum',
  full_name='google.ads.googleads.v0.enums.AdvertisingChannelTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADVERTISINGCHANNELTYPEENUM_ADVERTISINGCHANNELTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=208,
)

_ADVERTISINGCHANNELTYPEENUM_ADVERTISINGCHANNELTYPE.containing_type = _ADVERTISINGCHANNELTYPEENUM
DESCRIPTOR.message_types_by_name['AdvertisingChannelTypeEnum'] = _ADVERTISINGCHANNELTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdvertisingChannelTypeEnum = _reflection.GeneratedProtocolMessageType('AdvertisingChannelTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADVERTISINGCHANNELTYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.advertising_channel_type_pb2'
  ,
  __doc__ = """The channel type a campaign may target to serve on.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.AdvertisingChannelTypeEnum)
  ))
_sym_db.RegisterMessage(AdvertisingChannelTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\033AdvertisingChannelTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
