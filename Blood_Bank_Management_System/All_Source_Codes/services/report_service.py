from models.report import Report
from utils.decorator import log_activity
from utils.file_handler import FileHandler
from datetime import datetime


class ReportService:

    def __init__(self):

        self.reports = []

    @log_activity
    def generate_report(
            self,
            report_id,
            report_type):

        report = Report(
            report_id,
            report_type
        )

        self.reports.append(report)

        report.generate_report()

    @log_activity
    def export_report(
            self,
            filename,
            data):

        FileHandler.generate_csv_report(
            filename,
            data
        )

    def view_reports(self):

        if not self.reports:
            print("No Reports Generated")
            return

        print("\n===== REPORT LIST =====")

        for report in self.reports:
            print(report)

    # Generator Function
    def report_generator(self):

        for report in self.reports:
            yield report

    # ─────────────────────────────────────────
    # EXPORT METHODS FOR EACH REPORT TYPE
    # ─────────────────────────────────────────

    def export_donor_report(self, donors_list):
        """Export all donors to CSV"""
        donors_data = []
        for donor in donors_list:
            donors_data.append({
                'person_id': donor.person_id,
                'name': donor.name,
                'age': donor.age,
                'gender': donor.gender,
                'mobile_number': donor.mobile_number,
                'donor_id': donor.donor_id,
                'blood_group': donor.blood_group
            })
        
        if donors_data:
            self.export_report("reports/donor_report.csv", donors_data)
            print("✓ Donor Report Exported Successfully")
        else:
            print("No donor data to export")

    def export_camp_report(self, camps_list):
        """Export all blood camps to CSV"""
        camps_data = []
        for camp in camps_list:
            camps_data.append({
                'camp_id': camp.camp_id,
                'camp_name': camp.camp_name,
                'location': camp.location,
                'camp_date': camp.camp_date,
                'participants': len(camp.participants)
            })
        
        if camps_data:
            self.export_report("reports/camp_report.csv", camps_data)
            print("✓ Camp Report Exported Successfully")
        else:
            print("No camp data to export")

    def export_donation_report(self, donations_list):
        """Export all donations to CSV"""
        donations_data = []
        for donation in donations_list:
            donations_data.append({
                'donation_id': donation.donation_id,
                'donor': donation.donor,
                'donation_date': donation.donation_date,
                'quantity': donation.quantity
            })
        
        if donations_data:
            self.export_report("reports/donation_report.csv", donations_data)
            print("✓ Donation Report Exported Successfully")
        else:
            print("No donation data to export")

    def export_hospital_report(self, hospitals_list):
        """Export all hospitals to CSV"""
        hospitals_data = []
        for hospital in hospitals_list:
            hospitals_data.append({
                'person_id': hospital.person_id,
                'name': hospital.name,
                'age': hospital.age,
                'gender': hospital.gender,
                'mobile_number': hospital.mobile_number,
                'representative_id': hospital.representative_id,
                'hospital_name': hospital.hospital_name
            })
        
        if hospitals_data:
            self.export_report("reports/hospital_report.csv", hospitals_data)
            print("✓ Hospital Report Exported Successfully")
        else:
            print("No hospital data to export")

    def export_stock_report(self, blood_units):
        """Export current blood inventory stock to CSV"""
        stock_data = []
        for blood_group, quantity in blood_units.items():
            stock_data.append({
                'blood_group': blood_group,
                'quantity': quantity
            })
        
        if stock_data:
            self.export_report("reports/stock_report.csv", stock_data)
            print("✓ Stock Report Exported Successfully")
        else:
            print("No stock data to export")