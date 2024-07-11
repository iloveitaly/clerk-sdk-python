"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from clerk import models
from clerk._hooks import HookContext
from clerk.types import Nullable, UNSET
import clerk.utils as utils
from typing import Optional

class EmailAddresses(BaseSDK):
    
    
    def create(
        self, *,
        user_id: Optional[str] = None,
        email_address: Optional[str] = None,
        verified: Optional[Nullable[bool]] = None,
        primary: Optional[Nullable[bool]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.EmailAddress:
        r"""Create an email address

        Create a new email address

        :param user_id: The ID representing the user
        :param email_address: The new email address. Must adhere to the RFC 5322 specification for email address format.
        :param verified: When created, the email address will be marked as verified.
        :param primary: Create this email address as the primary email address for the user. Default: false, unless it is the first email address.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.CreateEmailAddressRequestBody(
            user_id=user_id,
            email_address=email_address,
            verified=verified,
            primary=primary,
        )
        
        req = self.build_request(
            method="POST",
            path="/email_addresses",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[models.CreateEmailAddressRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="CreateEmailAddress", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.EmailAddress])
        if utils.match_response(http_res, ["400","401","403","404","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def create_async(
        self, *,
        user_id: Optional[str] = None,
        email_address: Optional[str] = None,
        verified: Optional[Nullable[bool]] = None,
        primary: Optional[Nullable[bool]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.EmailAddress:
        r"""Create an email address

        Create a new email address

        :param user_id: The ID representing the user
        :param email_address: The new email address. Must adhere to the RFC 5322 specification for email address format.
        :param verified: When created, the email address will be marked as verified.
        :param primary: Create this email address as the primary email address for the user. Default: false, unless it is the first email address.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.CreateEmailAddressRequestBody(
            user_id=user_id,
            email_address=email_address,
            verified=verified,
            primary=primary,
        )
        
        req = self.build_request(
            method="POST",
            path="/email_addresses",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[models.CreateEmailAddressRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="CreateEmailAddress", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.EmailAddress])
        if utils.match_response(http_res, ["400","401","403","404","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def get(
        self, *,
        email_address_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.EmailAddress:
        r"""Retrieve an email address

        Returns the details of an email address.

        :param email_address_id: The ID of the email address to retrieve
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.GetEmailAddressRequest(
            email_address_id=email_address_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/email_addresses/{email_address_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="GetEmailAddress", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.EmailAddress])
        if utils.match_response(http_res, ["400","401","403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def get_async(
        self, *,
        email_address_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.EmailAddress:
        r"""Retrieve an email address

        Returns the details of an email address.

        :param email_address_id: The ID of the email address to retrieve
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.GetEmailAddressRequest(
            email_address_id=email_address_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/email_addresses/{email_address_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="GetEmailAddress", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.EmailAddress])
        if utils.match_response(http_res, ["400","401","403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def delete(
        self, *,
        email_address_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DeletedObject:
        r"""Delete an email address

        Delete the email address with the given ID

        :param email_address_id: The ID of the email address to delete
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.DeleteEmailAddressRequest(
            email_address_id=email_address_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/email_addresses/{email_address_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="DeleteEmailAddress", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeletedObject])
        if utils.match_response(http_res, ["400","401","403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def delete_async(
        self, *,
        email_address_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DeletedObject:
        r"""Delete an email address

        Delete the email address with the given ID

        :param email_address_id: The ID of the email address to delete
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.DeleteEmailAddressRequest(
            email_address_id=email_address_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/email_addresses/{email_address_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="DeleteEmailAddress", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeletedObject])
        if utils.match_response(http_res, ["400","401","403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def update(
        self, *,
        email_address_id: str,
        verified: Optional[Nullable[bool]] = None,
        primary: Optional[Nullable[bool]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.EmailAddress:
        r"""Update an email address

        Updates an email address.

        :param email_address_id: The ID of the email address to update
        :param verified: The email address will be marked as verified.
        :param primary: Set this email address as the primary email address for the user.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.UpdateEmailAddressRequest(
            email_address_id=email_address_id,
            request_body=models.UpdateEmailAddressRequestBody(
                verified=verified,
                primary=primary,
            ),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/email_addresses/{email_address_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, True, "json", Optional[models.UpdateEmailAddressRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="UpdateEmailAddress", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.EmailAddress])
        if utils.match_response(http_res, ["400","401","403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def update_async(
        self, *,
        email_address_id: str,
        verified: Optional[Nullable[bool]] = None,
        primary: Optional[Nullable[bool]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.EmailAddress:
        r"""Update an email address

        Updates an email address.

        :param email_address_id: The ID of the email address to update
        :param verified: The email address will be marked as verified.
        :param primary: Set this email address as the primary email address for the user.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_config is None:
            timeout_config = self.sdk_configuration.timeout_config
        
        if server_url is not None:
            base_url = server_url
        
        request = models.UpdateEmailAddressRequest(
            email_address_id=email_address_id,
            request_body=models.UpdateEmailAddressRequestBody(
                verified=verified,
                primary=primary,
            ),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/email_addresses/{email_address_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, True, "json", Optional[models.UpdateEmailAddressRequestBody]),
            timeout_config=timeout_config,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="UpdateEmailAddress", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","401","403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.EmailAddress])
        if utils.match_response(http_res, ["400","401","403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    