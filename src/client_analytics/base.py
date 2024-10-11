from typing import Dict, Any


class BaseAnalyticsClient:
    def __init__(self, config: Dict[str, Any], **kwargs):
        self.config = config
        self._client = None
        self._kwargs = kwargs

