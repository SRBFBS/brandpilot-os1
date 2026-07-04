import requests

from brandpilot.config import settings


class BaserowClient:
    def __init__(self):
        self.base_url = settings.baserow_url.rstrip("/")

        self.headers = {
            "Authorization": f"Token {settings.baserow_token}",
            "Content-Type": "application/json",
        }

    def test_connection(self):
        url = (
            f"{self.base_url}/api/database/rows/table/1058553/"
            "?user_field_names=true"
        )

        print("\n===== BrandPilot Debug =====")
        print(f"URL: {url}")

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30,
        )

        print(f"Status: {response.status_code}")

        try:
            print(response.json())
        except Exception:
            print(response.text)

        if response.status_code == 200:
            return True, response.json()

        return False, response.text