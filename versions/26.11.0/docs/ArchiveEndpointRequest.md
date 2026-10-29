# ArchiveEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**[TapeJobSource]**](TapeJobSource.md) | The filesystem paths to archive onto tape. | 
**start_date** | **datetime** | When the archive job should start running. | 
**name** | **str** | Human-readable name for the archive job. | 
**group** | **int** | ID of the tape group to write the primary copy to. | [optional] 
**group2** | **int, none_type** | ID of a second tape group to write a redundant copy to. Omit or null to write a single copy. | [optional] 
**export** | **bool** | When true, eject (export) the primary tape from the library after writing. | [optional] 
**export2** | **bool, none_type** | When true, eject (export) the second-copy tape from the library after writing. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


