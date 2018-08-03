# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/ad_group_type.proto

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
  name='google/ads/googleads_v0/proto/enums/ad_group_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n7google/ads/googleads_v0/proto/enums/ad_group_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"b\n\x0f\x41\x64GroupTypeEnum\"O\n\x0b\x41\x64GroupType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x13\n\x0fSEARCH_STANDARD\x10\x02\x12\r\n\tHOTEL_ADS\x10\x06\x42\xc1\x01\n!com.google.ads.googleads.v0.enumsB\x10\x41\x64GroupTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_ADGROUPTYPEENUM_ADGROUPTYPE = _descriptor.EnumDescriptor(
  name='AdGroupType',
  full_name='google.ads.googleads.v0.enums.AdGroupTypeEnum.AdGroupType',
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
      name='SEARCH_STANDARD', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOTEL_ADS', index=3, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=109,
  serialized_end=188,
)
_sym_db.RegisterEnumDescriptor(_ADGROUPTYPEENUM_ADGROUPTYPE)


_ADGROUPTYPEENUM = _descriptor.Descriptor(
  name='AdGroupTypeEnum',
  full_name='google.ads.googleads.v0.enums.AdGroupTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADGROUPTYPEENUM_ADGROUPTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=188,
)

_ADGROUPTYPEENUM_ADGROUPTYPE.containing_type = _ADGROUPTYPEENUM
DESCRIPTOR.message_types_by_name['AdGroupTypeEnum'] = _ADGROUPTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupTypeEnum = _reflection.GeneratedProtocolMessageType('AdGroupTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPTYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.ad_group_type_pb2'
  ,
  __doc__ = """Defines types of an ad group, specific to a particular campaign channel
  type. This type drives validations that restrict which entities can be
  added to the ad group.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.AdGroupTypeEnum)
  ))
_sym_db.RegisterMessage(AdGroupTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\020AdGroupTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
