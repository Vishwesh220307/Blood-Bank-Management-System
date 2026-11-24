class Validator:

    VALID_BLOOD_GROUPS = ("A+","A-","B+","B-","AB+","AB-","O+","O-")
    @staticmethod
    def validate_blood_group(blood_group):
        if blood_group in Validator.VALID_BLOOD_GROUPS:
            return True
        return False
    @staticmethod
    def validate_age(age):
        if 18 <= age <= 65:
            return True
        return False
    @staticmethod
    def validate_mobile(mobile_number):
        if (
            len(mobile_number) == 10
            and mobile_number.isdigit()
        ):
            return True
        return False
    @staticmethod
    def validate_quantity(quantity):
        if quantity > 0:
            return True
        return False
    @staticmethod
    def validate_name(name):
        if len(name.strip()) > 0:
            return True

        return False
    @staticmethod
    def validate_donor_id(donor_id):
        if donor_id.startswith("D"):
            return True
        return False