from datetime import datetime


class BloodDonation:

    def __init__(self, donation_id, donor, donation_date, quantity):
        self.donation_id = donation_id
        # Handle both donor object and donor name string
        self.donor_obj = donor if hasattr(donor, 'donate_blood') else None
        self.donor = donor.name if hasattr(donor, 'donate_blood') else donor
        self.donation_date = donation_date
        self.quantity = quantity

    def record_donation(self):
        print("\n===== BLOOD DONATION RECORDED =====")
        print(f"Donation ID   : {self.donation_id}")
        print(f"Donor         : {self.donor}")
        print(f"Date          : {self.donation_date}")
        print(f"Quantity      : {self.quantity} Unit(s)")

    def generate_certificate(self):
        print("\n===== DONATION CERTIFICATE =====")
        print("Blood Bank Management System")
        print(f"Certificate ID : {self.donation_id}")
        print(f"Donor Name     : {self.donor}")
        print(f"Donation Date  : {self.donation_date}")
        print(f"Quantity       : {self.quantity} Unit(s)")
        print("Thank You For Donating Blood!")

    def __str__(self):
        return (
            f"Donation ID: {self.donation_id}, "
            f"Donor: {self.donor}, "
            f"Date: {self.donation_date}, "
            f"Quantity: {self.quantity}"
        )

    def __repr__(self):
        return (
            f"BloodDonation('{self.donation_id}', "
            f"'{self.donor}', "
            f"'{self.donation_date}', "
            f"{self.quantity})"
        )