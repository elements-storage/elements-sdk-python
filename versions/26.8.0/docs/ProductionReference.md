# ProductionReference

Productions are logical groups of workspaces. Productions do not exist at a single location on the filesystem, but can span multiple volumes. However the production name is still used as a path segment in the workspace path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**is_special** | **bool** |  | [optional] [readonly] 
**special_type** | **int, none_type** |  | [optional] [readonly] 
**total_size** | **int, none_type** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**obscure_name** | **bool** | Makes new workspace paths use numeric IDs instead of plain text | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] [readonly] 
**long_description** | **str** |  | [optional] [readonly] 
**active** | **bool** |  | [optional] [readonly] 
**template** | **int, none_type** |  | [optional] [readonly] 
**default_group** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


