from models.donation import BloodDonation
from utils.decorator import log_activity


class DonationService:

    def __init__(self):
        self.donations = []

    # -------------------------
    # Record Donation
    # -------------------------
    @log_activity
    def record_donation(
            self,
            donation_id,
            donor,
            donation_date,
            quantity):

        donation = BloodDonation(
            donation_id,
            donor,
            donation_date,
            quantity
        )

        self.donations.append(donation)

        donor.donate_blood(
            donation_date
        )

        donation.record_donation()

    # -------------------------
    # View Donation History
    # -------------------------
    def view_donation_history(
            self,
            donor):

        donor.view_donation_history()

    # -------------------------
    # Check Donor Eligibility
    # -------------------------
    def check_donor_eligibility(
            self,
            donor):

        donor.check_eligibility()

    # -------------------------
    # View All Donations
    # -------------------------
    def view_all_donations(self):

        if not self.donations:
            print("No Donations Available")
            return

        print("\n===== DONATION RECORDS =====")

        for donation in self.donations:
            print(donation)

    # -------------------------
    # Generate Certificates
    # -------------------------
    def generate_certificate(
            self,
            donation_id):

        for donation in self.donations:

            if donation.donation_id == donation_id:

                donation.generate_certificate()
                return

        print("Donation Record Not Found")

    # -------------------------
    # Sort Donations
    # Lambda Function
    # -------------------------
    def sort_by_quantity(self):

        sorted_donations = sorted(
            self.donations,
            key=lambda donation:
            donation.quantity,
            reverse=True
        )

        print("\n===== SORTED DONATIONS =====")

        for donation in sorted_donations:
            print(donation)

    # -------------------------
    # Donation Generator
    # Generator Function
    # -------------------------
    def donation_generator(self):

        for donation in self.donations:
            yield donation