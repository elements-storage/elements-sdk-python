# AIDatasetWithPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**last_change** | **datetime** |  | [readonly] 
**image_count** | **int** |  | [readonly] 
**sample_annotations** | [**[AIAnnotation]**](AIAnnotation.md) |  categories &#x3D; AICategory.objects.filter(dataset&#x3D;obj).prefetch_related(&#39;annotations&#39;).annotate(first_annotation_id&#x3D;Min(&#39;annotations__id&#39;))[:10] sample_annotations &#x3D; AIAnnotation.objects.filter(id__in&#x3D;[x.first_annotation_id for x in categories]) return AIAnnotationSerializer(sample_annotations, many&#x3D;True).data  | [readonly] 
**name** | **str** |  | 
**connection** | **int** |  | 
**training_model** | [**AIModel**](AIModel.md) |  | [optional] 
**last_finished_model** | [**AIModel**](AIModel.md) |  | [optional] 
**type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#models) [[Back to API list]](../README.md#api-endpoints) [[Back to README]](../README.md)


