# Proxy

A generated proxy (preview) of an asset produced from a proxy profile, tracking its generation state and the URLs to access the generated files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**urls** | **{str: (str, none_type)}** |  | [readonly] 
**profile** | [**ProxyProfileMini**](ProxyProfileMini.md) |  | 
**failed_reason** | **str, none_type** |  | [readonly] 
**skipped** | **bool** |  | [readonly] 
**generated** | **bool** |  | [readonly] 
**generated_date** | **datetime, none_type** |  | 
**failed** | **bool** |  | 
**failed_count** | **int** |  | 
**name** | **str** |  | 
**variant_config** | **str** |  | 
**source_audio_layout_preserved** | **bool** |  | 
**codecs** | **str, none_type** |  | 
**image_format** | **str** |  | 
**asset** | **int** |  | 
**variant_id** | **str** |  | defaults to "default"
**transforms** | [**Transforms**](Transforms.md) |  | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


