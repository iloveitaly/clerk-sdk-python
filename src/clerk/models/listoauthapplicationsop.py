"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .oauthapplications import OAuthApplications, OAuthApplicationsTypedDict
from clerk.types import BaseModel
from clerk.utils import FieldMetadata, QueryParamMetadata
from typing import Callable, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListOAuthApplicationsRequestTypedDict(TypedDict):
    limit: NotRequired[float]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[float]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    

class ListOAuthApplicationsRequest(BaseModel):
    limit: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    

class ListOAuthApplicationsResponseTypedDict(TypedDict):
    result: OAuthApplicationsTypedDict
    

class ListOAuthApplicationsResponse(BaseModel):
    next: Callable[[], Optional[ListOAuthApplicationsResponse]]
    
    result: OAuthApplications
    