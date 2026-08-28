# CustomFieldPartialUpdate

Custom fields are user-defined key-value metadata pairs that can be attached to assets and files. The manager user defines the type and shape of the field, and the end users will work with the values. Custom field definitions can be shared between multiple Media Roots

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**options** | **[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**type** | **str** | The kind of field, which controls its input widget and value format. | [optional] 
**use_for_uploads** | **bool** | Show this field in the upload panel. | [optional] 
**require_to_upload** | **bool** | Require a value for this field when uploading files. | [optional] 
**non_user_editable** | **bool** | Prevent end users from editing this field&#39;s value in the UI (the field will only be editable via API and Automation). | [optional] 
**validation** | **str, none_type** | Validation rule applied to values entered for this field. | [optional] 
**regex** | **str, none_type** | Regular expression that values must match (when validation is &#x60;regex&#x60;). | [optional] 
**range_min** | **int, none_type** | Minimum allowed numeric value (when validation is &#x60;range&#x60;). | [optional] 
**range_max** | **int, none_type** | Maximum allowed numeric value (when validation is &#x60;range&#x60;). | [optional] 
**number_of_digits** | **int, none_type** | Required number of digits (when validation is &#x60;number_of_digits&#x60;). | [optional] 
**metadata_prefill** | **str, none_type** | Name of an embedded metadata field to pre-fill this field&#39;s value from. | [optional] 
**highlight_expiration** | **bool** | For date fields, visually highlight assets whose date has passed or is near. | [optional] 
**multiple_response** | **bool** | Allow multiple values to be selected/entered. | [optional] 
**help_text** | **str, none_type** | Help text shown to users filling in this field. | [optional] 
**users_from_group** | **int, none_type** | For user-type fields, restrict selectable users to members of this group. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


