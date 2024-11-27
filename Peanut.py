class Peanut:
    def __init__(self):
        self.name = 'Peanut'
        self.type = 'Legume'
        self.ta_initial_value = 1200
        self.initial_ppf_value = 600
        self.initial_co2_value = 1200
        self.bcf = 0.5
        self.cuemax = 0.65
        self.cuemin = 0.3
        self.photoperiod = 12
        self.nominal_photoperiod = 12
        self.time_at_organ_formation = 49
        self.n = 2
        self.cqy_min = 0.02
        self.time_at_canopy_senescence = 65
        self.time_at_crop_maturity = 110
        self.opf = 1.19
        self.fraction_of_edible_biomass = 0.49
        self.calories_per_kilogram = (1 - 0.0639) * 1000 * (4 * 158.2 + 4 * 261.5 + 9 * 496) / (158.2 + 261.5 + 496)
        self.edible_fresh_basis_water_content = 0.0639
        self.inedible_fresh_basis_water_content = 0.9
        self.light_cycle_temperature = 26
        self.carbohydrate_fraction_of_dry_mass = 158.2 / (158.2 + 261.5 + 496)
        self.protein_fraction_of_dry_mass = 261.5 / (158.2 + 261.5 + 496)
        self.fat_fraction_of_dry_mass = 496 / (158.2 + 261.5 + 496)

        # Initialize Canopy Closure Constants
        self.canopy_closure_constants = [0] * 25
        self.canopy_closure_constants[1] = 3.7487E6
        self.canopy_closure_constants[2] = 2.9200E3
        self.canopy_closure_constants[5] = 9.4008E-8
        self.canopy_closure_constants[6] = -1.8840E4
        self.canopy_closure_constants[7] = 23.912
        self.canopy_closure_constants[11] = 51.256
        self.canopy_closure_constants[16] = -0.05963
        self.canopy_closure_constants[17] = 5.5180E-6
        self.canopy_closure_constants[21] = 2.5969E-5

        # Initialize Canopy Quantum Yield Constants
        self.canopy_quantum_yield_constants = [0] * 25
        self.canopy_quantum_yield_constants[7] = 4.1513E-2
        self.canopy_quantum_yield_constants[8] = 5.1157E-5
        self.canopy_quantum_yield_constants[9] = -2.0992E-8
        self.canopy_quantum_yield_constants[13] = 4.0864E-8
        self.canopy_quantum_yield_constants[17] = -2.1582E-8
        self.canopy_quantum_yield_constants[18] = -1.0468E-10
        self.canopy_quantum_yield_constants[23] = 4.8541E-14
        self.canopy_quantum_yield_constants[25] = 3.9259E-21

# Note: This Python class assumes the presence of equivalent functionality and environmental setup as the MATLAB version.
