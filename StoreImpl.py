class StoreImpl:
    """
    Implementation of a generic store that can hold a variety of resources.
    It can operate in modes suitable for both environmental and material resources.
    """
    
    def __init__(self, store_content, store_type, capacity=0, level=0):
        if store_type.lower() not in ['environmental', 'material']:
            raise ValueError('Store type must be set to either "Environmental" or "Material"')
        self.contents = store_content
        self.type = store_type
        self.tickcount = 0
        self.current_level = level
        self.current_capacity = capacity
        self.overflow = 0
        self.resupply_frequency = 0
        self.resupply_amount = 0

    def tick(self, tick_count):
        self.tickcount = tick_count
        if self.tickcount > 0 and self.resupply_frequency > 0:
            if self.tickcount % self.resupply_frequency == 0:
                self.add(self.resupply_amount)

    def add(self, amount_requested):
        if amount_requested < 0:
            return 0
        if self.type == 'environmental':
            self.current_level += amount_requested
            self.current_capacity = self.current_level  # Enforce capacity match level
            return amount_requested
        else:
            if self.current_level + amount_requested > self.current_capacity:
                actually_added = self.current_capacity - self.current_level
                self.current_level = self.current_capacity
                self.overflow += (amount_requested - actually_added)
            else:
                self.current_level += amount_requested
                actually_added = amount_requested
            return actually_added

    def take(self, amount_to_take):
        if amount_to_take < 0:
            return 0
        if amount_to_take > self.current_level:
            amount_retrieved = self.current_level
            self.current_level = 0
        else:
            self.current_level -= amount_to_take
            amount_retrieved = amount_to_take
        return amount_retrieved

    def take_overflow(self):
        overflow_taken = self.overflow
        self.overflow = 0
        return overflow_taken

    def fill(self, fill_store=None):
        if self.type != 'material':
            raise ValueError('The "fill" method can only be applied to stores of type "Material"')
        amount_to_add = self.current_capacity - self.current_level
        if fill_store:
            if fill_store.current_level < amount_to_add:
                print(f'Insufficient resources in {fill_store.contents} to fill {self.contents}.')
            amount_to_add = min(amount_to_add, fill_store.current_level)
            amount_added = self.add(fill_store.take(amount_to_add))
        else:
            amount_added = self.add(amount_to_add)
        return amount_added

# Example usage
# Creating a store for Oxygen in an environmental setting
o2_store = StoreImpl('O2', 'environmental', 100, 50)

# Ticking the store to simulate time passing
o2_store.tick(1)

# Adding resources to the store
o2_store.add(25)

# Taking resources from the store
o2_store.take(30)

# Checking for overflow and handling it
o2_store.take_overflow()

# Simulating filling the store from another source
other_store = StoreImpl('Backup O2', 'material', 500, 300)
o2_store.fill(other_store)
