"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel
from clerk.utils import FieldMetadata, PathParamMetadata
from enum import Enum
from typing import TypedDict
from typing_extensions import Annotated


class RevertTemplatePathParamTemplateType(str, Enum):
    r"""The type of template to revert"""
    EMAIL = "email"
    SMS = "sms"


class RevertTemplateRequestTypedDict(TypedDict):
    template_type: RevertTemplatePathParamTemplateType
    r"""The type of template to revert"""
    slug: str
    r"""The slug of the template to revert"""
    

class RevertTemplateRequest(BaseModel):
    template_type: Annotated[RevertTemplatePathParamTemplateType, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The type of template to revert"""
    slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The slug of the template to revert"""
    