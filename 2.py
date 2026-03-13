def add_weather():
    try:
        temp=float(input("Enter temperature"))
        humd=float(input("Enter humidity"))
        date=input("Enter date-Enter month-Enter year")
        f=open("Weather.txt",'a')
        f.write(f"{date},{temp},{humd}\n")
        f.close()
        print("Added successfully.")
    except ValueError:
        print("Invalid temperature!Enter Numeric")
    except Exception as e:
        print("Error:",e,"\n")
def display_weather():
    try:
        f=open("Weather.txt",'r')
        records=f.readlines()
        f.close()
        if not records:
            print("No records.\n")
            return
        for record in records:
            date,temp, humd = record.strip().split(",")
            print(f"{date}\t{temp}\t{humd}")
        print()
    except ValueError:
        print("Invalid input! Enter Numeric.\n")
    except Exception as e:
        print("Error:", e, "\n")
def search_weather():
    try:
        search_date = input("Enter Date to Search:")
        found = False

        f= open("weather.txt", 'r')
        for record in f:
            date,temp,humd = record.strip().split(",")
            if date == search_date:
                print("\nWeather Record Found:")
                print("Date:", date)
                print("Temperature:", temp)
                print("Humidity:", humd, "\n")
                found = True
                break
        f.close()

        if not found:
            print("Record not found.\n")

    except FileNotFoundError:
        print("File not found.\n")
def update_weather():
    try:
        update_date = input("Enter Date to Update: ")
        updated = False
        f= open("weather.txt", 'r')
        records = f.readlines()
        f.close()
        f= open("weather.txt", "w")
        for record in records:
            date,temperature,humidity = record.strip().split(",")

            if date == update_date:
                temp= float(input("Enter New Temperature: "))
                humd = float(input("Enter New Humidity: "))
                f.write(f"{date},{temp},{humd}\n")
                updated = True
            else:
                f.write(record)
        f.close()

        if updated:
            print("Weather record updated successfully.\n")
        else:
            print("Record not found.\n")

    except FileNotFoundError:
        print("File not found.\n")
    except ValueError:
        print("Invalid numeric value.\n")


def delete_weather():
    try:
        date = input("Enter Date to Delete: ")
        deleted = False
        f= open("weather.txt", "r")
        records = f.readlines()
        f.close()
        f = open("weather.txt", "w")
        for record in records:
            date, temp, humd = record.strip().split(",")
            if date !=date:
                f.write(record)
            else:
                deleted = True
        f.close()

        if deleted:
            print("deleted successfully.\n")
        else:
            print("Record not found.\n")

    except FileNotFoundError:
        print("File not found.\n")


def main():
    while True:
        print("Weather Record Management System")
        print("1. Add Weather Record")
        print("2. Display All Records")
        print("3. Search Weather Record")
        print("4. Update Weather Record")
        print("5. Delete Weather Record")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_weather()
        elif choice == "2":
            display_weather()
        elif choice == "3":
            search_weather()
        elif choice == "4":
            update_weather()
        elif choice == "5":
            delete_weather()
        elif choice == "6":
            print("Exit")
            break
        else:
            print("Invalid choice!\n")
main()
    
    
