class CO2Injector:
    def __init__(self, environment, co2_store, target_molar_fraction, co2_source, external_store_list, habitat_store_list, bpc_store_list, external_store_list_s, habitat_store_list_s, bpc_store_list_s):
        self.Environment = environment
        self.CO2Store = co2_store
        self.TargetMolarFraction = target_molar_fraction
        self.CO2Source = co2_source
        self.external_store_list_s = external_store_list_s
        self.habitat_store_list_s = habitat_store_list_s
        self.external_store_list = external_store_list
        self.habitat_store_list = habitat_store_list
        self.BPCStoreList = bpc_store_list
        self.BPCStoreList_s = bpc_store_list_s

    def tick(self, track):
        co2_injected = 0

        if track:
            e_vec_before = [store.current_level for store in self.external_store_list]
            h_vec_before = [store.current_level for store in self.habitat_store_list]
            bpc_vec_before = [store.current_level for store in self.BPCStoreList]

        current_co2_percentage = self.Environment.CO2Percentage
        total_moles = self.Environment.totalMoles

        if current_co2_percentage < self.TargetMolarFraction:
            co2_to_inject = (self.TargetMolarFraction * total_moles - self.CO2Store.current_level) / (1 - self.TargetMolarFraction)
            self.CO2Source.take(co2_to_inject)
            co2_injected = self.CO2Store.add(co2_to_inject)

        if track:
            e_vec_after = [store.current_level for store in self.external_store_list]
            h_vec_after = [store.current_level for store in self.habitat_store_list]
            bpc_vec_after = [store.current_level for store in self.BPCStoreList]

            delta = [(after - before) for before, after in zip(e_vec_before + h_vec_before + bpc_vec_before, e_vec_after + h_vec_after + bpc_vec_after)]
            resource_list = self.external_store_list_s + self.habitat_store_list_s + self.BPCStoreList_s
            resource_changes = [(resource, change) for resource, change in zip(resource_list, delta) if change != 0]
            
            # Placeholder for logging or further action
            print(f"Changes tracked: {resource_changes}")

        return co2_injected

# Example of related StoreImpl class
class StoreImpl:
    def __init__(self, name, type, current_level=0):
        self.name = name
        self.type = type
        self.current_level = current_level
    
    def take(self, moles):
        taken = min(moles, self.current_level)
        self.current_level -= taken
        return taken

    def add(self, moles):
        self.current_level += moles
        return moles

# Example of a simplified Environment class
class Environment:
    def __init__(self, co2_percentage, total_moles):
        self.co2_percentage = co2_percentage
        self.total_moles = total_moles

    @property
    def CO2Percentage(self):
        return self.co2_percentage

    @property
    def totalMoles(self):
        return self.total_moles
