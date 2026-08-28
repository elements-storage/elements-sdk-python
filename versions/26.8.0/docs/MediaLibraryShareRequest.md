# MediaLibraryShareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires** | **datetime** | When the sharing link expires. | 
**permissions** | [**MediaRootPermissionAccessOptions**](MediaRootPermissionAccessOptions.md) |  | 
**bundles** | **[int]** | IDs of media file bundles to share. | [optional] 
**directories** | **[int]** | IDs of media directories to share. | [optional] 
**view_limit** | **int, none_type** | Maximum number of times the link may be opened (null for unlimited). | [optional] 
**user** | **int** | Existing user to share with, instead of creating an anonymous link. | [optional] 
**email** | **str** | Email address to create the sharing link for. | [optional] 
**link_type** | **str, none_type** | What the link grants: &#x60;download-original&#x60;, &#x60;download-proxy&#x60;, &#x60;embed-player&#x60;, &#x60;embed-full&#x60; or &#x60;playlist&#x60;. | [optional] 
**password** | **str, none_type** | Optional password required to open the link. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


