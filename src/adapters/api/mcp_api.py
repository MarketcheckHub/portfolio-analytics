from enum import Enum

import requests

from src.adapters.api.api import APIAdapter


class MarketcheckPriceAPIAdapter(APIAdapter):
    class Level(Enum):
        BASIC = "basic"
        PREMIUM = "premium"
        PREMIUM_PLUS = "premium_plus"

    def __init__(self, api_key, api_secret: str = None):
        super().__init__(api_key, api_secret)
        self.url = "https://mc-api.marketcheck.com/v2/predict/car/us/marketcheck_price"

    def get_params(self, level: Level, **kwargs):
        vin = kwargs.get("vin")
        miles = kwargs.get("miles")
        dealer_type = kwargs.get("dealer_type")
        zipcode = kwargs.get("zip")
        params = {
            "api_key": self.api_key,
            "vin": vin,
            "miles": miles,
            "dealer_type": dealer_type,
            "zip": zipcode
        }
        if level == self.Level.PREMIUM:
            state = kwargs.get("state")
            if not state:
                raise ValueError("State is required for PREMIUM search level")
            params["state"] = state

        elif level == self.Level.PREMIUM_PLUS:
            state = kwargs.get("state")
            city = kwargs.get("city")
            if not state or not city:
                raise ValueError("State and city are required for PREMIUM_PLUS search level")
            params["state"] = state
            params["city"] = city

        elif level == self.Level.BASIC:
            is_certified = kwargs.get("is_certified")
            if not is_certified:
                raise ValueError("is_certified is required for BASIC search level")
            params["is_certified"] = is_certified

        return params

    def search(self, **kwargs):
        level = kwargs.get("level", self.Level.BASIC)
        url_suffix = ""
        if level == self.Level.PREMIUM:
            url_suffix = "/comparables"
        elif level == self.Level.PREMIUM_PLUS:
            url_suffix = "/comparables/decode"
        try:
            return requests.get(
                f"{self.url}{url_suffix}",
                params=self.get_params(level, **kwargs)
            )
        except requests.RequestException as e:
            raise e
