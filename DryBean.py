class DryBean:
    def __init__(self):
        self.Name = 'Dry Bean'
        self.Type = 'Legume'
        self.taInitialValue = 1200
        self.initialPPFValue = 600
        self.initialCO2Value = 1200
        self.BCF = 0.45
        self.CUEmax = 0.65
        self.CUEmin = 0.5
        self.Photoperiod = 18
        self.NominalPhotoperiod = 12
        self.TimeAtOrganFormation = 40
        self.N = 2
        self.CQYMin = 0.02
        self.TimeAtCanopySenescence = 42
        self.TimeAtCropMaturity = 63
        self.OPF = 1.1
        self.FractionOfEdibleBiomass = 0.97
        self.CaloriesPerKilogram = (1-0.1175)*1000*(4*600.1+9*8.3+4*235.8)/(600.1+8.3+235.8)
        self.EdibleFreshBasisWaterContent = 0.1175
        self.InedibleFreshBasisWaterContent = 0.9
        self.CanopyClosureConstants = [2.9041E5, 1.5594E3, 0, 0, 0, 0, 15.840, 0, 0, 0, 0, 6.1120E-3, 0, 0, 0, 0, 0, -3.7409E-9, 0, 0, 0, 0, 0, 0, 9.6484E-19]
        self.CanopyQuantumYieldConstants = [0, 0, 0, 0, 0, 0, 0, 4.191E-2, 5.3852E-5, -2.1275E-8, 0, -1.238E-5, 0, 0, 0, 0, 0, -1.544E-11, 6.469E-15, 0, 0, 0, 0, 0, 0]
        self.LightCycleTemperature = 26
        self.CarbohydrateFractionOfDryMass = 600.1/(600.1+8.3+235.8)
        self.ProteinFractionOfDryMass = 235.8/(600.1+8.3+235.8)
        self.FatFractionOfDryMass = 8.3/(600.1+8.3+235.8)

# Example usage
dry_bean = DryBean()
print(f"Dry Bean Calories Per Kilogram: {dry_bean.CaloriesPerKilogram}")
