# WorkspaceOffloadRequest

Workspace offload requests are made by users who are requesting an administrator to offload a workspace to its secondary location in ELEMENTS Valet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**workspace** | [**WorkspaceMini**](WorkspaceMini.md) |  | 
**user** | [**ElementsUserMini**](ElementsUserMini.md) |  | 
**is_retrieval** | **bool** | When true, this is a request to retrieve (un-park) the workspace from its parking location; when false, a request to park (offload) it. | 
**created_at** | **datetime** |  | [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


