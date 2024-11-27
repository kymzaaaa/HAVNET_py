class FoodMatter:
    carbohydrate_calories_per_gram = 4  # 4 kilocalories per gram of carbohydrates
    protein_calories_per_gram = 4       # 4 kilocalories per gram of proteins
    fat_calories_per_gram = 9           # 9 kilocalories per gram of fats

    def __init__(self, plant_type, mass, water_content):
        self.Type = plant_type
        self.Mass = mass
        self.WaterContent = water_content  # in kg
        
        # Assuming the Type object has attributes like CarbohydrateFractionOfDryMass, etc.
        dry_mass = mass - water_content
        self.CarbohydrateContent = plant_type.CarbohydrateFractionOfDryMass * dry_mass
        self.ProteinContent = plant_type.ProteinFractionOfDryMass * dry_mass
        self.FatContent = plant_type.FatFractionOfDryMass * dry_mass
        self.CaloricContent = dry_mass * 1E3 * (
            plant_type.CarbohydrateFractionOfDryMass * FoodMatter.carbohydrate_calories_per_gram +
            plant_type.ProteinFractionOfDryMass * FoodMatter.protein_calories_per_gram +
            plant_type.FatFractionOfDryMass * FoodMatter.fat_calories_per_gram
        )

# Example use:
class PlantType:
    def __init__(self, carbs_fraction, protein_fraction, fat_fraction):
        self.CarbohydrateFractionOfDryMass = carbs_fraction
        self.ProteinFractionOfDryMass = protein_fraction
        self.FatFractionOfDryMass = fat_fraction

# Create a PlantType instance with example values
example_plant_type = PlantType(0.6, 0.2, 0.2)

# Create a FoodMatter instance
food = FoodMatter(example_plant_type, 1.0, 0.2)  # 1 kg of mass with 0.2 kg of water
print(f"Caloric Content: {food.CaloricContent} kcal")
