"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetPublicInterstitialRequestTypedDict(TypedDict):
    frontend_api: NotRequired[str]
    r"""The Frontend API key of your instance"""
    publishable_key: NotRequired[str]
    r"""The publishable key of your instance"""
    

class GetPublicInterstitialRequest(BaseModel):
    frontend_api: Annotated[Optional[str], pydantic.Field(alias="frontendApi"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""The Frontend API key of your instance"""
    publishable_key: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""The publishable key of your instance"""
    
