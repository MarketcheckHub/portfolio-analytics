import csv
import os
from typing import Dict, Any

from src.adapters.api.history_api import HistoryAPIAdapter
from src.client_analytics.base import BaseAnalytics
from src.adapters.api.mcp_api import MarketcheckPriceAPIAdapter

API_KEY = os.getenv("API_KEY_DEV")


class ADESAAnalytics(BaseAnalytics):

    def __init__(self, input_fn, client, **kwargs):
        super().__init__(input_fn, client, **kwargs)
        self._client = client
        self._input_fn = input_fn
        self._kwargs = kwargs
        self.mcp_adapter = MarketcheckPriceAPIAdapter(api_key=API_KEY)
        self.history_adapter = HistoryAPIAdapter(api_key=API_KEY)

    def perform_analytics(self):
        in_file = open(self._input_fn, mode='r')
        csv_reader = csv.DictReader(in_file)
        for row in csv_reader:
            vin = row.get("vin")
            if not vin:
                raise ValueError("VIN is required for VIN History API search")
            try:
                response = self.history_adapter.search(vin=vin)
                print(response.status_code)
                print(response.json())
            except Exception as e:
                print(f"Request failed: {e}")
