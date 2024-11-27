import math

class StoreImpl:
    def __init__(self, name, type, current_capacity=None, current_level=None):
        self.name = name
        self.type = type
        self.current_capacity = current_capacity
        self.current_level = current_level if current_level is not None else 0

    def take(self, moles):
        taken = min(moles, self.current_level)
        self.current_level -= taken
        return taken

    def add(self, moles):
        self.current_level += moles
        self.current_capacity = max(self.current_capacity, self.current_level)
    
    def tick(self, tick_count):
        # Implement tick behavior if necessary, such as resupply or decay
        return self

class BPCSimEnvironmentImpl:
    def __init__(self, name, pressure, volume, o2_percentage, co2_percentage, nitrogen_percentage, water_percentage,
                 other_percentage, leak_percentage, potable_water_store, grey_water_store, dirty_water_store,
                 dry_waste_store, food_store, max_o2_fraction, solid_waste_store):
        self.name = name
        self.volume = volume
        self.temperature = 23
        self.leakage_percentage = leak_percentage
        self.tickcount = 0

        # Define the stores
        self.O2Store = StoreImpl('O2', 'Environmental', self.calculate_moles(o2_percentage, pressure, volume), self.calculate_moles(o2_percentage, pressure, volume))
        self.CO2Store = StoreImpl('CO2', 'Environmental', self.calculate_moles(co2_percentage, pressure, volume), self.calculate_moles(co2_percentage, pressure, volume))
        self.NitrogenStore = StoreImpl('N2', 'Environmental', self.calculate_moles(nitrogen_percentage, pressure, volume), self.calculate_moles(nitrogen_percentage, pressure, volume))
        self.VaporStore = StoreImpl('H2O Vapor', 'Environmental', self.calculate_moles(water_percentage, pressure, volume), self.calculate_moles(water_percentage, pressure, volume))
        self.OtherStore = StoreImpl('Other', 'Environmental', self.calculate_moles(other_percentage, pressure, volume), self.calculate_moles(other_percentage, pressure, volume))
        
        self.PotableWaterStore = potable_water_store
        self.GreyWaterStore = grey_water_store
        self.DirtyWaterStore = dirty_water_store
        self.DryWasteStore = dry_waste_store
        self.FoodStore = food_store
        self.SolidWasteStore = solid_waste_store

        self.DangerousOxygenThreshold = max_o2_fraction
        self.ideal_gas_constant = 8.314  # J/K/mol

    def calculate_moles(self, fractional_percentage, total_pressure, volume):
        return (fractional_percentage * total_pressure * volume) / (self.ideal_gas_constant * (self.temperature + 273.15))

    def perform_leak(self):
        for store in [self.O2Store, self.CO2Store, self.NitrogenStore, self.VaporStore, self.OtherStore]:
            store.take(store.current_level * self.leakage_percentage / 100)

    def tick(self, track):
        if track == 1:
            gas_before_vec = [store.current_level for store in [self.O2Store, self.CO2Store, self.NitrogenStore, self.VaporStore, self.OtherStore]]

        self.tickcount += 1
        self.perform_leak()

        if track == 1:
            gas_after_vec = [store.current_level for store in [self.O2Store, self.CO2Store, self.NitrogenStore, self.VaporStore, self.OtherStore]]
            print("Track gas changes:", list(zip(gas_before_vec, gas_after_vec)))

    @property
    def pressure(self):
        total_moles = sum([store.current_level for store in [self.O2Store, self.CO2Store, self.NitrogenStore, self.VaporStore, self.OtherStore]])
        return total_moles * self.ideal_gas_constant * (self.temperature + 273.15) / self.volume

    @property
    def O2Percentage(self):
        total_moles = sum([store.current_level for store in [self.O2Store, self.CO2Store, self.NitrogenStore, self.VaporStore, self.OtherStore]])
        return self.O2Store.current_level / total_moles if total_moles else 0
