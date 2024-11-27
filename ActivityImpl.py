class ActivityImpl:
    """
    ActivityImpl class in Python.
    Activities are performed by crew members (CrewPerson) for a certain amount of
    time with a certain intensity in a certain order.
    """

    def __init__(self, ID, location, duration):
        self.ID = ID
        self.Location = location
        self.Duration = duration
        self.Name = None
        self.Intensity = None
        self.VaporProduced = None
        self.DirtyWaterProduced = None
        self.O2Needed = None
        self.CO2Output = None
        self.PotableWaterNeeded = None

        if self.ID == 1:
            self.Name = "Exercise - Aerobic"
            self.Intensity = 5
            self.VaporProduced = 43.3272  # moles/hour (sweat included)
            self.DirtyWaterProduced = 0  # kg/hour
            self.O2Needed = 3.8462  # moles/hour
            self.CO2Output = 3.6595  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
        elif self.ID == 2:
            self.Name = "Exercise - Resistive"
            self.Intensity = 5
            self.VaporProduced = 80.3523  # moles/hour (sweat included)
            self.DirtyWaterProduced = 0  # kg/hour
            self.O2Needed = 2.7569  # moles/hour
            self.CO2Output = 2.6500  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
        elif self.ID == 3:
            self.Name = "Recovery - 1st hour"
            self.Intensity = 2
            self.VaporProduced = 8.5627  # moles/hour
            self.DirtyWaterProduced = 0  # kg/hour
            self.O2Needed = 1.1375  # moles/hour
            self.CO2Output = 0.9675  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
        elif self.ID == 4:
            self.Name = "Recovery - 2nd hour"
            self.Intensity = 2
            self.VaporProduced = 5.2404  # moles/hour
            self.DirtyWaterProduced = 0  # kg/hour
            self.O2Needed = 1.1375  # moles/hour
            self.CO2Output = 0.9675  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
        elif self.ID == 5:
            self.Name = "Recovery - 3rd hour"
            self.Intensity = 2
            self.VaporProduced = 4.6924  # moles/hour
            self.DirtyWaterProduced = 0  # kg/hour
            self.O2Needed = 1.1375  # moles/hour
            self.CO2Output = 0.9675  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
        elif self.ID == 6:
            self.Name = "IVA"
            self.Intensity = 2
            self.VaporProduced = 4.5554  # moles/hour
            self.DirtyWaterProduced = 0  # kg/hour
            self.O2Needed = 1.1375  # moles/hour
            self.CO2Output = 0.9675  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
        elif self.ID == 7:
            self.Name = "Personal Hygiene and Toilet"
            self.Intensity = 2
            self.VaporProduced = 4.5554  # moles/hour
            self.DirtyWaterProduced = 1.4000  # kg/day
            self.O2Needed = 1.1375  # moles/hour
            self.CO2Output = 0.9675  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
        elif self.ID == 8:
            self.Name = "Sleep"
            self.Intensity = 1
            self.VaporProduced = 3.6991  # moles/hour
            self.DirtyWaterProduced = 0  # kg/day
            self.O2Needed = 0.7133  # moles/hour
            self.CO2Output = 0.6169  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
        elif self.ID == 9:
            self.Name = "Laundry"
            self.Intensity = 2
            self.VaporProduced = 4.5554  # moles/hour
            self.DirtyWaterProduced = 0  # kg/day
            self.O2Needed = 1.1375  # moles/hour
            self.CO2Output = 0.9675  # moles/hour
            self.PotableWaterNeeded = self.VaporProduced * 0.01802 + self.DirtyWaterProduced
