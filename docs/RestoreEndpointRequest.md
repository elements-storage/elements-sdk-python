# RestoreEndpointRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the restore job. | 
**source** | [**[TapeJobSource]**](TapeJobSource.md) | Paths on the tape to restore. | 
**exclude** | **[str]** | Paths to exclude from the restore. | 
**tape** | **str** | Barcode of the tape to restore from. | 
**start_date** | **datetime** | When the restore job should start running. | 
**destination** | **str, none_type** | Destination path to restore the files to. Defaults to their original location. | [optional] 
**export** | **bool** | Eject (export) the tape from the library after restoring. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


