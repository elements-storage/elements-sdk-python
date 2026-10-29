# CloudAccountPartialUpdate

Credentials and configuration for a cloud storage provider account, used by cloud volumes and workspaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**access_id** | **str, none_type** | Provider-specific access key / account ID. Leave empty to use IAM role-based auth (AWS). | [optional] 
**secret** | **str, none_type** | Provider-specific secret key credential | [optional] 
**tenant** | **str, none_type** | Azure tenant ID (Azure only). | [optional] 
**subscription** | **str, none_type** | Azure subscription ID (Azure only). | [optional] 
**endpoint** | **str, none_type** | Custom service endpoint URL (for S3-compatible providers). | [optional] 
**enabled** | **bool** |  | [optional] 
**mount_credentials_management** | **str, none_type** | Decides how the ELEMENTS Client will obtain credentials to mount cloud workspaces from this account. For &#x60;share&#x60; the server will expose service account credentials to clients (insecure). With &#x60;token&#x60; server will issue short lived tokens for mounting | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


