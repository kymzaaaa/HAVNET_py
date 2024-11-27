class MAV_OLD:
    def __init__(self, number_of_crew, mission_duration_in_hours, boil_off_rate_lox, boil_off_rate_ch4):
        self.mission_duration_days = mission_duration_in_hours / 24
        self.number_of_crew = number_of_crew
        self.boil_off_rate_lox = boil_off_rate_lox / 100  # Convert percentage to decimal
        self.boil_off_rate_ch4 = boil_off_rate_ch4 / 100  # Convert percentage to decimal

        # MAV Propellant Requirements (Extended for various crew sizes)
        self.crew_size_vs_lox_req = [
            13662, 17021, 19977, 22717, 25316, 27813, 30231, 22717*2, 34888, 37147,
            39367, 22717*3, 0, 0, 0, 22717*4, 0, 0, 0, 22717*5
        ]
        self.crew_size_vs_lch4_req = [
            4173, 5199, 6101, 6938, 7732, 8494, 9233, 6938*2, 10655, 11345, 
            12023, 6938*3, 0, 0, 0, 6938*4, 0, 0, 0, 6938*5
        ]

        # LOX Requirements
        self.calculate_lox_requirements()

        # LCH4 Requirements
        self.calculate_lch4_requirements()

    def calculate_lox_requirements(self):
        self.lox_day_prod_rate = self.crew_size_vs_lox_req[self.number_of_crew - 1] / self.mission_duration_days
        lox_level = 0
        self.lox_lost_cumulative = 0
        for i in range(int(self.mission_duration_days)):
            lox_level = lox_level * (1 - self.boil_off_rate_lox) + self.lox_day_prod_rate
            lox_lost = lox_level * self.boil_off_rate_lox
            self.lox_lost_cumulative += lox_lost

        lox_percentage_prod_increase = self.lox_lost_cumulative / (self.crew_size_vs_lox_req[self.number_of_crew - 1] - self.lox_lost_cumulative)
        self.lox_day_req_prod_rate = self.lox_day_prod_rate * (1 + lox_percentage_prod_increase)

    def calculate_lch4_requirements(self):
        self.lch4_day_prod_rate = self.crew_size_vs_lch4_req[self.number_of_crew - 1] / self.mission_duration_days
        lch4_level = 0
        self.lch4_lost_cumulative = 0
        for j in range(int(self.mission_duration_days)):
            lch4_level = lch4_level * (1 - self.boil_off_rate_ch4) + self.lch4_day_prod_rate
            lch4_lost = lch4_level * self.boil_off_rate_ch4
            self.lch4_lost_cumulative += lch4_lost

        lch4_percentage_prod_increase = self.lch4_lost_cumulative / (self.crew_size_vs_lch4_req[self.number_of_crew - 1] - self.lch4_lost_cumulative)
        self.lch4_day_req_prod_rate = self.lch4_day_prod_rate * (1 + lch4_percentage_prod_increase)
