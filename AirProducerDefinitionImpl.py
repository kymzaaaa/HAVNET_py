class AirProducerDefinitionImpl:
    """
    AirProducerDefinitionImpl Summary:
    Detailed explanation goes here
    """

    def __init__(self, sink=None, desiredFlowRate=None, maxFlowRate=None):
        self.ProductionStore = sink
        self.DesiredFlowRate = desiredFlowRate
        self.MaxFlowRate = maxFlowRate
