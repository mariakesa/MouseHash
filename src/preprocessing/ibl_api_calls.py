from abc import ABC, abstractmethod
from one.api import ONE

class IBLSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IBLSingleton, cls).__new__(cls)
            ONE.setup(base_url='https://openalyx.internationalbrainlab.org', silent=True)
            cls._instance.one= ONE(password='international')
        return cls._instance

class IBLApiLoader(ABC):
    def __init__(self, API_singleton):
        self.ibl_api = API_singleton

    @abstractmethod
    def load(self):
        pass
    def get_eids(self):
        eids = self.ibl_api.search(dataset='channels.mlapdv')
        return eids

class ProbeLocationLoader(IBLApiLoader):
    
    def load(self):
        eids=self.get_eids()
    
class SpikeDataLoader(IBLApiLoader):

    def load(self):
        return "Spike data loaded"
    
class BehaviorDataLoader(IBLApiLoader):

    def load(self):
        return "Behavior data loaded"

class DataLoaderFactory:
    @staticmethod
    def get_loader(dataset_type, ibl_api):
        loaders = {
            "probe_locations": ProbeLocationLoader(ibl_api),
            "spike_data": SpikeDataLoader(ibl_api),
            "behavior": BehaviorDataLoader(ibl_api)
        }
        return loaders.get(dataset_type, None)

# Usage
ibl_api = IBLSingleton().one
probe_loader = DataLoaderFactory.get_loader("probe_locations", ibl_api)
probe_data = probe_loader.load()