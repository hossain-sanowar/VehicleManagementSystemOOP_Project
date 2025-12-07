# 🚗 Vehicle Management System – Python OOP Project

A production-style Python project demonstrating **core Object-Oriented Programming (OOP) principles** with **real-world engineering features** such as logging, error handling, JSON persistence, CLI interaction, and unit testing.

This project is designed to reflect how **scalable backend systems** are structured, making it ideal for **portfolio, interview preparation, and ML engineering foundations**.

---

## 📌 Project Overview

The **Vehicle Management System** simulates a fleet of vehicles (`Car`, `Bike`, `Truck`) managed through a centralized `FleetManager`.  
It demonstrates how theoretical OOP concepts translate into **maintainable, testable, and extensible software systems**.

### ✅ Concepts Demonstrated
- Abstraction
- Inheritance
- Polymorphism
- Encapsulation
- Instance, Class, & Static Methods
- Composition
- Logging, Error Handling, Persistence, CLI, and Unit Testing

---

## 🧩 Key Features

- **Abstract Base Class (`Vehicle`)** enforcing the `drive()` interface  
- **Concrete Implementations (`Car`, `Bike`, `Truck`)** with unique behaviors  
- **FleetManager** for centralized fleet operations and reporting  
- **Encapsulation** for protecting internal state such as fuel level  
- **Polymorphism** through dynamic `drive()` behavior  
- **JSON Persistence** for saving and loading fleet data  
- **Command-Line Interface (CLI)** built with `argparse`  
- **Automated Unit Testing** using `pytest`  

---

## 📂 Project Structure

```text
VehicleManagementSystemOOP_Project/
│
├── __init__.py
├── base.py
├── car.py
├── bike.py
├── truck.py
├── fleet_manager.py
├── main.py
│
└── tests/
    ├── test_vehicle.py
    └── test_fleet_manager.py
🛠️ Installation & Setup
bash
Copy code
git clone https://github.com/hossain-sanowar/VehicleManagementSystemOOP_Project.git
cd VehicleManagementSystemOOP_Project
pip install -r requirements.txt
Ensure Python 3.8+ is installed.

▶️ Usage Examples
Run the Application
bash
Copy code
python3 -m VehicleManagementSystemOOP_Project.main
Enable Logging Verbosity
bash
Copy code
python3 -m VehicleManagementSystemOOP_Project.main -v     # INFO
python3 -m VehicleManagementSystemOOP_Project.main -vv    # DEBUG
Add a Vehicle
bash
Copy code
python3 -m VehicleManagementSystemOOP_Project.main add --type Car --brand Audi --year 2022 --save
Drive a Vehicle
bash
Copy code
python3 -m VehicleManagementSystemOOP_Project.main drive --brand Audi --km 30 --save
Generate Fleet Report
bash
Copy code
python3 -m VehicleManagementSystemOOP_Project.main report
Save & Load Fleet
bash
Copy code
python3 -m VehicleManagementSystemOOP_Project.main save
python3 -m VehicleManagementSystemOOP_Project.main load
🎯 OOP Principles Applied
Abstraction – Vehicle defines the required interface

Inheritance – Car, Bike, Truck extend base functionality

Polymorphism – Each subclass implements drive() differently

Encapsulation – Internal state protected via __fuel_level

Method Types

Instance → drive()

Class → from_dict()

Static → is_motorized()

Composition – FleetManager controls multiple vehicle objects

✅ Advanced Engineering Features
Configurable logging

Robust error handling

JSON persistence

Full CLI support

Unit testing with pytest

📖 Interview Notes
Abstraction vs Encapsulation

Abstraction hides implementation details

Encapsulation hides internal data

Real-World Analogy

ATM Machine → Abstraction

Bank Account Balance → Encapsulation

🚀 Future Enhancements
GUI interface (Tkinter / Streamlit)

Database persistence (SQLite / PostgreSQL)

REST API integration (FastAPI / Flask)

CI/CD automation with GitHub Actions

ML-based vehicle analytics & forecasting

👨‍💻 Author
Md. Sanowar Hossain
Aspiring Machine Learning Engineer | Python Developer
🔗 GitHub: https://github.com/hossain-sanowar

⭐ If this project helped you, please consider giving it a star!

yaml
Copy code

---

## ✅ What I Improved
- Fixed formatting & broken markdown
- Cleaned OOP terminology
- Added **installation section**
- Added **ML relevance**
- Improved **project structure layout**
- Removed repetition
- Made it **recruiter & portfolio ready**

---

If you want, I can also:
✅ Add a **GitHub Actions CI/CD workflow**
✅ Add **badges (build, tests, Python version)**
✅ Write a **dedicated ML extension README**
✅ Add a **diagram section for OOP architecture**
✅ Prepare a **README for Kaggle/ML portfolios**

Just tell me what you’d like to add next 🚀
