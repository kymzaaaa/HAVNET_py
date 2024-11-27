class WHC:
    # Note: This is for one astronaut. The main script track when a WHC activity
    # happens for any crew member even when schedules are not in alignment

    def __init__(self, astro, environment, greyWaterStore_outside, dirtyWaterStore_outside, ExternalStoreList, HabitatStoreList, BPCStoreList, ExternalStoreList_s, HabitatStoreList_s, BPCStoreList_s):
        self.Environment = environment
        self.greyWaterStore_outside = greyWaterStore_outside
        self.dirtyWaterStore_outside = dirtyWaterStore_outside
        self.externalStoreList_s = ExternalStoreList_s
        self.habitatStoreList_s = HabitatStoreList_s
        self.externalStoreList = ExternalStoreList
        self.habitatStoreList = HabitatStoreList
        self.BPCStoreList = BPCStoreList
        self.BPCStoreList_s = BPCStoreList_s
        self.astro = astro
        # Water usage constants
        self.flushWater = 0.6  # KG
        self.oralHygiene = 0.552  # KG
        self.showerWater = 1.296  # KG
        self.handWash = 0.768  # KG

    def tick(self, track, waterLeak):
        if track == 1:
            E_vec_before = [store.currentLevel for store in self.externalStoreList]
            H_vec_before = [store.currentLevel for store in self.habitatStoreList]
            BPC_vec_before = [store.currentLevel for store in self.BPCStoreList]

        if self.Environment.DirtyWaterStore.currentLevel > self.flushWater:  # Have the WHC run only when there is pee in the habitat dirty water storage
            # Potable water store in the habitat is transferred to the marshab grey water store in the amount needed for oral hygiene, handwash, and shower.
            self.Environment.GreyWaterStore.add(self.oralHygiene + self.showerWater + self.handWash)
            self.Environment.PotableWaterStore.take((self.oralHygiene + self.showerWater + self.handWash + self.flushWater) * (1 + waterLeak))
            self.Environment.DirtyWaterStore.add(self.flushWater)

            # Empty the grey water store in the habitat to the grey water store outside
            self.greyWaterStore_outside.add(self.Environment.GreyWaterStore.currentLevel * (1 - waterLeak))
            self.Environment.GreyWaterStore.take(self.Environment.GreyWaterStore.currentLevel)

            # Empty the dirty water store in the habitat to the dirty water store outside
            self.dirtyWaterStore_outside.add(self.Environment.DirtyWaterStore.currentLevel)
            self.Environment.DirtyWaterStore.take(self.Environment.DirtyWaterStore.currentLevel)

        if track == 1:
            E_vec_after = [store.currentLevel for store in self.externalStoreList]
            H_vec_after = [store.currentLevel for store in self.habitatStoreList]
            BPC_vec_after = [store.currentLevel for store in self.BPCStoreList]

            # Delta tracking
            delta = [after - before for before, after in zip(E_vec_before + H_vec_before + BPC_vec_before, E_vec_after + H_vec_after + BPC_vec_after)]
            resourceList = self.externalStoreList_s + self.habitatStoreList_s + self.BPCStoreList_s
            indexMask = [i for i, x in enumerate(delta) if x != 0]
            resourceChanged = [resourceList[i] for i in indexMask]
            quantity = [delta[i] for i in indexMask]
            tick = [self.Environment.tickcount] * len(quantity)

            # Logging to file would go here, with each tick's changes written out
