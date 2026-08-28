# Production

Productions are logical groups of workspaces. Productions do not exist at a single location on the filesystem, but can span multiple volumes. However the production name is still used as a path segment in the workspace path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**is_special** | **bool** |  | [readonly] 
**total_size** | **int, none_type** |  | [readonly] 
**name** | **str** |  | 
**obscure_name** | **bool** | Makes new workspace paths use numeric IDs instead of plain text | 
**description** | **str, none_type** |  | 
**long_description** | **str** |  | 
**active** | **bool** |  | 
**template** | **int, none_type** |  | 
**default_group** | **int, none_type** |  | 
**special_type** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


