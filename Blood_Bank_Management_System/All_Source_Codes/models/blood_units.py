# models/blood_units.py

from datetime import datetime


class BloodUnit:

    def __init__(self, unit_id, blood_group, quantity,
                 collection_date, expiry_date):

        self.unit_id = unit_id
        self.blood_group = blood_group
        self.quantity = quantity
        self.collection_date = collection_date
        self.expiry_date = expiry_date

    def add_blood_unit(self):
        print("\n===== BLOOD UNIT ADDED =====")
        print(f"Unit ID         : {self.unit_id}")
        print(f"Blood Group     : {self.blood_group}")
        print(f"Quantity        : {self.quantity}")
        print(f"Collection Date : {self.collection_date}")
        print(f"Expiry Date     : {self.expiry_date}")

    def update_stock(self, quantity):
        self.quantity += quantity
        print(f"Stock Updated Successfully.")
        print(f"Current Quantity : {self.quantity}")

    def check_expiry(self):

        today = datetime.today().date()
        expiry = datetime.strptime(
            self.expiry_date,
            "%Y-%m-%d"
        ).date()

        if expiry < today:
            print("Blood Unit Expired.")
            return True

        print("Blood Unit is Valid.")
        return False

    def __str__(self):
        return (
            f"Unit ID: {self.unit_id}, "
            f"Blood Group: {self.blood_group}, "
            f"Quantity: {self.quantity}"
        )

    def __repr__(self):
        return (
            f"BloodUnit('{self.unit_id}', "
            f"'{self.blood_group}', "
            f"{self.quantity}, "
            f"'{self.collection_date}', "
            f"'{self.expiry_date}')"
        )