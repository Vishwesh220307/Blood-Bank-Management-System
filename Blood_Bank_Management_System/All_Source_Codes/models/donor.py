from models.person import Person
from datetime import datetime, timedelta


class Donor(Person):

    def __init__(self, person_id, name, age, gender,
                 mobile_number, donor_id, blood_group):

        super().__init__(
            person_id,
            name,
            age,
            gender,
            mobile_number
        )

        self.donor_id = donor_id
        self.blood_group = blood_group
        self.last_donation_date = None
        self.donation_history = []
        self.DONATION_INTERVAL_DAYS = 56

    def donate_blood(self, donation_date):

        self.last_donation_date = donation_date
        self.donation_history.append(donation_date)

        print("Blood Donation Recorded Successfully")

    def view_donation_history(self):

        print("\n===== DONATION HISTORY =====")

        if not self.donation_history:
            print("No Donation History Found")
            return

        for donation in self.donation_history:
            print(donation)

    def check_eligibility(self):
        """Check if donor is eligible to donate blood"""
        
        if self.last_donation_date is None:
            print("Eligible for Donation (First Time Donor)")
            return True
        
        try:
            # Parse last donation date if it's a string
            if isinstance(self.last_donation_date, str):
                last_date = datetime.strptime(self.last_donation_date, "%Y-%m-%d").date()
            else:
                last_date = self.last_donation_date if hasattr(self.last_donation_date, 'date') else self.last_donation_date
            
            # Calculate days since last donation
            today = datetime.now().date()
            days_since_donation = (today - last_date).days
            
            if days_since_donation >= self.DONATION_INTERVAL_DAYS:
                print(f"Eligible for Donation ({days_since_donation} days since last donation)")
                return True
            else:
                days_remaining = self.DONATION_INTERVAL_DAYS - days_since_donation
                print(f"NOT Eligible. Can donate after {days_remaining} more days")
                return False
                
        except Exception as e:
            print(f"Error checking eligibility: {e}")
            return False

    def display_details(self):

        print("\n===== DONOR DETAILS =====")
        print("Donor ID:", self.donor_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Blood Group:", self.blood_group)
        print("Mobile:", self.mobile_number)

    def __str__(self):
        return f"{self.donor_id} - {self.name} ({self.blood_group})"

    def __repr__(self):
        return f"Donor('{self.donor_id}','{self.name}')"