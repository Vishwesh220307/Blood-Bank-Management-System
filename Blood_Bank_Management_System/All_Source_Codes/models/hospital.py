from models.person import Person


class HospitalRepresentative(Person):

    def __init__(self,
                 person_id,
                 name,
                 age,
                 gender,
                 mobile_number,
                 representative_id,
                 hospital_name):

        super().__init__(
            person_id,
            name,
            age,
            gender,
            mobile_number
        )

        self.representative_id = representative_id
        self.hospital_name = hospital_name

    def request_blood(self):

        print("Blood Request Submitted Successfully")

    def view_request_status(self):

        print("Request Status Viewed")

    def display_details(self):

        print("\n===== HOSPITAL REPRESENTATIVE =====")
        print("Representative ID:", self.representative_id)
        print("Name:", self.name)
        print("Hospital:", self.hospital_name)
        print("Mobile:", self.mobile_number)

    def __str__(self):
        return f"{self.representative_id} - {self.hospital_name}"

    def __repr__(self):
        return (
            f"HospitalRepresentative("
            f"'{self.representative_id}',"
            f"'{self.hospital_name}')"
        )