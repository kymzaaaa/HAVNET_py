class SabatierReactor:
    def __init__(self, hydrogen_store, carbon_dioxide_store, grey_water_store, methane_store, fraction_of_co2):
        self.hydrogen_store = hydrogen_store
        self.carbon_dioxide_store = carbon_dioxide_store
        self.grey_water_store = grey_water_store
        self.methane_store = methane_store
        self.fraction_of_co2 = fraction_of_co2

    def tick(self):
        # Take CO2 from Carbon Dioxide Store
        current_co2_consumed = self.carbon_dioxide_store.current_level * self.fraction_of_co2
        self.carbon_dioxide_store.take(current_co2_consumed)

        # Take H2 from Hydrogen Store
        if self.hydrogen_store.current_level < current_co2_consumed * 4:
            print('not enough hydrogen for sabatier reaction, reaction does not proceed')
        else:
            current_h2_consumed = current_co2_consumed * 4
            self.hydrogen_store.take(current_h2_consumed)

        # Follows stoichiometric ratio: CO2 + 4H2 = CH4 + 2H2O
        self.methane_store.add(current_co2_consumed)
        self.grey_water_store.add(current_co2_consumed * 2)
