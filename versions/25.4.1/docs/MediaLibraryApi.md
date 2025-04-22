# elements_sdk.MediaLibraryApi



Method | HTTP request | Description
------------- | ------------- | -------------
[**bookmark_media_directory**](MediaLibraryApi.md#bookmark_media_directory) | **POST** `/api/2/media/files/{id}/bookmark` | 
[**clear_subclip_clipboard**](MediaLibraryApi.md#clear_subclip_clipboard) | **DELETE** `/api/2/media/subclips/clipboard/clear` | 
[**clear_subtitle_clipboard**](MediaLibraryApi.md#clear_subtitle_clipboard) | **DELETE** `/api/2/media/subtitles/clipboard/clear` | 
[**combine_assets_into_set**](MediaLibraryApi.md#combine_assets_into_set) | **POST** `/api/2/media/stacks/combine-into-set` | 
[**count_unresolved_comments**](MediaLibraryApi.md#count_unresolved_comments) | **GET** `/api/2/media/comments/count-unresolved` | 
[**create_asset_rating**](MediaLibraryApi.md#create_asset_rating) | **POST** `/api/2/media/assets/{asset_id}/ratings` | 
[**create_asset_subtitle_link**](MediaLibraryApi.md#create_asset_subtitle_link) | **POST** `/api/2/media/assets/{asset_id}/subtitle-links` | 
[**create_comment**](MediaLibraryApi.md#create_comment) | **POST** `/api/2/media/comments` | 
[**create_custom_field**](MediaLibraryApi.md#create_custom_field) | **POST** `/api/2/media/custom-fields` | 
[**create_editor_project**](MediaLibraryApi.md#create_editor_project) | **POST** `/api/2/media/editor` | 
[**create_editor_subtitle**](MediaLibraryApi.md#create_editor_subtitle) | **POST** `/api/2/media/subtitles` | 
[**create_external_transcoder**](MediaLibraryApi.md#create_external_transcoder) | **POST** `/api/2/media/external-transcoders` | 
[**create_marker**](MediaLibraryApi.md#create_marker) | **POST** `/api/2/media/assets/{asset_id}/markers` | 
[**create_media_file_template**](MediaLibraryApi.md#create_media_file_template) | **POST** `/api/2/media/files/templates` | 
[**create_media_root**](MediaLibraryApi.md#create_media_root) | **POST** `/api/2/media/roots` | 
[**create_media_root_permission**](MediaLibraryApi.md#create_media_root_permission) | **POST** `/api/2/media/root-permissions` | 
[**create_media_tag**](MediaLibraryApi.md#create_media_tag) | **POST** `/api/2/media/tags` | 
[**create_proxy_profile**](MediaLibraryApi.md#create_proxy_profile) | **POST** `/api/2/media/proxy-profiles` | 
[**create_saved_search**](MediaLibraryApi.md#create_saved_search) | **POST** `/api/2/media/saved-searches` | 
[**create_sharing_permission_preset**](MediaLibraryApi.md#create_sharing_permission_preset) | **POST** `/api/2/media/sharing-permission-presets` | 
[**create_subclip**](MediaLibraryApi.md#create_subclip) | **POST** `/api/2/media/{asset_id}/subclips` | 
[**create_subclip_clipboard_entry**](MediaLibraryApi.md#create_subclip_clipboard_entry) | **POST** `/api/2/media/subclips/clipboard` | 
[**create_subtitle_clipboard_entry**](MediaLibraryApi.md#create_subtitle_clipboard_entry) | **POST** `/api/2/media/subtitles/clipboard` | 
[**create_workflow**](MediaLibraryApi.md#create_workflow) | **POST** `/api/2/media/workflows` | 
[**delete_asset**](MediaLibraryApi.md#delete_asset) | **DELETE** `/api/2/media/assets/{id}` | 
[**delete_asset_rating**](MediaLibraryApi.md#delete_asset_rating) | **DELETE** `/api/2/media/assets/{asset_id}/ratings/{id}` | 
[**delete_asset_subtitle_link**](MediaLibraryApi.md#delete_asset_subtitle_link) | **DELETE** `/api/2/media/assets/{asset_id}/subtitle-links/{id}` | 
[**delete_comment**](MediaLibraryApi.md#delete_comment) | **DELETE** `/api/2/media/comments/{id}` | 
[**delete_custom_field**](MediaLibraryApi.md#delete_custom_field) | **DELETE** `/api/2/media/custom-fields/{id}` | 
[**delete_easy_sharing_token_for_bundle**](MediaLibraryApi.md#delete_easy_sharing_token_for_bundle) | **DELETE** `/api/2/media/bundles/{id}/easy-sharing-token` | 
[**delete_easy_sharing_token_for_directory**](MediaLibraryApi.md#delete_easy_sharing_token_for_directory) | **DELETE** `/api/2/media/files/{id}/easy-sharing-token` | 
[**delete_external_transcoder**](MediaLibraryApi.md#delete_external_transcoder) | **DELETE** `/api/2/media/external-transcoders/{id}` | 
[**delete_marker**](MediaLibraryApi.md#delete_marker) | **DELETE** `/api/2/media/assets/{asset_id}/markers/{id}` | 
[**delete_media_file_template**](MediaLibraryApi.md#delete_media_file_template) | **DELETE** `/api/2/media/files/templates/{id}` | 
[**delete_media_library_objects**](MediaLibraryApi.md#delete_media_library_objects) | **POST** `/api/2/media/delete` | 
[**delete_media_pinned_item**](MediaLibraryApi.md#delete_media_pinned_item) | **DELETE** `/api/2/media/pinned-items/{id}` | 
[**delete_media_root**](MediaLibraryApi.md#delete_media_root) | **DELETE** `/api/2/media/roots/{id}` | 
[**delete_media_root_cover_image**](MediaLibraryApi.md#delete_media_root_cover_image) | **DELETE** `/api/2/media/roots/{id}/cover` | 
[**delete_media_root_permission**](MediaLibraryApi.md#delete_media_root_permission) | **DELETE** `/api/2/media/root-permissions/{id}` | 
[**delete_media_tag**](MediaLibraryApi.md#delete_media_tag) | **DELETE** `/api/2/media/tags/{id}` | 
[**delete_media_update**](MediaLibraryApi.md#delete_media_update) | **DELETE** `/api/2/media/updates/{id}` | 
[**delete_proxy**](MediaLibraryApi.md#delete_proxy) | **DELETE** `/api/2/media/assets/{asset_id}/proxies/{id}` | 
[**delete_proxy_profile**](MediaLibraryApi.md#delete_proxy_profile) | **DELETE** `/api/2/media/proxy-profiles/{id}` | 
[**delete_proxy_profile_watermark_image**](MediaLibraryApi.md#delete_proxy_profile_watermark_image) | **DELETE** `/api/2/media/proxy-profiles/{id}/watermark` | 
[**delete_saved_search**](MediaLibraryApi.md#delete_saved_search) | **DELETE** `/api/2/media/saved-searches/{id}` | 
[**delete_sharing_permission_preset**](MediaLibraryApi.md#delete_sharing_permission_preset) | **DELETE** `/api/2/media/sharing-permission-presets/{id}` | 
[**delete_subclip**](MediaLibraryApi.md#delete_subclip) | **DELETE** `/api/2/media/{asset_id}/subclips/{id}` | 
[**delete_subclip_clipboard_entry**](MediaLibraryApi.md#delete_subclip_clipboard_entry) | **DELETE** `/api/2/media/subclips/clipboard/{id}` | 
[**delete_subtitle_clipboard_entry**](MediaLibraryApi.md#delete_subtitle_clipboard_entry) | **DELETE** `/api/2/media/subtitles/clipboard/{id}` | 
[**delete_workflow**](MediaLibraryApi.md#delete_workflow) | **DELETE** `/api/2/media/workflows/{id}` | 
[**discover_media**](MediaLibraryApi.md#discover_media) | **POST** `/api/2/scanner/discover` | 
[**download_asset_proxy_file**](MediaLibraryApi.md#download_asset_proxy_file) | **GET** `/api/2/media/assets/{id}/proxy-files/{filename}` | 
[**download_media_file**](MediaLibraryApi.md#download_media_file) | **GET** `/api/2/media/files/{id}/download` | 
[**download_proxy**](MediaLibraryApi.md#download_proxy) | **GET** `/api/2/media/assets/{asset_id}/proxies/{id}/download` | 
[**editor_export_xml_for_assset**](MediaLibraryApi.md#editor_export_xml_for_assset) | **GET** `/api/2/media/editor/asset/{asset_ids}/xml-export` | 
[**editor_export_xml_for_bundle**](MediaLibraryApi.md#editor_export_xml_for_bundle) | **GET** `/api/2/media/editor/bundle/{bundle_ids}/xml-export` | 
[**editor_export_xml_for_project**](MediaLibraryApi.md#editor_export_xml_for_project) | **GET** `/api/2/media/editor/{id}/xml-export` | 
[**exclude_directory_from_proxy_generation**](MediaLibraryApi.md#exclude_directory_from_proxy_generation) | **POST** `/api/2/media/files/{id}/dont-proxy` | 
[**exclude_directory_from_scan**](MediaLibraryApi.md#exclude_directory_from_scan) | **POST** `/api/2/media/files/{id}/dont-scan` | 
[**export_comments_for_avid**](MediaLibraryApi.md#export_comments_for_avid) | **GET** `/api/2/media/editor/asset/{asset_id}/{export_format}-export/avid-comments` | 
[**export_editor_timeline**](MediaLibraryApi.md#export_editor_timeline) | **POST** `/api/2/media/editor/timeline-export` | 
[**extract_stream**](MediaLibraryApi.md#extract_stream) | **POST** `/api/2/media/assets/{id}/extract-stream` | 
[**forget_deleted_media_files**](MediaLibraryApi.md#forget_deleted_media_files) | **POST** `/api/2/media/files/{id}/forget-deleted` | 
[**generate_proxies**](MediaLibraryApi.md#generate_proxies) | **POST** `/api/2/media/proxies` | 
[**get_all_asset_project_links**](MediaLibraryApi.md#get_all_asset_project_links) | **GET** `/api/2/media/assets/{asset_id}/project-links` | 
[**get_all_asset_ratings**](MediaLibraryApi.md#get_all_asset_ratings) | **GET** `/api/2/media/assets/{asset_id}/ratings` | 
[**get_all_asset_subtitle_links**](MediaLibraryApi.md#get_all_asset_subtitle_links) | **GET** `/api/2/media/assets/{asset_id}/subtitle-links` | 
[**get_all_asset_tape_backups**](MediaLibraryApi.md#get_all_asset_tape_backups) | **GET** `/api/2/media/backups` | 
[**get_all_assets**](MediaLibraryApi.md#get_all_assets) | **GET** `/api/2/media/assets` | 
[**get_all_bundles_for_media_root**](MediaLibraryApi.md#get_all_bundles_for_media_root) | **GET** `/api/2/media/bundles/flat/{root}` | 
[**get_all_bundles_in_subtree**](MediaLibraryApi.md#get_all_bundles_in_subtree) | **GET** `/api/2/media/bundles/flat/subtree/{file}` | 
[**get_all_click_links**](MediaLibraryApi.md#get_all_click_links) | **GET** `/api/2/media/assets/click-links` | 
[**get_all_comments**](MediaLibraryApi.md#get_all_comments) | **GET** `/api/2/media/comments` | 
[**get_all_custom_fields**](MediaLibraryApi.md#get_all_custom_fields) | **GET** `/api/2/media/custom-fields` | 
[**get_all_external_transcoders**](MediaLibraryApi.md#get_all_external_transcoders) | **GET** `/api/2/media/external-transcoders` | 
[**get_all_markers**](MediaLibraryApi.md#get_all_markers) | **GET** `/api/2/media/assets/{asset_id}/markers` | 
[**get_all_media_file_bundles**](MediaLibraryApi.md#get_all_media_file_bundles) | **GET** `/api/2/media/bundles` | 
[**get_all_media_file_templates**](MediaLibraryApi.md#get_all_media_file_templates) | **GET** `/api/2/media/files/templates` | 
[**get_all_media_files**](MediaLibraryApi.md#get_all_media_files) | **GET** `/api/2/media/files` | 
[**get_all_media_files_for_bundles**](MediaLibraryApi.md#get_all_media_files_for_bundles) | **POST** `/api/2/media/files/for-bundles` | 
[**get_all_media_files_for_media_root**](MediaLibraryApi.md#get_all_media_files_for_media_root) | **GET** `/api/2/media/files/flat/{root}` | 
[**get_all_media_files_in_subtree**](MediaLibraryApi.md#get_all_media_files_in_subtree) | **GET** `/api/2/media/files/flat/subtree/{file}` | 
[**get_all_media_root_permissions**](MediaLibraryApi.md#get_all_media_root_permissions) | **GET** `/api/2/media/root-permissions` | 
[**get_all_media_roots**](MediaLibraryApi.md#get_all_media_roots) | **GET** `/api/2/media/roots` | 
[**get_all_media_tags**](MediaLibraryApi.md#get_all_media_tags) | **GET** `/api/2/media/tags` | 
[**get_all_media_updates**](MediaLibraryApi.md#get_all_media_updates) | **GET** `/api/2/media/updates` | 
[**get_all_pinned_items**](MediaLibraryApi.md#get_all_pinned_items) | **GET** `/api/2/media/pinned-items` | 
[**get_all_proxy_generators**](MediaLibraryApi.md#get_all_proxy_generators) | **GET** `/api/2/media/proxy-generators` | 
[**get_all_proxy_profiles**](MediaLibraryApi.md#get_all_proxy_profiles) | **GET** `/api/2/media/proxy-profiles` | 
[**get_all_saved_searches**](MediaLibraryApi.md#get_all_saved_searches) | **GET** `/api/2/media/saved-searches` | 
[**get_all_sharing_permission_presets**](MediaLibraryApi.md#get_all_sharing_permission_presets) | **GET** `/api/2/media/sharing-permission-presets` | 
[**get_all_subclip_clipboard_entries**](MediaLibraryApi.md#get_all_subclip_clipboard_entries) | **GET** `/api/2/media/subclips/clipboard` | 
[**get_all_subclips**](MediaLibraryApi.md#get_all_subclips) | **GET** `/api/2/media/{asset_id}/subclips` | 
[**get_all_subtitle_clipboard_entries**](MediaLibraryApi.md#get_all_subtitle_clipboard_entries) | **GET** `/api/2/media/subtitles/clipboard` | 
[**get_all_transcoder_profiles**](MediaLibraryApi.md#get_all_transcoder_profiles) | **GET** `/api/2/transcoder-profiles` | 
[**get_all_workflows**](MediaLibraryApi.md#get_all_workflows) | **GET** `/api/2/media/workflows` | 
[**get_asset**](MediaLibraryApi.md#get_asset) | **GET** `/api/2/media/assets/{id}` | 
[**get_asset_rating**](MediaLibraryApi.md#get_asset_rating) | **GET** `/api/2/media/assets/{asset_id}/ratings/{id}` | 
[**get_asset_stack_members**](MediaLibraryApi.md#get_asset_stack_members) | **GET** `/api/2/media/stacks/{id}/members` | 
[**get_asset_subtitle_link**](MediaLibraryApi.md#get_asset_subtitle_link) | **GET** `/api/2/media/assets/{asset_id}/subtitle-links/{id}` | 
[**get_bookmarked_media_files_directories**](MediaLibraryApi.md#get_bookmarked_media_files_directories) | **GET** `/api/2/media/files/bookmarks` | 
[**get_bundle_files**](MediaLibraryApi.md#get_bundle_files) | **GET** `/api/2/media/bundles/{id}/files` | 
[**get_comment**](MediaLibraryApi.md#get_comment) | **GET** `/api/2/media/comments/{id}` | 
[**get_custom_field**](MediaLibraryApi.md#get_custom_field) | **GET** `/api/2/media/custom-fields/{id}` | 
[**get_custom_field_options**](MediaLibraryApi.md#get_custom_field_options) | **GET** `/api/2/media/custom-fields/{id}/options` | 
[**get_easy_sharing_token_for_bundle**](MediaLibraryApi.md#get_easy_sharing_token_for_bundle) | **GET** `/api/2/media/bundles/{id}/easy-sharing-token` | 
[**get_easy_sharing_token_for_directory**](MediaLibraryApi.md#get_easy_sharing_token_for_directory) | **GET** `/api/2/media/files/{id}/easy-sharing-token` | 
[**get_editor_project**](MediaLibraryApi.md#get_editor_project) | **GET** `/api/2/media/editor/{id}` | 
[**get_editor_subtitle**](MediaLibraryApi.md#get_editor_subtitle) | **GET** `/api/2/media/subtitles/{id}` | 
[**get_external_transcoder**](MediaLibraryApi.md#get_external_transcoder) | **GET** `/api/2/media/external-transcoders/{id}` | 
[**get_frame**](MediaLibraryApi.md#get_frame) | **GET** `/api/2/media/assets/{id}/frames/{frame}` | 
[**get_media_file**](MediaLibraryApi.md#get_media_file) | **GET** `/api/2/media/files/{id}` | 
[**get_media_file_bundle**](MediaLibraryApi.md#get_media_file_bundle) | **GET** `/api/2/media/bundles/{id}` | 
[**get_media_file_contents**](MediaLibraryApi.md#get_media_file_contents) | **GET** `/api/2/media/files/{id}/contents` | 
[**get_media_file_template**](MediaLibraryApi.md#get_media_file_template) | **GET** `/api/2/media/files/templates/{id}` | 
[**get_media_pinned_item**](MediaLibraryApi.md#get_media_pinned_item) | **GET** `/api/2/media/pinned-items/{id}` | 
[**get_media_root**](MediaLibraryApi.md#get_media_root) | **GET** `/api/2/media/roots/{id}` | 
[**get_media_root_cover_image**](MediaLibraryApi.md#get_media_root_cover_image) | **GET** `/api/2/media/roots/{id}/cover` | 
[**get_media_root_permission**](MediaLibraryApi.md#get_media_root_permission) | **GET** `/api/2/media/root-permissions/{id}` | 
[**get_media_root_users**](MediaLibraryApi.md#get_media_root_users) | **GET** `/api/2/media/roots/{id}/users` | 
[**get_media_tag**](MediaLibraryApi.md#get_media_tag) | **GET** `/api/2/media/tags/{id}` | 
[**get_multiple_assets**](MediaLibraryApi.md#get_multiple_assets) | **POST** `/api/2/media/assets/multiple` | 
[**get_multiple_bundles**](MediaLibraryApi.md#get_multiple_bundles) | **POST** `/api/2/media/bundles/multiple` | 
[**get_multiple_files**](MediaLibraryApi.md#get_multiple_files) | **POST** `/api/2/media/files/multiple` | 
[**get_my_media_root_permissions**](MediaLibraryApi.md#get_my_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine` | 
[**get_my_resolved_media_root_permissions**](MediaLibraryApi.md#get_my_resolved_media_root_permissions) | **GET** `/api/2/media/root-permissions/mine/resolved` | 
[**get_proxy**](MediaLibraryApi.md#get_proxy) | **GET** `/api/2/media/assets/{asset_id}/proxies/{id}` | 
[**get_proxy_generation_info**](MediaLibraryApi.md#get_proxy_generation_info) | **GET** `/api/2/media/assets/{asset_id}/proxies/{id}/progress` | 
[**get_proxy_generator**](MediaLibraryApi.md#get_proxy_generator) | **GET** `/api/2/media/proxy-generators/{id}` | 
[**get_proxy_profile**](MediaLibraryApi.md#get_proxy_profile) | **GET** `/api/2/media/proxy-profiles/{id}` | 
[**get_proxy_profile_proxy_count**](MediaLibraryApi.md#get_proxy_profile_proxy_count) | **GET** `/api/2/media/proxy-profiles/{id}/proxy-count` | 
[**get_proxy_profile_watermark_image**](MediaLibraryApi.md#get_proxy_profile_watermark_image) | **GET** `/api/2/media/proxy-profiles/{id}/watermark` | 
[**get_saved_search**](MediaLibraryApi.md#get_saved_search) | **GET** `/api/2/media/saved-searches/{id}` | 
[**get_sharing_permission_preset**](MediaLibraryApi.md#get_sharing_permission_preset) | **GET** `/api/2/media/sharing-permission-presets/{id}` | 
[**get_subtitles**](MediaLibraryApi.md#get_subtitles) | **GET** `/api/2/media/assets/{id}/subtitle/{title}` | 
[**get_transcoder_profile**](MediaLibraryApi.md#get_transcoder_profile) | **GET** `/api/2/transcoder-profiles/{id}` | 
[**get_vantage_workflows**](MediaLibraryApi.md#get_vantage_workflows) | **GET** `/api/2/media/external-transcoders/{id}/workflows` | 
[**get_workflow**](MediaLibraryApi.md#get_workflow) | **GET** `/api/2/media/workflows/{id}` | 
[**instantiate_media_file_template**](MediaLibraryApi.md#instantiate_media_file_template) | **POST** `/api/2/media/files/templates/{id}/instantiate` | 
[**link_assets_as_versions**](MediaLibraryApi.md#link_assets_as_versions) | **POST** `/api/2/media/stacks/link-versions` | 
[**locate_editor_project_paths**](MediaLibraryApi.md#locate_editor_project_paths) | **GET** `/api/2/media/editor/{id}/locate-paths` | 
[**lookup_media_files**](MediaLibraryApi.md#lookup_media_files) | **POST** `/api/2/media/files/lookup` | 
[**mark_file_archived**](MediaLibraryApi.md#mark_file_archived) | **POST** `/api/2/media/files/{id}/mark-archived` | 
[**mark_file_not_archived**](MediaLibraryApi.md#mark_file_not_archived) | **POST** `/api/2/media/files/{id}/mark-not-archived` | 
[**mark_media_directory_as_showroom**](MediaLibraryApi.md#mark_media_directory_as_showroom) | **POST** `/api/2/media/files/{id}/showroom` | 
[**patch_asset**](MediaLibraryApi.md#patch_asset) | **PATCH** `/api/2/media/assets/{id}` | 
[**patch_asset_subtitle_link**](MediaLibraryApi.md#patch_asset_subtitle_link) | **PATCH** `/api/2/media/assets/{asset_id}/subtitle-links/{id}` | 
[**patch_comment**](MediaLibraryApi.md#patch_comment) | **PATCH** `/api/2/media/comments/{id}` | 
[**patch_custom_field**](MediaLibraryApi.md#patch_custom_field) | **PATCH** `/api/2/media/custom-fields/{id}` | 
[**patch_editor_project**](MediaLibraryApi.md#patch_editor_project) | **PATCH** `/api/2/media/editor/{id}` | 
[**patch_editor_subtitle**](MediaLibraryApi.md#patch_editor_subtitle) | **PATCH** `/api/2/media/subtitles/{id}` | 
[**patch_external_transcoder**](MediaLibraryApi.md#patch_external_transcoder) | **PATCH** `/api/2/media/external-transcoders/{id}` | 
[**patch_marker**](MediaLibraryApi.md#patch_marker) | **PATCH** `/api/2/media/assets/{asset_id}/markers/{id}` | 
[**patch_media_file**](MediaLibraryApi.md#patch_media_file) | **PATCH** `/api/2/media/files/{id}` | 
[**patch_media_file_template**](MediaLibraryApi.md#patch_media_file_template) | **PATCH** `/api/2/media/files/templates/{id}` | 
[**patch_media_pinned_item**](MediaLibraryApi.md#patch_media_pinned_item) | **PATCH** `/api/2/media/pinned-items/{id}` | 
[**patch_media_root**](MediaLibraryApi.md#patch_media_root) | **PATCH** `/api/2/media/roots/{id}` | 
[**patch_media_root_permission**](MediaLibraryApi.md#patch_media_root_permission) | **PATCH** `/api/2/media/root-permissions/{id}` | 
[**patch_media_tag**](MediaLibraryApi.md#patch_media_tag) | **PATCH** `/api/2/media/tags/{id}` | 
[**patch_proxy_profile**](MediaLibraryApi.md#patch_proxy_profile) | **PATCH** `/api/2/media/proxy-profiles/{id}` | 
[**patch_saved_search**](MediaLibraryApi.md#patch_saved_search) | **PATCH** `/api/2/media/saved-searches/{id}` | 
[**patch_sharing_permission_preset**](MediaLibraryApi.md#patch_sharing_permission_preset) | **PATCH** `/api/2/media/sharing-permission-presets/{id}` | 
[**patch_subclip**](MediaLibraryApi.md#patch_subclip) | **PATCH** `/api/2/media/{asset_id}/subclips/{id}` | 
[**patch_workflow**](MediaLibraryApi.md#patch_workflow) | **PATCH** `/api/2/media/workflows/{id}` | 
[**pin_media_item_globally**](MediaLibraryApi.md#pin_media_item_globally) | **POST** `/api/2/media/pinned-items/{id}/pin-globally` | 
[**pin_media_root_permission**](MediaLibraryApi.md#pin_media_root_permission) | **POST** `/api/2/media/root-permissions/{id}/pin` | 
[**recursively_tag_media_directory**](MediaLibraryApi.md#recursively_tag_media_directory) | **POST** `/api/2/media/files/{id}/tag` | 
[**reinclude_directory_for_proxy_generation**](MediaLibraryApi.md#reinclude_directory_for_proxy_generation) | **DELETE** `/api/2/media/files/{id}/dont-proxy` | 
[**reinclude_directory_for_scan**](MediaLibraryApi.md#reinclude_directory_for_scan) | **DELETE** `/api/2/media/files/{id}/dont-scan` | 
[**reindex_media_directory**](MediaLibraryApi.md#reindex_media_directory) | **POST** `/api/2/media/files/{id}/search-reindex` | 
[**remove_asset_from_set**](MediaLibraryApi.md#remove_asset_from_set) | **DELETE** `/api/2/media/assets/{id}/set` | 
[**rename_custom_field**](MediaLibraryApi.md#rename_custom_field) | **POST** `/api/2/media/custom-fields/{id}/rename` | 
[**render_sequence**](MediaLibraryApi.md#render_sequence) | **POST** `/api/2/media/editor/render` | 
[**render_subclip**](MediaLibraryApi.md#render_subclip) | **POST** `/api/2/media/{asset_id}/subclips/{id}/render` | 
[**request_media_scan**](MediaLibraryApi.md#request_media_scan) | **POST** `/api/2/scanner/scan` | 
[**resolve_comment**](MediaLibraryApi.md#resolve_comment) | **POST** `/api/2/media/comments/{id}/resolve` | 
[**share_media_library_objects**](MediaLibraryApi.md#share_media_library_objects) | **POST** `/api/2/media/share` | 
[**test_external_transcoder_connection**](MediaLibraryApi.md#test_external_transcoder_connection) | **POST** `/api/2/media/external-transcoders/test-connection` | 
[**transition_workflow**](MediaLibraryApi.md#transition_workflow) | **POST** `/api/2/media/workflow/transition` | 
[**unbookmark_media_directory**](MediaLibraryApi.md#unbookmark_media_directory) | **DELETE** `/api/2/media/files/{id}/bookmark` | 
[**unlink_asset_version**](MediaLibraryApi.md#unlink_asset_version) | **DELETE** `/api/2/media/assets/{id}/versions` | 
[**unmark_media_directory_as_showroom**](MediaLibraryApi.md#unmark_media_directory_as_showroom) | **DELETE** `/api/2/media/files/{id}/showroom` | 
[**unpin_media_item_globally**](MediaLibraryApi.md#unpin_media_item_globally) | **POST** `/api/2/media/pinned-items/{id}/unpin-globally` | 
[**unresolve_comment**](MediaLibraryApi.md#unresolve_comment) | **POST** `/api/2/media/comments/{id}/unresolve` | 
[**update_asset**](MediaLibraryApi.md#update_asset) | **PUT** `/api/2/media/assets/{id}` | 
[**update_asset_subtitle_link**](MediaLibraryApi.md#update_asset_subtitle_link) | **PUT** `/api/2/media/assets/{asset_id}/subtitle-links/{id}` | 
[**update_comment**](MediaLibraryApi.md#update_comment) | **PUT** `/api/2/media/comments/{id}` | 
[**update_custom_field**](MediaLibraryApi.md#update_custom_field) | **PUT** `/api/2/media/custom-fields/{id}` | 
[**update_editor_project**](MediaLibraryApi.md#update_editor_project) | **PUT** `/api/2/media/editor/{id}` | 
[**update_editor_subtitle**](MediaLibraryApi.md#update_editor_subtitle) | **PUT** `/api/2/media/subtitles/{id}` | 
[**update_external_transcoder**](MediaLibraryApi.md#update_external_transcoder) | **PUT** `/api/2/media/external-transcoders/{id}` | 
[**update_marker**](MediaLibraryApi.md#update_marker) | **PUT** `/api/2/media/assets/{asset_id}/markers/{id}` | 
[**update_media_file**](MediaLibraryApi.md#update_media_file) | **PUT** `/api/2/media/files/{id}` | 
[**update_media_file_template**](MediaLibraryApi.md#update_media_file_template) | **PUT** `/api/2/media/files/templates/{id}` | 
[**update_media_pinned_item**](MediaLibraryApi.md#update_media_pinned_item) | **PUT** `/api/2/media/pinned-items/{id}` | 
[**update_media_root**](MediaLibraryApi.md#update_media_root) | **PUT** `/api/2/media/roots/{id}` | 
[**update_media_root_cover_image**](MediaLibraryApi.md#update_media_root_cover_image) | **POST** `/api/2/media/roots/{id}/cover` | 
[**update_media_root_permission**](MediaLibraryApi.md#update_media_root_permission) | **PUT** `/api/2/media/root-permissions/{id}` | 
[**update_media_tag**](MediaLibraryApi.md#update_media_tag) | **PUT** `/api/2/media/tags/{id}` | 
[**update_proxy_profile**](MediaLibraryApi.md#update_proxy_profile) | **PUT** `/api/2/media/proxy-profiles/{id}` | 
[**update_proxy_profile_watermark_image**](MediaLibraryApi.md#update_proxy_profile_watermark_image) | **POST** `/api/2/media/proxy-profiles/{id}/watermark` | 
[**update_saved_search**](MediaLibraryApi.md#update_saved_search) | **PUT** `/api/2/media/saved-searches/{id}` | 
[**update_sharing_permission_preset**](MediaLibraryApi.md#update_sharing_permission_preset) | **PUT** `/api/2/media/sharing-permission-presets/{id}` | 
[**update_subclip**](MediaLibraryApi.md#update_subclip) | **PUT** `/api/2/media/{asset_id}/subclips/{id}` | 
[**update_workflow**](MediaLibraryApi.md#update_workflow) | **PUT** `/api/2/media/workflows/{id}` | 
[**web_upload_completed**](MediaLibraryApi.md#web_upload_completed) | **POST** `/api/2/media/web/upload-completed` | 


# **bookmark_media_directory**
    def bookmark_media_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions OR allow_upload Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.bookmark_media_directory(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->bookmark_media_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **clear_subclip_clipboard**
    def clear_subclip_clipboard()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.clear_subclip_clipboard()
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->clear_subclip_clipboard: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **clear_subtitle_clipboard**
    def clear_subtitle_clipboard()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.clear_subtitle_clipboard()
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->clear_subtitle_clipboard: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **combine_assets_into_set**
    def combine_assets_into_set(multiple_assets_request)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.multiple_assets_request import MultipleAssetsRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    multiple_assets_request = MultipleAssetsRequest(
        assets=[
            1,
        ],
    ) # MultipleAssetsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.combine_assets_into_set(multiple_assets_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->combine_assets_into_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multiple_assets_request** | [**MultipleAssetsRequest**](MultipleAssetsRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **count_unresolved_comments**
    def UnresolvedCount count_unresolved_comments()



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.unresolved_count import UnresolvedCount
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    root = 1 # int | Filter the returned list by `root`. (optional)
    user = 1 # int | Filter the returned list by `user`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    cursor = "cursor_example" # str | The pagination cursor value. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.count_unresolved_comments(asset=asset, root=root, user=user, ordering=ordering, cursor=cursor, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->count_unresolved_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **root** | **int**| Filter the returned list by &#x60;root&#x60;. | [optional]
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**UnresolvedCount**](UnresolvedCount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_asset_rating**
    def AssetRating create_asset_rating(asset_id, asset_rating_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db, show_ratings Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_rating_update import AssetRatingUpdate
from elements_sdk.model.asset_rating import AssetRating
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    asset_rating_update = AssetRatingUpdate(
        user=ElementsUserMiniReference(
            id=1,
        ),
        rating=-2147483648,
    ) # AssetRatingUpdate | 
    root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_asset_rating(asset_id, asset_rating_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_asset_rating: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_asset_rating(asset_id, asset_rating_update, root=root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **asset_rating_update** | [**AssetRatingUpdate**](AssetRatingUpdate.md)|  |
 **root** | **int**|  | [optional]

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_asset_subtitle_link**
    def AssetSubtitleLink create_asset_subtitle_link(asset_id, asset_subtitle_link_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_subtitle_link import AssetSubtitleLink
from elements_sdk.model.asset_subtitle_link_update import AssetSubtitleLinkUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    asset_subtitle_link_update = AssetSubtitleLinkUpdate(
        subtitle=AssetMiniReference(
            id=1,
            default_proxy=Proxy(
                id=1,
                profile=ProxyProfileMini(
                    id=1,
                    name="name_example",
                    allow_download=True,
                    proxy_generator="ffmpeg",
                ),
                transforms=Transforms(
                    to_source_point=[
                        [
                            1,
                        ],
                    ],
                    to_source_size=[
                        [
                            1,
                        ],
                    ],
                    from_source_point=[
                        [
                            1,
                        ],
                    ],
                    from_source_size=[
                        [
                            1,
                        ],
                    ],
                ),
                generated_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                failed=True,
                failed_count=-2147483648,
                name="name_example",
                variant_id="default",
                variant_config="variant_config_example",
                source_audio_layout_preserved=True,
                asset=1,
            ),
            format=FormatMetadata(
            ),
        ),
        label="label_example",
        key="key_example",
    ) # AssetSubtitleLinkUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_asset_subtitle_link(asset_id, asset_subtitle_link_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_asset_subtitle_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **asset_subtitle_link_update** | [**AssetSubtitleLinkUpdate**](AssetSubtitleLinkUpdate.md)|  |

### Return type

[**AssetSubtitleLink**](AssetSubtitleLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_comment**
    def Comment create_comment(comment_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.comment import Comment
from elements_sdk.model.comment_update import CommentUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    comment_update = CommentUpdate(
        assignee=None,
        user=None,
        drawing={
            "key": "key_example",
        },
        tags=[
            TagReference(
                id=1,
            ),
        ],
        text="text_example",
        time=3.14,
        is_cloud=True,
        resolved=True,
        resolved_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        asset=1,
        root=1,
        parent=1,
    ) # CommentUpdate | 
    root = 1 # int |  (optional)
    bundle = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_comment(comment_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_comment(comment_update, root=root, bundle=bundle)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_update** | [**CommentUpdate**](CommentUpdate.md)|  |
 **root** | **int**|  | [optional]
 **bundle** | **int**|  | [optional]

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_custom_field**
    def CustomField create_custom_field(custom_field_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.custom_field import CustomField
from elements_sdk.model.custom_field_update import CustomFieldUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    custom_field_update = CustomFieldUpdate(
        labels=[
            {
                "key": "key_example",
            },
        ],
        options=[
            "options_example",
        ],
        name="name_example",
        order=-2147483648,
        type="type_example",
        use_for_uploads=True,
        require_to_upload=True,
        non_user_editable=True,
        validation="number_of_digits",
        regex="regex_example",
        range_min=-2147483648,
        range_max=-2147483648,
        number_of_digits=-2147483648,
        metadata_prefill="metadata_prefill_example",
        highlight_expiration=True,
        multiple_response=True,
        help_text="help_text_example",
        users_from_group=1,
    ) # CustomFieldUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_custom_field(custom_field_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_update** | [**CustomFieldUpdate**](CustomFieldUpdate.md)|  |

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_editor_project**
    def EditorProject create_editor_project(editor_project_update)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.editor_project_update import EditorProjectUpdate
from elements_sdk.model.editor_project import EditorProject
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    editor_project_update = EditorProjectUpdate(
        file=1,
        parent=1,
        parent_path="parent_path_example",
        existing_file=1,
        format="format_example",
        project={},
    ) # EditorProjectUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_editor_project(editor_project_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_editor_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editor_project_update** | [**EditorProjectUpdate**](EditorProjectUpdate.md)|  |

### Return type

[**EditorProject**](EditorProject.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_editor_subtitle**
    def EditorSubtitle create_editor_subtitle(editor_subtitle_update)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.editor_subtitle import EditorSubtitle
from elements_sdk.model.editor_subtitle_update import EditorSubtitleUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    editor_subtitle_update = EditorSubtitleUpdate(
        file=1,
        parent=1,
        name="name_example",
        format="format_example",
        subtitle=Subtitle(
            info={
                "key": "key_example",
            },
            styles={
                "key": "key_example",
            },
            events=[
                SubtitleEvent(
                    start=1,
                    end=1,
                    text="text_example",
                    marked=True,
                    layer=1,
                    style="style_example",
                    name="name_example",
                    marginl=1,
                    marginr=1,
                    marginv=1,
                    effect="effect_example",
                    type="type_example",
                ),
            ],
        ),
    ) # EditorSubtitleUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_editor_subtitle(editor_subtitle_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_editor_subtitle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editor_subtitle_update** | [**EditorSubtitleUpdate**](EditorSubtitleUpdate.md)|  |

### Return type

[**EditorSubtitle**](EditorSubtitle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_external_transcoder**
    def ExternalTranscoder create_external_transcoder(external_transcoder_update)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.external_transcoder import ExternalTranscoder
from elements_sdk.model.external_transcoder_update import ExternalTranscoderUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    external_transcoder_update = ExternalTranscoderUpdate(
        path_mappings=[
            PathMapping(
                local="local_example",
                remote="remote_example",
            ),
        ],
        name="name_example",
        type="transkoder",
        address="address_example",
    ) # ExternalTranscoderUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_external_transcoder(external_transcoder_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_transcoder_update** | [**ExternalTranscoderUpdate**](ExternalTranscoderUpdate.md)|  |

### Return type

[**ExternalTranscoder**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_marker**
    def Marker create_marker(asset_id, marker_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.marker import Marker
from elements_sdk.model.marker_update import MarkerUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    marker_update = MarkerUpdate(
        title="title_example",
        text="text_example",
        t_in=3.14,
        t_out=3.14,
        asset=1,
    ) # MarkerUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_marker(asset_id, marker_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **marker_update** | [**MarkerUpdate**](MarkerUpdate.md)|  |

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_media_file_template**
    def MediaFileTemplate create_media_file_template(media_file_template_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_template_update import MediaFileTemplateUpdate
from elements_sdk.model.media_file_template import MediaFileTemplate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    media_file_template_update = MediaFileTemplateUpdate(
        file=MediaFileReference(
            id=1,
            volume=VolumeMini(
                id=1,
                path="path_example",
                display_name="display_name_example",
                visual_tag="visual_tag_example",
                type="generic",
            ),
            resolved_permission=MediaRootPermission(
                id=1,
                user=None,
                group=None,
                allow_read=True,
                allow_create=True,
                allow_write_fs=True,
                allow_write_db=True,
                allow_proxy_download=True,
                allow_original_download=True,
                allow_upload=True,
                allow_sharing=True,
                allow_delete_fs=True,
                allow_delete_db=True,
                show_tags=True,
                show_comments=True,
                show_locations=True,
                show_custom_fields=True,
                show_ratings=True,
                show_subclips=True,
                show_subtitles=True,
                show_ai_metadata=True,
                show_markers=True,
                show_history=True,
                path="path_example",
                root=1,
                is_temporary_for_token=1,
            ),
            root=MediaRootMini(
                id=1,
                name="name_example",
                description="description_example",
                volume=VolumeMini(
                    id=1,
                    path="path_example",
                    display_name="display_name_example",
                    visual_tag="visual_tag_example",
                    type="generic",
                ),
                path="path_example",
                prefetch_thumbnail_strips=True,
                view_mode="view_mode_example",
                cover="cover_example",
            ),
            modified_by=ElementsUserMini(
                id=1,
                avatar="avatar_example",
                email="email_example",
                full_name="full_name_example",
                is_external=True,
                is_cloud=True,
                username="username_example",
            ),
            exclusion_info=MediaFileExclusionInfo(
                scan=PathExclusionInfo(
                    is_parent_excluded=True,
                    path_excluded="path_excluded_example",
                    pattern_excluded="pattern_excluded_example",
                ),
                proxy=PathExclusionInfo(
                    is_parent_excluded=True,
                    path_excluded="path_excluded_example",
                    pattern_excluded="pattern_excluded_example",
                ),
            ),
        ),
        name="name_example",
    ) # MediaFileTemplateUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_media_file_template(media_file_template_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_file_template_update** | [**MediaFileTemplateUpdate**](MediaFileTemplateUpdate.md)|  |

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_media_root**
    def MediaRootDetail create_media_root(media_root_detail_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_detail import MediaRootDetail
from elements_sdk.model.media_root_detail_update import MediaRootDetailUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    media_root_detail_update = MediaRootDetailUpdate(
        custom_fields=[
            CustomFieldReference(
                id=1,
            ),
        ],
        volume=VolumeReference(
            id=1,
            fs_properties=FSProperties(
                needs_node=True,
                supports_directory_quotas=True,
                supports_workspace_quotas=True,
                supports_soft_quotas=True,
                supports_user_quotas=True,
                supports_group_quotas=True,
                supports_xattrs=True,
                supports_snapshots=True,
                creating_directory_quota_destroys_content=True,
                removing_directory_quota_destroys_content=True,
                supports_posix_permissions=True,
                supports_dates=True,
                supports_renaming=True,
            ),
            backend=Backend(
                name="name_example",
                properties=BackendProperties(
                    supports_sharing_rw_permissions_priority=True,
                    supports_sharing_afp=True,
                    supports_sharing_smb_require_logon=True,
                    supports_sharing_smb_recycle_bin=True,
                    supports_sharing_smb_xattrs=True,
                    supports_sharing_smb_symlinks=True,
                    supports_sharing_smb_custom_options=True,
                    supports_sharing_smb_allow_execute=True,
                    supports_sharing_smb_locking_options=True,
                    supports_sharing_smb_hidden=True,
                    supports_sharing_veto=True,
                    supports_sharing_nfs_permissions=True,
                ),
            ),
            status=VolumeStatus(
                online=True,
                size_total=1,
                size_used=1,
                size_free=1,
                snfs=VolumeSNFSStatus(
                    stripe_groups=[
                        SNFSStripeGroup(
                            name="name_example",
                            status_tags=[
                                "status_tags_example",
                            ],
                            affinity="affinity_example",
                            size_total=1,
                            size_used=1,
                            size_free=1,
                        ),
                    ],
                ),
                beegfs=VolumeBeeGFSStatus(
                    nodes=[
                        BeeGFSNode(
                            node=None,
                            host="host_example",
                            roles=[
                                "roles_example",
                            ],
                            addresses=[
                                "addresses_example",
                            ],
                        ),
                    ],
                    targets=[
                        BeeGFSTarget(
                            node=None,
                            id=1,
                            host="host_example",
                            storage_pool=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            online=True,
                            consistent=True,
                            errors=[
                                "errors_example",
                            ],
                        ),
                    ],
                ),
            ),
        ),
        workflow=None,
        jobs=[
            JobReference(
                id=1,
            ),
        ],
        name="name_example",
        path="path_example",
        description="description_example",
        needs_rescan=True,
        view_mode="view_mode_example",
        view_style="view_style_example",
        view_default_tab="view_default_tab_example",
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_markers=True,
        show_history=True,
        show_ai_metadata=True,
        prefetch_thumbnail_strips=True,
        cover="cover_example",
        name_field="name_field_example",
        share_comments=True,
        share_link_duration=-2147483648,
        disable_framestacks=True,
        default_proxy_profile=1,
        cloud_proxy_profile=1,
        proxy_profiles=[
            1,
        ],
        tags=[
            1,
        ],
    ) # MediaRootDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_media_root(media_root_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_root_detail_update** | [**MediaRootDetailUpdate**](MediaRootDetailUpdate.md)|  |

### Return type

[**MediaRootDetail**](MediaRootDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_media_root_permission**
    def MediaRootPermission create_media_root_permission(media_root_permission_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_permission_update import MediaRootPermissionUpdate
from elements_sdk.model.media_root_permission import MediaRootPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    media_root_permission_update = MediaRootPermissionUpdate(
        user=None,
        group=None,
        allow_read=True,
        allow_create=True,
        allow_write_fs=True,
        allow_write_db=True,
        allow_proxy_download=True,
        allow_original_download=True,
        allow_upload=True,
        allow_sharing=True,
        allow_delete_fs=True,
        allow_delete_db=True,
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_ai_metadata=True,
        show_markers=True,
        show_history=True,
        path="path_example",
        root=1,
        is_temporary_for_token=1,
    ) # MediaRootPermissionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_media_root_permission(media_root_permission_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_root_permission_update** | [**MediaRootPermissionUpdate**](MediaRootPermissionUpdate.md)|  |

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_media_tag**
    def UnfilteredTag create_media_tag(unfiltered_tag_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.unfiltered_tag_update import UnfilteredTagUpdate
from elements_sdk.model.unfiltered_tag import UnfilteredTag
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    unfiltered_tag_update = UnfilteredTagUpdate(
        roots=[
            1,
        ],
        name="name_example",
        shared=True,
        color="color_example",
    ) # UnfilteredTagUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_media_tag(unfiltered_tag_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unfiltered_tag_update** | [**UnfilteredTagUpdate**](UnfilteredTagUpdate.md)|  |

### Return type

[**UnfilteredTag**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_proxy_profile**
    def ProxyProfile create_proxy_profile(proxy_profile_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_profile import ProxyProfile
from elements_sdk.model.proxy_profile_update import ProxyProfileUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    proxy_profile_update = ProxyProfileUpdate(
        name="name_example",
        proxy_generator="ffmpeg",
        type="video",
        resolution="resolution_example",
        rate_control="CRF",
        crf=-2147483648,
        bitrate=-2147483648,
        audio_bitrate=-2147483648,
        variants_limit=-2147483648,
        enable_dense_filmstrip=True,
        image_format="png",
        enable_watermark=True,
        watermark_image="watermark_image_example",
        watermark_position="TL",
        watermark_opacity=3.14,
        watermark_size=3.14,
        enable_timecode=True,
        timecode_position="TL",
        timecode_opacity=3.14,
        timecode_size=3.14,
        lut="lut_example",
        hotfolder_copy_to="hotfolder_copy_to_example",
        hotfolder_read_from="hotfolder_read_from_example",
        hotfolder_queue_timeout=-2147483648,
        hotfolder_encode_timeout=-2147483648,
        vantage_workflow_id="vantage_workflow_id_example",
        external_transcoder_staging_path="external_transcoder_staging_path_example",
        allow_download=True,
        keep_audio_layout=True,
        external_transcoder=1,
    ) # ProxyProfileUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_proxy_profile(proxy_profile_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_profile_update** | [**ProxyProfileUpdate**](ProxyProfileUpdate.md)|  |

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_saved_search**
    def SavedSearch create_saved_search(saved_search_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.saved_search import SavedSearch
from elements_sdk.model.saved_search_update import SavedSearchUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    saved_search_update = SavedSearchUpdate(
        root=None,
        query=[
            {},
        ],
        name="name_example",
    ) # SavedSearchUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_saved_search(saved_search_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_saved_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_search_update** | [**SavedSearchUpdate**](SavedSearchUpdate.md)|  |

### Return type

[**SavedSearch**](SavedSearch.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_sharing_permission_preset**
    def SharingPermissionPreset create_sharing_permission_preset(sharing_permission_preset_update)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.sharing_permission_preset_update import SharingPermissionPresetUpdate
from elements_sdk.model.sharing_permission_preset import SharingPermissionPreset
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    sharing_permission_preset_update = SharingPermissionPresetUpdate(
        allow_read=True,
        allow_create=True,
        allow_write_fs=True,
        allow_write_db=True,
        allow_proxy_download=True,
        allow_original_download=True,
        allow_upload=True,
        allow_sharing=True,
        allow_delete_fs=True,
        allow_delete_db=True,
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_ai_metadata=True,
        show_markers=True,
        show_history=True,
        name="name_example",
        default=True,
    ) # SharingPermissionPresetUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_sharing_permission_preset(sharing_permission_preset_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_sharing_permission_preset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sharing_permission_preset_update** | [**SharingPermissionPresetUpdate**](SharingPermissionPresetUpdate.md)|  |

### Return type

[**SharingPermissionPreset**](SharingPermissionPreset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_subclip**
    def Subclip create_subclip(asset_id, subclip_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * Must be shared OR Must own the object   * allow_write_db, show_subclips Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.subclip_update import SubclipUpdate
from elements_sdk.model.subclip import Subclip
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    subclip_update = SubclipUpdate(
        rendered=None,
        shared=True,
        name="name_example",
        t_in=3.14,
        t_out=3.14,
        root=MediaRootMiniReference(
            id=1,
            volume=VolumeMini(
                id=1,
                path="path_example",
                display_name="display_name_example",
                visual_tag="visual_tag_example",
                type="generic",
            ),
            path="path_example",
        ),
    ) # SubclipUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_subclip(asset_id, subclip_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **subclip_update** | [**SubclipUpdate**](SubclipUpdate.md)|  |

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_subclip_clipboard_entry**
    def SubclipClipboardEntry create_subclip_clipboard_entry(subclip_clipboard_entry_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.subclip_clipboard_entry_update import SubclipClipboardEntryUpdate
from elements_sdk.model.subclip_clipboard_entry import SubclipClipboardEntry
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    subclip_clipboard_entry_update = SubclipClipboardEntryUpdate(
        cut=SubclipReference(
            id=1,
            asset=AssetMini(
                id=1,
                default_proxy=Proxy(
                    id=1,
                    profile=ProxyProfileMini(
                        id=1,
                        name="name_example",
                        allow_download=True,
                        proxy_generator="ffmpeg",
                    ),
                    transforms=Transforms(
                        to_source_point=[
                            [
                                1,
                            ],
                        ],
                        to_source_size=[
                            [
                                1,
                            ],
                        ],
                        from_source_point=[
                            [
                                1,
                            ],
                        ],
                        from_source_size=[
                            [
                                1,
                            ],
                        ],
                    ),
                    generated_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    failed=True,
                    failed_count=-2147483648,
                    name="name_example",
                    variant_id="default",
                    variant_config="variant_config_example",
                    source_audio_layout_preserved=True,
                    asset=1,
                ),
                format=FormatMetadata(
                ),
            ),
            root=MediaRootMini(
                id=1,
                name="name_example",
                description="description_example",
                volume=VolumeMini(
                    id=1,
                    path="path_example",
                    display_name="display_name_example",
                    visual_tag="visual_tag_example",
                    type="generic",
                ),
                path="path_example",
                prefetch_thumbnail_strips=True,
                view_mode="view_mode_example",
                cover="cover_example",
            ),
        ),
        bundle=None,
    ) # SubclipClipboardEntryUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_subclip_clipboard_entry(subclip_clipboard_entry_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_subclip_clipboard_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subclip_clipboard_entry_update** | [**SubclipClipboardEntryUpdate**](SubclipClipboardEntryUpdate.md)|  |

### Return type

[**SubclipClipboardEntry**](SubclipClipboardEntry.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_subtitle_clipboard_entry**
    def SubtitleClipboardEntry create_subtitle_clipboard_entry(subtitle_clipboard_entry_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.subtitle_clipboard_entry import SubtitleClipboardEntry
from elements_sdk.model.subtitle_clipboard_entry_update import SubtitleClipboardEntryUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    subtitle_clipboard_entry_update = SubtitleClipboardEntryUpdate(
        subtitle=AssetMiniReference(
            id=1,
            default_proxy=Proxy(
                id=1,
                profile=ProxyProfileMini(
                    id=1,
                    name="name_example",
                    allow_download=True,
                    proxy_generator="ffmpeg",
                ),
                transforms=Transforms(
                    to_source_point=[
                        [
                            1,
                        ],
                    ],
                    to_source_size=[
                        [
                            1,
                        ],
                    ],
                    from_source_point=[
                        [
                            1,
                        ],
                    ],
                    from_source_size=[
                        [
                            1,
                        ],
                    ],
                ),
                generated_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                failed=True,
                failed_count=-2147483648,
                name="name_example",
                variant_id="default",
                variant_config="variant_config_example",
                source_audio_layout_preserved=True,
                asset=1,
            ),
            format=FormatMetadata(
            ),
        ),
        bundle=None,
    ) # SubtitleClipboardEntryUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_subtitle_clipboard_entry(subtitle_clipboard_entry_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_subtitle_clipboard_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subtitle_clipboard_entry_update** | [**SubtitleClipboardEntryUpdate**](SubtitleClipboardEntryUpdate.md)|  |

### Return type

[**SubtitleClipboardEntry**](SubtitleClipboardEntry.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **create_workflow**
    def Workflow create_workflow(workflow_update)



### Required permissions    * User account permission: `media:roots:manage`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.workflow_update import WorkflowUpdate
from elements_sdk.model.workflow import Workflow
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    workflow_update = WorkflowUpdate(
        states=[
            {},
        ],
        transitions=[
            {},
        ],
        roots=[
            1,
        ],
        name="name_example",
    ) # WorkflowUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_workflow(workflow_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->create_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_update** | [**WorkflowUpdate**](WorkflowUpdate.md)|  |

### Return type

[**Workflow**](Workflow.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_asset**
    def delete_asset(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_delete_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_asset(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_asset_rating**
    def delete_asset_rating(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * Must own the object   * allow_write_db, show_ratings Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this Rating.
    root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_asset_rating(asset_id, id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_asset_rating: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.delete_asset_rating(asset_id, id, root=root)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this Rating. |
 **root** | **int**|  | [optional]

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_asset_subtitle_link**
    def delete_asset_subtitle_link(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_delete_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this Asset subtitle file link.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_asset_subtitle_link(asset_id, id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_asset_subtitle_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this Asset subtitle file link. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_comment**
    def delete_comment(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_delete_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Comment.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_comment(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_custom_field**
    def delete_custom_field(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Custom field.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_custom_field(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_easy_sharing_token_for_bundle**
    def delete_easy_sharing_token_for_bundle(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_sharing Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Bundle.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_easy_sharing_token_for_bundle(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_easy_sharing_token_for_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Bundle. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_easy_sharing_token_for_directory**
    def delete_easy_sharing_token_for_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_sharing Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_easy_sharing_token_for_directory(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_easy_sharing_token_for_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_external_transcoder**
    def delete_external_transcoder(id)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this external transcoder.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_external_transcoder(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_marker**
    def delete_marker(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this marker.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_marker(asset_id, id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this marker. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_media_file_template**
    def delete_media_file_template(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Template.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_media_file_template(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_media_library_objects**
    def [TaskInfo] delete_media_library_objects(media_library_delete_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.media_library_delete_request import MediaLibraryDeleteRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    media_library_delete_request = MediaLibraryDeleteRequest(
        bundles=[
            1,
        ],
        files=[
            1,
        ],
        assets=[
            1,
        ],
        delete_from_database=False,
        delete_from_storage=False,
    ) # MediaLibraryDeleteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_media_library_objects(media_library_delete_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_library_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_library_delete_request** | [**MediaLibraryDeleteRequest**](MediaLibraryDeleteRequest.md)|  |

### Return type

[**[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_media_pinned_item**
    def delete_media_pinned_item(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media pinned item.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_media_pinned_item(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_pinned_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media pinned item. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_media_root**
    def delete_media_root(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media root.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_media_root(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_media_root_cover_image**
    def delete_media_root_cover_image(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media root.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_media_root_cover_image(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_root_cover_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_media_root_permission**
    def delete_media_root_permission(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Media Root Permission.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_media_root_permission(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_media_tag**
    def delete_media_tag(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Tag.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_media_tag(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_media_update**
    def delete_media_update(id)



### Required permissions    * User account permission: `media:access` (read) / `media:updates:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Update.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_media_update(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_media_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Update. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_proxy**
    def delete_proxy(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_delete_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this proxy.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_proxy(asset_id, id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_proxy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this proxy. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_proxy_profile**
    def TaskInfo delete_proxy_profile(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this proxy profile.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_proxy_profile(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_proxy_profile_watermark_image**
    def delete_proxy_profile_watermark_image(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this proxy profile.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_proxy_profile_watermark_image(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_proxy_profile_watermark_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_saved_search**
    def delete_saved_search(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this saved search.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_saved_search(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_saved_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this saved search. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_sharing_permission_preset**
    def delete_sharing_permission_preset(id)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Sharing Permission Preset.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_sharing_permission_preset(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_sharing_permission_preset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Sharing Permission Preset. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_subclip**
    def delete_subclip(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * Must be shared OR Must own the object   * allow_write_db, show_subclips Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this subclip.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_subclip(asset_id, id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this subclip. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_subclip_clipboard_entry**
    def delete_subclip_clipboard_entry(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this subclip clipboard entry.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_subclip_clipboard_entry(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_subclip_clipboard_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subclip clipboard entry. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_subtitle_clipboard_entry**
    def delete_subtitle_clipboard_entry(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this subtitle clipboard entry.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_subtitle_clipboard_entry(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_subtitle_clipboard_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this subtitle clipboard entry. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **delete_workflow**
    def delete_workflow(id)



### Required permissions    * User account permission: `media:roots:manage`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Workflow.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_workflow(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->delete_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Workflow. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **discover_media**
    def MediaFile discover_media(scanner_discover_endpoint_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from elements_sdk.model.scanner_discover_endpoint_request import ScannerDiscoverEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    scanner_discover_endpoint_request = ScannerDiscoverEndpointRequest(
        path="path_example",
        recursive=True,
    ) # ScannerDiscoverEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.discover_media(scanner_discover_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->discover_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scanner_discover_endpoint_request** | [**ScannerDiscoverEndpointRequest**](ScannerDiscoverEndpointRequest.md)|  |

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **download_asset_proxy_file**
    def download_asset_proxy_file(id, filename)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.
    filename = "filename_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_asset_proxy_file(id, filename)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->download_asset_proxy_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |
 **filename** | **str**|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **download_media_file**
    def download_media_file(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_original_download Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_media_file(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->download_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **download_proxy**
    def download_proxy(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this proxy.
    bundle_id = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_proxy(asset_id, id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->download_proxy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.download_proxy(asset_id, id, bundle_id=bundle_id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->download_proxy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this proxy. |
 **bundle_id** | **int**|  | [optional]

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **editor_export_xml_for_assset**
    def XMLExport editor_export_xml_for_assset(asset_ids)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.xml_export import XMLExport
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_ids = "asset_ids_example" # str | 
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    uri = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.editor_export_xml_for_assset(asset_ids)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_assset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.editor_export_xml_for_assset(asset_ids, ordering=ordering, limit=limit, offset=offset, uri=uri)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_assset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | **str**|  |
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **uri** | **bool**|  | [optional]

### Return type

[**XMLExport**](XMLExport.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **editor_export_xml_for_bundle**
    def XMLExport editor_export_xml_for_bundle(bundle_ids)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.xml_export import XMLExport
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    bundle_ids = "bundle_ids_example" # str | 
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    uri = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.editor_export_xml_for_bundle(bundle_ids)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_bundle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.editor_export_xml_for_bundle(bundle_ids, ordering=ordering, limit=limit, offset=offset, uri=uri)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_ids** | **str**|  |
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **uri** | **bool**|  | [optional]

### Return type

[**XMLExport**](XMLExport.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **editor_export_xml_for_project**
    def XMLExport editor_export_xml_for_project(id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.xml_export import XMLExport
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    uri = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.editor_export_xml_for_project(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.editor_export_xml_for_project(id, uri=uri)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->editor_export_xml_for_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **uri** | **bool**|  | [optional]

### Return type

[**XMLExport**](XMLExport.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **exclude_directory_from_proxy_generation**
    def exclude_directory_from_proxy_generation(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.exclude_directory_from_proxy_generation(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->exclude_directory_from_proxy_generation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **exclude_directory_from_scan**
    def exclude_directory_from_scan(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.exclude_directory_from_scan(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->exclude_directory_from_scan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_comments_for_avid**
    def XMLExport export_comments_for_avid(asset_id, export_format)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.xml_export import XMLExport
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    export_format = "export_format_example" # str | 
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.export_comments_for_avid(asset_id, export_format)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->export_comments_for_avid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.export_comments_for_avid(asset_id, export_format, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->export_comments_for_avid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **export_format** | **str**|  |
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**XMLExport**](XMLExport.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **export_editor_timeline**
    def export_editor_timeline(timeline_export_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.timeline_export_request import TimelineExportRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    timeline_export_request = TimelineExportRequest(
        project={},
        sequence="sequence_example",
        format="format_example",
    ) # TimelineExportRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.export_editor_timeline(timeline_export_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->export_editor_timeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeline_export_request** | [**TimelineExportRequest**](TimelineExportRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **extract_stream**
    def TaskInfo extract_stream(id, extract_request)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_fs Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.extract_request import ExtractRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.
    extract_request = ExtractRequest(
        stream=1,
        destination="destination_example",
    ) # ExtractRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.extract_stream(id, extract_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->extract_stream: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |
 **extract_request** | [**ExtractRequest**](ExtractRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **forget_deleted_media_files**
    def forget_deleted_media_files(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_delete_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.forget_deleted_media_files(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->forget_deleted_media_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **generate_proxies**
    def [TaskInfo] generate_proxies(generate_proxies_request)



### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.generate_proxies_request import GenerateProxiesRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    generate_proxies_request = GenerateProxiesRequest(
        bundles=[
            1,
        ],
        directories=[
            1,
        ],
        proxy_profiles=[
            1,
        ],
        enqueue_at_front=True,
        force=True,
        retry_failed=True,
    ) # GenerateProxiesRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_proxies(generate_proxies_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->generate_proxies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_proxies_request** | [**GenerateProxiesRequest**](GenerateProxiesRequest.md)|  |

### Return type

[**[TaskInfo]**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_asset_project_links**
    def [AssetProjectLink] get_all_asset_project_links(asset_id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_project_link import AssetProjectLink
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    project = 1 # int | Filter the returned list by `project`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_asset_project_links(asset_id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_project_links: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_asset_project_links(asset_id, asset=asset, project=project, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_project_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **project** | **int**| Filter the returned list by &#x60;project&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AssetProjectLink]**](AssetProjectLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_asset_ratings**
    def [AssetRating] get_all_asset_ratings(asset_id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read, show_ratings Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_rating import AssetRating
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    user = 1 # int | Filter the returned list by `user`. (optional)
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_asset_ratings(asset_id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_ratings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_asset_ratings(asset_id, user=user, asset=asset, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_ratings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AssetRating]**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_asset_subtitle_links**
    def [AssetSubtitleLink] get_all_asset_subtitle_links(asset_id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_subtitle_link import AssetSubtitleLink
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    subtitle = 1 # int | Filter the returned list by `subtitle`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_asset_subtitle_links(asset_id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_subtitle_links: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_asset_subtitle_links(asset_id, subtitle=subtitle, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_subtitle_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **subtitle** | **int**| Filter the returned list by &#x60;subtitle&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AssetSubtitleLink]**](AssetSubtitleLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_asset_tape_backups**
    def [AssetBackup] get_all_asset_tape_backups()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_backup import AssetBackup
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    include_asset = True # bool |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    exclude_unrecognized = True # bool |  (optional)
    in_media_root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_asset_tape_backups(asset=asset, ordering=ordering, limit=limit, offset=offset, include_asset=include_asset, advanced_search=advanced_search, exclude_unrecognized=exclude_unrecognized, in_media_root=in_media_root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_asset_tape_backups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **include_asset** | **bool**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **exclude_unrecognized** | **bool**|  | [optional]
 **in_media_root** | **int**|  | [optional]

### Return type

[**[AssetBackup]**](AssetBackup.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_assets**
    def [Asset] get_all_assets()



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset import Asset
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    sync_id = "sync_id_example" # str | Filter the returned list by `sync_id`. (optional)
    display_name = "display_name_example" # str | Filter the returned list by `display_name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    include_proxies = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    include_proxy_transforms = True # bool |  (optional)
    include_full_info = True # bool |  (optional)
    resolve_asset_permission = True # bool |  (optional)
    for_root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_assets(sync_id=sync_id, display_name=display_name, ordering=ordering, limit=limit, offset=offset, include_proxies=include_proxies, include_modified_by=include_modified_by, include_proxy_transforms=include_proxy_transforms, include_full_info=include_full_info, resolve_asset_permission=resolve_asset_permission, for_root=for_root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_id** | **str**| Filter the returned list by &#x60;sync_id&#x60;. | [optional]
 **display_name** | **str**| Filter the returned list by &#x60;display_name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **include_proxies** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **include_proxy_transforms** | **bool**|  | [optional]
 **include_full_info** | **bool**|  | [optional]
 **resolve_asset_permission** | **bool**|  | [optional]
 **for_root** | **int**|  | [optional]

### Return type

[**[Asset]**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_bundles_for_media_root**
    def [MediaFileBundle] get_all_bundles_for_media_root(root)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_bundle import MediaFileBundle
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    root = "root_example" # str | 
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    location = 1 # int | Filter the returned list by `location`. (optional)
    shared_via_tokens = "shared_via_tokens_example" # str | Filter the returned list by `shared_via_tokens`. (optional)
    shared_via_tokens__token = "shared_via_tokens__token_example" # str | Filter the returned list by `shared_via_tokens__token`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    include_deleted = True # bool |  (optional)
    include_deleted_and_archived = True # bool |  (optional)
    include_unrecognized = True # bool |  (optional)
    include_proxies = True # bool |  (optional)
    include_parents = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    in_media_root = 1 # int |  (optional)
    in_directory = 1 # int |  (optional)
    for_root = 1 # int |  (optional)
    resolve_asset_permission = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_bundles_for_media_root(root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_bundles_for_media_root: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_bundles_for_media_root(root, asset=asset, location=location, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, name=name, ordering=ordering, limit=limit, offset=offset, include_deleted=include_deleted, include_deleted_and_archived=include_deleted_and_archived, include_unrecognized=include_unrecognized, include_proxies=include_proxies, include_parents=include_parents, include_modified_by=include_modified_by, advanced_search=advanced_search, in_media_root=in_media_root, in_directory=in_directory, for_root=for_root, resolve_asset_permission=resolve_asset_permission)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_bundles_for_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**|  |
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **location** | **int**| Filter the returned list by &#x60;location&#x60;. | [optional]
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional]
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **include_deleted** | **bool**|  | [optional]
 **include_deleted_and_archived** | **bool**|  | [optional]
 **include_unrecognized** | **bool**|  | [optional]
 **include_proxies** | **bool**|  | [optional]
 **include_parents** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **in_media_root** | **int**|  | [optional]
 **in_directory** | **int**|  | [optional]
 **for_root** | **int**|  | [optional]
 **resolve_asset_permission** | **bool**|  | [optional]

### Return type

[**[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_bundles_in_subtree**
    def [MediaFileBundle] get_all_bundles_in_subtree(file)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_bundle import MediaFileBundle
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    file = "file_example" # str | 
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    location = 1 # int | Filter the returned list by `location`. (optional)
    shared_via_tokens = "shared_via_tokens_example" # str | Filter the returned list by `shared_via_tokens`. (optional)
    shared_via_tokens__token = "shared_via_tokens__token_example" # str | Filter the returned list by `shared_via_tokens__token`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    include_deleted = True # bool |  (optional)
    include_deleted_and_archived = True # bool |  (optional)
    include_unrecognized = True # bool |  (optional)
    include_proxies = True # bool |  (optional)
    include_parents = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    in_media_root = 1 # int |  (optional)
    in_directory = 1 # int |  (optional)
    for_root = 1 # int |  (optional)
    resolve_asset_permission = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_bundles_in_subtree(file)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_bundles_in_subtree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_bundles_in_subtree(file, asset=asset, location=location, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, name=name, ordering=ordering, limit=limit, offset=offset, include_deleted=include_deleted, include_deleted_and_archived=include_deleted_and_archived, include_unrecognized=include_unrecognized, include_proxies=include_proxies, include_parents=include_parents, include_modified_by=include_modified_by, advanced_search=advanced_search, in_media_root=in_media_root, in_directory=in_directory, for_root=for_root, resolve_asset_permission=resolve_asset_permission)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_bundles_in_subtree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  |
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **location** | **int**| Filter the returned list by &#x60;location&#x60;. | [optional]
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional]
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **include_deleted** | **bool**|  | [optional]
 **include_deleted_and_archived** | **bool**|  | [optional]
 **include_unrecognized** | **bool**|  | [optional]
 **include_proxies** | **bool**|  | [optional]
 **include_parents** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **in_media_root** | **int**|  | [optional]
 **in_directory** | **int**|  | [optional]
 **for_root** | **int**|  | [optional]
 **resolve_asset_permission** | **bool**|  | [optional]

### Return type

[**[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_click_links**
    def [AssetCloudLink] get_all_click_links()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_cloud_link import AssetCloudLink
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    connection = 1 # int | Filter the returned list by `connection`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_click_links(asset=asset, connection=connection, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_click_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **connection** | **int**| Filter the returned list by &#x60;connection&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[AssetCloudLink]**](AssetCloudLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_comments**
    def [Comment] get_all_comments()



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.comment import Comment
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    root = 1 # int | Filter the returned list by `root`. (optional)
    user = 1 # int | Filter the returned list by `user`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    cursor = "cursor_example" # str | The pagination cursor value. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    for_root = 1 # int |  (optional)
    tasks_for_user = 1 # int |  (optional)
    include_full_asset = True # bool |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_comments(asset=asset, root=root, user=user, ordering=ordering, cursor=cursor, limit=limit, offset=offset, for_root=for_root, tasks_for_user=tasks_for_user, include_full_asset=include_full_asset, advanced_search=advanced_search, filter=filter)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **root** | **int**| Filter the returned list by &#x60;root&#x60;. | [optional]
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **for_root** | **int**|  | [optional]
 **tasks_for_user** | **int**|  | [optional]
 **include_full_asset** | **bool**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**[Comment]**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_custom_fields**
    def [CustomField] get_all_custom_fields()



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.custom_field import CustomField
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_custom_fields(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_custom_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[CustomField]**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_external_transcoders**
    def [ExternalTranscoder] get_all_external_transcoders()



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.external_transcoder import ExternalTranscoder
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    id = 1 # int | Filter the returned list by `id`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_external_transcoders(name=name, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_external_transcoders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[ExternalTranscoder]**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_markers**
    def [Marker] get_all_markers(asset_id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.marker import Marker
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    user = 1 # int | Filter the returned list by `user`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_markers(asset_id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_markers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_markers(asset_id, user=user, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_markers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Marker]**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_file_bundles**
    def [MediaFileBundle] get_all_media_file_bundles()



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_bundle import MediaFileBundle
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    location = 1 # int | Filter the returned list by `location`. (optional)
    shared_via_tokens = "shared_via_tokens_example" # str | Filter the returned list by `shared_via_tokens`. (optional)
    shared_via_tokens__token = "shared_via_tokens__token_example" # str | Filter the returned list by `shared_via_tokens__token`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    include_deleted = True # bool |  (optional)
    include_deleted_and_archived = True # bool |  (optional)
    include_unrecognized = True # bool |  (optional)
    include_proxies = True # bool |  (optional)
    include_parents = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    in_media_root = 1 # int |  (optional)
    in_directory = 1 # int |  (optional)
    for_root = 1 # int |  (optional)
    resolve_asset_permission = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_file_bundles(asset=asset, location=location, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, name=name, ordering=ordering, limit=limit, offset=offset, include_deleted=include_deleted, include_deleted_and_archived=include_deleted_and_archived, include_unrecognized=include_unrecognized, include_proxies=include_proxies, include_parents=include_parents, include_modified_by=include_modified_by, advanced_search=advanced_search, in_media_root=in_media_root, in_directory=in_directory, for_root=for_root, resolve_asset_permission=resolve_asset_permission)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_file_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **location** | **int**| Filter the returned list by &#x60;location&#x60;. | [optional]
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional]
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **include_deleted** | **bool**|  | [optional]
 **include_deleted_and_archived** | **bool**|  | [optional]
 **include_unrecognized** | **bool**|  | [optional]
 **include_proxies** | **bool**|  | [optional]
 **include_parents** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **in_media_root** | **int**|  | [optional]
 **in_directory** | **int**|  | [optional]
 **for_root** | **int**|  | [optional]
 **resolve_asset_permission** | **bool**|  | [optional]

### Return type

[**[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_file_templates**
    def [MediaFileTemplate] get_all_media_file_templates()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_template import MediaFileTemplate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_file_templates(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_file_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[MediaFileTemplate]**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_files**
    def [MediaFile] get_all_media_files()



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    bundle = 1 # int | Filter the returned list by `bundle`. (optional)
    bundle__in = "bundle__in_example" # str | Filter the returned list by `bundle__in`. (optional)
    parent = 1 # int | Filter the returned list by `parent`. (optional)
    path = "path_example" # str |  (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    is_dir = "is_dir_example" # str | Filter the returned list by `is_dir`. (optional)
    is_showroom = "is_showroom_example" # str | Filter the returned list by `is_showroom`. (optional)
    present = "present_example" # str | Filter the returned list by `present`. (optional)
    archived = "archived_example" # str | Filter the returned list by `archived`. (optional)
    volume = 1 # int | Filter the returned list by `volume`. (optional)
    shared_via_tokens = "shared_via_tokens_example" # str | Filter the returned list by `shared_via_tokens`. (optional)
    shared_via_tokens__token = "shared_via_tokens__token_example" # str | Filter the returned list by `shared_via_tokens__token`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    resolve_file_permission = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    include_effective_custom_fields = True # bool |  (optional)
    include_root = True # bool |  (optional)
    include_parents = True # bool |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    in_media_root = 1 # int |  (optional)
    in_directory = 1 # int |  (optional)
    include_deleted = True # bool |  (optional)
    include_deleted_and_archived = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_files(bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, archived=archived, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset, resolve_file_permission=resolve_file_permission, include_modified_by=include_modified_by, include_effective_custom_fields=include_effective_custom_fields, include_root=include_root, include_parents=include_parents, advanced_search=advanced_search, in_media_root=in_media_root, in_directory=in_directory, include_deleted=include_deleted, include_deleted_and_archived=include_deleted_and_archived)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **int**| Filter the returned list by &#x60;bundle&#x60;. | [optional]
 **bundle__in** | **str**| Filter the returned list by &#x60;bundle__in&#x60;. | [optional]
 **parent** | **int**| Filter the returned list by &#x60;parent&#x60;. | [optional]
 **path** | **str**|  | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional]
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional]
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional]
 **archived** | **str**| Filter the returned list by &#x60;archived&#x60;. | [optional]
 **volume** | **int**| Filter the returned list by &#x60;volume&#x60;. | [optional]
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional]
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **resolve_file_permission** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **include_effective_custom_fields** | **bool**|  | [optional]
 **include_root** | **bool**|  | [optional]
 **include_parents** | **bool**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **in_media_root** | **int**|  | [optional]
 **in_directory** | **int**|  | [optional]
 **include_deleted** | **bool**|  | [optional]
 **include_deleted_and_archived** | **bool**|  | [optional]

### Return type

[**[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_files_for_bundles**
    def [MediaFile] get_all_media_files_for_bundles(all_media_files_for_bundles_request)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from elements_sdk.model.all_media_files_for_bundles_request import AllMediaFilesForBundlesRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    all_media_files_for_bundles_request = AllMediaFilesForBundlesRequest(
        bundles=[
            1,
        ],
    ) # AllMediaFilesForBundlesRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_media_files_for_bundles(all_media_files_for_bundles_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_for_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all_media_files_for_bundles_request** | [**AllMediaFilesForBundlesRequest**](AllMediaFilesForBundlesRequest.md)|  |

### Return type

[**[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_files_for_media_root**
    def [MediaFile] get_all_media_files_for_media_root(root)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    root = "root_example" # str | 
    bundle = 1 # int | Filter the returned list by `bundle`. (optional)
    bundle__in = "bundle__in_example" # str | Filter the returned list by `bundle__in`. (optional)
    parent = 1 # int | Filter the returned list by `parent`. (optional)
    path = "path_example" # str | Filter the returned list by `path`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    is_dir = "is_dir_example" # str | Filter the returned list by `is_dir`. (optional)
    is_showroom = "is_showroom_example" # str | Filter the returned list by `is_showroom`. (optional)
    present = "present_example" # str | Filter the returned list by `present`. (optional)
    archived = "archived_example" # str | Filter the returned list by `archived`. (optional)
    volume = 1 # int | Filter the returned list by `volume`. (optional)
    shared_via_tokens = "shared_via_tokens_example" # str | Filter the returned list by `shared_via_tokens`. (optional)
    shared_via_tokens__token = "shared_via_tokens__token_example" # str | Filter the returned list by `shared_via_tokens__token`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_media_files_for_media_root(root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_for_media_root: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_files_for_media_root(root, bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, archived=archived, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_for_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **str**|  |
 **bundle** | **int**| Filter the returned list by &#x60;bundle&#x60;. | [optional]
 **bundle__in** | **str**| Filter the returned list by &#x60;bundle__in&#x60;. | [optional]
 **parent** | **int**| Filter the returned list by &#x60;parent&#x60;. | [optional]
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional]
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional]
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional]
 **archived** | **str**| Filter the returned list by &#x60;archived&#x60;. | [optional]
 **volume** | **int**| Filter the returned list by &#x60;volume&#x60;. | [optional]
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional]
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_files_in_subtree**
    def [MediaFile] get_all_media_files_in_subtree(file)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    file = "file_example" # str | 
    bundle = 1 # int | Filter the returned list by `bundle`. (optional)
    bundle__in = "bundle__in_example" # str | Filter the returned list by `bundle__in`. (optional)
    parent = 1 # int | Filter the returned list by `parent`. (optional)
    path = "path_example" # str | Filter the returned list by `path`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    is_dir = "is_dir_example" # str | Filter the returned list by `is_dir`. (optional)
    is_showroom = "is_showroom_example" # str | Filter the returned list by `is_showroom`. (optional)
    present = "present_example" # str | Filter the returned list by `present`. (optional)
    archived = "archived_example" # str | Filter the returned list by `archived`. (optional)
    volume = 1 # int | Filter the returned list by `volume`. (optional)
    shared_via_tokens = "shared_via_tokens_example" # str | Filter the returned list by `shared_via_tokens`. (optional)
    shared_via_tokens__token = "shared_via_tokens__token_example" # str | Filter the returned list by `shared_via_tokens__token`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_media_files_in_subtree(file)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_in_subtree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_files_in_subtree(file, bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, archived=archived, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_files_in_subtree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  |
 **bundle** | **int**| Filter the returned list by &#x60;bundle&#x60;. | [optional]
 **bundle__in** | **str**| Filter the returned list by &#x60;bundle__in&#x60;. | [optional]
 **parent** | **int**| Filter the returned list by &#x60;parent&#x60;. | [optional]
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional]
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional]
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional]
 **archived** | **str**| Filter the returned list by &#x60;archived&#x60;. | [optional]
 **volume** | **int**| Filter the returned list by &#x60;volume&#x60;. | [optional]
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional]
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_root_permissions**
    def [MediaRootPermission] get_all_media_root_permissions()



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_permission import MediaRootPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    root = 1 # int | Filter the returned list by `root`. (optional)
    id = 1 # int | Filter the returned list by `id`. (optional)
    is_temporary_for_token = 1 # int | Filter the returned list by `is_temporary_for_token`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_root_permissions(root=root, id=id, is_temporary_for_token=is_temporary_for_token, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_root_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **int**| Filter the returned list by &#x60;root&#x60;. | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **is_temporary_for_token** | **int**| Filter the returned list by &#x60;is_temporary_for_token&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[MediaRootPermission]**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_roots**
    def [MediaRoot] get_all_media_roots()



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root import MediaRoot
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    path = "path_example" # str | Filter the returned list by `path`. (optional)
    volume = 1 # int | Filter the returned list by `volume`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    resolve_permissions = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_roots(path=path, volume=volume, name=name, ordering=ordering, limit=limit, offset=offset, resolve_permissions=resolve_permissions)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_roots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional]
 **volume** | **int**| Filter the returned list by &#x60;volume&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **resolve_permissions** | **bool**|  | [optional]

### Return type

[**[MediaRoot]**](MediaRoot.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_tags**
    def [UnfilteredTag] get_all_media_tags()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.unfiltered_tag import UnfilteredTag
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | Filter the returned list by `id`. (optional)
    id__in = "id__in_example" # str |  (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    name__icontains = "name__icontains_example" # str | Filter the returned list by `name__icontains`. (optional)
    roots = "roots_example" # str | Filter the returned list by `roots`. (optional)
    roots__isnull = "roots__isnull_example" # str | Filter the returned list by `roots__isnull`. (optional)
    shared = "shared_example" # str | Filter the returned list by `shared`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    for_root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_tags(id=id, id__in=id__in, name=name, name__icontains=name__icontains, roots=roots, roots__isnull=roots__isnull, shared=shared, ordering=ordering, limit=limit, offset=offset, for_root=for_root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **id__in** | **str**|  | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **name__icontains** | **str**| Filter the returned list by &#x60;name__icontains&#x60;. | [optional]
 **roots** | **str**| Filter the returned list by &#x60;roots&#x60;. | [optional]
 **roots__isnull** | **str**| Filter the returned list by &#x60;roots__isnull&#x60;. | [optional]
 **shared** | **str**| Filter the returned list by &#x60;shared&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **for_root** | **int**|  | [optional]

### Return type

[**[UnfilteredTag]**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_media_updates**
    def [MediaUpdate] get_all_media_updates()



### Required permissions    * User account permission: `media:access` (read) / `media:updates:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_update import MediaUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset = 1 # int | Filter the returned list by `asset`. (optional)
    user = 1 # int | Filter the returned list by `user`. (optional)
    root = 1 # int | Filter the returned list by `root`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    cursor = "cursor_example" # str | The pagination cursor value. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_media_updates(asset=asset, user=user, root=root, ordering=ordering, cursor=cursor, limit=limit, offset=offset, filter=filter)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_media_updates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **int**| Filter the returned list by &#x60;asset&#x60;. | [optional]
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **root** | **int**| Filter the returned list by &#x60;root&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**[MediaUpdate]**](MediaUpdate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_pinned_items**
    def [MediaPinnedItem] get_all_pinned_items()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_pinned_item import MediaPinnedItem
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    user = 1 # int | Filter the returned list by `user`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_pinned_items(user=user, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_pinned_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[MediaPinnedItem]**](MediaPinnedItem.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_proxy_generators**
    def [ProxyGenerator] get_all_proxy_generators()



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_generator import ProxyGenerator
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_proxy_generators(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_proxy_generators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[ProxyGenerator]**](ProxyGenerator.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_proxy_profiles**
    def [ProxyProfile] get_all_proxy_profiles()



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_profile import ProxyProfile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)
    for_root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_proxy_profiles(name=name, ordering=ordering, limit=limit, offset=offset, for_root=for_root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_proxy_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]
 **for_root** | **int**|  | [optional]

### Return type

[**[ProxyProfile]**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_saved_searches**
    def [SavedSearch] get_all_saved_searches()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.saved_search import SavedSearch
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    root = 1 # int | Filter the returned list by `root`. (optional)
    user = 1 # int | Filter the returned list by `user`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_saved_searches(name=name, root=root, user=user, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_saved_searches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **root** | **int**| Filter the returned list by &#x60;root&#x60;. | [optional]
 **user** | **int**| Filter the returned list by &#x60;user&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[SavedSearch]**](SavedSearch.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_sharing_permission_presets**
    def [SharingPermissionPreset] get_all_sharing_permission_presets()



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.sharing_permission_preset import SharingPermissionPreset
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    id = 1 # int | Filter the returned list by `id`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_sharing_permission_presets(name=name, id=id, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_sharing_permission_presets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[SharingPermissionPreset]**](SharingPermissionPreset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_subclip_clipboard_entries**
    def [SubclipClipboardEntry] get_all_subclip_clipboard_entries()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.subclip_clipboard_entry import SubclipClipboardEntry
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    cut = 1 # int | Filter the returned list by `cut`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_subclip_clipboard_entries(cut=cut, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_subclip_clipboard_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cut** | **int**| Filter the returned list by &#x60;cut&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[SubclipClipboardEntry]**](SubclipClipboardEntry.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_subclips**
    def [Subclip] get_all_subclips(asset_id)



### Required permissions    * User account permission: `media:access`   * License component: media   * Must be shared OR Must own the object   * allow_read, show_subclips Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.subclip import Subclip
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    root = 1 # int | Filter the returned list by `root`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_all_subclips(asset_id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_subclips: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_subclips(asset_id, root=root, name=name, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_subclips: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **root** | **int**| Filter the returned list by &#x60;root&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Subclip]**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_subtitle_clipboard_entries**
    def [SubtitleClipboardEntry] get_all_subtitle_clipboard_entries()



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.subtitle_clipboard_entry import SubtitleClipboardEntry
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    subtitle = 1 # int | Filter the returned list by `subtitle`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_subtitle_clipboard_entries(subtitle=subtitle, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_subtitle_clipboard_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subtitle** | **int**| Filter the returned list by &#x60;subtitle&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[SubtitleClipboardEntry]**](SubtitleClipboardEntry.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_transcoder_profiles**
    def [TranscoderProfile] get_all_transcoder_profiles()



### Required permissions    * User account permission: `tasks:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.transcoder_profile import TranscoderProfile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_transcoder_profiles(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_transcoder_profiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[TranscoderProfile]**](TranscoderProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_all_workflows**
    def [Workflow] get_all_workflows()



### Required permissions    * User account permission: `media:roots:manage`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.workflow import Workflow
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_all_workflows(ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_all_workflows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[Workflow]**](Workflow.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_asset**
    def Asset get_asset(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset import Asset
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.
    include_proxies = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    include_proxy_transforms = True # bool |  (optional)
    include_full_info = True # bool |  (optional)
    resolve_asset_permission = True # bool |  (optional)
    for_root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_asset(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_asset(id, include_proxies=include_proxies, include_modified_by=include_modified_by, include_proxy_transforms=include_proxy_transforms, include_full_info=include_full_info, resolve_asset_permission=resolve_asset_permission, for_root=for_root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |
 **include_proxies** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **include_proxy_transforms** | **bool**|  | [optional]
 **include_full_info** | **bool**|  | [optional]
 **resolve_asset_permission** | **bool**|  | [optional]
 **for_root** | **int**|  | [optional]

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_asset_rating**
    def AssetRating get_asset_rating(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read, show_ratings Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_rating import AssetRating
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this Rating.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_asset_rating(asset_id, id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_asset_rating: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this Rating. |

### Return type

[**AssetRating**](AssetRating.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_asset_stack_members**
    def [Asset] get_asset_stack_members(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset import Asset
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media asset stack.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_asset_stack_members(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_asset_stack_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media asset stack. |

### Return type

[**[Asset]**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_asset_subtitle_link**
    def AssetSubtitleLink get_asset_subtitle_link(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_subtitle_link import AssetSubtitleLink
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this Asset subtitle file link.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_asset_subtitle_link(asset_id, id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_asset_subtitle_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this Asset subtitle file link. |

### Return type

[**AssetSubtitleLink**](AssetSubtitleLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_bookmarked_media_files_directories**
    def [MediaFile] get_bookmarked_media_files_directories()



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions OR allow_upload Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    bundle = 1 # int | Filter the returned list by `bundle`. (optional)
    bundle__in = "bundle__in_example" # str | Filter the returned list by `bundle__in`. (optional)
    parent = 1 # int | Filter the returned list by `parent`. (optional)
    path = "path_example" # str | Filter the returned list by `path`. (optional)
    name = "name_example" # str | Filter the returned list by `name`. (optional)
    is_dir = "is_dir_example" # str | Filter the returned list by `is_dir`. (optional)
    is_showroom = "is_showroom_example" # str | Filter the returned list by `is_showroom`. (optional)
    present = "present_example" # str | Filter the returned list by `present`. (optional)
    archived = "archived_example" # str | Filter the returned list by `archived`. (optional)
    volume = 1 # int | Filter the returned list by `volume`. (optional)
    shared_via_tokens = "shared_via_tokens_example" # str | Filter the returned list by `shared_via_tokens`. (optional)
    shared_via_tokens__token = "shared_via_tokens__token_example" # str | Filter the returned list by `shared_via_tokens__token`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_bookmarked_media_files_directories(bundle=bundle, bundle__in=bundle__in, parent=parent, path=path, name=name, is_dir=is_dir, is_showroom=is_showroom, present=present, archived=archived, volume=volume, shared_via_tokens=shared_via_tokens, shared_via_tokens__token=shared_via_tokens__token, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_bookmarked_media_files_directories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **int**| Filter the returned list by &#x60;bundle&#x60;. | [optional]
 **bundle__in** | **str**| Filter the returned list by &#x60;bundle__in&#x60;. | [optional]
 **parent** | **int**| Filter the returned list by &#x60;parent&#x60;. | [optional]
 **path** | **str**| Filter the returned list by &#x60;path&#x60;. | [optional]
 **name** | **str**| Filter the returned list by &#x60;name&#x60;. | [optional]
 **is_dir** | **str**| Filter the returned list by &#x60;is_dir&#x60;. | [optional]
 **is_showroom** | **str**| Filter the returned list by &#x60;is_showroom&#x60;. | [optional]
 **present** | **str**| Filter the returned list by &#x60;present&#x60;. | [optional]
 **archived** | **str**| Filter the returned list by &#x60;archived&#x60;. | [optional]
 **volume** | **int**| Filter the returned list by &#x60;volume&#x60;. | [optional]
 **shared_via_tokens** | **str**| Filter the returned list by &#x60;shared_via_tokens&#x60;. | [optional]
 **shared_via_tokens__token** | **str**| Filter the returned list by &#x60;shared_via_tokens__token&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_bundle_files**
    def [MediaFileMini] get_bundle_files(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_mini import MediaFileMini
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Bundle.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_bundle_files(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_bundle_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Bundle. |

### Return type

[**[MediaFileMini]**](MediaFileMini.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_comment**
    def Comment get_comment(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.comment import Comment
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Comment.
    for_root = 1 # int |  (optional)
    tasks_for_user = 1 # int |  (optional)
    include_full_asset = True # bool |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_comment(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_comment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_comment(id, for_root=for_root, tasks_for_user=tasks_for_user, include_full_asset=include_full_asset, advanced_search=advanced_search, filter=filter)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. |
 **for_root** | **int**|  | [optional]
 **tasks_for_user** | **int**|  | [optional]
 **include_full_asset** | **bool**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_custom_field**
    def CustomField get_custom_field(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.custom_field import CustomField
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Custom field.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_custom_field(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. |

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_custom_field_options**
    def [FieldOption] get_custom_field_options(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.field_option import FieldOption
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Custom field.
    q = "q_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_custom_field_options(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_custom_field_options: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_custom_field_options(id, q=q)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_custom_field_options: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. |
 **q** | **str**|  | [optional]

### Return type

[**[FieldOption]**](FieldOption.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_easy_sharing_token_for_bundle**
    def OneTimeAccessToken get_easy_sharing_token_for_bundle(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_sharing Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.one_time_access_token import OneTimeAccessToken
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Bundle.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_easy_sharing_token_for_bundle(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_easy_sharing_token_for_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Bundle. |

### Return type

[**OneTimeAccessToken**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_easy_sharing_token_for_directory**
    def OneTimeAccessToken get_easy_sharing_token_for_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_sharing Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.one_time_access_token import OneTimeAccessToken
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_easy_sharing_token_for_directory(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_easy_sharing_token_for_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

[**OneTimeAccessToken**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_editor_project**
    def EditorProject get_editor_project(id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.editor_project import EditorProject
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_editor_project(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_editor_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

[**EditorProject**](EditorProject.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_editor_subtitle**
    def EditorSubtitle get_editor_subtitle(id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.editor_subtitle import EditorSubtitle
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_editor_subtitle(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_editor_subtitle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

[**EditorSubtitle**](EditorSubtitle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_external_transcoder**
    def ExternalTranscoder get_external_transcoder(id)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.external_transcoder import ExternalTranscoder
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this external transcoder.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_external_transcoder(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. |

### Return type

[**ExternalTranscoder**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_frame**
    def file_type get_frame(id, frame)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_original_download Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.
    frame = "frame_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_frame(id, frame)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_frame: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |
 **frame** | **str**|  |

### Return type

**file_type**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_file**
    def MediaFile get_media_file(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions OR allow_upload Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    resolve_file_permission = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    include_effective_custom_fields = True # bool |  (optional)
    include_root = True # bool |  (optional)
    include_parents = True # bool |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    in_media_root = 1 # int |  (optional)
    in_directory = 1 # int |  (optional)
    include_deleted = True # bool |  (optional)
    include_deleted_and_archived = True # bool |  (optional)
    path = "path_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_file(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_media_file(id, resolve_file_permission=resolve_file_permission, include_modified_by=include_modified_by, include_effective_custom_fields=include_effective_custom_fields, include_root=include_root, include_parents=include_parents, advanced_search=advanced_search, in_media_root=in_media_root, in_directory=in_directory, include_deleted=include_deleted, include_deleted_and_archived=include_deleted_and_archived, path=path)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **resolve_file_permission** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **include_effective_custom_fields** | **bool**|  | [optional]
 **include_root** | **bool**|  | [optional]
 **include_parents** | **bool**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **in_media_root** | **int**|  | [optional]
 **in_directory** | **int**|  | [optional]
 **include_deleted** | **bool**|  | [optional]
 **include_deleted_and_archived** | **bool**|  | [optional]
 **path** | **str**|  | [optional]

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_file_bundle**
    def MediaFileBundle get_media_file_bundle(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_bundle import MediaFileBundle
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Bundle.
    include_deleted = True # bool |  (optional)
    include_deleted_and_archived = True # bool |  (optional)
    include_unrecognized = True # bool |  (optional)
    include_proxies = True # bool |  (optional)
    include_parents = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    offset = 1 # int |  (optional)
    limit = 1 # int |  (optional)
    advanced_search = "advanced_search_example" # str |  (optional)
    in_media_root = 1 # int |  (optional)
    in_directory = 1 # int |  (optional)
    for_root = 1 # int |  (optional)
    resolve_asset_permission = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_file_bundle(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_bundle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_media_file_bundle(id, include_deleted=include_deleted, include_deleted_and_archived=include_deleted_and_archived, include_unrecognized=include_unrecognized, include_proxies=include_proxies, include_parents=include_parents, include_modified_by=include_modified_by, offset=offset, limit=limit, advanced_search=advanced_search, in_media_root=in_media_root, in_directory=in_directory, for_root=for_root, resolve_asset_permission=resolve_asset_permission)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_bundle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Bundle. |
 **include_deleted** | **bool**|  | [optional]
 **include_deleted_and_archived** | **bool**|  | [optional]
 **include_unrecognized** | **bool**|  | [optional]
 **include_proxies** | **bool**|  | [optional]
 **include_parents** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **offset** | **int**|  | [optional]
 **limit** | **int**|  | [optional]
 **advanced_search** | **str**|  | [optional]
 **in_media_root** | **int**|  | [optional]
 **in_directory** | **int**|  | [optional]
 **for_root** | **int**|  | [optional]
 **resolve_asset_permission** | **bool**|  | [optional]

### Return type

[**MediaFileBundle**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_file_contents**
    def MediaFileContents get_media_file_contents(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_contents import MediaFileContents
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    include_deleted = True # bool |  (optional)
    include_deleted_and_archived = True # bool |  (optional)
    include_unrecognized = True # bool |  (optional)
    offset = 1 # int |  (optional)
    limit = 1 # int |  (optional)
    ordering = "ordering_example" # str |  (optional)
    include_modified_by = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_file_contents(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_contents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_media_file_contents(id, include_deleted=include_deleted, include_deleted_and_archived=include_deleted_and_archived, include_unrecognized=include_unrecognized, offset=offset, limit=limit, ordering=ordering, include_modified_by=include_modified_by)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **include_deleted** | **bool**|  | [optional]
 **include_deleted_and_archived** | **bool**|  | [optional]
 **include_unrecognized** | **bool**|  | [optional]
 **offset** | **int**|  | [optional]
 **limit** | **int**|  | [optional]
 **ordering** | **str**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]

### Return type

[**MediaFileContents**](MediaFileContents.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_file_template**
    def MediaFileTemplate get_media_file_template(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_template import MediaFileTemplate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Template.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_file_template(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. |

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_pinned_item**
    def MediaPinnedItem get_media_pinned_item(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_pinned_item import MediaPinnedItem
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media pinned item.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_pinned_item(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_pinned_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media pinned item. |

### Return type

[**MediaPinnedItem**](MediaPinnedItem.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_root**
    def MediaRootDetail get_media_root(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_detail import MediaRootDetail
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media root.
    resolve_permissions = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_root(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_root: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_media_root(id, resolve_permissions=resolve_permissions)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. |
 **resolve_permissions** | **bool**|  | [optional]

### Return type

[**MediaRootDetail**](MediaRootDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_root_cover_image**
    def get_media_root_cover_image(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media root.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_media_root_cover_image(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_root_cover_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_root_permission**
    def MediaRootPermission get_media_root_permission(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_permission import MediaRootPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Media Root Permission.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_root_permission(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. |

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_root_users**
    def [ElementsUserMini] get_media_root_users(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.elements_user_mini import ElementsUserMini
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media root.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_root_users(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_root_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. |

### Return type

[**[ElementsUserMini]**](ElementsUserMini.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_media_tag**
    def UnfilteredTag get_media_tag(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.unfiltered_tag import UnfilteredTag
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Tag.
    for_root = 1 # int |  (optional)
    id__in = "id__in_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_media_tag(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_media_tag(id, for_root=for_root, id__in=id__in)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. |
 **for_root** | **int**|  | [optional]
 **id__in** | **str**|  | [optional]

### Return type

[**UnfilteredTag**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_multiple_assets**
    def [Asset] get_multiple_assets(multiple_assets_request)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset import Asset
from elements_sdk.model.multiple_assets_request import MultipleAssetsRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    multiple_assets_request = MultipleAssetsRequest(
        assets=[
            1,
        ],
    ) # MultipleAssetsRequest | 
    include_proxies = True # bool |  (optional)
    include_modified_by = True # bool |  (optional)
    include_proxy_transforms = True # bool |  (optional)
    include_full_info = True # bool |  (optional)
    resolve_asset_permission = True # bool |  (optional)
    for_root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_multiple_assets(multiple_assets_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_assets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_multiple_assets(multiple_assets_request, include_proxies=include_proxies, include_modified_by=include_modified_by, include_proxy_transforms=include_proxy_transforms, include_full_info=include_full_info, resolve_asset_permission=resolve_asset_permission, for_root=for_root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_assets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multiple_assets_request** | [**MultipleAssetsRequest**](MultipleAssetsRequest.md)|  |
 **include_proxies** | **bool**|  | [optional]
 **include_modified_by** | **bool**|  | [optional]
 **include_proxy_transforms** | **bool**|  | [optional]
 **include_full_info** | **bool**|  | [optional]
 **resolve_asset_permission** | **bool**|  | [optional]
 **for_root** | **int**|  | [optional]

### Return type

[**[Asset]**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_multiple_bundles**
    def [MediaFileBundle] get_multiple_bundles(get_multiple_bundles_request)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.get_multiple_bundles_request import GetMultipleBundlesRequest
from elements_sdk.model.media_file_bundle import MediaFileBundle
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    get_multiple_bundles_request = GetMultipleBundlesRequest(
        bundles=[
            1,
        ],
        files=[
            1,
        ],
    ) # GetMultipleBundlesRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_multiple_bundles(get_multiple_bundles_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_multiple_bundles_request** | [**GetMultipleBundlesRequest**](GetMultipleBundlesRequest.md)|  |

### Return type

[**[MediaFileBundle]**](MediaFileBundle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_multiple_files**
    def [MediaFile] get_multiple_files(get_multiple_files_request)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from elements_sdk.model.get_multiple_files_request import GetMultipleFilesRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    get_multiple_files_request = GetMultipleFilesRequest(
        files=[
            1,
        ],
    ) # GetMultipleFilesRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_multiple_files(get_multiple_files_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_multiple_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_multiple_files_request** | [**GetMultipleFilesRequest**](GetMultipleFilesRequest.md)|  |

### Return type

[**[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_my_media_root_permissions**
    def [MediaRootPermission] get_my_media_root_permissions()



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_permission import MediaRootPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    root = 1 # int | Filter the returned list by `root`. (optional)
    id = 1 # int | Filter the returned list by `id`. (optional)
    is_temporary_for_token = 1 # int | Filter the returned list by `is_temporary_for_token`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_my_media_root_permissions(root=root, id=id, is_temporary_for_token=is_temporary_for_token, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_my_media_root_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **int**| Filter the returned list by &#x60;root&#x60;. | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **is_temporary_for_token** | **int**| Filter the returned list by &#x60;is_temporary_for_token&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[MediaRootPermission]**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_my_resolved_media_root_permissions**
    def [MediaRootPermission] get_my_resolved_media_root_permissions()



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_permission import MediaRootPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    root = 1 # int | Filter the returned list by `root`. (optional)
    id = 1 # int | Filter the returned list by `id`. (optional)
    is_temporary_for_token = 1 # int | Filter the returned list by `is_temporary_for_token`. (optional)
    ordering = "ordering_example" # str | Which field to use when ordering the results. (optional)
    limit = 1 # int | Number of results to return per page. (optional)
    offset = 1 # int | The initial index from which to return the results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_my_resolved_media_root_permissions(root=root, id=id, is_temporary_for_token=is_temporary_for_token, ordering=ordering, limit=limit, offset=offset)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_my_resolved_media_root_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root** | **int**| Filter the returned list by &#x60;root&#x60;. | [optional]
 **id** | **int**| Filter the returned list by &#x60;id&#x60;. | [optional]
 **is_temporary_for_token** | **int**| Filter the returned list by &#x60;is_temporary_for_token&#x60;. | [optional]
 **ordering** | **str**| Which field to use when ordering the results. | [optional]
 **limit** | **int**| Number of results to return per page. | [optional]
 **offset** | **int**| The initial index from which to return the results. | [optional]

### Return type

[**[MediaRootPermission]**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_proxy**
    def Proxy get_proxy(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy import Proxy
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this proxy.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_proxy(asset_id, id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this proxy. |

### Return type

[**Proxy**](Proxy.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_proxy_generation_info**
    def ProxyGenerationInfoResponse get_proxy_generation_info(asset_id, id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_generation_info_response import ProxyGenerationInfoResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this proxy.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_proxy_generation_info(asset_id, id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_generation_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this proxy. |

### Return type

[**ProxyGenerationInfoResponse**](ProxyGenerationInfoResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_proxy_generator**
    def ProxyGenerator get_proxy_generator(id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_generator import ProxyGenerator
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_proxy_generator(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_generator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**ProxyGenerator**](ProxyGenerator.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_proxy_profile**
    def ProxyProfile get_proxy_profile(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_profile import ProxyProfile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this proxy profile.
    for_root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_proxy_profile(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_proxy_profile(id, for_root=for_root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. |
 **for_root** | **int**|  | [optional]

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_proxy_profile_proxy_count**
    def ProxyCount get_proxy_profile_proxy_count(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_count import ProxyCount
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this proxy profile.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_proxy_profile_proxy_count(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_profile_proxy_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. |

### Return type

[**ProxyCount**](ProxyCount.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_proxy_profile_watermark_image**
    def get_proxy_profile_watermark_image(id)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this proxy profile.

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_proxy_profile_watermark_image(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_proxy_profile_watermark_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_saved_search**
    def SavedSearch get_saved_search(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.saved_search import SavedSearch
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this saved search.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_saved_search(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_saved_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this saved search. |

### Return type

[**SavedSearch**](SavedSearch.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_sharing_permission_preset**
    def SharingPermissionPreset get_sharing_permission_preset(id)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.sharing_permission_preset import SharingPermissionPreset
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Sharing Permission Preset.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sharing_permission_preset(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_sharing_permission_preset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Sharing Permission Preset. |

### Return type

[**SharingPermissionPreset**](SharingPermissionPreset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_subtitles**
    def file_type get_subtitles(id, title)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.
    title = "title_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_subtitles(id, title)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_subtitles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |
 **title** | **str**|  |

### Return type

**file_type**

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_transcoder_profile**
    def TranscoderProfile get_transcoder_profile(id)



### Required permissions    * User account permission: `tasks:view` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.transcoder_profile import TranscoderProfile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this transcoder profile.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transcoder_profile(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_transcoder_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this transcoder profile. |

### Return type

[**TranscoderProfile**](TranscoderProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_vantage_workflows**
    def VantageWorkflows get_vantage_workflows(id)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.vantage_workflows import VantageWorkflows
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this external transcoder.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_vantage_workflows(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_vantage_workflows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. |

### Return type

[**VantageWorkflows**](VantageWorkflows.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **get_workflow**
    def Workflow get_workflow(id)



### Required permissions    * User account permission: `media:roots:manage`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.workflow import Workflow
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Workflow.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_workflow(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->get_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Workflow. |

### Return type

[**Workflow**](Workflow.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **instantiate_media_file_template**
    def instantiate_media_file_template(id, instantiate_file_template_request)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.instantiate_file_template_request import InstantiateFileTemplateRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Template.
    instantiate_file_template_request = InstantiateFileTemplateRequest(
        parent=1,
        name="name_example",
        custom_fields={
            "key": "key_example",
        },
    ) # InstantiateFileTemplateRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.instantiate_media_file_template(id, instantiate_file_template_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->instantiate_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. |
 **instantiate_file_template_request** | [**InstantiateFileTemplateRequest**](InstantiateFileTemplateRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **link_assets_as_versions**
    def link_assets_as_versions(multiple_assets_request)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.multiple_assets_request import MultipleAssetsRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    multiple_assets_request = MultipleAssetsRequest(
        assets=[
            1,
        ],
    ) # MultipleAssetsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.link_assets_as_versions(multiple_assets_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->link_assets_as_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multiple_assets_request** | [**MultipleAssetsRequest**](MultipleAssetsRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **locate_editor_project_paths**
    def [LocateResult] locate_editor_project_paths(id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.locate_result import LocateResult
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.locate_editor_project_paths(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->locate_editor_project_paths: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

[**[LocateResult]**](LocateResult.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **lookup_media_files**
    def [MediaFile] lookup_media_files(media_files_lookup_request)



### Required permissions    * Authenticated user   * Authenticated user 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from elements_sdk.model.media_files_lookup_request import MediaFilesLookupRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    media_files_lookup_request = MediaFilesLookupRequest(
        query="query_example",
    ) # MediaFilesLookupRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.lookup_media_files(media_files_lookup_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->lookup_media_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_files_lookup_request** | [**MediaFilesLookupRequest**](MediaFilesLookupRequest.md)|  |

### Return type

[**[MediaFile]**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **mark_file_archived**
    def TaskInfo mark_file_archived(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_delete_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mark_file_archived(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->mark_file_archived: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **mark_file_not_archived**
    def TaskInfo mark_file_not_archived(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.mark_file_not_archived(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->mark_file_not_archived: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **mark_media_directory_as_showroom**
    def mark_media_directory_as_showroom(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.mark_media_directory_as_showroom(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->mark_media_directory_as_showroom: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_asset**
    def Asset patch_asset(id, asset_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset import Asset
from elements_sdk.model.asset_partial_update import AssetPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.
    asset_partial_update = AssetPartialUpdate(
        custom_fields={
            "key": "key_example",
        },
        tags=[
            TagReference(
                id=1,
            ),
        ],
        workflow_state=-2147483648,
        timecode=3.14,
        set_stack_order=-2147483648,
    ) # AssetPartialUpdate | 
    root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_asset(id, asset_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_asset(id, asset_partial_update, root=root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |
 **asset_partial_update** | [**AssetPartialUpdate**](AssetPartialUpdate.md)|  |
 **root** | **int**|  | [optional]

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_asset_subtitle_link**
    def AssetSubtitleLink patch_asset_subtitle_link(asset_id, id, asset_subtitle_link_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_subtitle_link import AssetSubtitleLink
from elements_sdk.model.asset_subtitle_link_partial_update import AssetSubtitleLinkPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this Asset subtitle file link.
    asset_subtitle_link_partial_update = AssetSubtitleLinkPartialUpdate(
        subtitle=AssetMiniReference(
            id=1,
            default_proxy=Proxy(
                id=1,
                profile=ProxyProfileMini(
                    id=1,
                    name="name_example",
                    allow_download=True,
                    proxy_generator="ffmpeg",
                ),
                transforms=Transforms(
                    to_source_point=[
                        [
                            1,
                        ],
                    ],
                    to_source_size=[
                        [
                            1,
                        ],
                    ],
                    from_source_point=[
                        [
                            1,
                        ],
                    ],
                    from_source_size=[
                        [
                            1,
                        ],
                    ],
                ),
                generated_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                failed=True,
                failed_count=-2147483648,
                name="name_example",
                variant_id="default",
                variant_config="variant_config_example",
                source_audio_layout_preserved=True,
                asset=1,
            ),
            format=FormatMetadata(
            ),
        ),
        label="label_example",
        key="key_example",
    ) # AssetSubtitleLinkPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_asset_subtitle_link(asset_id, id, asset_subtitle_link_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_asset_subtitle_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this Asset subtitle file link. |
 **asset_subtitle_link_partial_update** | [**AssetSubtitleLinkPartialUpdate**](AssetSubtitleLinkPartialUpdate.md)|  |

### Return type

[**AssetSubtitleLink**](AssetSubtitleLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_comment**
    def Comment patch_comment(id, comment_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.comment import Comment
from elements_sdk.model.comment_partial_update import CommentPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Comment.
    comment_partial_update = CommentPartialUpdate(
        assignee=None,
        user=None,
        drawing={
            "key": "key_example",
        },
        tags=[
            TagReference(
                id=1,
            ),
        ],
        text="text_example",
        time=3.14,
        is_cloud=True,
        resolved=True,
        resolved_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        asset=1,
        root=1,
        parent=1,
    ) # CommentPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_comment(id, comment_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. |
 **comment_partial_update** | [**CommentPartialUpdate**](CommentPartialUpdate.md)|  |

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_custom_field**
    def CustomField patch_custom_field(id, custom_field_partial_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.custom_field_partial_update import CustomFieldPartialUpdate
from elements_sdk.model.custom_field import CustomField
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Custom field.
    custom_field_partial_update = CustomFieldPartialUpdate(
        labels=[
            {
                "key": "key_example",
            },
        ],
        options=[
            "options_example",
        ],
        name="name_example",
        order=-2147483648,
        type="type_example",
        use_for_uploads=True,
        require_to_upload=True,
        non_user_editable=True,
        validation="number_of_digits",
        regex="regex_example",
        range_min=-2147483648,
        range_max=-2147483648,
        number_of_digits=-2147483648,
        metadata_prefill="metadata_prefill_example",
        highlight_expiration=True,
        multiple_response=True,
        help_text="help_text_example",
        users_from_group=1,
    ) # CustomFieldPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_custom_field(id, custom_field_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. |
 **custom_field_partial_update** | [**CustomFieldPartialUpdate**](CustomFieldPartialUpdate.md)|  |

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_editor_project**
    def EditorProject patch_editor_project(id, editor_project_partial_update)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.editor_project_partial_update import EditorProjectPartialUpdate
from elements_sdk.model.editor_project import EditorProject
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    editor_project_partial_update = EditorProjectPartialUpdate(
        file=1,
        parent=1,
        parent_path="parent_path_example",
        existing_file=1,
        format="format_example",
        project={},
    ) # EditorProjectPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_editor_project(id, editor_project_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_editor_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **editor_project_partial_update** | [**EditorProjectPartialUpdate**](EditorProjectPartialUpdate.md)|  |

### Return type

[**EditorProject**](EditorProject.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_editor_subtitle**
    def EditorSubtitle patch_editor_subtitle(id, editor_subtitle_partial_update)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.editor_subtitle_partial_update import EditorSubtitlePartialUpdate
from elements_sdk.model.editor_subtitle import EditorSubtitle
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    editor_subtitle_partial_update = EditorSubtitlePartialUpdate(
        file=1,
        parent=1,
        name="name_example",
        format="format_example",
        subtitle=Subtitle(
            info={
                "key": "key_example",
            },
            styles={
                "key": "key_example",
            },
            events=[
                SubtitleEvent(
                    start=1,
                    end=1,
                    text="text_example",
                    marked=True,
                    layer=1,
                    style="style_example",
                    name="name_example",
                    marginl=1,
                    marginr=1,
                    marginv=1,
                    effect="effect_example",
                    type="type_example",
                ),
            ],
        ),
    ) # EditorSubtitlePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_editor_subtitle(id, editor_subtitle_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_editor_subtitle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **editor_subtitle_partial_update** | [**EditorSubtitlePartialUpdate**](EditorSubtitlePartialUpdate.md)|  |

### Return type

[**EditorSubtitle**](EditorSubtitle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_external_transcoder**
    def ExternalTranscoder patch_external_transcoder(id, external_transcoder_partial_update)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.external_transcoder import ExternalTranscoder
from elements_sdk.model.external_transcoder_partial_update import ExternalTranscoderPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this external transcoder.
    external_transcoder_partial_update = ExternalTranscoderPartialUpdate(
        path_mappings=[
            PathMapping(
                local="local_example",
                remote="remote_example",
            ),
        ],
        name="name_example",
        type="transkoder",
        address="address_example",
    ) # ExternalTranscoderPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_external_transcoder(id, external_transcoder_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. |
 **external_transcoder_partial_update** | [**ExternalTranscoderPartialUpdate**](ExternalTranscoderPartialUpdate.md)|  |

### Return type

[**ExternalTranscoder**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_marker**
    def Marker patch_marker(asset_id, id, marker_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.marker_partial_update import MarkerPartialUpdate
from elements_sdk.model.marker import Marker
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this marker.
    marker_partial_update = MarkerPartialUpdate(
        title="title_example",
        text="text_example",
        t_in=3.14,
        t_out=3.14,
        asset=1,
    ) # MarkerPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_marker(asset_id, id, marker_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this marker. |
 **marker_partial_update** | [**MarkerPartialUpdate**](MarkerPartialUpdate.md)|  |

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_media_file**
    def MediaFile patch_media_file(id, media_file_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from elements_sdk.model.media_file_partial_update import MediaFilePartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    media_file_partial_update = MediaFilePartialUpdate(
        info={
            "key": "key_example",
        },
        custom_fields={
            "key": "key_example",
        },
        total_files=-2147483648,
        needs_rescan=True,
    ) # MediaFilePartialUpdate | 
    root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_media_file(id, media_file_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_media_file(id, media_file_partial_update, root=root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **media_file_partial_update** | [**MediaFilePartialUpdate**](MediaFilePartialUpdate.md)|  |
 **root** | **int**|  | [optional]

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_media_file_template**
    def MediaFileTemplate patch_media_file_template(id, media_file_template_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_template import MediaFileTemplate
from elements_sdk.model.media_file_template_partial_update import MediaFileTemplatePartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Template.
    media_file_template_partial_update = MediaFileTemplatePartialUpdate(
        file=MediaFileReference(
            id=1,
            volume=VolumeMini(
                id=1,
                path="path_example",
                display_name="display_name_example",
                visual_tag="visual_tag_example",
                type="generic",
            ),
            resolved_permission=MediaRootPermission(
                id=1,
                user=None,
                group=None,
                allow_read=True,
                allow_create=True,
                allow_write_fs=True,
                allow_write_db=True,
                allow_proxy_download=True,
                allow_original_download=True,
                allow_upload=True,
                allow_sharing=True,
                allow_delete_fs=True,
                allow_delete_db=True,
                show_tags=True,
                show_comments=True,
                show_locations=True,
                show_custom_fields=True,
                show_ratings=True,
                show_subclips=True,
                show_subtitles=True,
                show_ai_metadata=True,
                show_markers=True,
                show_history=True,
                path="path_example",
                root=1,
                is_temporary_for_token=1,
            ),
            root=MediaRootMini(
                id=1,
                name="name_example",
                description="description_example",
                volume=VolumeMini(
                    id=1,
                    path="path_example",
                    display_name="display_name_example",
                    visual_tag="visual_tag_example",
                    type="generic",
                ),
                path="path_example",
                prefetch_thumbnail_strips=True,
                view_mode="view_mode_example",
                cover="cover_example",
            ),
            modified_by=ElementsUserMini(
                id=1,
                avatar="avatar_example",
                email="email_example",
                full_name="full_name_example",
                is_external=True,
                is_cloud=True,
                username="username_example",
            ),
            exclusion_info=MediaFileExclusionInfo(
                scan=PathExclusionInfo(
                    is_parent_excluded=True,
                    path_excluded="path_excluded_example",
                    pattern_excluded="pattern_excluded_example",
                ),
                proxy=PathExclusionInfo(
                    is_parent_excluded=True,
                    path_excluded="path_excluded_example",
                    pattern_excluded="pattern_excluded_example",
                ),
            ),
        ),
        name="name_example",
    ) # MediaFileTemplatePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_media_file_template(id, media_file_template_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. |
 **media_file_template_partial_update** | [**MediaFileTemplatePartialUpdate**](MediaFileTemplatePartialUpdate.md)|  |

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_media_pinned_item**
    def MediaPinnedItem patch_media_pinned_item(id, media_pinned_item_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_pinned_item import MediaPinnedItem
from elements_sdk.model.media_pinned_item_partial_update import MediaPinnedItemPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media pinned item.
    media_pinned_item_partial_update = MediaPinnedItemPartialUpdate(
        bookmarked_file=None,
        saved_search=None,
        pin_order=-2147483648,
    ) # MediaPinnedItemPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_media_pinned_item(id, media_pinned_item_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_pinned_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media pinned item. |
 **media_pinned_item_partial_update** | [**MediaPinnedItemPartialUpdate**](MediaPinnedItemPartialUpdate.md)|  |

### Return type

[**MediaPinnedItem**](MediaPinnedItem.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_media_root**
    def MediaRootDetail patch_media_root(id, media_root_detail_partial_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_detail import MediaRootDetail
from elements_sdk.model.media_root_detail_partial_update import MediaRootDetailPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media root.
    media_root_detail_partial_update = MediaRootDetailPartialUpdate(
        custom_fields=[
            CustomFieldReference(
                id=1,
            ),
        ],
        workflow=None,
        jobs=[
            JobReference(
                id=1,
            ),
        ],
        name="name_example",
        description="description_example",
        needs_rescan=True,
        view_mode="view_mode_example",
        view_style="view_style_example",
        view_default_tab="view_default_tab_example",
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_markers=True,
        show_history=True,
        show_ai_metadata=True,
        prefetch_thumbnail_strips=True,
        cover="cover_example",
        name_field="name_field_example",
        share_comments=True,
        share_link_duration=-2147483648,
        disable_framestacks=True,
        default_proxy_profile=1,
        cloud_proxy_profile=1,
        proxy_profiles=[
            1,
        ],
        tags=[
            1,
        ],
    ) # MediaRootDetailPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_media_root(id, media_root_detail_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. |
 **media_root_detail_partial_update** | [**MediaRootDetailPartialUpdate**](MediaRootDetailPartialUpdate.md)|  |

### Return type

[**MediaRootDetail**](MediaRootDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_media_root_permission**
    def MediaRootPermission patch_media_root_permission(id, media_root_permission_partial_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_permission_partial_update import MediaRootPermissionPartialUpdate
from elements_sdk.model.media_root_permission import MediaRootPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Media Root Permission.
    media_root_permission_partial_update = MediaRootPermissionPartialUpdate(
        user=None,
        group=None,
        allow_read=True,
        allow_create=True,
        allow_write_fs=True,
        allow_write_db=True,
        allow_proxy_download=True,
        allow_original_download=True,
        allow_upload=True,
        allow_sharing=True,
        allow_delete_fs=True,
        allow_delete_db=True,
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_ai_metadata=True,
        show_markers=True,
        show_history=True,
        path="path_example",
        root=1,
        is_temporary_for_token=1,
    ) # MediaRootPermissionPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_media_root_permission(id, media_root_permission_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. |
 **media_root_permission_partial_update** | [**MediaRootPermissionPartialUpdate**](MediaRootPermissionPartialUpdate.md)|  |

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_media_tag**
    def UnfilteredTag patch_media_tag(id, unfiltered_tag_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.unfiltered_tag_partial_update import UnfilteredTagPartialUpdate
from elements_sdk.model.unfiltered_tag import UnfilteredTag
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Tag.
    unfiltered_tag_partial_update = UnfilteredTagPartialUpdate(
        roots=[
            1,
        ],
        name="name_example",
        shared=True,
        color="color_example",
    ) # UnfilteredTagPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_media_tag(id, unfiltered_tag_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. |
 **unfiltered_tag_partial_update** | [**UnfilteredTagPartialUpdate**](UnfilteredTagPartialUpdate.md)|  |

### Return type

[**UnfilteredTag**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_proxy_profile**
    def ProxyProfile patch_proxy_profile(id, proxy_profile_partial_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_profile_partial_update import ProxyProfilePartialUpdate
from elements_sdk.model.proxy_profile import ProxyProfile
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this proxy profile.
    proxy_profile_partial_update = ProxyProfilePartialUpdate(
        name="name_example",
        proxy_generator="ffmpeg",
        type="video",
        resolution="resolution_example",
        rate_control="CRF",
        crf=-2147483648,
        bitrate=-2147483648,
        audio_bitrate=-2147483648,
        variants_limit=-2147483648,
        enable_dense_filmstrip=True,
        image_format="png",
        enable_watermark=True,
        watermark_image="watermark_image_example",
        watermark_position="TL",
        watermark_opacity=3.14,
        watermark_size=3.14,
        enable_timecode=True,
        timecode_position="TL",
        timecode_opacity=3.14,
        timecode_size=3.14,
        lut="lut_example",
        hotfolder_copy_to="hotfolder_copy_to_example",
        hotfolder_read_from="hotfolder_read_from_example",
        hotfolder_queue_timeout=-2147483648,
        hotfolder_encode_timeout=-2147483648,
        vantage_workflow_id="vantage_workflow_id_example",
        external_transcoder_staging_path="external_transcoder_staging_path_example",
        allow_download=True,
        keep_audio_layout=True,
        external_transcoder=1,
    ) # ProxyProfilePartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_proxy_profile(id, proxy_profile_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. |
 **proxy_profile_partial_update** | [**ProxyProfilePartialUpdate**](ProxyProfilePartialUpdate.md)|  |

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_saved_search**
    def SavedSearch patch_saved_search(id, saved_search_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.saved_search import SavedSearch
from elements_sdk.model.saved_search_partial_update import SavedSearchPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this saved search.
    saved_search_partial_update = SavedSearchPartialUpdate(
        root=None,
        query=[
            {},
        ],
        name="name_example",
    ) # SavedSearchPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_saved_search(id, saved_search_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_saved_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this saved search. |
 **saved_search_partial_update** | [**SavedSearchPartialUpdate**](SavedSearchPartialUpdate.md)|  |

### Return type

[**SavedSearch**](SavedSearch.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_sharing_permission_preset**
    def SharingPermissionPreset patch_sharing_permission_preset(id, sharing_permission_preset_partial_update)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.sharing_permission_preset import SharingPermissionPreset
from elements_sdk.model.sharing_permission_preset_partial_update import SharingPermissionPresetPartialUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Sharing Permission Preset.
    sharing_permission_preset_partial_update = SharingPermissionPresetPartialUpdate(
        allow_read=True,
        allow_create=True,
        allow_write_fs=True,
        allow_write_db=True,
        allow_proxy_download=True,
        allow_original_download=True,
        allow_upload=True,
        allow_sharing=True,
        allow_delete_fs=True,
        allow_delete_db=True,
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_ai_metadata=True,
        show_markers=True,
        show_history=True,
        name="name_example",
        default=True,
    ) # SharingPermissionPresetPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_sharing_permission_preset(id, sharing_permission_preset_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_sharing_permission_preset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Sharing Permission Preset. |
 **sharing_permission_preset_partial_update** | [**SharingPermissionPresetPartialUpdate**](SharingPermissionPresetPartialUpdate.md)|  |

### Return type

[**SharingPermissionPreset**](SharingPermissionPreset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_subclip**
    def Subclip patch_subclip(asset_id, id, subclip_partial_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * Must be shared OR Must own the object   * allow_write_db, show_subclips Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.subclip_partial_update import SubclipPartialUpdate
from elements_sdk.model.subclip import Subclip
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this subclip.
    subclip_partial_update = SubclipPartialUpdate(
        rendered=None,
        shared=True,
        name="name_example",
        t_in=3.14,
        t_out=3.14,
        root=MediaRootMiniReference(
            id=1,
            volume=VolumeMini(
                id=1,
                path="path_example",
                display_name="display_name_example",
                visual_tag="visual_tag_example",
                type="generic",
            ),
            path="path_example",
        ),
    ) # SubclipPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_subclip(asset_id, id, subclip_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this subclip. |
 **subclip_partial_update** | [**SubclipPartialUpdate**](SubclipPartialUpdate.md)|  |

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **patch_workflow**
    def Workflow patch_workflow(id, workflow_partial_update)



### Required permissions    * User account permission: `media:roots:manage`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.workflow_partial_update import WorkflowPartialUpdate
from elements_sdk.model.workflow import Workflow
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Workflow.
    workflow_partial_update = WorkflowPartialUpdate(
        states=[
            {},
        ],
        transitions=[
            {},
        ],
        roots=[
            1,
        ],
        name="name_example",
    ) # WorkflowPartialUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_workflow(id, workflow_partial_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->patch_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Workflow. |
 **workflow_partial_update** | [**WorkflowPartialUpdate**](WorkflowPartialUpdate.md)|  |

### Return type

[**Workflow**](Workflow.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **pin_media_item_globally**
    def MediaPinnedItem pin_media_item_globally(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_pinned_item import MediaPinnedItem
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media pinned item.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.pin_media_item_globally(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->pin_media_item_globally: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media pinned item. |

### Return type

[**MediaPinnedItem**](MediaPinnedItem.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **pin_media_root_permission**
    def MediaPinnedItem pin_media_root_permission(id)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_pinned_item import MediaPinnedItem
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Media Root Permission.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.pin_media_root_permission(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->pin_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. |

### Return type

[**MediaPinnedItem**](MediaPinnedItem.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **recursively_tag_media_directory**
    def recursively_tag_media_directory(id, tag_media_directory_request)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.tag_media_directory_request import TagMediaDirectoryRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    tag_media_directory_request = TagMediaDirectoryRequest(
        tag=1,
        add=True,
    ) # TagMediaDirectoryRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.recursively_tag_media_directory(id, tag_media_directory_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->recursively_tag_media_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **tag_media_directory_request** | [**TagMediaDirectoryRequest**](TagMediaDirectoryRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **reinclude_directory_for_proxy_generation**
    def reinclude_directory_for_proxy_generation(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.reinclude_directory_for_proxy_generation(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->reinclude_directory_for_proxy_generation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **reinclude_directory_for_scan**
    def reinclude_directory_for_scan(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.reinclude_directory_for_scan(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->reinclude_directory_for_scan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **reindex_media_directory**
    def reindex_media_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.reindex_media_directory(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->reindex_media_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **remove_asset_from_set**
    def remove_asset_from_set(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_asset_from_set(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->remove_asset_from_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **rename_custom_field**
    def TaskInfo rename_custom_field(id, rename_custom_field_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.rename_custom_field_request import RenameCustomFieldRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Custom field.
    rename_custom_field_request = RenameCustomFieldRequest(
        name="name_example",
    ) # RenameCustomFieldRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rename_custom_field(id, rename_custom_field_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->rename_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. |
 **rename_custom_field_request** | [**RenameCustomFieldRequest**](RenameCustomFieldRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **render_sequence**
    def TaskInfo render_sequence(render_endpoint_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.render_endpoint_request import RenderEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    render_endpoint_request = RenderEndpointRequest(
        sequence={},
        project={},
        options=SequenceRenderRequestOptions(
            output_path="output_path_example",
            combine=False,
            data_source="source",
            tails=3.14,
            wrap_opatom=False,
            resolution="resolution_example",
            fps="fps_example",
        ),
    ) # RenderEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.render_sequence(render_endpoint_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->render_sequence: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **render_endpoint_request** | [**RenderEndpointRequest**](RenderEndpointRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **render_subclip**
    def TaskInfo render_subclip(asset_id, id, render_request)



### Required permissions    * User account permission: `media:access`   * License component: media   * Must be shared OR Must own the object   * allow_read, show_subclips Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.task_info import TaskInfo
from elements_sdk.model.render_request import RenderRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this subclip.
    render_request = RenderRequest(
        destination="destination_example",
    ) # RenderRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.render_subclip(asset_id, id, render_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->render_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this subclip. |
 **render_request** | [**RenderRequest**](RenderRequest.md)|  |

### Return type

[**TaskInfo**](TaskInfo.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **request_media_scan**
    def request_media_scan(scanner_scan_endpoint_request)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.scanner_scan_endpoint_request import ScannerScanEndpointRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    scanner_scan_endpoint_request = ScannerScanEndpointRequest(
        path="path_example",
        recursive=True,
        notify=True,
        force_rescan=True,
    ) # ScannerScanEndpointRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.request_media_scan(scanner_scan_endpoint_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->request_media_scan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scanner_scan_endpoint_request** | [**ScannerScanEndpointRequest**](ScannerScanEndpointRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **resolve_comment**
    def Comment resolve_comment(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.comment import Comment
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Comment.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.resolve_comment(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->resolve_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. |

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **share_media_library_objects**
    def OneTimeAccessToken share_media_library_objects(media_library_share_request)



### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_library_share_request import MediaLibraryShareRequest
from elements_sdk.model.one_time_access_token import OneTimeAccessToken
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    media_library_share_request = MediaLibraryShareRequest(
        bundles=[
            1,
        ],
        directories=[
            1,
        ],
        expires=dateutil_parser('1970-01-01T00:00:00.00Z'),
        view_limit=1,
        permissions=MediaRootPermissionAccessOptions(
            show_tags=True,
            show_comments=True,
            show_locations=True,
            show_custom_fields=True,
            show_ratings=True,
            show_subclips=True,
            show_subtitles=True,
            show_ai_metadata=True,
            show_markers=True,
            show_history=True,
            allow_read=True,
            allow_create=True,
            allow_write_fs=True,
            allow_write_db=True,
            allow_proxy_download=True,
            allow_original_download=True,
            allow_upload=True,
            allow_sharing=True,
            allow_delete_fs=True,
            allow_delete_db=True,
        ),
        user=1,
        email="email_example",
        link_type="link_type_example",
        password="password_example",
    ) # MediaLibraryShareRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.share_media_library_objects(media_library_share_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->share_media_library_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_library_share_request** | [**MediaLibraryShareRequest**](MediaLibraryShareRequest.md)|  |

### Return type

[**OneTimeAccessToken**](OneTimeAccessToken.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **test_external_transcoder_connection**
    def TestExternalTranscoderConnectionResponse test_external_transcoder_connection(test_external_transcoder_connection_request)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.test_external_transcoder_connection_request import TestExternalTranscoderConnectionRequest
from elements_sdk.model.test_external_transcoder_connection_response import TestExternalTranscoderConnectionResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    test_external_transcoder_connection_request = TestExternalTranscoderConnectionRequest(
        type="type_example",
        address="address_example",
    ) # TestExternalTranscoderConnectionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.test_external_transcoder_connection(test_external_transcoder_connection_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->test_external_transcoder_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_external_transcoder_connection_request** | [**TestExternalTranscoderConnectionRequest**](TestExternalTranscoderConnectionRequest.md)|  |

### Return type

[**TestExternalTranscoderConnectionResponse**](TestExternalTranscoderConnectionResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **transition_workflow**
    def WorkflowTransitionResponse transition_workflow(workflow_transition_request)



### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.workflow_transition_request import WorkflowTransitionRequest
from elements_sdk.model.workflow_transition_response import WorkflowTransitionResponse
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    workflow_transition_request = WorkflowTransitionRequest(
        bundles=[
            1,
        ],
        directories=[
            1,
        ],
        job=1,
        root=1,
        variables={
            "key": "key_example",
        },
    ) # WorkflowTransitionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.transition_workflow(workflow_transition_request)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->transition_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_transition_request** | [**WorkflowTransitionRequest**](WorkflowTransitionRequest.md)|  |

### Return type

[**WorkflowTransitionResponse**](WorkflowTransitionResponse.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **unbookmark_media_directory**
    def unbookmark_media_directory(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions OR allow_upload Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.unbookmark_media_directory(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->unbookmark_media_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **unlink_asset_version**
    def unlink_asset_version(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.

    # example passing only required values which don't have defaults set
    try:
        api_instance.unlink_asset_version(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->unlink_asset_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **unmark_media_directory_as_showroom**
    def unmark_media_directory_as_showroom(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.

    # example passing only required values which don't have defaults set
    try:
        api_instance.unmark_media_directory_as_showroom(id)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->unmark_media_directory_as_showroom: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **unpin_media_item_globally**
    def MediaPinnedItem unpin_media_item_globally(id)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_pinned_item import MediaPinnedItem
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media pinned item.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.unpin_media_item_globally(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->unpin_media_item_globally: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media pinned item. |

### Return type

[**MediaPinnedItem**](MediaPinnedItem.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **unresolve_comment**
    def Comment unresolve_comment(id)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_read Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.comment import Comment
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Comment.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.unresolve_comment(id)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->unresolve_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. |

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_asset**
    def Asset update_asset(id, asset_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset import Asset
from elements_sdk.model.asset_update import AssetUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Asset.
    asset_update = AssetUpdate(
        custom_fields={
            "key": "key_example",
        },
        tags=[
            TagReference(
                id=1,
            ),
        ],
        workflow_state=-2147483648,
        timecode=3.14,
        set_stack_order=-2147483648,
    ) # AssetUpdate | 
    root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_asset(id, asset_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_asset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_asset(id, asset_update, root=root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_asset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Asset. |
 **asset_update** | [**AssetUpdate**](AssetUpdate.md)|  |
 **root** | **int**|  | [optional]

### Return type

[**Asset**](Asset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_asset_subtitle_link**
    def AssetSubtitleLink update_asset_subtitle_link(asset_id, id, asset_subtitle_link_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.asset_subtitle_link import AssetSubtitleLink
from elements_sdk.model.asset_subtitle_link_update import AssetSubtitleLinkUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this Asset subtitle file link.
    asset_subtitle_link_update = AssetSubtitleLinkUpdate(
        subtitle=AssetMiniReference(
            id=1,
            default_proxy=Proxy(
                id=1,
                profile=ProxyProfileMini(
                    id=1,
                    name="name_example",
                    allow_download=True,
                    proxy_generator="ffmpeg",
                ),
                transforms=Transforms(
                    to_source_point=[
                        [
                            1,
                        ],
                    ],
                    to_source_size=[
                        [
                            1,
                        ],
                    ],
                    from_source_point=[
                        [
                            1,
                        ],
                    ],
                    from_source_size=[
                        [
                            1,
                        ],
                    ],
                ),
                generated_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                failed=True,
                failed_count=-2147483648,
                name="name_example",
                variant_id="default",
                variant_config="variant_config_example",
                source_audio_layout_preserved=True,
                asset=1,
            ),
            format=FormatMetadata(
            ),
        ),
        label="label_example",
        key="key_example",
    ) # AssetSubtitleLinkUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_asset_subtitle_link(asset_id, id, asset_subtitle_link_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_asset_subtitle_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this Asset subtitle file link. |
 **asset_subtitle_link_update** | [**AssetSubtitleLinkUpdate**](AssetSubtitleLinkUpdate.md)|  |

### Return type

[**AssetSubtitleLink**](AssetSubtitleLink.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_comment**
    def Comment update_comment(id, comment_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.comment import Comment
from elements_sdk.model.comment_update import CommentUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Comment.
    comment_update = CommentUpdate(
        assignee=None,
        user=None,
        drawing={
            "key": "key_example",
        },
        tags=[
            TagReference(
                id=1,
            ),
        ],
        text="text_example",
        time=3.14,
        is_cloud=True,
        resolved=True,
        resolved_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        asset=1,
        root=1,
        parent=1,
    ) # CommentUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_comment(id, comment_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_comment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Comment. |
 **comment_update** | [**CommentUpdate**](CommentUpdate.md)|  |

### Return type

[**Comment**](Comment.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_custom_field**
    def CustomField update_custom_field(id, custom_field_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.custom_field import CustomField
from elements_sdk.model.custom_field_update import CustomFieldUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Custom field.
    custom_field_update = CustomFieldUpdate(
        labels=[
            {
                "key": "key_example",
            },
        ],
        options=[
            "options_example",
        ],
        name="name_example",
        order=-2147483648,
        type="type_example",
        use_for_uploads=True,
        require_to_upload=True,
        non_user_editable=True,
        validation="number_of_digits",
        regex="regex_example",
        range_min=-2147483648,
        range_max=-2147483648,
        number_of_digits=-2147483648,
        metadata_prefill="metadata_prefill_example",
        highlight_expiration=True,
        multiple_response=True,
        help_text="help_text_example",
        users_from_group=1,
    ) # CustomFieldUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_custom_field(id, custom_field_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_custom_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Custom field. |
 **custom_field_update** | [**CustomFieldUpdate**](CustomFieldUpdate.md)|  |

### Return type

[**CustomField**](CustomField.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_editor_project**
    def EditorProject update_editor_project(id, editor_project_update)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.editor_project_update import EditorProjectUpdate
from elements_sdk.model.editor_project import EditorProject
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    editor_project_update = EditorProjectUpdate(
        file=1,
        parent=1,
        parent_path="parent_path_example",
        existing_file=1,
        format="format_example",
        project={},
    ) # EditorProjectUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_editor_project(id, editor_project_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_editor_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **editor_project_update** | [**EditorProjectUpdate**](EditorProjectUpdate.md)|  |

### Return type

[**EditorProject**](EditorProject.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_editor_subtitle**
    def EditorSubtitle update_editor_subtitle(id, editor_subtitle_update)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.editor_subtitle import EditorSubtitle
from elements_sdk.model.editor_subtitle_update import EditorSubtitleUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    editor_subtitle_update = EditorSubtitleUpdate(
        file=1,
        parent=1,
        name="name_example",
        format="format_example",
        subtitle=Subtitle(
            info={
                "key": "key_example",
            },
            styles={
                "key": "key_example",
            },
            events=[
                SubtitleEvent(
                    start=1,
                    end=1,
                    text="text_example",
                    marked=True,
                    layer=1,
                    style="style_example",
                    name="name_example",
                    marginl=1,
                    marginr=1,
                    marginv=1,
                    effect="effect_example",
                    type="type_example",
                ),
            ],
        ),
    ) # EditorSubtitleUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_editor_subtitle(id, editor_subtitle_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_editor_subtitle: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **editor_subtitle_update** | [**EditorSubtitleUpdate**](EditorSubtitleUpdate.md)|  |

### Return type

[**EditorSubtitle**](EditorSubtitle.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_external_transcoder**
    def ExternalTranscoder update_external_transcoder(id, external_transcoder_update)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write) 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.external_transcoder import ExternalTranscoder
from elements_sdk.model.external_transcoder_update import ExternalTranscoderUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this external transcoder.
    external_transcoder_update = ExternalTranscoderUpdate(
        path_mappings=[
            PathMapping(
                local="local_example",
                remote="remote_example",
            ),
        ],
        name="name_example",
        type="transkoder",
        address="address_example",
    ) # ExternalTranscoderUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_external_transcoder(id, external_transcoder_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_external_transcoder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this external transcoder. |
 **external_transcoder_update** | [**ExternalTranscoderUpdate**](ExternalTranscoderUpdate.md)|  |

### Return type

[**ExternalTranscoder**](ExternalTranscoder.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_marker**
    def Marker update_marker(asset_id, id, marker_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.marker import Marker
from elements_sdk.model.marker_update import MarkerUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this marker.
    marker_update = MarkerUpdate(
        title="title_example",
        text="text_example",
        t_in=3.14,
        t_out=3.14,
        asset=1,
    ) # MarkerUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_marker(asset_id, id, marker_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_marker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this marker. |
 **marker_update** | [**MarkerUpdate**](MarkerUpdate.md)|  |

### Return type

[**Marker**](Marker.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_media_file**
    def MediaFile update_media_file(id, media_file_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * allow_write_db Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file import MediaFile
from elements_sdk.model.media_file_update import MediaFileUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this File.
    media_file_update = MediaFileUpdate(
        info={
            "key": "key_example",
        },
        custom_fields={
            "key": "key_example",
        },
        total_files=-2147483648,
        needs_rescan=True,
    ) # MediaFileUpdate | 
    root = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_media_file(id, media_file_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_media_file(id, media_file_update, root=root)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this File. |
 **media_file_update** | [**MediaFileUpdate**](MediaFileUpdate.md)|  |
 **root** | **int**|  | [optional]

### Return type

[**MediaFile**](MediaFile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_media_file_template**
    def MediaFileTemplate update_media_file_template(id, media_file_template_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_file_template_update import MediaFileTemplateUpdate
from elements_sdk.model.media_file_template import MediaFileTemplate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Template.
    media_file_template_update = MediaFileTemplateUpdate(
        file=MediaFileReference(
            id=1,
            volume=VolumeMini(
                id=1,
                path="path_example",
                display_name="display_name_example",
                visual_tag="visual_tag_example",
                type="generic",
            ),
            resolved_permission=MediaRootPermission(
                id=1,
                user=None,
                group=None,
                allow_read=True,
                allow_create=True,
                allow_write_fs=True,
                allow_write_db=True,
                allow_proxy_download=True,
                allow_original_download=True,
                allow_upload=True,
                allow_sharing=True,
                allow_delete_fs=True,
                allow_delete_db=True,
                show_tags=True,
                show_comments=True,
                show_locations=True,
                show_custom_fields=True,
                show_ratings=True,
                show_subclips=True,
                show_subtitles=True,
                show_ai_metadata=True,
                show_markers=True,
                show_history=True,
                path="path_example",
                root=1,
                is_temporary_for_token=1,
            ),
            root=MediaRootMini(
                id=1,
                name="name_example",
                description="description_example",
                volume=VolumeMini(
                    id=1,
                    path="path_example",
                    display_name="display_name_example",
                    visual_tag="visual_tag_example",
                    type="generic",
                ),
                path="path_example",
                prefetch_thumbnail_strips=True,
                view_mode="view_mode_example",
                cover="cover_example",
            ),
            modified_by=ElementsUserMini(
                id=1,
                avatar="avatar_example",
                email="email_example",
                full_name="full_name_example",
                is_external=True,
                is_cloud=True,
                username="username_example",
            ),
            exclusion_info=MediaFileExclusionInfo(
                scan=PathExclusionInfo(
                    is_parent_excluded=True,
                    path_excluded="path_excluded_example",
                    pattern_excluded="pattern_excluded_example",
                ),
                proxy=PathExclusionInfo(
                    is_parent_excluded=True,
                    path_excluded="path_excluded_example",
                    pattern_excluded="pattern_excluded_example",
                ),
            ),
        ),
        name="name_example",
    ) # MediaFileTemplateUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_media_file_template(id, media_file_template_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_file_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Template. |
 **media_file_template_update** | [**MediaFileTemplateUpdate**](MediaFileTemplateUpdate.md)|  |

### Return type

[**MediaFileTemplate**](MediaFileTemplate.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_media_pinned_item**
    def MediaPinnedItem update_media_pinned_item(id, media_pinned_item_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_pinned_item_update import MediaPinnedItemUpdate
from elements_sdk.model.media_pinned_item import MediaPinnedItem
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media pinned item.
    media_pinned_item_update = MediaPinnedItemUpdate(
        bookmarked_file=None,
        saved_search=None,
        pin_order=-2147483648,
    ) # MediaPinnedItemUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_media_pinned_item(id, media_pinned_item_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_pinned_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media pinned item. |
 **media_pinned_item_update** | [**MediaPinnedItemUpdate**](MediaPinnedItemUpdate.md)|  |

### Return type

[**MediaPinnedItem**](MediaPinnedItem.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_media_root**
    def MediaRootDetail update_media_root(id, media_root_detail_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_detail import MediaRootDetail
from elements_sdk.model.media_root_detail_update import MediaRootDetailUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media root.
    media_root_detail_update = MediaRootDetailUpdate(
        custom_fields=[
            CustomFieldReference(
                id=1,
            ),
        ],
        volume=VolumeReference(
            id=1,
            fs_properties=FSProperties(
                needs_node=True,
                supports_directory_quotas=True,
                supports_workspace_quotas=True,
                supports_soft_quotas=True,
                supports_user_quotas=True,
                supports_group_quotas=True,
                supports_xattrs=True,
                supports_snapshots=True,
                creating_directory_quota_destroys_content=True,
                removing_directory_quota_destroys_content=True,
                supports_posix_permissions=True,
                supports_dates=True,
                supports_renaming=True,
            ),
            backend=Backend(
                name="name_example",
                properties=BackendProperties(
                    supports_sharing_rw_permissions_priority=True,
                    supports_sharing_afp=True,
                    supports_sharing_smb_require_logon=True,
                    supports_sharing_smb_recycle_bin=True,
                    supports_sharing_smb_xattrs=True,
                    supports_sharing_smb_symlinks=True,
                    supports_sharing_smb_custom_options=True,
                    supports_sharing_smb_allow_execute=True,
                    supports_sharing_smb_locking_options=True,
                    supports_sharing_smb_hidden=True,
                    supports_sharing_veto=True,
                    supports_sharing_nfs_permissions=True,
                ),
            ),
            status=VolumeStatus(
                online=True,
                size_total=1,
                size_used=1,
                size_free=1,
                snfs=VolumeSNFSStatus(
                    stripe_groups=[
                        SNFSStripeGroup(
                            name="name_example",
                            status_tags=[
                                "status_tags_example",
                            ],
                            affinity="affinity_example",
                            size_total=1,
                            size_used=1,
                            size_free=1,
                        ),
                    ],
                ),
                beegfs=VolumeBeeGFSStatus(
                    nodes=[
                        BeeGFSNode(
                            node=None,
                            host="host_example",
                            roles=[
                                "roles_example",
                            ],
                            addresses=[
                                "addresses_example",
                            ],
                        ),
                    ],
                    targets=[
                        BeeGFSTarget(
                            node=None,
                            id=1,
                            host="host_example",
                            storage_pool=1,
                            size_total=1,
                            size_used=1,
                            size_free=1,
                            online=True,
                            consistent=True,
                            errors=[
                                "errors_example",
                            ],
                        ),
                    ],
                ),
            ),
        ),
        workflow=None,
        jobs=[
            JobReference(
                id=1,
            ),
        ],
        name="name_example",
        path="path_example",
        description="description_example",
        needs_rescan=True,
        view_mode="view_mode_example",
        view_style="view_style_example",
        view_default_tab="view_default_tab_example",
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_markers=True,
        show_history=True,
        show_ai_metadata=True,
        prefetch_thumbnail_strips=True,
        cover="cover_example",
        name_field="name_field_example",
        share_comments=True,
        share_link_duration=-2147483648,
        disable_framestacks=True,
        default_proxy_profile=1,
        cloud_proxy_profile=1,
        proxy_profiles=[
            1,
        ],
        tags=[
            1,
        ],
    ) # MediaRootDetailUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_media_root(id, media_root_detail_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_root: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. |
 **media_root_detail_update** | [**MediaRootDetailUpdate**](MediaRootDetailUpdate.md)|  |

### Return type

[**MediaRootDetail**](MediaRootDetail.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_media_root_cover_image**
    def update_media_root_cover_image(id, image_upload_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.image_upload_request import ImageUploadRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this media root.
    image_upload_request = ImageUploadRequest(
        data="data_example",
    ) # ImageUploadRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_media_root_cover_image(id, image_upload_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_root_cover_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this media root. |
 **image_upload_request** | [**ImageUploadRequest**](ImageUploadRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_media_root_permission**
    def MediaRootPermission update_media_root_permission(id, media_root_permission_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.media_root_permission_update import MediaRootPermissionUpdate
from elements_sdk.model.media_root_permission import MediaRootPermission
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Media Root Permission.
    media_root_permission_update = MediaRootPermissionUpdate(
        user=None,
        group=None,
        allow_read=True,
        allow_create=True,
        allow_write_fs=True,
        allow_write_db=True,
        allow_proxy_download=True,
        allow_original_download=True,
        allow_upload=True,
        allow_sharing=True,
        allow_delete_fs=True,
        allow_delete_db=True,
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_ai_metadata=True,
        show_markers=True,
        show_history=True,
        path="path_example",
        root=1,
        is_temporary_for_token=1,
    ) # MediaRootPermissionUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_media_root_permission(id, media_root_permission_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_root_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Media Root Permission. |
 **media_root_permission_update** | [**MediaRootPermissionUpdate**](MediaRootPermissionUpdate.md)|  |

### Return type

[**MediaRootPermission**](MediaRootPermission.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_media_tag**
    def UnfilteredTag update_media_tag(id, unfiltered_tag_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.unfiltered_tag_update import UnfilteredTagUpdate
from elements_sdk.model.unfiltered_tag import UnfilteredTag
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Tag.
    unfiltered_tag_update = UnfilteredTagUpdate(
        roots=[
            1,
        ],
        name="name_example",
        shared=True,
        color="color_example",
    ) # UnfilteredTagUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_media_tag(id, unfiltered_tag_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_media_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Tag. |
 **unfiltered_tag_update** | [**UnfilteredTagUpdate**](UnfilteredTagUpdate.md)|  |

### Return type

[**UnfilteredTag**](UnfilteredTag.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_proxy_profile**
    def ProxyProfile update_proxy_profile(id, proxy_profile_update)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.proxy_profile import ProxyProfile
from elements_sdk.model.proxy_profile_update import ProxyProfileUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this proxy profile.
    proxy_profile_update = ProxyProfileUpdate(
        name="name_example",
        proxy_generator="ffmpeg",
        type="video",
        resolution="resolution_example",
        rate_control="CRF",
        crf=-2147483648,
        bitrate=-2147483648,
        audio_bitrate=-2147483648,
        variants_limit=-2147483648,
        enable_dense_filmstrip=True,
        image_format="png",
        enable_watermark=True,
        watermark_image="watermark_image_example",
        watermark_position="TL",
        watermark_opacity=3.14,
        watermark_size=3.14,
        enable_timecode=True,
        timecode_position="TL",
        timecode_opacity=3.14,
        timecode_size=3.14,
        lut="lut_example",
        hotfolder_copy_to="hotfolder_copy_to_example",
        hotfolder_read_from="hotfolder_read_from_example",
        hotfolder_queue_timeout=-2147483648,
        hotfolder_encode_timeout=-2147483648,
        vantage_workflow_id="vantage_workflow_id_example",
        external_transcoder_staging_path="external_transcoder_staging_path_example",
        allow_download=True,
        keep_audio_layout=True,
        external_transcoder=1,
    ) # ProxyProfileUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_proxy_profile(id, proxy_profile_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_proxy_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. |
 **proxy_profile_update** | [**ProxyProfileUpdate**](ProxyProfileUpdate.md)|  |

### Return type

[**ProxyProfile**](ProxyProfile.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_proxy_profile_watermark_image**
    def update_proxy_profile_watermark_image(id, image_upload_request)



### Required permissions    * User account permission: `media:access` (read) / `media:roots:manage` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.image_upload_request import ImageUploadRequest
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this proxy profile.
    image_upload_request = ImageUploadRequest(
        data="data_example",
    ) # ImageUploadRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_proxy_profile_watermark_image(id, image_upload_request)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_proxy_profile_watermark_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this proxy profile. |
 **image_upload_request** | [**ImageUploadRequest**](ImageUploadRequest.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_saved_search**
    def SavedSearch update_saved_search(id, saved_search_update)



### Required permissions    * User account permission: `media:access`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.saved_search import SavedSearch
from elements_sdk.model.saved_search_update import SavedSearchUpdate
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this saved search.
    saved_search_update = SavedSearchUpdate(
        root=None,
        query=[
            {},
        ],
        name="name_example",
    ) # SavedSearchUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_saved_search(id, saved_search_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_saved_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this saved search. |
 **saved_search_update** | [**SavedSearchUpdate**](SavedSearchUpdate.md)|  |

### Return type

[**SavedSearch**](SavedSearch.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_sharing_permission_preset**
    def SharingPermissionPreset update_sharing_permission_preset(id, sharing_permission_preset_update)



### Required permissions    * User account permission: `media:access` (read) / `system:admin-access` (write)   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.sharing_permission_preset_update import SharingPermissionPresetUpdate
from elements_sdk.model.sharing_permission_preset import SharingPermissionPreset
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Sharing Permission Preset.
    sharing_permission_preset_update = SharingPermissionPresetUpdate(
        allow_read=True,
        allow_create=True,
        allow_write_fs=True,
        allow_write_db=True,
        allow_proxy_download=True,
        allow_original_download=True,
        allow_upload=True,
        allow_sharing=True,
        allow_delete_fs=True,
        allow_delete_db=True,
        show_tags=True,
        show_comments=True,
        show_locations=True,
        show_custom_fields=True,
        show_ratings=True,
        show_subclips=True,
        show_subtitles=True,
        show_ai_metadata=True,
        show_markers=True,
        show_history=True,
        name="name_example",
        default=True,
    ) # SharingPermissionPresetUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_sharing_permission_preset(id, sharing_permission_preset_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_sharing_permission_preset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Sharing Permission Preset. |
 **sharing_permission_preset_update** | [**SharingPermissionPresetUpdate**](SharingPermissionPresetUpdate.md)|  |

### Return type

[**SharingPermissionPreset**](SharingPermissionPreset.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_subclip**
    def Subclip update_subclip(asset_id, id, subclip_update)



### Required permissions    * User account permission: `media:access`   * License component: media   * Must be shared OR Must own the object   * allow_write_db, show_subclips Media Library permissions 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.subclip_update import SubclipUpdate
from elements_sdk.model.subclip import Subclip
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    asset_id = "asset_id_example" # str | 
    id = 1 # int | A unique integer value identifying this subclip.
    subclip_update = SubclipUpdate(
        rendered=None,
        shared=True,
        name="name_example",
        t_in=3.14,
        t_out=3.14,
        root=MediaRootMiniReference(
            id=1,
            volume=VolumeMini(
                id=1,
                path="path_example",
                display_name="display_name_example",
                visual_tag="visual_tag_example",
                type="generic",
            ),
            path="path_example",
        ),
    ) # SubclipUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_subclip(asset_id, id, subclip_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_subclip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  |
 **id** | **int**| A unique integer value identifying this subclip. |
 **subclip_update** | [**SubclipUpdate**](SubclipUpdate.md)|  |

### Return type

[**Subclip**](Subclip.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **update_workflow**
    def Workflow update_workflow(id, workflow_update)



### Required permissions    * User account permission: `media:roots:manage`   * License component: media 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.workflow_update import WorkflowUpdate
from elements_sdk.model.workflow import Workflow
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    id = 1 # int | A unique integer value identifying this Workflow.
    workflow_update = WorkflowUpdate(
        states=[
            {},
        ],
        transitions=[
            {},
        ],
        roots=[
            1,
        ],
        name="name_example",
    ) # WorkflowUpdate | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_workflow(id, workflow_update)
        pprint(api_response)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->update_workflow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Workflow. |
 **workflow_update** | [**WorkflowUpdate**](WorkflowUpdate.md)|  |

### Return type

[**Workflow**](Workflow.md)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

# **web_upload_completed**
    def web_upload_completed(web_upload_completed)



### Required permissions    * User account permission: `media:access` 

### Example


```python
import elements_sdk
from elements_sdk.api import media_library_api
from elements_sdk.model.web_upload_completed import WebUploadCompleted
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.
configuration = elements_sdk.Configuration(
    host="https://elements.local:8080",
    discard_unknown_keys=True,
)

configuration.client_side_validation = False
configuration.api_key['Bearer'] = 'Bearer your-api-token-here'

with elements_sdk.ApiClient(configuration) as api_client:
    api_instance = media_library_api.MediaLibraryApi(api_client)
    web_upload_completed = WebUploadCompleted(
        paths=[
            "paths_example",
        ],
    ) # WebUploadCompleted | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.web_upload_completed(web_upload_completed)
    except elements_sdk.ApiException as e:
        print("Exception when calling MediaLibraryApi->web_upload_completed: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_upload_completed** | [**WebUploadCompleted**](WebUploadCompleted.md)|  |

### Return type

void (empty response body)

[[Back to top]](#) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to Model list]](../#documentation-for-models) [[Back to README]](../)

