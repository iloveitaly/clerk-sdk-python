"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import TypedDict


class Type(str, Enum):
    OAUTH_GOOGLE = "oauth_google"
    OAUTH_MOCK = "oauth_mock"
    SAML = "saml"
    OAUTH_DISCORD = "oauth_discord"
    OAUTH_APPLE = "oauth_apple"

class IdentificationLinkTypedDict(TypedDict):
    type: Type
    id: str
    

class IdentificationLink(BaseModel):
    type: Type
    id: str
    
