# NotificationSettingUpdate

A user's preference for how to be notified about a given topic of events (e.g. via email or a chat integration). A setting with no user is a system-wide default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | The category of events this setting covers (e.g. &#x60;default&#x60;, &#x60;automation&#x60;). | 
**type** | **str** | The delivery channel for the notification (e.g. &#x60;email&#x60;, &#x60;slack&#x60;, &#x60;teams&#x60;, &#x60;push&#x60;). | 
**user** | **int, none_type** | The user this setting applies to. Null marks a system-wide default. | 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


