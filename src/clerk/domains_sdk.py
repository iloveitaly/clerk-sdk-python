"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from clerk import models
from clerk._hooks import HookContext
from clerk.types import Nullable, UNSET
import clerk.utils as utils
from typing import Optional

class DomainsSDK(BaseSDK):
    
    
    def list(
        self, *,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.Domains:
        r"""List all instance domains

        Use this endpoint to get a list of all domains for an instance.
        The response will contain the primary domain for the instance and any satellite domains. Each domain in the response contains information about the URLs where Clerk operates and the required CNAME targets.

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
        req = self.build_request(
            method="GET",
            path="/domains",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
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
            hook_ctx=HookContext(operation_id="ListDomains", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.Domains])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def list_async(
        self, *,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.Domains:
        r"""List all instance domains

        Use this endpoint to get a list of all domains for an instance.
        The response will contain the primary domain for the instance and any satellite domains. Each domain in the response contains information about the URLs where Clerk operates and the required CNAME targets.

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
        req = self.build_request(
            method="GET",
            path="/domains",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
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
            hook_ctx=HookContext(operation_id="ListDomains", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.Domains])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def add(
        self, *,
        name: str,
        is_satellite: bool,
        proxy_url: Optional[str] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.Domain:
        r"""Add a domain

        Add a new domain for your instance.
        Useful in the case of multi-domain instances, allows adding satellite domains to an instance.
        The new domain must have a `name`. The domain name can contain the port for development instances, like `localhost:3000`.
        At the moment, instances can have only one primary domain, so the `is_satellite` parameter must be set to `true`.
        If you're planning to configure the new satellite domain to run behind a proxy, pass the `proxy_url` parameter accordingly.

        :param name: The new domain name. Can contain the port for development instances.
        :param is_satellite: Marks the new domain as satellite. Only `true` is accepted at the moment.
        :param proxy_url: The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances.
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
        
        request = models.AddDomainRequestBody(
            name=name,
            is_satellite=is_satellite,
            proxy_url=proxy_url,
        )
        
        req = self.build_request(
            method="POST",
            path="/domains",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[models.AddDomainRequestBody]),
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
            hook_ctx=HookContext(operation_id="AddDomain", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","402","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.Domain])
        if utils.match_response(http_res, ["400","402","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def add_async(
        self, *,
        name: str,
        is_satellite: bool,
        proxy_url: Optional[str] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.Domain:
        r"""Add a domain

        Add a new domain for your instance.
        Useful in the case of multi-domain instances, allows adding satellite domains to an instance.
        The new domain must have a `name`. The domain name can contain the port for development instances, like `localhost:3000`.
        At the moment, instances can have only one primary domain, so the `is_satellite` parameter must be set to `true`.
        If you're planning to configure the new satellite domain to run behind a proxy, pass the `proxy_url` parameter accordingly.

        :param name: The new domain name. Can contain the port for development instances.
        :param is_satellite: Marks the new domain as satellite. Only `true` is accepted at the moment.
        :param proxy_url: The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances.
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
        
        request = models.AddDomainRequestBody(
            name=name,
            is_satellite=is_satellite,
            proxy_url=proxy_url,
        )
        
        req = self.build_request(
            method="POST",
            path="/domains",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[models.AddDomainRequestBody]),
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
            hook_ctx=HookContext(operation_id="AddDomain", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","402","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.Domain])
        if utils.match_response(http_res, ["400","402","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def delete(
        self, *,
        domain_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DeletedObject:
        r"""Delete a satellite domain

        Deletes a satellite domain for the instance.
        It is currently not possible to delete the instance's primary domain.

        :param domain_id: The ID of the domain that will be deleted. Must be a satellite domain.
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
        
        request = models.DeleteDomainRequest(
            domain_id=domain_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/domains/{domain_id}",
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
            hook_ctx=HookContext(operation_id="DeleteDomain", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeletedObject])
        if utils.match_response(http_res, ["403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def delete_async(
        self, *,
        domain_id: str,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DeletedObject:
        r"""Delete a satellite domain

        Deletes a satellite domain for the instance.
        It is currently not possible to delete the instance's primary domain.

        :param domain_id: The ID of the domain that will be deleted. Must be a satellite domain.
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
        
        request = models.DeleteDomainRequest(
            domain_id=domain_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/domains/{domain_id}",
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
            hook_ctx=HookContext(operation_id="DeleteDomain", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["403","404","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeletedObject])
        if utils.match_response(http_res, ["403","404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def update(
        self, *,
        domain_id: str,
        name: Optional[Nullable[str]] = None,
        proxy_url: Optional[Nullable[str]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.Domain:
        r"""Update a domain

        The `proxy_url` can be updated only for production instances.
        Update one of the instance's domains. Both primary and satellite domains can be updated.
        If you choose to use Clerk via proxy, use this endpoint to specify the `proxy_url`.
        Whenever you decide you'd rather switch to DNS setup for Clerk, simply set `proxy_url`
        to `null` for the domain. When you update a production instance's primary domain name,
        you have to make sure that you've completed all the necessary setup steps for DNS and
        emails to work. Expect downtime otherwise. Updating a primary domain's name will also
        update the instance's home origin, affecting the default application paths.

        :param domain_id: The ID of the domain that will be updated.
        :param name: The new domain name. For development instances, can contain the port, i.e `myhostname:3000`. For production instances, must be a valid FQDN, i.e `mysite.com`. Cannot contain protocol scheme.
        :param proxy_url: The full URL of the proxy that will forward requests to Clerk's Frontend API. Can only be updated for production instances.
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
        
        request = models.UpdateDomainRequest(
            domain_id=domain_id,
            request_body=models.UpdateDomainRequestBody(
                name=name,
                proxy_url=proxy_url,
            ),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/domains/{domain_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, False, "json", models.UpdateDomainRequestBody),
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
            hook_ctx=HookContext(operation_id="UpdateDomain", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.Domain])
        if utils.match_response(http_res, ["400","404","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def update_async(
        self, *,
        domain_id: str,
        name: Optional[Nullable[str]] = None,
        proxy_url: Optional[Nullable[str]] = None,
        retries: Optional[Nullable[utils.RetryConfig]] = UNSET,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.Domain:
        r"""Update a domain

        The `proxy_url` can be updated only for production instances.
        Update one of the instance's domains. Both primary and satellite domains can be updated.
        If you choose to use Clerk via proxy, use this endpoint to specify the `proxy_url`.
        Whenever you decide you'd rather switch to DNS setup for Clerk, simply set `proxy_url`
        to `null` for the domain. When you update a production instance's primary domain name,
        you have to make sure that you've completed all the necessary setup steps for DNS and
        emails to work. Expect downtime otherwise. Updating a primary domain's name will also
        update the instance's home origin, affecting the default application paths.

        :param domain_id: The ID of the domain that will be updated.
        :param name: The new domain name. For development instances, can contain the port, i.e `myhostname:3000`. For production instances, must be a valid FQDN, i.e `mysite.com`. Cannot contain protocol scheme.
        :param proxy_url: The full URL of the proxy that will forward requests to Clerk's Frontend API. Can only be updated for production instances.
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
        
        request = models.UpdateDomainRequest(
            domain_id=domain_id,
            request_body=models.UpdateDomainRequestBody(
                name=name,
                proxy_url=proxy_url,
            ),
        )
        
        req = self.build_request(
            method="PATCH",
            path="/domains/{domain_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.request_body, False, False, "json", models.UpdateDomainRequestBody),
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
            hook_ctx=HookContext(operation_id="UpdateDomain", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","404","422","4XX","5XX"],
            retry_config=retry_config
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.Domain])
        if utils.match_response(http_res, ["400","404","422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    