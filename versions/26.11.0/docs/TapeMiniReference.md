# TapeMiniReference

An LTFS tape cartridge tracked by the Tape Archive, including its identifiers, capacity and wear counters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | [optional] [readonly] 
**uuid** | **str** |  | [optional] [readonly] 
**generation** | **int** |  | [optional] [readonly] 
**custom_a** | **str** | Free-form custom metadata field for organizing tapes. | [optional] [readonly] 
**custom_b** | **str** | Free-form custom metadata field for organizing tapes. | [optional] [readonly] 
**custom_c** | **str** | Free-form custom metadata field for organizing tapes. | [optional] [readonly] 
**custom_d** | **str** | Free-form custom metadata field for organizing tapes. | [optional] [readonly] 
**free_space** | **int, none_type** | Remaining free space on the tape, in bytes. | [optional] [readonly] 
**load_counter** | **int** | Number of times the tape has been loaded into a drive. | [optional] [readonly] 
**error_counter** | **int** | Number of errors recorded against this tape. | [optional] [readonly] 
**error_reason** | **str, none_type** |  | [optional] [readonly] 
**active** | **bool** |  | [optional] [readonly] 
**lto** | **str, none_type** | LTO generation/format of the tape. | [optional] [readonly] 
**group** | **int, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


