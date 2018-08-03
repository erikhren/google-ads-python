# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/media_bundle_error.proto

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
  name='google/ads/googleads_v0/proto/errors/media_bundle_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n=google/ads/googleads_v0/proto/errors/media_bundle_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xb8\x05\n\x14MediaBundleErrorEnum\"\x9f\x05\n\x10MediaBundleError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x03\x12\"\n\x1e\x44OUBLECLICK_BUNDLE_NOT_ALLOWED\x10\x04\x12\x1c\n\x18\x45XTERNAL_URL_NOT_ALLOWED\x10\x05\x12\x12\n\x0e\x46ILE_TOO_LARGE\x10\x06\x12.\n*GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED\x10\x07\x12\x11\n\rINVALID_INPUT\x10\x08\x12\x18\n\x14INVALID_MEDIA_BUNDLE\x10\t\x12\x1e\n\x1aINVALID_MEDIA_BUNDLE_ENTRY\x10\n\x12\x15\n\x11INVALID_MIME_TYPE\x10\x0b\x12\x10\n\x0cINVALID_PATH\x10\x0c\x12\x19\n\x15INVALID_URL_REFERENCE\x10\r\x12\x18\n\x14MEDIA_DATA_TOO_LARGE\x10\x0e\x12&\n\"MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY\x10\x0f\x12\x10\n\x0cSERVER_ERROR\x10\x10\x12\x11\n\rSTORAGE_ERROR\x10\x11\x12\x1d\n\x19SWIFFY_BUNDLE_NOT_ALLOWED\x10\x12\x12\x12\n\x0eTOO_MANY_FILES\x10\x13\x12\x13\n\x0fUNEXPECTED_SIZE\x10\x14\x12/\n+UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT\x10\x15\x12\x1d\n\x19UNSUPPORTED_HTML5_FEATURE\x10\x16\x12)\n%URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT\x10\x17\x12\x1b\n\x17\x43USTOM_EXIT_NOT_ALLOWED\x10\x18\x42\xcb\x01\n\"com.google.ads.googleads.v0.errorsB\x15MediaBundleErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_MEDIABUNDLEERRORENUM_MEDIABUNDLEERROR = _descriptor.EnumDescriptor(
  name='MediaBundleError',
  full_name='google.ads.googleads.v0.errors.MediaBundleErrorEnum.MediaBundleError',
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
      name='BAD_REQUEST', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLECLICK_BUNDLE_NOT_ALLOWED', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL_URL_NOT_ALLOWED', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE_TOO_LARGE', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE_WEB_DESIGNER_ZIP_FILE_NOT_PUBLISHED', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_INPUT', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MEDIA_BUNDLE', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MEDIA_BUNDLE_ENTRY', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MIME_TYPE', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PATH', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_URL_REFERENCE', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIA_DATA_TOO_LARGE', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_PRIMARY_MEDIA_BUNDLE_ENTRY', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVER_ERROR', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORAGE_ERROR', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWIFFY_BUNDLE_NOT_ALLOWED', index=17, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_FILES', index=18, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEXPECTED_SIZE', index=19, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_GOOGLE_WEB_DESIGNER_ENVIRONMENT', index=20, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_HTML5_FEATURE', index=21, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_IN_MEDIA_BUNDLE_NOT_SSL_COMPLIANT', index=22, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_EXIT_NOT_ALLOWED', index=23, number=24,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=123,
  serialized_end=794,
)
_sym_db.RegisterEnumDescriptor(_MEDIABUNDLEERRORENUM_MEDIABUNDLEERROR)


_MEDIABUNDLEERRORENUM = _descriptor.Descriptor(
  name='MediaBundleErrorEnum',
  full_name='google.ads.googleads.v0.errors.MediaBundleErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEDIABUNDLEERRORENUM_MEDIABUNDLEERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=794,
)

_MEDIABUNDLEERRORENUM_MEDIABUNDLEERROR.containing_type = _MEDIABUNDLEERRORENUM
DESCRIPTOR.message_types_by_name['MediaBundleErrorEnum'] = _MEDIABUNDLEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MediaBundleErrorEnum = _reflection.GeneratedProtocolMessageType('MediaBundleErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _MEDIABUNDLEERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.media_bundle_error_pb2'
  ,
  __doc__ = """Container for enum describing possible media bundle errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.MediaBundleErrorEnum)
  ))
_sym_db.RegisterMessage(MediaBundleErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\025MediaBundleErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
