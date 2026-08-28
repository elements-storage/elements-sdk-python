# SequenceRenderRequestOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_path** | **str** | Destination path for the rendered output. | 
**tails** | **float** | Duration of subclip tails to leave in seconds | 
**resolution** | **str** | Output resolution. | 
**fps** | **str** | Output frame rate, as an exact fraction. | 
**combine** | **bool** | When true, render the whole sequence into a single output file. | [optional]  if omitted the server will use the default value of False
**data_source** | **str** | Whether to render from the original &#x60;source&#x60; media or from &#x60;proxy&#x60; media. | [optional]  if omitted the server will use the default value of "source"
**wrap_opatom** | **bool** | When true, wrap the output as OP-Atom MXF. | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


