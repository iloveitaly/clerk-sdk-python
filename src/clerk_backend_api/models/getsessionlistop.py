"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class QueryParamStatus(str, Enum):
    r"""Filter sessions by the provided status"""
    ABANDONED = "abandoned"
    ACTIVE = "active"
    ENDED = "ended"
    EXPIRED = "expired"
    REMOVED = "removed"
    REPLACED = "replaced"
    REVOKED = "revoked"

class GetSessionListRequestTypedDict(TypedDict):
    client_id: NotRequired[str]
    r"""List sessions for the given client"""
    user_id: NotRequired[str]
    r"""List sessions for the given user"""
    status: NotRequired[QueryParamStatus]
    r"""Filter sessions by the provided status"""
    limit: NotRequired[float]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[float]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    

class GetSessionListRequest(BaseModel):
    client_id: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""List sessions for the given client"""
    user_id: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""List sessions for the given user"""
    status: Annotated[Optional[QueryParamStatus], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Filter sessions by the provided status"""
    limit: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    
