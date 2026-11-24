class BloodCompatibility:
    COMPATIBILITY = {
        "O-": ("O-",),
        "O+": ("O+","O-"),
        "A-": ("A-","O-"),
        "A+": ("A+","A-","O+","O-" ),
        "B-": ("B-","O-"   ),
        "B+": ("B+","B-","O+","O-"  ),
        "AB-": ("AB-","A-","B-","O-"),
        "AB+": ("AB+","AB-","A+","A-","B+","B-","O+", "O-"  )
    }
    @staticmethod
    def check_compatibility(recipient_group, donor_group):
        if recipient_group not in BloodCompatibility.COMPATIBILITY:
            return False
        return donor_group in BloodCompatibility.COMPATIBILITY[
            recipient_group
        ]
    @staticmethod
    def show_compatible_donors(recipient_group):
        if recipient_group not in BloodCompatibility.COMPATIBILITY:
            print("Invalid Blood Group")
            return
        print(
            f"Compatible Donors for {recipient_group}:"
        )
        for group in BloodCompatibility.COMPATIBILITY[
            recipient_group
        ]:
            print(group)