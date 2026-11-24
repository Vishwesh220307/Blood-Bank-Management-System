# 🩸 Blood Bank Management System

A Python-based desktop application designed to simplify and manage blood bank operations, including donor registration, blood inventory, donations, hospital management, blood requests, and blood donation camps.

## 📌 Project Overview

The **Blood Bank Management System** is developed using Python and Tkinter to provide a graphical interface for managing essential blood bank activities.

The application organizes donor information, monitors blood stock, maintains donation records, handles hospital blood requests, and generates reports to support efficient blood bank management.

## ✨ Key Features

- **Donor Management:** Register, search, update, and manage donor records.
- **Blood Inventory Management:** Maintain blood group-wise stock and monitor availability.
- **Donation Management:** Record and maintain blood donation details.
- **Hospital Management:** Maintain hospital and representative information.
- **Blood Request Management:** Manage hospital requests for specific blood groups and quantities.
- **Blood Camp Management:** Maintain blood donation camp information.
- **Blood Distribution:** Manage blood stock distribution.
- **Report Generation:** Generate reports in CSV format for different management activities.
- **Data Persistence:** Store and retrieve application records using JSON files.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| JSON | Data storage and management |
| CSV | Report generation |
| Object-Oriented Programming | Application structure and code organization |

## 📂 Project Structure

```text
Blood_Bank_Management_System/
│
├── All_Source_Codes/
│   │
│   ├── gui.py
│   │
│   ├── models/
│   │   ├── donor.py
│   │   ├── hospital.py
│   │   ├── donation.py
│   │   ├── blood_inventory.py
│   │   ├── blood_request.py
│   │   ├── blood_camp.py
│   │   └── person.py
│   │
│   ├── services/
│   │   ├── donor_service.py
│   │   ├── inventory_service.py
│   │   ├── donation_service.py
│   │   ├── hospital_service.py
│   │   ├── request_service.py
│   │   ├── camp_service.py
│   │   ├── distribution_service.py
│   │   └── report_service.py
│   │
│   ├── utils/
│   │   ├── file_handler.py
│   │   ├── validator.py
│   │   ├── decorator.py
│   │   ├── exception.py
│   │   └── compatibility.py
│   │
│   ├── data/
│   │   ├── donors.json
│   │   ├── hospitals.json
│   │   ├── inventory.json
│   │   ├── donation.json
│   │   ├── requests.json
│   │   └── camps.json
│   │
│   └── reports/
│       ├── donor_report.csv
│       ├── hospital_report.csv
│       ├── donation_report.csv
│       ├── stock_report.csv
│       └── camp_report.csv
│
└── Report.pdf
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Vishwesh2203/Blood-Bank-Management-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Blood-Bank-Management-System/All_Source_Codes
```

### 3. Run the Application

Make sure Python 3 is installed on your system.

Execute:

```bash
python gui.py
```

The Tkinter graphical interface will launch.

## 💾 Data Storage

The application uses JSON files to store information related to:

- Donors
- Hospitals
- Blood inventory
- Donations
- Blood requests
- Donation camps

CSV files are used to generate and maintain management reports.

## 🎯 Learning Outcomes

This project demonstrates the practical implementation of:

- Object-Oriented Programming (OOP)
- Classes, Objects and Inheritance
- Modular Programming
- File Handling using JSON and CSV
- Exception Handling
- Data Validation
- Python GUI Development using Tkinter
- Application Management through Service Classes

## 📄 Project Documentation

Refer to `Report.pdf` included in this repository for the project report and documentation.

## ⚠️ Disclaimer

This project is developed for educational purposes. It is not a certified medical or blood bank management platform and should not be used for real-world clinical decision-making.

## 👨‍💻 Author

**Vishwesh Singh Visen**

B.Tech – Computer Science Engineering (AI & ML)

## ⭐ Support

If you find this project interesting, consider giving this repository a star!
