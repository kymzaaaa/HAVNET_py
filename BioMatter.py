class BioMatter:
    """
    BioMatter class represents crops that have been sent to the biomass
    store by the BiomassPSImpl. The FoodProcessor takes BioMatter from the
    Biomass store and converts it to FoodMatter, which is then sent to the
    FoodStore. CrewPersons consume food directly from the FoodStore.

    Attributes:
        Type (PlantType): The type of the plant.
        Mass (float): The mass of the bio matter.
        InedibleFraction (float): Mass fraction that is inedible.
        EdibleWaterContent (float): Mass of edible water content.
        InedibleWaterContent (float): Mass of inedible water content.
    """

    def __init__(self, type=None, mass=None, inedibleFraction=None, edibleWaterContent=None, inedibleWaterContent=None):
        """
        Initializes a new instance of the BioMatter class.

        Args:
            type (PlantType): The type of the plant.
            mass (float): The mass of the bio matter.
            inedibleFraction (float): Mass fraction that is inedible.
            edibleWaterContent (float): Mass of edible water content.
            inedibleWaterContent (float): Mass of inedible water content.
        """
        if type is not None:
            self.Type = type
            self.Mass = mass
            self.InedibleFraction = inedibleFraction
            self.EdibleWaterContent = edibleWaterContent
            self.InedibleWaterContent = inedibleWaterContent
