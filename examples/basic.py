from elements_sdk import (
    ApiClient,
    Configuration,
    StorageApi,
    Volume,
    Workspace,
    ElementsUser,
    MainApi,
    ApiException
)

# For the elements_sdk module documentation, check out
# https://python.sdk.elements.tv

API_TOKEN = 'amino-acid-knoll-hatching'
ELEMENTS_HOST = 'elements.local'

config = Configuration(
    host=f'http://{ELEMENTS_HOST}',
    api_key={'Authorization': f'Bearer {API_TOKEN}'},
)


def create_user_example():
    with ApiClient(config) as api_client:
        main_api = MainApi(api_client)

        try:
            user: ElementsUser = main_api.create_user(dict(
                username='testhans',
                unix_username='elements_testhans',
                full_name='TestHans',
                email='test@elements.tv',
                permissions=["client:access"],
                groups=[]
            ))
            main_api.apply_configuration()
            print(f"Created user '{user.full_name}' successfully")
        except ApiException as e:
            print(f"Exception when calling MainApi->create_user: {e}")


def delete_user_example():
    with ApiClient(config) as api_client:
        main_api = MainApi(api_client)

        username = 'testhans'

        try:
            user = main_api.get_all_users(username=username)
            if len(user) == 1:
                main_api.delete_user(user[0].id)
                main_api.apply_configuration()
                print(f"Deleted user '{username}' successfully")
            else:
                print(f"User '{username}' not found")
        except ApiException as e:
            print(f"Exception when calling MainApi->get_all_users: {e}")


def create_workspace_example():
    with ApiClient(config) as api_client:
        storage_api = StorageApi(api_client)

        try:
            volume: Volume = storage_api.get_all_volumes()
            workspace: Workspace = storage_api.create_workspace(dict(
                name="Test4",
                active=True,
                production=4,
                volume=volume[0].id
            ))
            main_api.apply_configuration()
            print(f"Created workspace '{workspace.name}' with id '{workspace.id}' successfully")
        except ApiException as e:
            print(f"Exception when calling StorageApi->create_workspace: {e}")


def delete_workspace_example():
    with ApiClient(config) as api_client:
        storage_api = StorageApi(api_client)

        workspace_id = 15

        try:
            workspace: Workspace = storage_api.get_workspace(workspace_id)
            storage_api.delete_workspace(workspace_id)
            main_api.apply_configuration()
            print(f"Workspace '{workspace.name}' with id '{workspace.id}' was deleted successfully")
        except ApiException as e:
            print(f"Exception when calling StorageApi->get_workspace: {e}")


create_user_example()
delete_user_example()
create_workspace_example()
delete_workspace_example()
