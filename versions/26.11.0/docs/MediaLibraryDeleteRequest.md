# MediaLibraryDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundles** | **[int]** | IDs of media file bundles to delete. | [optional] 
**files** | **[int]** | IDs of media files to delete. | [optional] 
**assets** | **[int]** | IDs of assets to delete. | [optional] 
**delete_from_database** | **bool** | Destroy the selected objects&#39; records and metadata in the Media Library database. | [optional]  if omitted the server will use the default value of False
**delete_from_storage** | **bool** | Delete the underlying files from storage (moving them to the recycle bin if enabled). | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


