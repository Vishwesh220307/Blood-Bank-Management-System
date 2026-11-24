from utils.validator import Validator
class InputHandler:
    """Handles user input with validation and safe type conversions"""
    @staticmethod
    def get_integer(prompt, min_val=None, max_val=None):
        """Get validated integer input from user"""
        while True:
            try:
                value = int(input(prompt))  
                if min_val is not None and value < min_val:
                    print(f"Error: Value must be at least {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Error: Value must be at most {max_val}")
                    continue                    
                return value            
            except ValueError:
                print("Error: Please enter a valid number")
            except KeyboardInterrupt:
                print("\nOperation cancelled")
                return None
    @staticmethod
    def get_string(prompt, min_length=1, max_length=None):
        """Get validated string input from user"""
        while True:
            try:
                value = input(prompt).strip()               
                if len(value) < min_length:
                    print(f"Error: Input must be at least {min_length} character(s)")
                    continue                    
                if max_length and len(value) > max_length:
                    print(f"Error: Input must be at most {max_length} character(s)")
                    continue                    
                return value                
            except KeyboardInterrupt:
                print("\nOperation cancelled")
                return None
    @staticmethod
    def get_age(prompt="Age: "):
        """Get validated age (18-65 for donors)"""
        while True:
            try:
                age = int(input(prompt))
                if not Validator.validate_age(age):
                    print(f"Error: Age must be between 18 and 65 (Got {age})")
                    continue                   
                return age               
            except ValueError:
                print("Error: Please enter a valid age")
            except KeyboardInterrupt:
                print("\nOperation cancelled")
                return None
    @staticmethod
    def get_mobile(prompt="Mobile: "):
        """Get validated mobile number"""
        while True:
            try:
                mobile = input(prompt).strip()                
                if not Validator.validate_mobile(mobile):
                    print("Error: Mobile must be 10 digits")
                    continue                   
                return mobile               
            except KeyboardInterrupt:
                print("\nOperation cancelled")
                return None
    @staticmethod
    def get_blood_group(prompt="Blood Group: "):
        """Get validated blood group"""
        while True:
            try:
                bg = input(prompt).strip().upper()               
                if not Validator.validate_blood_group(bg):
                    valid_groups = ", ".join(Validator.VALID_BLOOD_GROUPS)
                    print(f"Error: Invalid blood group. Valid: {valid_groups}")
                    continue                    
                return bg               
            except KeyboardInterrupt:
                print("\nOperation cancelled")
                return None
    @staticmethod
    def get_quantity(prompt="Quantity: "):
        """Get validated positive quantity"""
        while True:
            try:
                qty = int(input(prompt))               
                if not Validator.validate_quantity(qty):
                    print("Error: Quantity must be greater than 0")
                    continue                   
                return qty               
            except ValueError:
                print("Error: Please enter a valid number")
            except KeyboardInterrupt:
                print("\nOperation cancelled")
                return None
    @staticmethod
    def get_choice(prompt="Enter Choice: ", valid_choices=None):
        """Get menu choice with optional validation"""
        while True:
            try:
                choice = input(prompt).strip()               
                if valid_choices and choice not in valid_choices:
                    print(f"Error: Please enter one of: {', '.join(valid_choices)}")
                    continue                   
                return choice               
            except KeyboardInterrupt:
                print("\nOperation cancelled")
                return None
