# AssetPartialUpdate

Each Asset is a unique instance of media content. Assets are either singular files or groups of files comprising a single media object (for example separate video and audio files or a framestack). The relation between Asset and its individual files is through the MediaFileBundle model. Assets are checksummed and multiple copies of the same media will refer to the same Asset. Asset carries the media metadata and all user-created objects such as comments or markers will link back to the Asset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**tags** | [**[TagReference]**](TagReference.md) |  | [optional] 
**workflow_state** | **int** |  | [optional] 
**timecode** | **float, none_type** |  | [optional] 
**set_stack_order** | **int** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


