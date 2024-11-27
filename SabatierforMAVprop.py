class SabatierforMAVprop:
    def __init__(self, environment, h2_source, co2_source, water_output, ch4_output, power_source, external_store_list, habitat_store_list, bpc_store_list, external_store_list_s, habitat_store_list_s, bpc_store_list_s):
        self.environment = environment
        self.co2_consumer_definition = co2_source
        self.h2_consumer_definition = h2_source
        self.power_consumer_definition = power_source
        self.grey_water_producer_definition = water_output
        self.methane_producer_definition = ch4_output
        self.external_store_list = external_store_list
        self.habitat_store_list = habitat_store_list
        self.external_store_list_s = external_store_list_s
        self.habitat_store_list_s = habitat_store_list_s
        self.bpc_store_list = bpc_store_list
        self.bpc_store_list_s = bpc_store_list_s
        self.compressor_error = 0
        self.reactor_error = 0
        self.separator_error = 0
        self.co2_vented = 0
        self.water_vapor_vented = 0
        self.compressor_operation = [0, 0]
        self.compressor_power_consumed = 0
        self.reactor_power_consumed = 0
        self.condensor_power_consumed = 0
        self.reaction_h2_co2_ratio = 3.5
        self.ideal_gas_constant = 8.314
        self.reactor_water_conversion_efficiency = 0.9

    def tick(self, track, water_leak):
        if track:
            e_vec_before = [store.current_level for store in self.external_store_list]
            h_vec_before = [store.current_level for store in self.habitat_store_list]
            bpc_vec_before = [store.current_level for store in self.bpc_store_list]

        if not self.compressor_error and not self.reactor_error and not self.separator_error:
            if self.h2_consumer_definition.current_level > 0:
                h2_moles_to_react = self.h2_consumer_definition.take(self.h2_consumer_definition.current_level)
                co2_moles_to_react = self.co2_consumer_definition.take(1 / self.reaction_h2_co2_ratio * h2_moles_to_react)

                current_h2o_produced = self.grey_water_producer_definition.add((h2_moles_to_react / 2 * self.reactor_water_conversion_efficiency * (2 * 1.008 + 15.999) / 1000) * (1 - water_leak))
                self.water_vapor_vented += h2_moles_to_react / 2 * (1 - self.reactor_water_conversion_efficiency)
                self.co2_vented += co2_moles_to_react - h2_moles_to_react / 4
                self.methane_producer_definition.add(h2_moles_to_react / 4)
        else:
            current_h2o_produced = 0
            return current_h2o_produced

        if track:
            e_vec_after = [store.current_level for store in self.external_store_list]
            h_vec_after = [store.current_level for store in self.habitat_store_list]
            bpc_vec_after = [store.current_level for store in self.bpc_store_list]

            # Calculate changes
            delta = [after - before for after, before in zip(e_vec_after + h_vec_after + bpc_vec_after, e_vec_before + h_vec_before + bpc_vec_before)]
            resource_changed = [name for name, d in zip(self.external_store_list_s + self.habitat_store_list_s + self.bpc_store_list_s, delta) if d != 0]
            quantity_changed = [d for d in delta if d != 0]

            # Here should be the logic to record the changes, similar to the file writing in MATLAB
            # But for now, just simulate recording
            print("Changes recorded.")

        return current_h2o_produced
