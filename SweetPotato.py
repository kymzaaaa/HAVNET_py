class SweetPotato:
    """
    Implementation of a Sweet Potato crop model with specified characteristics.
    """
    
    def __init__(self):
        self.name = 'Sweet Potato'
        self.type = 'Planophile'
        self.ta_initial_value = 1200
        self.initial_PPF_value = 600  # adjusted value
        self.initial_CO2_value = 1200
        self.carbon_use_efficiency_24 = 0.625
        self.bcf = 0.44  # Updated according to BVAD Table 4.2.29
        self.CUEmax = 0.625
        self.CUEmin = 0
        self.photoperiod = 12  # days
        self.nominal_photoperiod = 18  # days
        self.time_at_organ_formation = 33  # days
        self.n = 1.5
        self.CQYMin = 0
        self.time_at_canopy_senescence = 121  # days
        self.time_at_crop_maturity = 120  # days
        self.opf = 1.02
        self.fraction_of_edible_biomass = 1
        self.calories_per_kilogram = (1 - 0.7728) * 1000 * (4 * 201.2 + 4 * 15.7 + 9 * 0.5) / (201.2 + 15.7 + 0.5)
        self.edible_fresh_basis_water_content = 0.7728
        self.inedible_fresh_basis_water_content = 0.9
        self.light_cycle_temperature = 28  # Celsius
        
        # Initialize Canopy Closure Constants
        self.canopy_closure_constants = [
            1.2070E6, 4.9484E3, 0, 0, 0, 0, 0,
            4.2978, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 4.0109E-7, 0, 2.0193E-12, 0
        ]
        
        # Initialize Canopy Quantum Yield Constants
        self.canopy_quantum_yield_constants = [
            0, 0, 0, 0, 0, 0, 0,
            3.9317E-2, 5.6741E-5, -2.1797E-8, 0, 0,
            -1.3836E-5, -6.3397E-9, 0, 0,
            0, 0, -1.3464E-11, 7.7362E-15, 0, 0,
            0, 0, 0
        ]

        # Carbohydrate, protein, and fat fractions based on REF
        self.carbohydrate_fraction_of_dry_mass = 201.2 / (201.2 + 15.7 + 0.5)
        self.protein_fraction_of_dry_mass = 15.7 / (201.2 + 15.7 + 0.5)
        self.fat_fraction_of_dry_mass = 0.5 / (201.2 + 15.7 + 0.5)

# Example instantiation
sweet_potato = SweetPotato()
