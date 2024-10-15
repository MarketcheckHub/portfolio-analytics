from abc import ABC, abstractmethod


class BaseAnalytics(ABC):

    def __init__(self, input_fn, client, **kwargs):
        self._input_fn = input_fn
        self._client = client
        self._kwargs = kwargs

    @abstractmethod
    def perform_analytics(self):
        pass

