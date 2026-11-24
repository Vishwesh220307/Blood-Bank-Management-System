from models.blood_camp import BloodCamp
from utils.decorator import log_activity


class CampService:

    def __init__(self):
        self.camps = []

    @log_activity
    def organize_camp(
            self,
            camp_id,
            camp_name,
            location,
            camp_date):

        camp = BloodCamp(
            camp_id,
            camp_name,
            location,
            camp_date
        )

        self.camps.append(camp)

        camp.organize_camp()

    @log_activity
    def register_donor(
            self,
            camp_id,
            donor):

        for camp in self.camps:

            if camp.camp_id == camp_id:

                camp.register_donor(donor)
                return

        print("Camp Not Found")

    def generate_camp_report(
            self,
            camp_id):

        for camp in self.camps:

            if camp.camp_id == camp_id:

                camp.generate_camp_report()
                return

        print("Camp Not Found")

    def view_all_camps(self):

        if not self.camps:
            print("No Camps Available")
            return

        print("\n===== CAMP LIST =====")

        for camp in self.camps:
            print(camp)