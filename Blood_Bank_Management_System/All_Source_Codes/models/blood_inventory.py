class BloodInventory:

    def __init__(self, inventory_id):
        self.inventory_id = inventory_id
        self.blood_units = {}

    def add_stock(self, blood_group, quantity):
        if blood_group in self.blood_units:
            self.blood_units[blood_group] += quantity
        else:
            self.blood_units[blood_group] = quantity

        print(f"{quantity} units of {blood_group} added successfully.")

    def remove_stock(self, blood_group, quantity):
        if blood_group not in self.blood_units:
            print("Blood group not found.")
            return

        if self.blood_units[blood_group] < quantity:
            print("Insufficient stock.")
            return

        self.blood_units[blood_group] -= quantity

        print(f"{quantity} units of {blood_group} removed successfully.")

    def view_inventory(self):

        print("\n===== BLOOD INVENTORY =====")

        if not self.blood_units:
            print("Inventory is empty.")
            return

        for blood_group, quantity in self.blood_units.items():
            print(f"{blood_group} : {quantity} units")

    def check_availability(self, blood_group):

        if blood_group in self.blood_units and self.blood_units[blood_group] > 0:
            print(f"{blood_group} blood is available.")
            return True

        print(f"{blood_group} blood is not available.")
        return False

    def __len__(self):
        return sum(self.blood_units.values())

    def __str__(self):
        return f"Inventory ID: {self.inventory_id}"

    def __repr__(self):
        return f"BloodInventory('{self.inventory_id}')"