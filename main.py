import json
import time


def conversion_menu():
    print("Conversion Menu:")
    print("1. Height (cm to inches)")
    print("2. Weight (grams to pounds and ounces)")
    print("3. Temperature (Celsius to Fahrenheit)")
    print("Enter 'q' to exit")
    choice = input("Enter your choice (1/2/3): ")
    return choice


def main():
    while True:
        choice = conversion_menu()

        if choice == 'q':
            print("Exiting the program...")
            break

        elif choice == '1':
            cm_input = input("Enter height in centimeters: ")
            if not cm_input.replace('.', '', 1).isdigit():  # Check if input is numeric
                print("Invalid input. Please enter a valid number.")
                continue  # Skip the loop and go to the next iteration

            cm = float(cm_input)
            with open('height_input.txt', 'w') as file:
                file.write(json.dumps({'cm': cm}))
            print("Waiting for 1 second...")
            time.sleep(1)  # Wait for 1 second
            try:
                with open('height_output.txt', 'r') as file:
                    result = json.load(file)
                    print(f"{cm} cm is equal to {result['inches']:.2f} inches.")
            except Exception as error:
                print(f"Error reading output file: {error}")

        elif choice == '2':
            grams_input = input("Enter weight in grams: ")
            if not grams_input.replace('.', '', 1).isdigit():  # Check if input is numeric
                print("Invalid input. Please enter a valid number.")
                continue  # Skip the loop and go to the next iteration

            grams = float(grams_input)
            with open('weight_input.txt', 'w') as file:
                file.write(json.dumps({'grams': grams}))
            print("Waiting for 1 second...")
            time.sleep(1)  # Wait for 1 second
            try:
                with open('weight_output.txt', 'r') as file:
                    result = json.load(file)
                    print(f"{grams} grams is equal to {result['pounds']:.2f} pounds.")
                    print(f"{grams} grams is equal to {result['ounces']:.2f} ounces.")
            except Exception as error:
                print(f"Error reading output file: {error}")

        elif choice == '3':
            celsius_input = input("Enter temperature in Celsius: ")
            if not celsius_input.replace('.', '', 1).isdigit():  # Check if input is numeric
                print("Invalid input. Please enter a valid number.")
                continue  # Skip the loop and go to the next iteration

            celsius = float(celsius_input)
            with open('temperature_input.txt', 'w') as file:
                file.write(json.dumps({'celsius': celsius}))
            print("Waiting for 1 second...")
            time.sleep(1)  # Wait for 1 second
            try:
                with open('temperature_output.txt', 'r') as file:
                    result = json.load(file)
                    print(f"{celsius} degrees Celsius is equal to {result['fahrenheit']:.2f} degrees Fahrenheit.")
            except Exception as error:
                print(f"Error reading output file: {error}")

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

