import requests

from src.adapters.api.api import APIAdapter


class HistoryAPIAdapter(APIAdapter):

    def __init__(self, api_key, api_secret: str = None):
        super().__init__(api_key, api_secret)
        self.url = "https://mc-api.marketcheck.com/v2/history/car"

    def get_params(self, **kwargs):
        sort_order = kwargs.get("sort_order", "desc")
        page = kwargs.get("page", 1)
        params = {
            "api_key": self.api_key,
            "sort_order": sort_order,
            "page": page,
        }
        return params

    def search(self, **kwargs):
        vin = kwargs.get("vin")
        if not vin:
            raise ValueError("VIN is required for VIN History API search")
        try:
            return requests.get(
                f"{self.url}/{vin}",
                params=self.get_params(**kwargs)
            )
        except requests.RequestException as e:
            raise ValueError(f"Request failed: {e}")
