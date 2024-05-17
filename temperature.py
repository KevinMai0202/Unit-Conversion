import json
import time


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


while True:
    try:
        with open('temperature_input.txt', 'r') as file:
            data = json.load(file)
            celsius = data['celsius']

        fahrenheit = celsius_to_fahrenheit(celsius)

        with open('temperature_output.txt', 'w') as file:
            json.dump({'fahrenheit': fahrenheit}, file)

        # Add a delay of 1 second
        time.sleep(1)

    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"An error occurred: {error}. Waiting for valid input...")
