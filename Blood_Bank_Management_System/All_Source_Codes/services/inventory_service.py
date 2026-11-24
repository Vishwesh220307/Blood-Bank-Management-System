from models.blood_inventory import BloodInventory
from utils.decorator import log_activity
from utils.validator import Validator
from utils.exception import (
    InvalidBloodGroupError,
    BloodStockNotAvailableError
)


class InventoryService:

    def __init__(self):
        self.inventory = BloodInventory("INV001")

    # -------------------------
    # Add Blood Stock
    # -------------------------
    @log_activity
    def add_stock(self, blood_group, quantity):

        if not Validator.validate_blood_group(
                blood_group):
            raise InvalidBloodGroupError()

        self.inventory.add_stock(
            blood_group,
            quantity
        )

    # -------------------------
    # Remove Blood Stock
    # -------------------------
    @log_activity
    def remove_stock(self,
                     blood_group,
                     quantity):

        available = self.inventory.blood_units.get(
            blood_group,
            0
        )

        if available < quantity:
            raise BloodStockNotAvailableError()

        self.inventory.remove_stock(
            blood_group,
            quantity
        )

    # -------------------------
    # View Inventory
    # -------------------------
    def view_inventory(self):

        self.inventory.view_inventory()

    # -------------------------
    # Check Availability
    # -------------------------
    def check_availability(
            self,
            blood_group):

        return self.inventory.check_availability(
            blood_group
        )

    # -------------------------
    # Low Stock Alert
    # -------------------------
    def low_stock_alert(
            self,
            threshold=5):

        print("\n===== LOW STOCK ALERT =====")

        found = False

        for blood_group, quantity in \
                self.inventory.blood_units.items():

            if quantity <= threshold:

                print(
                    f"{blood_group} : "
                    f"{quantity} units remaining"
                )

                found = True

        if not found:
            print("No Low Stock Alerts")

    # -------------------------
    # Sort Blood Groups
    # Lambda Function
    # -------------------------
    def sort_inventory(self):

        sorted_inventory = sorted(
            self.inventory.blood_units.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\n===== SORTED INVENTORY =====")

        for group, quantity in sorted_inventory:

            print(
                f"{group} : "
                f"{quantity} units"
            )

    # -------------------------
    # Available Blood Groups
    # List Comprehension
    # -------------------------
    def available_blood_groups(self):

        groups = [
            group
            for group, qty
            in self.inventory.blood_units.items()
            if qty > 0
        ]

        print("\nAvailable Blood Groups:")

        for group in groups:
            print(group)

        return groups