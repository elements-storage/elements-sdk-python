# ProductionUpdate

Productions are logical groups of workspaces. Productions do not exist at a single location on the filesystem, but can span multiple volumes. However the production name is still used as a path segment in the workspace path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**obscure_name** | **bool** | Makes new workspace paths use numeric IDs instead of plain text | [optional] 
**description** | **str, none_type** |  | [optional] 
**long_description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**template** | **int, none_type** |  | [optional] 
**default_group** | **int, none_type** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


