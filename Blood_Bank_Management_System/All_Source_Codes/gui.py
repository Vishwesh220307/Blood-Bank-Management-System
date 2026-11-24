import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import date
from services.donor_service import DonorService
from services.inventory_service import InventoryService
from services.donation_service import DonationService
from services.hospital_service import HospitalService
from services.request_service import RequestService
from services.camp_service import CampService
from services.distribution_service import DistributionService
from services.report_service import ReportService
from models.donor import Donor
from models.blood_camp import BloodCamp
from models.hospital import HospitalRepresentative
from models.blood_request import BloodRequest
from models.donation import BloodDonation
from utils.file_handler import FileHandler
# Service instances
donor_service = DonorService()
inventory_service = InventoryService()
donation_service = DonationService()
hospital_service = HospitalService()
request_service = RequestService(inventory_service)
camp_service = CampService()
distribution_service = DistributionService()
report_service = ReportService()
def load_from_latest_date(filename):
    try:
        data = FileHandler.load_json(filename)
        return data[-1].get("entries", []) if data and isinstance(data, list) and len(data) > 0 else []
    except: return []
def check_keys(data, keys):
    return all(k in data for k in keys)
def load_all_data():
    try:
        for d in load_from_latest_date("data/donors.json"):
            if check_keys(d, ["person_id", "name", "age", "gender", "mobile_number", "donor_id", "blood_group"]):
                donor_service.donors.append(Donor(d["person_id"], d["name"], d["age"], d["gender"], d["mobile_number"], d["donor_id"], d["blood_group"]))
        for entry in load_from_latest_date("data/inventory.json"):
            if check_keys(entry, ["blood_group", "quantity"]):
                inventory_service.inventory.blood_units[entry["blood_group"]] = entry["quantity"]
        for camp_data in load_from_latest_date("data/camps.json"):
            if check_keys(camp_data, ["camp_id", "camp_name", "location", "camp_date"]):
                camp_service.camps.append(BloodCamp(camp_data["camp_id"], camp_data["camp_name"], camp_data["location"], camp_data["camp_date"]))
        for h in load_from_latest_date("data/hospitals.json"):
            if check_keys(h, ["person_id", "name", "age", "gender", "mobile_number", "representative_id", "hospital_name"]):
                hospital_service.hospitals.append(HospitalRepresentative(h["person_id"], h["name"], h["age"], h["gender"], h["mobile_number"], h["representative_id"], h["hospital_name"]))
        for r in load_from_latest_date("data/requests.json"):
            if check_keys(r, ["request_id", "hospital_name", "blood_group", "quantity"]):
                request = BloodRequest(r["request_id"], r["hospital_name"], r["blood_group"], r["quantity"])
                request.request_status = r.get("request_status", "Pending")
                request_service.requests.append(request)
        for d in load_from_latest_date("data/donation.json"):
            if check_keys(d, ["donation_id", "donor", "donation_date", "quantity"]):
                donation_service.donations.append(BloodDonation(d["donation_id"], d["donor"], d["donation_date"], d["quantity"]))
    except Exception as e: pass
def save_all_data():
    try:
        today = str(date.today())
        FileHandler.append_json_with_date("data/donors.json", [{"person_id": d.person_id, "name": d.name, "age": d.age, "gender": d.gender, "mobile_number": d.mobile_number, "donor_id": d.donor_id, "blood_group": d.blood_group} for d in donor_service.donors], today)
        FileHandler.append_json_with_date("data/inventory.json", [{"blood_group": bg, "quantity": qty} for bg, qty in inventory_service.inventory.blood_units.items()], today)
        FileHandler.append_json_with_date("data/camps.json", [{"camp_id": c.camp_id, "camp_name": c.camp_name, "location": c.location, "camp_date": c.camp_date, "participants": len(c.participants)} for c in camp_service.camps], today)
        FileHandler.append_json_with_date("data/hospitals.json", [{"person_id": h.person_id, "name": h.name, "age": h.age, "gender": h.gender, "mobile_number": h.mobile_number, "representative_id": h.representative_id, "hospital_name": h.hospital_name} for h in hospital_service.hospitals], today)
        FileHandler.append_json_with_date("data/requests.json", [{"request_id": r.request_id, "hospital_name": r.hospital_name, "blood_group": r.blood_group, "quantity": r.quantity, "request_status": r.request_status} for r in request_service.requests], today)
        FileHandler.append_json_with_date("data/donation.json", [{"donation_id": d.donation_id, "donor": d.donor, "donation_date": d.donation_date, "quantity": d.quantity} for d in donation_service.donations], today)
        report_service.export_donor_report(donor_service.donors)
        report_service.export_camp_report(camp_service.camps)
        report_service.export_donation_report(donation_service.donations)
        report_service.export_hospital_report(hospital_service.hospitals)
        report_service.export_stock_report(inventory_service.inventory.blood_units)
    except: pass
class BloodBankGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🩸 Blood Bank Management System")
        self.root.geometry("1000x900")
        self.root.config(bg="#f5f7fa")
        # Modern color scheme
        self.primary_color = "#d32f2f"      # Red for blood bank
        self.secondary_color = "#1976d2"    # Blue
        self.accent_color = "#f57c00"       # Orange
        self.text_color = "#212121"         # Dark gray
        self.light_bg = "#ffffff"           # White
        self.hover_color = "#e53935"        # Darker red     
        # Configure styles
        self.setup_styles()
        load_all_data()
        self.create_main_menu()
    def setup_styles(self):
        """Setup modern Tkinter styles"""
        style = ttk.Style()
        style.theme_use('clam')
        # Configure button styles
        style.configure('Heading.TLabel', font=('Segoe UI', 24, 'bold'), foreground=self.primary_color)
        style.configure('Title.TLabel', font=('Segoe UI', 18, 'bold'), foreground=self.text_color)
        style.configure('SubTitle.TLabel', font=('Segoe UI', 14, 'bold'), foreground=self.text_color)
        # Main menu button style
        style.configure('Main.TButton', font=('Segoe UI', 11, 'bold'), padding=15)
        style.configure('Menu.TButton', font=('Segoe UI', 10), padding=12)
        style.configure('Action.TButton', font=('Segoe UI', 9, 'bold'), padding=8)
        style.configure('Back.TButton', font=('Segoe UI', 9))
    def clear(self):
        for w in self.root.winfo_children(): w.destroy()
    def create_header(self, parent, title, subtitle=""):
        """Create a professional header"""
        header = tk.Frame(parent, bg=self.primary_color, height=80)
        header.pack(fill=tk.X, pady=(0, 20))
        tk.Label(header, text=title, font=('Segoe UI', 20, 'bold'), fg="#ffffff", bg=self.primary_color).pack(pady=15)
        if subtitle:
            tk.Label(header, text=subtitle, font=('Segoe UI', 10), fg="#ffcccc", bg=self.primary_color).pack()
    def create_card_button(self, parent, text, command, icon="", color=None):
        """Create a beautiful card-style button"""
        btn_color = color or self.secondary_color
        card = tk.Frame(parent, bg=self.light_bg, height=80, relief=tk.RAISED, bd=0)
        card.pack(fill=tk.X, pady=8, padx=0)
        card.config(highlightthickness=0)
        def on_enter(e):
            card.config(bg="#f0f0f0")
        def on_leave(e):
            card.config(bg=self.light_bg)
        def on_click():
            command()
        card.bind("<Enter>", on_enter)
        card.bind("<Leave>", on_leave)
        card.bind("<Button-1>", lambda e: on_click())
        btn = tk.Label(card, text=f"{icon}\n{text}", font=('Segoe UI', 11, 'bold'), 
                      fg=btn_color, bg=self.light_bg, cursor="hand2", wraplength=200)
        btn.pack(side=tk.LEFT, padx=20, pady=15, fill=tk.BOTH, expand=True)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.bind("<Button-1>", lambda e: on_click())
    def back(self, p):
        """Create a styled back button"""
        back_frame = tk.Frame(p, bg="transparent")
        back_frame.pack(anchor="nw", padx=15, pady=10)
        ttk.Button(back_frame, text="← Back to Menu", command=self.create_main_menu, style='Back.TButton').pack()
    def dialog(self, title, fields, func):
        """Create a modern dialog"""
        d = tk.Toplevel(self.root)
        d.title(title)
        d.geometry("500x500")
        d.config(bg="#f5f7fa")
        # Header
        header = tk.Frame(d, bg=self.primary_color, height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text=title, font=('Segoe UI', 14, 'bold'), fg="#ffffff", bg=self.primary_color).pack(pady=15)
        # Content frame
        content = tk.Frame(d, bg="#f5f7fa")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        e = {}
        for f in fields:
            tk.Label(content, text=f, font=('Segoe UI', 10, 'bold'), bg="#f5f7fa", fg=self.text_color).pack(anchor="w", pady=(10, 3))
            if "Blood" in f or "Gender" in f:
                w = ttk.Combobox(content, values=['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'M/F'] if "Blood" in f else ['M', 'F'], width=45, font=('Segoe UI', 10))
            else:
                w = tk.Entry(content, font=('Segoe UI', 10), bd=1, relief=tk.SOLID, highlightthickness=0)
                w.config(bg="#ffffff")
            w.pack(fill=tk.X, pady=(0, 15))
            e[f] = w
        # Button frame
        btn_frame = tk.Frame(content, bg="#f5f7fa")
        btn_frame.pack(fill=tk.X, pady=(20, 0))
        ttk.Button(btn_frame, text="Submit", command=lambda: func(e, d), style='Action.TButton').pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text="Cancel", command=d.destroy, style='Action.TButton').pack(side=tk.RIGHT, padx=5)
    def view(self, title, data):
        """Create a modern data view dialog"""
        d = tk.Toplevel(self.root)
        d.title(title)
        d.geometry("700x500")
        d.config(bg="#f5f7fa")
        # Header
        header = tk.Frame(d, bg=self.primary_color, height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text=title, font=('Segoe UI', 14, 'bold'), fg="#ffffff", bg=self.primary_color).pack(pady=15)
        # Content
        content = tk.Frame(d, bg="#f5f7fa")
        content.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        t = scrolledtext.ScrolledText(content, width=80, height=25, font=('Courier New', 9), bg="#ffffff", bd=1, relief=tk.SOLID)
        t.pack(fill=tk.BOTH, expand=True)
        t.insert(tk.END, data if data else "No data found")
        t.config(state=tk.DISABLED)
    def create_main_menu(self):
        """Create a stunning main menu"""
        self.clear()
        # Main frame with scrollbar
        main = tk.Frame(self.root, bg="#f5f7fa")
        main.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas and scrollbar for scrollable content
        canvas = tk.Canvas(main, bg="#f5f7fa", highlightthickness=0)
        scrollbar = ttk.Scrollbar(main, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f5f7fa")
        
        def on_frame_configure(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            # Make scrollable_frame width match canvas width
            canvas.itemconfig(canvas_window, width=canvas.winfo_width())
        
        def on_canvas_configure(event=None):
            canvas.itemconfig(canvas_window, width=event.width)
        
        scrollable_frame.bind("<Configure>", on_frame_configure)
        canvas.bind("<Configure>", on_canvas_configure)
        
        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Header with gradient effect
        header = tk.Frame(scrollable_frame, bg=self.primary_color, height=120)
        header.pack(fill=tk.X, pady=(0, 30))
        tk.Label(header, text="🩸", font=('Segoe UI', 60), bg=self.primary_color).pack()
        tk.Label(header, text="BLOOD BANK MANAGEMENT SYSTEM", font=('Segoe UI', 20, 'bold'), fg="#ffffff", bg=self.primary_color).pack()
        tk.Label(header, text="Professional Blood Donation & Distribution Management", font=('Segoe UI', 10), fg="#ffcccc", bg=self.primary_color).pack()
        
        # Main content with 2-column layout
        content = tk.Frame(scrollable_frame, bg="#f5f7fa")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left column
        left = tk.Frame(content, bg="#f5f7fa")
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        tk.Label(left, text="Core Services", font=('Segoe UI', 12, 'bold'), bg="#f5f7fa", fg=self.primary_color).pack(anchor="w", pady=(0, 10))
        menus_left = [
            ("👤 Donor Management", self.menu_donor),
            ("🩸 Inventory Management", self.menu_inv),
            ("💉 Donation Management", self.menu_don),
            ("🏥 Hospital Management", self.menu_hosp),
        ]
        for txt, cmd in menus_left:
            self.create_card_button(left, txt, cmd, color=self.secondary_color)
        
        # Right column
        right = tk.Frame(content, bg="#f5f7fa")
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        tk.Label(right, text="Operations", font=('Segoe UI', 12, 'bold'), bg="#f5f7fa", fg=self.accent_color).pack(anchor="w", pady=(0, 10))
        menus_right = [
            ("📋 Request Management", self.menu_req),
            ("🏕️ Camp Management", self.menu_camp),
            ("🚚 Distribution", self.menu_dist),
            ("📊 Reports", self.menu_rep),
        ]
        for txt, cmd in menus_right:
            self.create_card_button(right, txt, cmd, color=self.accent_color)
        
        # Bottom section
        bottom = tk.Frame(scrollable_frame, bg="#f5f7fa")
        bottom.pack(fill=tk.X, padx=20, pady=20)
        tk.Label(bottom, text="Data Management", font=('Segoe UI', 12, 'bold'), bg="#f5f7fa", fg="#666").pack(anchor="w", pady=(0, 10))
        btn_frame = tk.Frame(bottom, bg="#f5f7fa")
        btn_frame.pack(fill=tk.X)
        self.create_card_button(btn_frame, "💾 Save Data", self.save_act, color="#4caf50")
        self.create_card_button(btn_frame, "📂 Load Data", self.load_act, color="#2196f3")
        self.create_card_button(btn_frame, "❌ Exit System", self.root.quit, color="#f44336")
    def create_submenu(self, title, buttons):
        """Create a styled submenu"""
        self.clear()
        main = tk.Frame(self.root, bg="#f5f7fa")
        main.pack(fill=tk.BOTH, expand=True)
        # Back button
        back_frame = tk.Frame(main, bg="#f5f7fa")
        back_frame.pack(anchor="nw", padx=15, pady=10)
        tk.Button(back_frame, text="← Back", command=self.create_main_menu).pack()
        # Header
        header = tk.Frame(main, bg=self.primary_color, height=80)
        header.pack(fill=tk.X, padx=0, pady=(0, 20))
        tk.Label(header, text=title, font=('Segoe UI', 18, 'bold'), fg="#ffffff", bg=self.primary_color).pack(pady=15)
        # Content
        content = tk.Frame(main, bg="#f5f7fa")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        for txt, cmd in buttons:
            self.create_card_button(content, txt, cmd)
    # ============ DONOR ============
    def menu_donor(self):
        buttons = [("👤 Register New Donor", self.reg_donor), ("📋 View All Donors", self.view_donors), 
                  ("🔍 Search Donor", self.search_donor), ("✅ Check Eligibility", self.check_elig)]
        self.create_submenu("👤 DONOR MANAGEMENT", buttons)
    def reg_donor(self):
        def save(e, d):
            try:
                donor_service.register_donor(e["Person ID"].get(), e["Name"].get(), int(e["Age"].get()), 
                                           e["Gender (M/F)"].get(), e["Mobile Number"].get(), e["Donor ID"].get(), e["Blood Group"].get())
                messagebox.showinfo("✓ Success", "Donor registered successfully!")
                d.destroy()
                self.menu_donor()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        self.dialog("Register New Donor", ["Person ID", "Name", "Age", "Gender (M/F)", "Mobile Number", "Donor ID", "Blood Group"], save)
    def view_donors(self):
        data = "ID\t| NAME\t\t| BLOOD GROUP\t| ELIGIBLE\n" + "="*60 + "\n"
        data += "\n".join([f"{d.person_id}\t| {d.name[:15]:15}\t| {d.blood_group:5}\t| {'Yes' if d.check_eligibility() else 'No'}" for d in donor_service.donors]) if donor_service.donors else "No donors found"
        self.view("👤 All Donors", data)
    def search_donor(self):
        d = tk.Toplevel(self.root)
        d.title("Search Donor")
        d.geometry("450x250")
        d.config(bg="#f5f7fa")
        header = tk.Frame(d, bg=self.primary_color, height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Search Donor", font=('Segoe UI', 14, 'bold'), fg="#ffffff", bg=self.primary_color).pack(pady=15)
        content = tk.Frame(d, bg="#f5f7fa")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        tk.Label(content, text="Enter Donor ID:", font=('Segoe UI', 10, 'bold'), bg="#f5f7fa").pack(anchor="w", pady=(0, 5))
        e = tk.Entry(content, font=('Segoe UI', 10), width=40)
        e.pack(fill=tk.X, pady=(0, 20))
        def search():
            x = next((y for y in donor_service.donors if y.donor_id == e.get()), None)
            if x:
                info = f"Name: {x.name}\nAge: {x.age}\nBlood Group: {x.blood_group}\nGender: {x.gender}\nEligible: {'Yes' if x.check_eligibility() else 'No'}"
                messagebox.showinfo("✓ Found", info)
            else:
                messagebox.showerror("✗ Not Found", "Donor not found in database")
        ttk.Button(content, text="Search", command=search).pack(pady=10)
    def check_elig(self):
        d = tk.Toplevel(self.root)
        d.title("Check Eligibility")
        d.geometry("450x250")
        d.config(bg="#f5f7fa")
        header = tk.Frame(d, bg=self.primary_color, height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Check Donor Eligibility", font=('Segoe UI', 14, 'bold'), fg="#ffffff", bg=self.primary_color).pack(pady=15)
        content = tk.Frame(d, bg="#f5f7fa")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        tk.Label(content, text="Enter Donor Name:", font=('Segoe UI', 10, 'bold'), bg="#f5f7fa").pack(anchor="w", pady=(0, 5))
        e = tk.Entry(content, font=('Segoe UI', 10), width=40)
        e.pack(fill=tk.X, pady=(0, 20))
        def chk():
            x = next((y for y in donor_service.donors if y.name.lower() == e.get().lower()), None)
            if x:
                status = "✓ YES - Eligible to donate" if x.check_eligibility() else "✗ NO - Not eligible at this time"
                messagebox.showinfo("Eligibility Status", f"{x.name}\n\n{status}")
            else:
                messagebox.showerror("✗ Not Found", "Donor not found")
        tk.Button(content, text="Check", command=chk).pack(pady=10)
    # ============ INVENTORY ============
    def menu_inv(self):
        buttons = [("➕ Add Stock", self.add_stock), ("➖ Remove Stock", self.rem_stock), ("📊 View Inventory", self.view_inv)]
        self.create_submenu("🩸 INVENTORY MANAGEMENT", buttons)
    def add_stock(self):
        def save(e, d):
            try:
                inventory_service.add_stock(e["Blood Group"].get(), int(e["Quantity (units)"].get()))
                messagebox.showinfo("✓ Success", "Stock added successfully!")
                d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        self.dialog("Add Blood Stock", ["Blood Group", "Quantity (units)"], save)
    def rem_stock(self):
        def save(e, d):
            try:
                inventory_service.remove_stock(e["Blood Group"].get(), int(e["Quantity (units)"].get()))
                messagebox.showinfo("✓ Success", "Stock removed successfully!")
                d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        self.dialog("Remove Blood Stock", ["Blood Group", "Quantity (units)"], save)
    def view_inv(self):
        data = "BLOOD GROUP\t| QUANTITY (Units)\n" + "="*40 + "\n"
        data += "\n".join([f"{bg:8}\t| {qty:5}" for bg, qty in inventory_service.inventory.blood_units.items()])
        self.view("🩸 Blood Inventory", data)
    # ============ DONATION ============
    def menu_don(self):
        buttons = [("💉 Record Donation", self.rec_don), ("📋 View All Donations", self.view_don)]
        self.create_submenu("💉 DONATION MANAGEMENT", buttons)
    def rec_don(self):
        def save(e, d):
            try:
                x = next((y for y in donor_service.donors if y.name.lower() == e["Donor Name"].get().lower()), None)
                if not x: messagebox.showerror("✗ Error", "Donor not found. Register first!")
                elif not x.check_eligibility(): messagebox.showerror("✗ Error", "Donor is not eligible to donate")
                else:
                    donation_service.record_donation(e["Donation ID"].get(), x, e["Date (YYYY-MM-DD)"].get(), int(e["Quantity (units)"].get()))
                    inventory_service.add_stock(x.blood_group, int(e["Quantity (units)"].get()))
                    messagebox.showinfo("✓ Success", "Donation recorded & inventory updated!")
                    d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        self.dialog("Record Donation", ["Donation ID", "Donor Name", "Date (YYYY-MM-DD)", "Quantity (units)"], save)
    def view_don(self):
        data = "ID\t| DONOR\t\t| DATE\t\t| QUANTITY\n" + "="*60 + "\n"
        data += "\n".join([f"{d.donation_id}\t| {d.donor[:12]:12}\t| {d.donation_date}\t| {d.quantity}u" for d in donation_service.donations]) if donation_service.donations else "No donations recorded"
        self.view("💉 All Donations", data)
    # ============ HOSPITAL ============
    def menu_hosp(self):
        buttons = [("🏥 Register Hospital", self.reg_hosp), ("📋 View All Hospitals", self.view_hosp)]
        self.create_submenu("🏥 HOSPITAL MANAGEMENT", buttons)
    def reg_hosp(self):
        def save(e, d):
            try:
                hospital_service.register_hospital(e["Person ID"].get(), e["Name"].get(), int(e["Age"].get()), e["Gender (M/F)"].get(), 
                                                  e["Mobile Number"].get(), e["Representative ID"].get(), e["Hospital Name"].get())
                messagebox.showinfo("✓ Success", "Hospital registered!")
                d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        self.dialog("Register Hospital", ["Person ID", "Name", "Age", "Gender (M/F)", "Mobile Number", "Representative ID", "Hospital Name"], save)
    def view_hosp(self):
        data = "NAME\t\t| HOSPITAL\t\t| REP ID\n" + "="*60 + "\n"
        data += "\n".join([f"{h.name[:12]:12}\t| {h.hospital_name[:15]:15}\t| {h.representative_id}" for h in hospital_service.hospitals]) if hospital_service.hospitals else "No hospitals found"
        self.view("🏥 All Hospitals", data)
    # ============ REQUEST ============
    def menu_req(self):
        buttons = [("➕ Create Request", self.create_req), ("📋 View Requests", self.view_req), 
                  ("✅ Approve Request", self.appr_req), ("❌ Reject Request", self.rej_req)]
        self.create_submenu("📋 REQUEST MANAGEMENT", buttons)
    def create_req(self):
        def save(e, d):
            try:
                request_service.create_request(e["Request ID"].get(), e["Hospital Name"].get(), e["Blood Group"].get(), int(e["Quantity (units)"].get()))
                messagebox.showinfo("✓ Success", "Request created!")
                d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        self.dialog("Create Blood Request", ["Request ID", "Hospital Name", "Blood Group", "Quantity (units)"], save)
    def view_req(self):
        data = "ID\t| HOSPITAL\t| BG\t| QTY\t| STATUS\n" + "="*65 + "\n"
        data += "\n".join([f"{r.request_id}\t| {r.hospital_name[:10]:10}\t| {r.blood_group}\t| {r.quantity}\t| {r.request_status}" for r in request_service.requests]) if request_service.requests else "No requests"
        self.view("📋 All Requests", data)
    def appr_req(self):
        d = tk.Toplevel(self.root)
        d.title("Approve Request")
        d.geometry("450x250")
        d.config(bg="#f5f7fa")
        header = tk.Frame(d, bg="#4caf50", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Approve Request", font=('Segoe UI', 14, 'bold'), fg="#ffffff", bg="#4caf50").pack(pady=15)
        content = tk.Frame(d, bg="#f5f7fa")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        tk.Label(content, text="Request ID:", font=('Segoe UI', 10, 'bold'), bg="#f5f7fa").pack(anchor="w", pady=(0, 5))
        e = tk.Entry(content, font=('Segoe UI', 10), width=40)
        e.pack(fill=tk.X, pady=(0, 20))
        def appr():
            try:
                request_service.approve_request(e.get())
                messagebox.showinfo("✓ Success", "Request approved!")
                d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        ttk.Button(content, text="Approve", command=appr).pack(pady=10)
    def rej_req(self):
        d = tk.Toplevel(self.root)
        d.title("Reject Request")
        d.geometry("450x250")
        d.config(bg="#f5f7fa")
        header = tk.Frame(d, bg="#f44336", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Reject Request", font=('Segoe UI', 14, 'bold'), fg="#ffffff", bg="#f44336").pack(pady=15)
        content = tk.Frame(d, bg="#f5f7fa")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        tk.Label(content, text="Request ID:", font=('Segoe UI', 10, 'bold'), bg="#f5f7fa").pack(anchor="w", pady=(0, 5))
        e = tk.Entry(content, font=('Segoe UI', 10), width=40)
        e.pack(fill=tk.X, pady=(0, 20))
        def rej():
            try:
                request_service.reject_request(e.get())
                messagebox.showinfo("✓ Success", "Request rejected!")
                d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        ttk.Button(content, text="Reject", command=rej).pack(pady=10)
    # ============ CAMP ============
    def menu_camp(self):
        buttons = [("🏕️ Organize Camp", self.org_camp), ("📋 View All Camps", self.view_camp)]
        self.create_submenu("🏕️ CAMP MANAGEMENT", buttons)
    def org_camp(self):
        def save(e, d):
            try:
                camp_service.organize_camp(e["Camp ID"].get(), e["Camp Name"].get(), e["Location"].get(), e["Date (YYYY-MM-DD)"].get())
                messagebox.showinfo("✓ Success", "Camp organized!")
                d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        self.dialog("Organize Blood Camp", ["Camp ID", "Camp Name", "Location", "Date (YYYY-MM-DD)"], save)
    def view_camp(self):
        data = "ID\t| CAMP NAME\t| LOCATION\t| DATE\n" + "="*65 + "\n"
        data += "\n".join([f"{c.camp_id}\t| {c.camp_name[:12]:12}\t| {c.location[:10]:10}\t| {c.camp_date}" for c in camp_service.camps]) if camp_service.camps else "No camps organized"
        self.view("🏕️ All Camps", data)
    # ============ DISTRIBUTION ============
    def menu_dist(self):
        buttons = [("🚚 Issue Blood", self.issue_blood), ("📊 View Records", self.view_dist)]
        self.create_submenu("🚚 DISTRIBUTION MANAGEMENT", buttons)
    def issue_blood(self):
        def save(e, d):
            try:
                distribution_service.issue_blood(e["Hospital Name"].get(), e["Blood Group"].get(), int(e["Quantity (units)"].get()))
                messagebox.showinfo("✓ Success", "Blood issued successfully!")
                d.destroy()
            except Exception as ex: messagebox.showerror("✗ Error", str(ex))
        self.dialog("Issue Blood to Hospital", ["Hospital Name", "Blood Group", "Quantity (units)"], save)
    def view_dist(self):
        self.view("🚚 Distribution Records", "View distribution_report.csv in reports folder\n\nDistribution records are automatically logged to CSV files.")
    # ============ REPORTS ============
    def menu_rep(self):
        buttons = [("👤 Donor Report", lambda: self.gen_rep("donor")), ("🏕️ Camp Report", lambda: self.gen_rep("camp")), 
                  ("💉 Donation Report", lambda: self.gen_rep("donation")), ("🏥 Hospital Report", lambda: self.gen_rep("hospital")),
                  ("🩸 Stock Report", lambda: self.gen_rep("stock")), ("📋 All Reports", lambda: self.gen_rep("all"))]
        self.create_submenu("📊 REPORT MANAGEMENT", buttons)
    def gen_rep(self, rt):
        try:
            if rt == "all":
                report_service.export_donor_report(donor_service.donors)
                report_service.export_camp_report(camp_service.camps)
                report_service.export_donation_report(donation_service.donations)
                report_service.export_hospital_report(hospital_service.hospitals)
                report_service.export_stock_report(inventory_service.inventory.blood_units)
                messagebox.showinfo("✓ Success", "All reports generated successfully!\n\nCheck reports/ folder")
            elif rt == "donor": report_service.export_donor_report(donor_service.donors)
            elif rt == "camp": report_service.export_camp_report(camp_service.camps)
            elif rt == "donation": report_service.export_donation_report(donation_service.donations)
            elif rt == "hospital": report_service.export_hospital_report(hospital_service.hospitals)
            elif rt == "stock": report_service.export_stock_report(inventory_service.inventory.blood_units)
            if rt != "all": messagebox.showinfo("✓ Success", f"{rt.capitalize()} report generated!\n\nCheck reports/ folder")
        except Exception as e: messagebox.showerror("✗ Error", str(e))
    def save_act(self):
        try:
            save_all_data()
            messagebox.showinfo("✓ Success", "All data saved successfully!")
        except Exception as e: messagebox.showerror("✗ Error", str(e))
    def load_act(self):
        try:
            donor_service.donors.clear()
            inventory_service.inventory.blood_units.clear()
            camp_service.camps.clear()
            hospital_service.hospitals.clear()
            request_service.requests.clear()
            donation_service.donations.clear()
            load_all_data()
            messagebox.showinfo("✓ Success", "Data loaded successfully!")
            self.create_main_menu()
        except Exception as e: messagebox.showerror("✗ Error", str(e))
if __name__ == "__main__":
    root = tk.Tk()
    app = BloodBankGUI(root)
    root.mainloop()
