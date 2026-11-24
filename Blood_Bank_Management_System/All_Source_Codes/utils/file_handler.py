import json
import csv
import os
from utils.exception import FileNotFoundCustomError
class FileHandler:
    @staticmethod
    def save_json(filename, data):
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"{filename} saved successfully.")
        except Exception as e:
            print("Error:", e)
    @staticmethod
    def load_json(filename):
        try:
            if not os.path.exists(filename):
                raise FileNotFoundCustomError(
                    f"{filename} not found."
                )
            with open(filename, "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundCustomError as e:
            print(e)
            return []
        except Exception as e:
            print("Error:", e)
            return []
    @staticmethod
    def generate_csv_report(filename, data):
        try:
            if not data:
                print("No data available.")
                return
            with open(
                    filename,
                    "w",
                    newline=""
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=data[0].keys()
                )
                writer.writeheader()
                writer.writerows(data)
            print(
                f"{filename} report generated successfully."
            )
        except Exception as e:
            print("Error:", e)
    @staticmethod
    def file_exists(filename):
        return os.path.exists(filename)
    @staticmethod
    def append_json_with_date(filename, new_entries, date_str):
        """
        Append data to JSON file organized by date.
        Prevents overwriting by grouping entries by date.
        Format:
        [
            {
                "date": "2024-01-15",
                "entries": [...]
            }
        ]
        """
        try:
            # Load existing data
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    data = json.load(file)
            else:
                data = []       
            # Ensure data is a list
            if not isinstance(data, list):
                data = []           
            # Check if today's entry exists
            today_entry = None
            for entry in data:
                if entry.get("date") == date_str:
                    today_entry = entry
                    break
            # If today's entry exists, update it; otherwise create new one
            if today_entry:
                # Replace today's entries with new data
                today_entry["entries"] = new_entries
            else:
                # Add new date entry
                data.append({
                    "date": date_str,
                    "entries": new_entries
                })
            # Save updated data
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"{filename} saved successfully.")
        except Exception as e:
            print("Error:", e)