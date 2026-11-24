class BloodRequest:

    def __init__(self, request_id, hospital_name, blood_group, quantity):
        self.request_id = request_id
        self.hospital_name = hospital_name
        self.blood_group = blood_group
        self.quantity = quantity
        self.request_status = "Pending"

    def create_request(self):
        print("\n===== BLOOD REQUEST CREATED =====")
        print(f"Request ID    : {self.request_id}")
        print(f"Hospital Name : {self.hospital_name}")
        print(f"Blood Group   : {self.blood_group}")
        print(f"Quantity      : {self.quantity}")
        print(f"Status        : {self.request_status}")

    def approve_request(self):
        self.request_status = "Approved"
        print(f"Request {self.request_id} approved successfully.")

    def reject_request(self):
        self.request_status = "Rejected"
        print(f"Request {self.request_id} rejected.")

    def __str__(self):
        return (
            f"Request ID: {self.request_id}, "
            f"Hospital: {self.hospital_name}, "
            f"Blood Group: {self.blood_group}, "
            f"Quantity: {self.quantity}, "
            f"Status: {self.request_status}"
        )

    def __repr__(self):
        return (
            f"BloodRequest('{self.request_id}', "
            f"'{self.hospital_name}', "
            f"'{self.blood_group}', "
            f"{self.quantity})"
        )