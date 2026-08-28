# MCPUserKey

The current user's MCP connection code: a single short-lived string entered on the MCP tunnel sign-in page to connect an AI assistant (e.g. ChatGPT or Claude) to this ELEMENTS account. It bundles the instance id and a rotating key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Opaque connection code to paste into the MCP tunnel sign-in page. | [readonly] 
**expires_at** | **datetime** | When the code expires and is automatically rotated. | [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


