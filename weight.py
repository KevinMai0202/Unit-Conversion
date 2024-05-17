import json
import time


def grams_to_pounds(grams):
    return grams * 0.00220462


def grams_to_ounces(grams):
    return grams * 0.035274


while True:
    try:
        with open('weight_input.txt', 'r') as file:
            data = json.load(file)
            grams = data['grams']

        pounds = grams_to_pounds(grams)
        ounces = grams_to_ounces(grams)

        with open('weight_output.txt', 'w') as file:
            json.dump({'pounds': pounds, 'ounces': ounces}, file)

        # Add a delay of 1 second
        time.sleep(1)

    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"An error occurred: {error}. Waiting for valid input...")
