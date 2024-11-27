class AirConsumerDefinitionImpl:
    """
    AirConsumerDefinitionImpl Summary:
    Detailed explanation goes here
    """

    def __init__(self, SimEnvironment=None, desiredFlowRate=None, maxFlowRate=None):
        self.ConsumptionStore = SimEnvironment
        self.DesiredFlowRate = desiredFlowRate
        self.MaxFlowRate = maxFlowRate
