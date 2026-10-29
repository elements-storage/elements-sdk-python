# MediaFileBundle

Media File Bundles represent groups of files that together represent a single media object. For example, related video+audio OP-Atom files, or a DPX framestack. Media Library scanner will automatically detect these groups and create bundles. Bundling cannot be managed by the user except for the `disable_framestack` flag in the Media Root.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**mainfile** | [**MediaFileMini**](MediaFileMini.md) |  | 
**snm_attributes** | [**StornextManagerAttributes**](StornextManagerAttributes.md) |  | 
**is_shared** | **bool, none_type** |  | [readonly] 
**file_count** | **int** |  | [readonly] 
**exclusion_info** | [**MediaFileBundleExclusionInfo**](MediaFileBundleExclusionInfo.md) |  | 
**name** | **str** |  | 
**location** | **int** |  | 
**shared_via_tokens** | **[int]** |  | 
**asset** | [**Asset**](Asset.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


