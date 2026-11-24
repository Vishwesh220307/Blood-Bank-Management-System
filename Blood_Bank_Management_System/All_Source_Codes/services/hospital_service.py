from models.hospital import HospitalRepresentative
from utils.decorator import log_activity


class HospitalService:

    def __init__(self):
        self.hospitals = []

    # -------------------------
    # Register Hospital
    # -------------------------
    @log_activity
    def register_hospital(
            self,
            person_id,
            name,
            age,
            gender,
            mobile_number,
            representative_id,
            hospital_name):

        hospital = HospitalRepresentative(
            person_id,
            name,
            age,
            gender,
            mobile_number,
            representative_id,
            hospital_name
        )

        self.hospitals.append(hospital)

        print("Hospital Registered Successfully")

    # -------------------------
    # Search Hospital
    # -------------------------
    def search_hospital(
            self,
            representative_id):

        for hospital in self.hospitals:

            if hospital.representative_id == representative_id:
                return hospital

        return None

    # -------------------------
    # View Hospital Details
    # -------------------------
    def display_hospital(
            self,
            representative_id):

        hospital = self.search_hospital(
            representative_id
        )

        if hospital:
            hospital.display_details()
        else:
            print("Hospital Not Found")

    # -------------------------
    # Emergency Request
    # -------------------------
    @log_activity
    def emergency_request(
            self,
            representative_id):

        hospital = self.search_hospital(
            representative_id
        )

        if hospital:

            print(
                f"Emergency Blood Request Raised by "
                f"{hospital.hospital_name}"
            )

        else:
            print("Hospital Not Found")

    # -------------------------
    # View All Hospitals
    # -------------------------
    def view_all_hospitals(self):

        if not self.hospitals:
            print("No Hospitals Registered")
            return

        print("\n===== HOSPITAL LIST =====")

        for hospital in self.hospitals:
            print(hospital)

    # -------------------------
    # Sort Hospitals
    # Lambda Function
    # -------------------------
    def sort_hospitals(self):

        sorted_hospitals = sorted(
            self.hospitals,
            key=lambda hospital:
            hospital.hospital_name
        )

        print("\n===== SORTED HOSPITALS =====")

        for hospital in sorted_hospitals:
            print(hospital)