from httpx import Client


def officer_client() -> Client:
    client = Client(
        headers={
            'Content-Type': 'application/json',
        },
        base_url='https://valorant-api.com/v1'
    )
    return client
