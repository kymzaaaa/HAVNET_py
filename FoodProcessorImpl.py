class FoodProcessorImpl:
    def __init__(self, environment, external_store_list, habitat_store_list, bpc_store_list, external_store_list_s, habitat_store_list_s, bpc_store_list_s):
        self.Environment = environment
        self.BiomassConsumerDefinition = ResourceUseDefinitionImpl()
        self.PowerConsumerDefinition = ResourceUseDefinitionImpl()
        self.FoodProducerDefinition = ResourceUseDefinitionImpl()
        self.WaterProducerDefinition = ResourceUseDefinitionImpl()
        self.DryWasteProducerDefinition = ResourceUseDefinitionImpl()
        self.external_store_list_s = external_store_list_s
        self.habitat_store_list_s = habitat_store_list_s
        self.external_store_list = external_store_list
        self.habitat_store_list = habitat_store_list
        self.BPCStoreList = bpc_store_list
        self.BPCStoreList_s = bpc_store_list_s
        self.has_enough_power = False
        self.has_enough_biomass = False
        self.mass_consumed = 0
        self.current_power_consumed = 0
        self.current_food_produced = 0
        self.biomatter_consumed = []
        self.biomass_needed = 200
        self.power_needed = 100
        self.production_rate = 1

    def tick(self, track, water_leak):
        e_vec_before = [store.current_level for store in self.external_store_list]
        h_vec_before = [store.current_level for store in self.habitat_store_list]
        bpc_vec_before = [store.current_level for store in self.BPCStoreList]

        self.current_power_consumed = self.PowerConsumerDefinition.resource_store.take(self.power_needed, self.PowerConsumerDefinition)
        if self.current_power_consumed >= self.power_needed:
            self.biomatter_consumed = self.BiomassConsumerDefinition.resource_store.take(self.biomass_needed, self.BiomassConsumerDefinition)
            if not self.biomatter_consumed:
                return

            food_matter_array = [FoodMatter(bio.Type, bio.Mass * (1 - bio.InedibleFraction), bio.EdibleWaterContent) for bio in self.biomatter_consumed if bio.InedibleFraction > 0]
            total_biomass_consumed = sum(bio.Mass for bio in self.biomatter_consumed)
            current_water_produced = sum(bio.InedibleWaterContent for bio in self.biomatter_consumed)
            self.current_food_produced = sum(food.Mass for food in food_matter_array)

            self.FoodProducerDefinition.resource_store.add(food_matter_array, self.FoodProducerDefinition)
            self.DryWasteProducerDefinition.resource_store.add(total_biomass_consumed - self.current_food_produced, self.DryWasteProducerDefinition)
            self.WaterProducerDefinition.resource_store.add(current_water_produced * (1 - water_leak), self.WaterProducerDefinition)

        if track == 1:
            e_vec_after = [store.current_level for store in self.external_store_list]
            h_vec_after = [store.current_level for store in self.habitat_store_list]
            bpc_vec_after = [store.current_level for store in self.BPCStoreList]
            delta = [after - before for before, after in zip(e_vec_before + h_vec_before + bpc_vec_before, e_vec_after + h_vec_after + bpc_vec_after)]
            resource_list = self.external_store_list_s + self.habitat_store_list_s + self.BPCStoreList_s
            index_mask = [i for i, x in enumerate(delta) if x != 0]
            resource_changed = [resource_list[i] for i in index_mask]
            quantity = [delta[i] for i in index_mask]
            tick = [self.Environment.tick_count for _ in quantity]
            # Assuming a function to write to file or handle the delta tracking output appropriately
            log_changes(tick, resource_changed, quantity)

def log_changes(tick, resources, quantities):
    with open('d:BPC - FoodProcessor.txt', 'a') as f:
        for t, resource, quantity in zip(tick, resources, quantities):
            f.write(f"{t}|{resource}|{quantity}\n")
