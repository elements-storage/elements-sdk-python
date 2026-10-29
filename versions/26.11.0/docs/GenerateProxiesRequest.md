# GenerateProxiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy_profiles** | **[int]** | IDs of the proxy profiles to generate proxies for. | 
**bundles** | **[int]** | IDs of media file bundles to generate proxies for. | [optional] 
**directories** | **[int]** | IDs of media directories whose contents to generate proxies for. | [optional] 
**enqueue_at_front** | **bool** | When true, place the proxy generation tasks at the front of the queue. | [optional] 
**force** | **bool** | When true, regenerate proxies even if they already exist (otherwise they will be skipped). | [optional] 
**retry_failed** | **bool** | When true, retry generating proxies that have previously failed multiple times (otherwise they will be skipped). | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


