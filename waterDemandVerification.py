# Calculate the water demand for various components using Python

# Assuming 'greywaterlevel_bpc', 'potablewaterlevel_mav', and 'MarsHabpotablewaterlevel'
# are lists or arrays with relevant water level data

waterDemand4CM = {}

# Maximum minus minimum for BPC water demand
waterDemand4CM['BPCWater'] = max(greywaterlevel_bpc) - min(greywaterlevel_bpc)

# First minus last element for MAV water demand
waterDemand4CM['MAVWater'] = potablewaterlevel_mav[0] - potablewaterlevel_mav[-1]

# First minus last element for ECLS water demand
waterDemand4CM['ECLSWater'] = MarsHabpotablewaterlevel[0] - MarsHabpotablewaterlevel[-1]

# Total water requirement is the sum of all individual demands
waterDemand4CM['TotalWaterReq'] = (waterDemand4CM['BPCWater'] +
                                   waterDemand4CM['MAVWater'] +
                                   waterDemand4CM['ECLSWater'])

# Output or usage example
print("Water Demand for BPC:", waterDemand4CM['BPCWater'])
print("Water Demand for MAV:", waterDemand4CM['MAVWater'])
print("Water Demand for ECLS:", waterDemand4CM['ECLSWater'])
print("Total Water Requirement:", waterDemand4CM['TotalWaterReq'])
