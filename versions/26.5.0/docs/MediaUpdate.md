# MediaUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**asset** | [**AssetMicro**](AssetMicro.md) |  | 
**root** | [**MediaRootMiniWithCustomFields**](MediaRootMiniWithCustomFields.md) |  | 
**custom_fields_diff** | **{str: (str, none_type)}** |  | 
**added_tags** | [**[UnfilteredTag]**](UnfilteredTag.md) |  | [readonly] 
**removed_tags** | [**[UnfilteredTag]**](UnfilteredTag.md) |  | [readonly] 
**type** | **str** |  | 
**date** | **datetime** |  | [readonly] 
**rating** | **int, none_type** |  | 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**directory** | [**MediaFile**](MediaFile.md) |  | [optional] 
**user** | [**ElementsUserMiniWithAvatar**](ElementsUserMiniWithAvatar.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


