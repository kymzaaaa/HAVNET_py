import math
import random


class StoreImpl:
    def __init__(self, name, type_, capacity, initial_level):
        self.name = name
        self.type = type_
        self.current_capacity = capacity
        self.current_level = initial_level

    def add(self, amount):
        self.current_level += amount
        if self.current_level > self.current_capacity:
            self.current_level = self.current_capacity

    def take(self, amount):
        taken = min(self.current_level, amount)
        self.current_level -= taken
        return taken


class CrewPersonImpl3:
    def __init__(self, name, age, weight, gender, schedule, external_store_list, habitat_store_list, bpc_store_list,
                 external_store_list_s, habitat_store_list_s, bpc_store_list_s):
        self.Name = name
        self.Age = age
        self.Weight = weight
        self.Gender = gender
        self.Schedule = schedule
        self.CurrentActivity = schedule[0] if schedule else None
        self.TimeOnCurrentActivity = 1
        self.activityCount = 1
        self.CurrentTick = 0
        self.alive = True
        self.onTick = 0

        # Store lists
        self.external_store_list = external_store_list
        self.habitat_store_list = habitat_store_list
        self.bpc_store_list = bpc_store_list
        self.external_store_list_s = external_store_list_s
        self.habitat_store_list_s = habitat_store_list_s
        self.bpc_store_list_s = bpc_store_list_s

        # Physiological buffers
        self.waterTillDead = 5.3
        self.calorieTillDead = 180000
        self.CO2HighTillDead = 4
        self.O2HighTillDead = 24
        self.O2LowTillDead = 2
        self.TotalPressureLowTillDead = 1
        self.leisureTillBurnout = 168
        self.awakeTillExhaustion = 120

        self.consumedWaterBuffer = StoreImpl('Consumed Water Buffer', 'Material', self.waterTillDead, self.waterTillDead)
        self.consumedCaloriesBuffer = StoreImpl('Consumed Calories Buffer', 'Material', self.calorieTillDead,
                                                self.calorieTillDead)
        self.consumedCO2Buffer = StoreImpl('Consumed CO2 Buffer', 'Material',
                                           self.CO2HighTillDead * 0.482633011,
                                           self.CO2HighTillDead * 0.482633011)
        self.consumedLowOxygenBuffer = StoreImpl('Consumed Low O2 Buffer', 'Material', self.O2LowTillDead,
                                                 self.O2LowTillDead)
        self.highOxygenBuffer = StoreImpl('High O2 Buffer', 'Material', self.O2HighTillDead, self.O2HighTillDead)
        self.lowTotalPressureBuffer = StoreImpl('Low Total Pressure Buffer', 'Material', self.TotalPressureLowTillDead,
                                                self.TotalPressureLowTillDead)
        self.sleepBuffer = StoreImpl('Sleep Buffer', 'Material', self.awakeTillExhaustion, self.awakeTillExhaustion)
        self.leisureBuffer = StoreImpl('Leisure Buffer', 'Material', self.leisureTillBurnout, self.leisureTillBurnout)

    def tick(self, track):
        if not self.alive:
            return

        if track:
            e_vec_before = [store.current_level for store in self.external_store_list]
            h_vec_before = [store.current_level for store in self.habitat_store_list]
            bpc_vec_before = [store.current_level for store in self.bpc_store_list]

        self.consume_and_produce_resources()
        self.afflict_crew()
        self.health_check()
        self.recover_crew()
        self.advance_activity()

        self.CurrentTick += 1

        if track:
            e_vec_after = [store.current_level for store in self.external_store_list]
            h_vec_after = [store.current_level for store in self.habitat_store_list]
            bpc_vec_after = [store.current_level for store in self.bpc_store_list]

            delta = [
                round(after - before, 16)
                for before, after in zip(e_vec_before + h_vec_before + bpc_vec_before,
                                         e_vec_after + h_vec_after + bpc_vec_after)
            ]
            resource_list = self.external_store_list_s + self.habitat_store_list_s + self.bpc_store_list_s
            index_mask = [d != 0 for d in delta]

            resource_changed = [resource_list[i] for i, flag in enumerate(index_mask) if flag]
            quantity = [delta[i] for i, flag in enumerate(index_mask) if flag]
            tick = [self.CurrentTick] * len(quantity)

            if quantity:
                self.onTick = 1
            else:
                self.onTick = 0

    def advance_activity(self):
        if self.TimeOnCurrentActivity >= self.CurrentActivity.Duration:
            self.activityCount += 1
            next_index = self.activityCount % len(self.Schedule)
            self.CurrentActivity = self.Schedule[next_index]
            self.TimeOnCurrentActivity = 1
        else:
            self.TimeOnCurrentActivity += 1

    def consume_and_produce_resources(self):
        if self.CurrentActivity.Name != 'EVA':
            self.O2Needed = self.calculate_o2_needed()
            self.O2Consumed = self.CurrentActivity.Location.O2Store.take(self.O2Needed)
            self.CO2Produced = self.calculate_co2_produced()
            self.CurrentActivity.Location.CO2Store.add(self.CO2Produced)

        self.caloriesNeeded = self.calculate_food_needed()
        food_consumed = self.get_calories_from_store(self.caloriesNeeded)
        self.foodMassConsumed = sum(item['mass'] for item in food_consumed)
        self.caloriesConsumed = sum(item['calories'] for item in food_consumed)

    def get_calories_from_store(self, calories_needed):
        # Placeholder for food consumption logic
        return []

    def calculate_o2_needed(self):
        return self.CurrentActivity.O2Needed

    def calculate_co2_produced(self):
        return self.CurrentActivity.CO2Output

    def calculate_food_needed(self):
        activity_coefficient = 0.5 * (self.CurrentActivity.Intensity - 1) + 1
        if self.Gender.lower() == 'male':
            if self.Age < 30:
                kJ_needed = 106 * self.Weight + 5040 * activity_coefficient
            else:
                kJ_needed = 86 * self.Weight + 5990 * activity_coefficient
        else:
            if self.Age < 30:
                kJ_needed = 100 * self.Weight + 3200 * activity_coefficient
            else:
                kJ_needed = 50 * self.Weight + 6066.7 * activity_coefficient
        return kJ_needed / 24 / 4.184

    def afflict_crew(self):
        self.consumedCaloriesBuffer.take(self.caloriesNeeded - self.caloriesConsumed)

    def health_check(self):
        random_number = random.random()

        calorie_risk = self.calculate_risk(self.consumedCaloriesBuffer)
        if calorie_risk > random_number:
            self.kill()
            print(f"{self.Name} has died from starvation on tick {self.CurrentTick}")

    def calculate_risk(self, buffer):
        percentage_full = buffer.current_level / buffer.current_capacity
        return 1 / (1 + 10 ** (6 * percentage_full)) if percentage_full < 1 else 0

    def kill(self):
        self.alive = False
