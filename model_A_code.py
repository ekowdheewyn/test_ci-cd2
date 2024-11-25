import csv


def calculate_bmi(height, weight):
    """Calculate BMI."""
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        raise ValueError("Height cannot be zero.")


def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def input_height():
    """Input height in meters."""
    while True:
        try:
            height = float(input("Enter height in meters: "))
            if height <= 0:
                raise ValueError("Height must be a positive value.")
            return height
        except ValueError as e:
            print(f"Error: {e}")
            attempts = attempts + 1
            if attempts >= 3:
                print("Maximum attempts reached. Exiting program.")
                exit()


def input_weight():
    """Input weight in kilograms."""
    while True:
        try:
            weight = float(input("Enter weight in kilograms: "))
            if weight <= 0:
                raise ValueError("Weight must be a positive value.")
            return weight
        except ValueError as e:
            print(f"Error: {e}")
            attempts = attempts + 1
            if attempts >= 3:
                print("Maximum attempts reached. Exiting program.")
                exit()


def save_bmi_to_csv(bmi, classification):
    """Save BMI and classification to a CSV file."""
    with open("bmi_records.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([bmi, classification])


def load_bmi_from_csv():
    """Load BMI records from a CSV file."""
    try:
        with open("bmi_records.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            bmi_records = list(reader)
        return bmi_records
    except FileNotFoundError:
        return []


def main():
    """Main function to calculate BMI, classify, and save results."""
    bmi_records = load_bmi_from_csv()
    print("Welcome to the BMI Calculator!")
    print("Past BMI Records:")
    for record in bmi_records:
        print(f"BMI: {record[0]}, Classification: {record[1]}")
    height = input_height()
    weight = input_weight()
    bmi = calculate_bmi(height, weight)
    classification = classify_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Classification: {classification}")
    save_bmi_to_csv(bmi, classification)
    print("BMI record saved successfully!")


if __name__ == "__main__":
    main()