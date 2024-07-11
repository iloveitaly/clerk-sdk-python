# SignUps
(*sign_ups*)

### Available Operations

* [update](#update) - Update a sign-up

## update

Update the sign-up with the given ID

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.sign_ups.update(id="signup_1234567890abcdef", custom_action=False, external_id="ext_id_7890abcdef123456")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                         | The ID of the sign-up to update                                                                                                                                                                                                                                                                                                                            | signup_1234567890abcdef                                                                                                                                                                                                                                                                                                                                    |
| `custom_action`                                                                                                                                                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                         | Specifies whether a custom action has run for this sign-up attempt.<br/>This is important when your instance has been configured to require a custom action to run before converting a sign-up into a user.<br/>After executing any external business logic you deem necessary, you can mark the sign-up as ready-to-convert by setting `custom_action` to `true`. | false                                                                                                                                                                                                                                                                                                                                                      |
| `external_id`                                                                                                                                                                                                                                                                                                                                              | *Optional[Nullable[str]]*                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                         | The ID of the guest attempting to sign up as used in your external systems or your previous authentication solution.<br/>This will be copied to the resulting user when the sign-up is completed.                                                                                                                                                          | ext_id_7890abcdef123456                                                                                                                                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                            |


### Response

**[models.SignUp](../../models/signup.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403                | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |