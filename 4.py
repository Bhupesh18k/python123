def mean(data):
    total = 0
    count = 0
    for x in data:
        total += x
        count += 1
    if count != 0:
      return(total / count)
    else:
      return(0.0)
def median(data):
    if not data:
        return(0.0)
    arr = data[:]
    n = 0
    for x in arr:
        n += 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]
def variance(data):
    n = 0
    for x in data:
        n += 1
    if n < 2:
        return(0.0)
    mu = mean(data)
    total = 0
    for x in data:
        total += (x - mu) ** 2
    return(total / (n - 1))
def stdev(data):
    return(variance(data) ** 0.5)
def data_range(data):
    if not data:
        return(0)
    smallest = data[0]
    largest = data[0]
    for x in data:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return(largest - smallest)
class Person:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age
class Patient(Person):
    def __init__(self, pid, name, age, gender, contact):
        super().__init__(pid, name, age)
        self.gender = gender
        self.contact = contact
class Doctor(Person):
    def __init__(self, did, name, age, department, fee):
        super().__init__(did, name, age)
        self.department = department
        self.__fee = fee 
    def get_fee(self):
        return(self.__fee)
def write_text(text):
    f = open("patients.txt","a")
    f.write(text + "\n")
    f.close()
def read_text():
    try:
        f = open("patients.txt", "r")
        lines = f.readlines()
        f.close()
        return(lines)
    except FileNotFoundError:
        return([])
def write_doctor_csv(row):
    f = open("doctors.csv", "a")
    line = ""
    for i in range(len(row)):
        line += str(row[i])
        if i != len(row) - 1:
            line += ","
    f.write(line + "\n")
    f.close()
def write_appointment_csv(row):
    f = open("appointments.csv", "a")
    line = ""
    for i in range(len(row)):
        line += str(row[i])
        if i != len(row) - 1:
            line += ","
    f.write(line + "\n")
    f.close()
def write_billing_csv(row):
    f = open("billing.csv", "a")
    line = ""
    for i in range(len(row)):
        line += str(row[i])
        if i != len(row) - 1:
            line += ","
    f.write(line + "\n")
    f.close()
def read_doctors_csv():
    try:
        f = open("doctors.csv", "r")
        lines = f.readlines()
        f.close()
        data = []
        for line in lines:
            data.append(line.strip().split(","))
        return(data)
    except FileNotFoundError:
        return([])
def read_appointments_csv():
    try:
        f = open("appointments.csv", "r")
        lines = f.readlines()
        f.close()
        data = []
        for line in lines:
            data.append(line.strip().split(","))
        return(data)
    except FileNotFoundError:
        return([])
def read_billing_csv():
    try:
        f = open("billing.csv", "r")
        lines = f.readlines()
        f.close()
        data = []
        for line in lines:
            data.append(line.strip().split(","))
        return(data)
    except FileNotFoundError:
        return([])
doctors = []
patients=[]
patient_dict={}
def register_patient():
    try:
        pid = input("Patient ID: ")
        name = input("Name: ").title()
        age = int(input("Age: "))
        if age < 0:
            print("Age cannot be negative")
            return
        gender = input("Gender: ")
        contact = input("Contact: ")
        patient = Patient(pid, name, age, gender, contact)
        patients.append(patient)
        patient_dict[pid]=patient
        write_text(pid + "," + name + "," + str(age) + "," + gender + "," + contact)
        print("Patient registered")
    except ValueError:
        print("Invalid input")
def add_doctor():
    try:
        did = input("Doctor ID: ")
        name = input("Name: ").title()
        age = int(input("Age: "))
        dept = input("Department: ")
        fee = float(input("Consultation Fee: "))
        doctor = Doctor(did, name, age, dept, fee)
        doctors.append(doctor)
        write_doctor_csv([did, name, age, dept, fee])
        print("Doctor added")
    except ValueError:
        print("Invalid input")
def book_appointment():
    pid = input("Patient ID: ")
    did = input("Doctor ID: ")
    date = input("Appointment Date: ")
    write_appointment_csv([pid, did, date])
    print("Appointment booked")
def generate_bill():
    try:
        pid = input("Patient ID: ")
        did = input("Doctor ID: ")
        amount = float(input("Bill Amount: "))
        write_billing_csv([pid, did, amount])
        print(" Bill recorded")
    except ValueError:
        print(" Invalid amount")
def search_patient():
    pid = input("Enter Patient ID to search: ")
    if pid in patient_dict:
        p = patient_dict[pid]
        print("Patient Found:", p.pid, p.name, p.age, p.gender, p.contact)
    else:
        print("Patient not found")
def analysis_menu():
    print("\n--- DATA ANALYSIS ---")
    print("1. Patient Age Statistics")
    print("2. Billing Statistics")
    print("3. Age Group Distribution")
    print("4. Unique Departments")        
    print("5. Back")
    choice = input("Enter choice: ")
    if choice == "1":
        lines = read_text()
        ages = []
        for line in lines:
            parts = line.split(",")
            ages.append(int(parts[2]))
        print("Mean Age:", mean(ages))
        print("Median Age:", median(ages))
        print("Std Deviation:", stdev(ages))
        print("Range:", data_range(ages))
    elif choice == "2":
        bills = read_billing_csv()
        amounts = []
        for b in bills:
            amounts.append(float(b[2]))
        high_bills = list(filter(lambda x: x > 5000, amounts))
        print("Average Bill:", mean(amounts))
        print("Bill Std Dev:", stdev(amounts))
        print("High Value Bills:", high_bills)
    elif choice == "3":
        lines = read_text()
        groups = {"0-18": 0, "19-40": 0, "41-60": 0, "60+": 0}
        for line in lines:
            age = int(line.split(",")[2])
            if age <= 18:
                groups["0-18"] += 1
            elif age <= 40:
                groups["19-40"] += 1
            elif age <= 60:
                groups["41-60"] += 1
            else:
                groups["60+"] += 1
        for k in groups:
            print(k, ":", groups[k])
    elif choice == "4":
        docs = read_doctors_csv()
        departments = set()   
        for d in docs:
            departments.add(d[3])
        print("Departments Available:")
        for dept in departments:
            print(dept)
    elif choice=="5":
      return
while True:
    print("\n=== HEALTHCARE DATA MANAGEMENT & ANALYSIS SYSTEM ===")
    print("1. Register Patient")
    print("2. Add Doctor")
    print("3. Book Appointment")
    print("4. Generate Bill")
    print("5. Data Analysis")
    print("6. Search Patient") 
    print("7. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        register_patient()
    elif choice == "2":
        add_doctor()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        generate_bill()
    elif choice == "5":
        analysis_menu()
    elif choice == "6":
        search_patient()
    elif choice=="7":
      print("Thank you!")
      break
    else:
        print("Invalid choice")
