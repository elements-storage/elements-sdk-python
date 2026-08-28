# TapeMini

An LTFS tape cartridge tracked by the Tape Archive, including its identifiers, capacity and wear counters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**uuid** | **str** |  | 
**generation** | **int** |  | 
**custom_a** | **str** | Free-form custom metadata field for organizing tapes. | 
**custom_b** | **str** | Free-form custom metadata field for organizing tapes. | 
**custom_c** | **str** | Free-form custom metadata field for organizing tapes. | 
**custom_d** | **str** | Free-form custom metadata field for organizing tapes. | 
**free_space** | **int, none_type** | Remaining free space on the tape, in bytes. | 
**load_counter** | **int** | Number of times the tape has been loaded into a drive. | 
**error_counter** | **int** | Number of errors recorded against this tape. | 
**error_reason** | **str, none_type** |  | 
**active** | **bool** |  | 
**lto** | **str, none_type** | LTO generation/format of the tape. | 
**group** | **int, none_type** |  | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


