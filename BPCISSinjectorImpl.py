class BPCISSinjectorImpl:
    def __init__(self, target_total_pressure, target_o2_molar_fraction, o2_source, n2_source, environment, pca_mode,
                 external_store_list, habitat_store_list, bpc_store_list, external_store_list_s, habitat_store_list_s, bpc_store_list_s):
        self.TargetTotalPressure = target_total_pressure
        self.TargetO2MolarFraction = target_o2_molar_fraction
        self.TargetO2PartialPressure = target_o2_molar_fraction * target_total_pressure
        self.O2Source = o2_source
        self.N2Source = n2_source
        self.Environment = environment
        self.OperatingMode = pca_mode
        self.external_store_list = external_store_list
        self.habitat_store_list = habitat_store_list
        self.bpc_store_list = bpc_store_list
        self.external_store_list_s = external_store_list_s
        self.habitat_store_list_s = habitat_store_list_s
        self.bpc_store_list_s = bpc_store_list_s

        self.O2Vented = 0
        self.CO2Vented = 0
        self.N2Vented = 0
        self.VaporVented = 0
        self.OtherGasesVented = 0
        self.Error = 0
        self.UpperPPO2PercentageLimit = 0.3

        # Private properties
        self.PartialPressureBoundingBox = 1.37895146
        self.VentPortDiameter = 0.056
        self.MarsMeanAtmPressure = 6.36 * 0.1
        self.MarsMeanAtmDensity = 0.02
        self.idealGasConstant = 8.314
        self.O2molarMass = 2 * 15.999
        self.CO2molarMass = 12.011 + 2 * 15.999
        self.N2molarMass = 2 * 14.007
        self.VapormolarMass = 2 * 1.008 + 15.999
        self.OthermolarMass = 0.265 * 2 * 15.999 + (1 - 0.265) * 2 * 14.007

    def tick(self, previous_action, track):
        # Similar data tracking as in the original MATLAB code
        if track == 1:
            e_vec_before = [store.current_level for store in self.external_store_list]
            h_vec_before = [store.current_level for store in self.habitat_store_list]
            bpc_vec_before = [store.current_level for store in self.bpc_store_list]

        action = [0] * 4  # Initialize action tracking

        if self.Error == 0:
            # Simulating operations based on PCA mode
            if self.OperatingMode.upper() == 'PCA':
                # Implementing specific operations here
                # Detailed code would include checks for O2 levels, pressure adjustments, and resource balancing
                pass

            elif self.OperatingMode.upper() == 'PPRV':
                # Implement passive venting procedures here
                pass

            elif self.OperatingMode.upper() == 'EMU':
                # Implement operations for an EMU-type environment
                pass

        if track == 1:
            e_vec_after = [store.current_level for store in self.external_store_list]
            h_vec_after = [store.current_level for store in self.habitat_store_list]
            bpc_vec_after = [store.current_level for store in self.bpc_store_list]

            # Tracking changes to implement logging or corrective actions
            # Detailed tracking and logging mechanisms need to be implemented

        return action  # This should return the actions taken during the tick

