class Soybean:
    """
    Soybean class represents soybean crops with properties relevant to their growth and environment interactions.
    """
    
    def __init__(self):
        self.name = 'Soybean'
        self.type = 'Legume'
        self.ta_initial_value = 1200
        self.initial_PPF_value = 800
        self.initial_CO2_value = 1200
        self.BCF = 0.46
        self.CUEmax = 0.65
        self.CUEmin = 0.3
        self.photoperiod = 12
        self.nominal_photoperiod = 12
        self.time_at_organ_formation = 46
        self.N = 1.5
        self.CQY_min = 0.02
        self.time_at_canopy_senescence = 48
        self.time_at_crop_maturity = 86
        self.OPF = 1.16
        self.fraction_of_edible_biomass = 0.95
        self.calories_per_kilogram = (1 - 0.0854) * 1000 * (4*301.6 + 4*364.9 + 9*199.4) / (301.6 + 364.9 + 199.4)
        self.edible_fresh_basis_water_content = 0.0854
        self.inedible_fresh_basis_water_content = 0.9
        self.light_cycle_temperature = 26
        self.carbohydrate_fraction_of_dry_mass = 301.6 / (301.6 + 364.9 + 199.4)
        self.protein_fraction_of_dry_mass = 364.9 / (301.6 + 364.9 + 199.4)
        self.fat_fraction_of_dry_mass = 199.4 / (301.6 + 364.9 + 199.4)
        
        self.canopy_closure_constants = [
            6.7978E6, -4.3658E3, 1.5573, 0, 0, -4.326E4,
            33.959, 0, 0, 0, 112.63, 0,
            0, 0, -4.911E-9, -0.13637, 0, 0,
            0, 0, 6.6918E-5, -2.1367E-8, 1.5467E-11, 0,
            0
        ]
        
        self.canopy_quantum_yield_constants = [
            0, 0, 0, 0, 0, 0, 0,
            4.1513E-2, 5.1157E-5, -2.0992E-8, 0, 0, 0,
            4.0864E-8, 0, 0, -2.1582E-8, -1.0468E-10, 0,
            0, 0, 0, 4.8541E-14, 0, 3.9259E-21
        ]

# You can now create an instance of Soybean and access its properties as needed in your simulation or calculations.
