# Subtask

A single step within an Automation job's workflow: the task to run, its arguments, and its trigger, looping and branching behaviour.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**kwargs** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**trigger** | **str, none_type** | Event on the related step that triggers this step (e.g. on success/failure). | 
**name** | **str, none_type** |  | 
**noop_dont_save** | **bool** |  | 
**no_concurrency** | **bool** | Prevent this step from running concurrently with other instances of itself. | 
**timeout** | **int, none_type** | Maximum run time in seconds before the step times out. | 
**log_variable** | **bool** |  | 
**task** | **str, none_type** | Identifier of the task type this step runs. | 
**condition** | **str, none_type** | Boolean Jinja expression evaluated to decide whether this step runs. | 
**sync** | **bool** | Run this step synchronously in the caller context instead of as a background task. | 
**queue** | **str, none_type** |  | 
**enqueue_at_front** | **bool** |  | 
**loop** | **bool** | Run this step once per item produced by &#x60;loop_expression&#x60;. | 
**loop_expression** | **str, none_type** | Jinja expression yielding the items to loop over. | 
**loop_variable_name** | **str, none_type** | Variable name the current loop item is exposed as. | 
**parent** | **int** | The Automation job this step belongs to. | 
**relative_to** | **int, none_type** | Previous step that this one is positioned relative to in the job flow. | 
**validation_error** | **str, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


