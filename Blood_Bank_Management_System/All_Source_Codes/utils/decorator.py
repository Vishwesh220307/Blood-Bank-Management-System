from datetime import datetime
def log_activity(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        print(f"Operation : {func.__name__}")
        print(f"Date & Time : {datetime.now()}")
        print("=" * 40)
        result = func(*args, **kwargs)
        print("=" * 40)
        print(f"{func.__name__} completed successfully")
        print("=" * 40)
        return result
    return wrapper