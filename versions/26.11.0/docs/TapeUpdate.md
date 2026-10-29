# TapeUpdate

An LTFS tape cartridge tracked by the Tape Archive, including its identifiers, capacity and wear counters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**uuid** | **str** |  | [optional] 
**generation** | **int** |  | [optional] 
**custom_a** | **str** | Free-form custom metadata field for organizing tapes. | [optional] 
**custom_b** | **str** | Free-form custom metadata field for organizing tapes. | [optional] 
**custom_c** | **str** | Free-form custom metadata field for organizing tapes. | [optional] 
**custom_d** | **str** | Free-form custom metadata field for organizing tapes. | [optional] 
**free_space** | **int, none_type** | Remaining free space on the tape, in bytes. | [optional] 
**load_counter** | **int** | Number of times the tape has been loaded into a drive. | [optional] 
**error_counter** | **int** | Number of errors recorded against this tape. | [optional] 
**error_reason** | **str, none_type** |  | [optional] 
**active** | **bool** |  | [optional] 
**lto** | **str, none_type** | LTO generation/format of the tape. | [optional] 
**group** | **int, none_type** |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


