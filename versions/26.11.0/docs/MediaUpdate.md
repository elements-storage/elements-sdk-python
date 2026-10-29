# MediaUpdate

An entry in the Media Library activity feed recording a change to an asset (a new comment, tag change, rating or custom-field edit) and who made it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**asset** | [**AssetMicro**](AssetMicro.md) |  | 
**root** | [**MediaRootMiniWithCustomFields**](MediaRootMiniWithCustomFields.md) |  | 
**custom_fields_diff** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**added_tags** | [**[UnfilteredTag]**](UnfilteredTag.md) |  | [readonly] 
**removed_tags** | [**[UnfilteredTag]**](UnfilteredTag.md) |  | [readonly] 
**type** | **str** |  | 
**date** | **datetime** |  | [readonly] 
**rating** | **int, none_type** |  | 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**directory** | [**MediaFile**](MediaFile.md) |  | [optional] 
**user** | [**ElementsUserMiniWithAvatar**](ElementsUserMiniWithAvatar.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


