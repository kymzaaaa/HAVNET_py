class Tomato:
    """
    Implementation of a Tomato crop model with specified characteristics.
    """
    
    def __init__(self):
        self.name = 'Tomato'
        self.type = 'Planophile'
        self.ta_initial_value = 1200
        self.initial_PPF_value = 500  # adjusted value
        self.initial_CO2_value = 1200
        self.carbon_use_efficiency_24 = 0.65
        self.bcf = 0.42  # Updated according to BVAD Table 4.2.29
        self.CUEmax = 0.65
        self.CUEmin = 0
        self.photoperiod = 12  # days
        self.nominal_photoperiod = 12  # days
        self.time_at_organ_formation = 41  # days
        self.n = 2.5
        self.CQYMin = 0.01
        self.time_at_canopy_senescence = 56  # days
        self.time_at_crop_maturity = 80  # days
        self.opf = 1.09
        self.fraction_of_edible_biomass = 0.7
        self.calories_per_kilogram = (1 - 0.9452) * 1000 * (4 * 38.9 + 4 * 8.8 + 9 * 2) / (38.9 + 8.8 + 2)
        self.edible_fresh_basis_water_content = 0.9452
        self.inedible_fresh_basis_water_content = 0.9
        self.light_cycle_temperature = 26  # Celsius
        
        # Initialize Canopy Closure Constants
        self.canopy_closure_constants = [
            6.2774E5, 3.1724E3, 0, 0, 0, 0, 24.281,
            0, 0, 0, 0.44686, 5.6276E-3, 0, 0, 0,
            0, -3.0690E-6, 0, 0, 0, 0, 0, 0, 0, 0
        ]
        
        # Initialize Canopy Quantum Yield Constants
        self.canopy_quantum_yield_constants = [
            0, 0, 0, 0, 0, 0, 4.0061E-2,
            5.688E-5, -2.2598E-8, 0, 0,
            0, -1.182E-8, 5.0264E-12, 0,
            0, -7.1241E-9, 0, 0, 0, 0, 0, 0, 0, 0
        ]

        # Nutrient fractions based on REF
        self.carbohydrate_fraction_of_dry_mass = 38.9 / (38.9 + 8.8 + 2)
        self.protein_fraction_of_dry_mass = 8.8 / (38.9 + 8.8 + 2)
        self.fat_fraction_of_dry_mass = 2 / (38.9 + 8.8 + 2)

# Example instantiation
tomato = Tomato()
