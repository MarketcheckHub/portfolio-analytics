class APIAdapter:
    def __init__(self, api_key: str, api_secret: str = None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.url = "https://mc-api.marketcheck.com/v2"

    def search(self, **kwargs):
        pass
