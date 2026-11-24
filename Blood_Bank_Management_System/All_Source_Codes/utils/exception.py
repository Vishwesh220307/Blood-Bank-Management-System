class InvalidDonorIDError(Exception):
    def __init__(self, message="Invalid Donor ID"):
        super().__init__(message)
class InvalidBloodGroupError(Exception):
    def __init__(self, message="Invalid Blood Group"):
        super().__init__(message)
class BloodStockNotAvailableError(Exception):
    def __init__(self, message="Blood Stock Not Available"):
        super().__init__(message)
class ExpiredBloodUnitError(Exception):
    def __init__(self, message="Blood Unit Has Expired"):
        super().__init__(message)
class DuplicateDonorRegistrationError(Exception):
    def __init__(self, message="Donor Already Registered"):
        super().__init__(message)
class FileNotFoundCustomError(Exception):
    def __init__(self, message="File Not Found"):
        super().__init__(message)
class IncorrectUserInputError(Exception):
    def __init__(self, message="Incorrect User Input"):
        super().__init__(message)