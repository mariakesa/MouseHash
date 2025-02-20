class ProbeLocationLoader:
    def load(self):
        return "Probe locations loaded"
    
class SpikeDataLoader:
    def load(self):
        return "Spike data loaded"
    
class BehaviorDataLoader:
    def load(self):
        return "Behavior data loaded"

class DataLoaderFactory:
    @staticmethod
    def get_loader(dataset_type):
        loaders = {
            "probe_locations": ProbeLocationLoader(),
            "spike_data": SpikeDataLoader(),
            "behavior": BehaviorDataLoader()
        }
        return loaders.get(dataset_type, None)

# Usage
probe_loader = DataLoaderFactory.get_loader("probe_locations")
probe_data = probe_loader.load()