"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .organizationinvitations import OrganizationInvitations, OrganizationInvitationsTypedDict
from clerk.types import BaseModel
from clerk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Callable, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListPendingOrganizationInvitationsRequestTypedDict(TypedDict):
    organization_id: str
    r"""The organization ID."""
    limit: NotRequired[float]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[float]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    

class ListPendingOrganizationInvitationsRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The organization ID."""
    limit: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    

class ListPendingOrganizationInvitationsResponseTypedDict(TypedDict):
    result: OrganizationInvitationsTypedDict
    

class ListPendingOrganizationInvitationsResponse(BaseModel):
    next: Callable[[], Optional[ListPendingOrganizationInvitationsResponse]]
    
    result: OrganizationInvitations
    