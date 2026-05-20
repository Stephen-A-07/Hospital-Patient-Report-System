# Hospital Patient Report System

A modular Python project that generates patient prescription reports using validated doctor data, random medicine generation, and structured JSON reporting.

This project demonstrates clean architecture principles, Pydantic-based validation, abstract interfaces, logging, JSON serialization, and object-oriented design patterns.

---

## Features

* Patient and doctor validation using Pydantic
* Blood group validation using Enums
* Random prescription generation
* Doctor specialization matching
* JSON report generation
* Console report printing
* Logging to console and file
* UUID-based report tracking
* Clean modular architecture
* Error handling and validation

---

## Project Structure

```text
project/
│
├── blood_group_enum.py
│   └── Enum for valid blood groups (A+, B+, O+...)
│
├── schema.py
│   └── Pydantic models for Patient, Doctor, and Report
│
├── data.py
│   └── Loads and validates doctors.json
│
├── logger_config.py
│   └── Configures logging to file and console
│
├── interface.py
│   └── Abstract base class for report generators
│
├── prescription_generator.py
│   └── Finds doctor by specialization and generates prescriptions
│
├── report.py
│   └── JSONReportGenerator and ConsoleReportGenerator
│
├── main.py
│   └── Entry point of the application
│
├── doctors.json
│   └── Doctor database with medicines and specializations
│
├── reports/
│   └── Auto-generated JSON reports
│
├── logs/
│   └── Application log files
│
└── README.md
```

---

## Prerequisites

* Python 3.10 or higher

Install dependencies:

```bash
uv init
uv add install pydantic
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd project
```

### 2. Install Dependencies

```bash
uv init
uv add install pydantic
```

### 3. Verify Required Files

Make sure the following file exists:

```text
doctors.json
```

---

## How to Run

```bash
uv run main.py
```

---

## Example Workflow

The application will prompt for patient details:

```text
Enter patient name:
Enter age:
Enter blood group:
Enter doctor specialization:
```

The system will:

1. Validate input data
2. Find a matching doctor by specialization
3. Generate medicines randomly
4. Create a report object
5. Save the report as a unique JSON file
6. Print the report to the console

---

## Example Output

### Console Output

```text
====================================
        MEDICAL REPORT
====================================

Report ID : 7c2c3c7d-d8e4-4c18-a5ef-b83c66d5a123
Patient   : John Doe
Age       : 24
Blood Grp : O+

Doctor    : Dr. Smith
Specialist: General Physician

Prescription:
  - Paracetamol
  - Azithromycin
  - Vitamin C

Visit Time: 2026-05-20 10:23:01

====================================
```

### Generated JSON Report

Example file: `reports/7c2c3c7d-d8e4-4c18-a5ef-b83c66d5a123.json`

```json
{
    "report_id": "7c2c3c7d-d8e4-4c18-a5ef-b83c66d5a123",
    "patient": {
        "patient_id": "3d860acd-3c56-468f-9fb9-c50f0c5a9b25",
        "name": "John Doe",
        "age": 24,
        "blood_group": "O+",
        "doctor_specialization": "General Physician"
    },
    "doctor": {
        "doctor_id": "DOC-001",
        "name": "Dr. Smith",
        "specialization": "General Physician"
    },
    "prescription": [
        "Paracetamol",
        "Azithromycin",
        "Vitamin C"
    ],
    "visit_time": "2026-05-20 10:23:01"
}
```

---

## Concepts Practiced

### Python Concepts

* Object-Oriented Programming
* Modular Architecture
* Abstract Base Classes
* Interfaces
* Dependency Inversion
* Logging
* Exception Handling
* JSON Serialization
* UUID Generation
* Random Sampling
* File Handling
* Pathlib

### Pydantic Concepts

* BaseModel
* Field Validation
* Type Enforcement
* Data Serialization
* Nested Models

### Software Engineering Principles

* Single Responsibility Principle (SRP)
* Separation of Concerns
* Dependency Inversion Principle (DIP)
* Clean Code Practices

---

## Technologies Used

* Python 3.10+
* Pydantic
* JSON
* Logging Module
* UUID
* Pathlib

---

## Future Improvements

* Database integration (SQLite / PostgreSQL)
* REST API using FastAPI
* Web dashboard
* PDF report generation
* Authentication system
* Docker support
* Unit testing with pytest
* CI/CD integration

---

## Learning Outcomes

By building this project, you will learn:

* How to structure scalable Python projects
* How to validate data using Pydantic
* How to use abstract classes effectively
* How to design modular systems
* How to generate structured reports
* How to apply software engineering principles in Python

---

## Author

Built by Stephen

---

## License

This project is for educational and learning purposes.