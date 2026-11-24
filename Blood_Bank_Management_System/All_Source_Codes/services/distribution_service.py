from utils.decorator import log_activity


class DistributionService:

    def __init__(self):

        self.distributions = []

    @log_activity
    def issue_blood(
            self,
            hospital_name,
            blood_group,
            quantity):

        record = {
            "hospital": hospital_name,
            "blood_group": blood_group,
            "quantity": quantity
        }

        self.distributions.append(record)

        print(
            f"{quantity} units of "
            f"{blood_group} issued to "
            f"{hospital_name}"
        )

    @log_activity
    def transfer_blood(
            self,
            source,
            destination,
            blood_group,
            quantity):

        print(
            f"{quantity} units of "
            f"{blood_group} transferred "
            f"from {source} to {destination}"
        )

    @log_activity
    def emergency_allocation(
            self,
            hospital_name,
            blood_group,
            quantity):

        print(
            f"Emergency Allocation : "
            f"{quantity} units of "
            f"{blood_group} issued to "
            f"{hospital_name}"
        )

    def view_distribution_records(self):

        if not self.distributions:
            print("No Distribution Records")
            return

        print("\n===== DISTRIBUTION RECORDS =====")

        for record in self.distributions:
            print(record)