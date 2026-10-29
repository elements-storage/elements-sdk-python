# ProxyPlaybackMetadataTiming

Validated proxy timing used for frame and timecode calculations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fps_numerator** | **int** | Proxy frame rate numerator. | 
**fps_denominator** | **int** | Proxy frame rate denominator. | 
**frame_count** | **int** | Number of video frames in the proxy. | 
**proxy_timeline_start** | **float** | Media time of the first proxy frame, in seconds. | 
**source_timecode_start** | [**ProxyPlaybackMetadataSourceTimecodeStart**](ProxyPlaybackMetadataSourceTimecodeStart.md) |  | 
**video_track_timescale** | **int, none_type** | Proxy video track timescale, or null if unavailable. Usually 120000 for generated MP4 proxies. | [optional] 
**frame_duration_ticks** | **int, none_type** | Duration of one proxy frame in video track ticks, or null if unavailable. | [optional] 
**tolerance_seconds** | **float, none_type** | Allowed timestamp matching tolerance for frame identification, in seconds. | [optional] 

[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)


