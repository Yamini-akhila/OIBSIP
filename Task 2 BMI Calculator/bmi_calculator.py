def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def get_user_input():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            return weight, height
        except ValueError:
            print("Invalid input. Please enter numeric values for weight and height.")

def main():
    print("Welcome to the BMI Calculator!")
    while True:
        weight, height = get_user_input()
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"\nYour BMI is {bmi}. You are classified as: {category}\n")
        
        another = input("Would you like to calculate BMI for another person? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the BMI Calculator. Stay healthy!")
            break

if __name__ == "__main__":
    main()
