from datetime import datetime


class Report:

    def __init__(self, report_id, report_type):
        self.report_id = report_id
        self.report_type = report_type
        self.generated_date = datetime.now()

    def generate_report(self):

        print("\n===== REPORT GENERATED =====")
        print("Report ID:", self.report_id)
        print("Report Type:", self.report_type)
        print("Generated On:", self.generated_date)

    def export_report(self):

        print(f"{self.report_type} exported successfully.")

    def __str__(self):
        return (
            f"Report ID: {self.report_id}, "
            f"Type: {self.report_type}"
        )

    def __repr__(self):
        return (
            f"Report('{self.report_id}',"
            f"'{self.report_type}')"
        )