class BioMatter:
    def __init__(self, bio_type, mass, inedible_fraction, edible_water_content, inedible_water_content):
        self.Type = bio_type
        self.Mass = mass
        self.InedibleFraction = inedible_fraction
        self.EdibleWaterContent = edible_water_content
        self.InedibleWaterContent = inedible_water_content

class BiomassStoreImpl:
    def __init__(self, initial_capacity=None, initial_food_items=None):
        self.current_capacity = initial_capacity
        self.biomatter_items = []
        self.contents = []
        self.current_level = 0
        self.overflow = 0
        self.resupply_frequency = 0
        self.resupply_amount = 0
        
        if initial_capacity is not None:
            self.current_capacity = initial_capacity
            if initial_food_items is not None:
                if not all(isinstance(item, BioMatter) for item in initial_food_items):
                    raise ValueError('initial_food_items must be of type "BioMatter"')
                for item in initial_food_items:
                    self.current_level += item.Mass
                    if self.current_level > self.current_capacity:
                        print('Warning: total contents of initial_food_items exceeds declared capacity of store')
                        break
                    self.biomatter_items.append(item)
                    self.contents.append(item.Type.Name)
    
    def take(self, mass_requested, resource_management_definition=None):
        collected_mass = 0
        items_to_take = []
        items_to_delete = []
        
        if mass_requested < 0:
            return []
        
        final_mass_requested = mass_requested
        if resource_management_definition is not None:
            final_mass_requested = min(mass_requested, resource_management_definition.DesiredFlowRate,
                                       resource_management_definition.MaxFlowRate)
        
        for i, item in enumerate(self.biomatter_items):
            mass_still_needed = final_mass_requested - collected_mass
            if item.Mass < mass_still_needed:
                items_to_take.append(item)
                items_to_delete.append(i)
                collected_mass += item.Mass
            else:
                partial_mass = item.Mass - mass_still_needed
                partial_item = BioMatter(item.Type, mass_still_needed, item.InedibleFraction,
                                         item.EdibleWaterContent * (mass_still_needed / item.Mass),
                                         item.InedibleWaterContent * (mass_still_needed / item.Mass))
                items_to_take.append(partial_item)
                item.Mass = partial_mass
                collected_mass += mass_still_needed
            
            if collected_mass >= final_mass_requested:
                break
        
        for index in sorted(items_to_delete, reverse=True):
            del self.biomatter_items[index]
            del self.contents[index]
        
        self.current_level -= collected_mass
        return items_to_take

    def add(self, biomatter_requested, resource_management_definition=None):
        final_biomatter_requested = biomatter_requested
        if resource_management_definition is not None:
            finalflowrate = min(biomatter_requested.Mass, resource_management_definition.DesiredFlowRate,
                                resource_management_definition.MaxFlowRate)
            if finalflowrate != biomatter_requested.Mass:
                final_biomatter_requested = BioMatter(biomatter_requested.Type, finalflowrate,
                                                      biomatter_requested.InedibleFraction,
                                                      biomatter_requested.EdibleWaterContent * (finalflowrate / biomatter_requested.Mass),
                                                      biomatter_requested.InedibleWaterContent * (finalflowrate / biomatter_requested.Mass))
        
        if final_biomatter_requested.Mass + self.current_level > self.current_capacity:
            actually_added = self.current_capacity - self.current_level
            self.overflow += final_biomatter_requested.Mass - actually_added
        else:
            actually_added = final_biomatter_requested.Mass
        
        self.current_level += actually_added
        self.biomatter_items.append(final_biomatter_requested)
        self.contents.append(final_biomatter_requested.Type.Name)
        return actually_added

    def sort_contents(self):
        if len(self.biomatter_items) <= 1:
            return
        
        sorted_items = sorted(self.biomatter_items, key=lambda x: x.Type.Name)
        unique_types = sorted(set(item.Type.Name for item in sorted_items))
        self.contents = unique_types
        
        aggregated_items = []
        current_type = None
        aggregated_mass = 0
        aggregated_inedible_fraction = 0
        aggregated_edible_water_content = 0
        aggregated_inedible_water_content = 0
        
        for item in sorted_items:
            if item.Type.Name != current_type:
                if current_type is not None:
                    new_item = BioMatter(current_type, aggregated_mass, aggregated_inedible_fraction,
                                         aggregated_edible_water_content, aggregated_inedible_water_content)
                    aggregated_items.append(new_item)
                current_type = item.Type.Name
                aggregated_mass = 0
                aggregated_inedible_fraction = 0
                aggregated_edible_water_content = 0
                aggregated_inedible_water_content = 0
            
            aggregated_mass += item.Mass
            aggregated_inedible_fraction = (aggregated_inedible_fraction + item.InedibleFraction) / 2  # Simplified average
            aggregated_edible_water_content += item.EdibleWaterContent
            aggregated_inedible_water_content += item.InedibleWaterContent
        
        # Add last aggregated item
        if current_type is not None:
            new_item = BioMatter(current_type, aggregated_mass, aggregated_inedible_fraction,
                                 aggregated_edible_water_content, aggregated_inedible_water_content)
            aggregated_items.append(new_item)
        
        self.biomatter_items = aggregated_items

