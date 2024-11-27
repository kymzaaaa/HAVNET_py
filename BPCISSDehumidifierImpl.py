class BPCISSDehumidifierImpl:
    """
    BPCISSDehumidifierImpl - A class to simulate a dehumidifier similar to the ISS's CCAA system.
    """
    
    def __init__(self, environment, condensate_output, power_source, external_store_list, habitat_store_list, bpc_store_list, external_store_list_s, habitat_store_list_s, bpc_store_list_s):
        self.Environment = environment
        self.DirtyWaterOutput = condensate_output
        self.PowerSource = power_source
        self.external_store_list_s = external_store_list_s
        self.habitat_store_list_s = habitat_store_list_s
        self.external_store_list = external_store_list
        self.habitat_store_list = habitat_store_list
        self.BPCStoreList = bpc_store_list
        self.BPCStoreList_s = bpc_store_list_s
        
        self.Units = 10
        self.Error = 0
        self.TotalEnvironmentalCondensedWaterRemoved = 0
        self.PowerConsumed = 0
        
        # Private properties
        self.saturated_vapor_pressure = 2.837
        self.target_relative_humidity = 0.55
        self.relative_humidity_bounding_box = 0.1
        self.ideal_gas_constant = 8.3145
        self.max_condensate_extracted = 1.45 * 1E3 / (2 * 1.008 + 15.999)
        self.max_power_draw = 705
        self.min_power_draw = 469
        self.max_airflow_in_L = 11866 * 60
        self.min_airflow_in_L = 1444 * 60

    def tick(self, track, water_leak):
        if track == 1:
            e_vec_before = [store.current_level for store in self.external_store_list]
            h_vec_before = [store.current_level for store in self.habitat_store_list]
            bpc_vec_before = [store.current_level for store in self.BPCStoreList]

        self.PowerConsumed = 0
        vapor_moles_removed = 0

        if self.Error == 0:
            # Compute vapor moles that need to be removed
            vapor_pressure_current = self.Environment.vapor_percentage * self.Environment.pressure
            target_pressure_low = self.saturated_vapor_pressure * (self.target_relative_humidity - self.relative_humidity_bounding_box)
            target_pressure_high = self.saturated_vapor_pressure * (self.target_relative_humidity + self.relative_humidity_bounding_box)
            
            if vapor_pressure_current > target_pressure_high:
                vapor_moles_needed_to_remove = (self.Environment.vapor_store.current_level - 
                                                (target_pressure_low * self.Environment.volume / 
                                                 (self.ideal_gas_constant * (273.15 + self.Environment.temperature))))
            else:
                vapor_moles_needed_to_remove = 0
            
            power_to_consume = self.calculate_power(vapor_moles_needed_to_remove)
            current_power_consumed = self.PowerSource.take(power_to_consume)
            self.PowerConsumed = current_power_consumed

            if current_power_consumed < power_to_consume:
                self.PowerSource.add(current_power_consumed)
                print('CCAA shut down due to inadequate power input.')
                self.Error = 1
                return 0
            
            vapor_moles_to_take = max(vapor_moles_needed_to_remove, 0)
            vapor_moles_removed = self.Environment.vapor_store.take(vapor_moles_to_take)
            
            # Water output calculation and addition to the dirty water output
            self.DirtyWaterOutput.add(vapor_moles_removed * 18.01524 / 1000 * (1 - water_leak))

        if track == 1:
            e_vec_after = [store.current_level for store in self.external_store_list]
            h_vec_after = [store.current_level for store in self.habitat_store_list]
            bpc_vec_after = [store.current_level for store in self.BPCStoreList]
            
            self.track_changes(e_vec_before, h_vec_before, bpc_vec_before, e_vec_after, h_vec_after, bpc_vec_after)

        return vapor_moles_removed

    def calculate_power(self, vapor_moles_needed_to_remove):
        if vapor_moles_needed_to_remove >= (self.max_condensate_extracted * self.Units):
            return self.max_power_draw * self.Units
        else:
            return (self.Units * (self.max_power_draw - self.min_power_draw) / (self.Units * self.max_condensate_extracted) *
                    vapor_moles_needed_to_remove + self.Units * self.min_power_draw)

    def track_changes(self, e_vec_before, h_vec_before, bpc_vec_before, e_vec_after, h_vec_after, bpc_vec_after):
        deltas = [after - before for before, after in zip(e_vec_before + h_vec_before + bpc_vec_before,
                                                          e_vec_after + h_vec_after + bpc_vec_after)]
        resource_list = self.external_store_list_s + self.habitat_store_list_s + self.BPCStoreList_s
        resource_changes = [(resource, delta) for resource, delta in zip(resource_list, deltas) if delta != 0]
        
        # Assuming file I/O functions and logging here; replaced with print statements for simulation
        for tick_count, (resource, delta) in enumerate(resource_changes, start=1):
            print(f'Tick: {tick_count}, Resource: {resource}, Change: {delta}')

