from models.donor import Donor
from utils.validator import Validator
from utils.decorator import log_activity
from utils.exception import (
    InvalidBloodGroupError,
    DuplicateDonorRegistrationError
)
class DonorService:
    def __init__(self):
        self.donors = []
    # Register Donor
    @log_activity
    def register_donor(
            self,
            person_id,
            name,
            age,
            gender,
            mobile_number,
            donor_id,
            blood_group):
        # Check duplicate donor
        for donor in self.donors:
            if donor.donor_id == donor_id:
                raise DuplicateDonorRegistrationError()
        # Validate blood group
        if not Validator.validate_blood_group(
                blood_group):
            raise InvalidBloodGroupError()
        donor = Donor(
            person_id,
            name,
            age,
            gender,
            mobile_number,
            donor_id,
            blood_group
        )
        self.donors.append(donor)
        print("Donor Registered Successfully")
    # Update Donor
    @log_activity
    def update_donor(
            self,
            donor_id,
            name,
            age,
            gender,
            mobile_number):
        donor = self.search_donor(donor_id)
        if donor:
            donor.update_details(
                name,
                age,
                gender,
                mobile_number
            )
            print("Donor Updated Successfully")
        else:
            print("Donor Not Found")
    # Search Donor
    # Recursive Function
    def search_donor_recursive(
            self,
            donor_id,
            index=0):
        if index >= len(self.donors):
            return None
        if self.donors[index].donor_id == donor_id:
            return self.donors[index]
        return self.search_donor_recursive(
            donor_id,
            index + 1
        )
    def search_donor(self, donor_id):
        return self.search_donor_recursive(
            donor_id
        )
    # Display Donor
    def display_donor(self, donor_id):
        donor = self.search_donor(donor_id)
        if donor:
            donor.display_details()
        else:
            print("Donor Not Found")
    # Eligibility Check
    def check_eligibility(self, donor_id):
        donor = self.search_donor(donor_id)
        if donor:
            donor.check_eligibility()
        else:
            print("Donor Not Found")
    # Donation History
    def donation_history(self, donor_id):
        donor = self.search_donor(donor_id)
        if donor:
            donor.view_donation_history()
        else:
            print("Donor Not Found")
    # View All Donors
    def view_all_donors(self):
        if not self.donors:
            print("No Donors Available")
            return
        print("\n===== DONOR LIST =====")
        for donor in self.donors:
            print(donor)
    # Lambda Function
    # Sort by Donation Count
    def sort_by_donation_count(self):
        sorted_donors = sorted(
            self.donors,
            key=lambda donor:
            len(donor.donation_history),
            reverse=True
        )
        print("\n===== SORTED DONORS =====")
        for donor in sorted_donors:
            print(
                donor.name,
                "-",
                len(donor.donation_history)
            )