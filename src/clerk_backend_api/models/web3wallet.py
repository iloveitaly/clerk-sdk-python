"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api import utils
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from clerk_backend_api.utils import validate_open_enum
from enum import Enum
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class Web3WalletObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    WEB3_WALLET = "web3_wallet"


class AdminVerificationWeb3WalletStatus(str, Enum):
    VERIFIED = "verified"


class AdminVerificationWeb3WalletStrategy(str, Enum, metaclass=utils.OpenEnumMeta):
    ADMIN = "admin"


class Web3WalletVerificationAdminTypedDict(TypedDict):
    status: AdminVerificationWeb3WalletStatus
    strategy: AdminVerificationWeb3WalletStrategy
    attempts: NotRequired[Nullable[int]]
    expire_at: NotRequired[Nullable[int]]


class Web3WalletVerificationAdmin(BaseModel):
    status: AdminVerificationWeb3WalletStatus

    strategy: Annotated[
        AdminVerificationWeb3WalletStrategy, PlainValidator(validate_open_enum(False))
    ]

    attempts: OptionalNullable[int] = UNSET

    expire_at: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["attempts", "expire_at"]
        nullable_fields = ["attempts", "expire_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class Web3SignatureVerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"


class Web3SignatureVerificationStrategy(str, Enum):
    WEB3_METAMASK_SIGNATURE = "web3_metamask_signature"
    WEB3_COINBASE_WALLET_SIGNATURE = "web3_coinbase_wallet_signature"


class Web3SignatureTypedDict(TypedDict):
    status: Web3SignatureVerificationStatus
    strategy: Web3SignatureVerificationStrategy
    nonce: NotRequired[Nullable[str]]
    message: NotRequired[Nullable[str]]
    attempts: NotRequired[Nullable[int]]
    expire_at: NotRequired[Nullable[int]]


class Web3Signature(BaseModel):
    status: Web3SignatureVerificationStatus

    strategy: Web3SignatureVerificationStrategy

    nonce: OptionalNullable[str] = UNSET

    message: OptionalNullable[str] = UNSET

    attempts: OptionalNullable[int] = UNSET

    expire_at: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["nonce", "message", "attempts", "expire_at"]
        nullable_fields = ["nonce", "message", "attempts", "expire_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


Web3WalletVerificationTypedDict = Union[
    Web3WalletVerificationAdminTypedDict, Web3SignatureTypedDict
]


Web3WalletVerification = Union[Web3WalletVerificationAdmin, Web3Signature]


class Web3WalletTypedDict(TypedDict):
    object: Web3WalletObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    web3_wallet: str
    verification: Nullable[Web3WalletVerificationTypedDict]
    created_at: int
    r"""Unix timestamp of creation

    """
    updated_at: int
    r"""Unix timestamp of creation

    """
    id: NotRequired[str]


class Web3Wallet(BaseModel):
    object: Web3WalletObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    web3_wallet: str

    verification: Nullable[Web3WalletVerification]

    created_at: int
    r"""Unix timestamp of creation

    """

    updated_at: int
    r"""Unix timestamp of creation

    """

    id: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id"]
        nullable_fields = ["verification"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
