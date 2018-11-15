import csv

def main():
    header = ["Name", "Sex", "Age"]

    user_info = []

    newEntry = True
    
    while(newEntry):
        info = []
        info.append(input("Enter in your name: "))
        info.append(input("Enter in your sex(M or F): "))
        info.append(input("Enter in your age: "))
        user_info.append(info)
        if(input("Would you like to inset a new entry(Y or N)? ").lower() != "y"):
            newEntry = False

    with open("user_info_custom.csv", mode="w", newline="") as csv_file:
        csv_file.write(",".join(header) + "\n")
        for entry in user_info:
            csv_file.write(",".join(entry) + "\n")

    with open("user_info.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for entry in user_info:
            writer.writerow(entry)
main()
