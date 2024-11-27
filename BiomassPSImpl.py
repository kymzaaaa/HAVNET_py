class BiomassPSImpl:
    """
    BiomassPSImpl Summary:
    By: Sydney Do (sydneydo@mit.edu)
    Date Created: 5/31/2014
    Last Updated: 5/31/2014

    Original BioSim code comments by Scott Bell
    The Biomass RS is essentially responsible for growing plants. The Biomass RS
    consists of many ShelfImpls, and inside them, a Plant. The ShelfImpl gathers
    water and light for the plant. The plant itself breathes from the atmosphere
    and produces biomass. The plant matter (biomass) is fed into the food
    processor to create food for the crew. The plants can also (along with the
    AirRS) take CO2 out of the air and add O2.
    """

    def __init__(self, shelves):
        self.Shelves = shelves
        self.currentTick = 0
        self.PowerConsumerDefinition = ResourceUseDefinitionImpl()
        self.AirConsumerDefinition = ResourceUseDefinitionImpl()
        self.PotableWaterConsumerDefinition = ResourceUseDefinitionImpl()
        self.GreyWaterConsumerDefinition = ResourceUseDefinitionImpl()
        self.DirtyWaterProducerDefinition = ResourceUseDefinitionImpl()
        self.AirProducerDefinition = ResourceUseDefinitionImpl()
        self.BiomassProducerDefinition = ResourceUseDefinitionImpl()

    def tick(self):
        """
        Tick each shelf contained within the BiomassPS
        """
        self.currentTick += 1
