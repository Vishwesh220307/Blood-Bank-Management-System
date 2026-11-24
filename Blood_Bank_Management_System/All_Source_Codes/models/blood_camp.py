from datetime import datetime


class BloodCamp:

    def __init__(self, camp_id, camp_name, location, camp_date):
        self.camp_id = camp_id
        self.camp_name = camp_name
        self.location = location
        self.camp_date = camp_date
        self.participants = []

    def organize_camp(self):
        print(f"\nBlood Camp '{self.camp_name}' organized successfully.")
        print(f"Location : {self.location}")
        print(f"Date     : {self.camp_date}")

    def register_donor(self, donor):
        self.participants.append(donor)
        print(f"{donor.name} registered successfully for {self.camp_name}")

    def generate_camp_report(self):
        print("\n===== BLOOD CAMP REPORT =====")
        print(f"Camp ID      : {self.camp_id}")
        print(f"Camp Name    : {self.camp_name}")
        print(f"Location     : {self.location}")
        print(f"Date         : {self.camp_date}")
        print(f"Participants : {len(self.participants)}")

        print("\nParticipant List:")
        for donor in self.participants:
            print(f"- {donor.name} ({donor.blood_group})")

    def __str__(self):
        return (f"Camp ID: {self.camp_id}, "
                f"Camp Name: {self.camp_name}, "
                f"Location: {self.location}, "
                f"Date: {self.camp_date}")

    def __repr__(self):
        return (f"BloodCamp('{self.camp_id}', "
                f"'{self.camp_name}', "
                f"'{self.location}', "
                f"'{self.camp_date}')")
