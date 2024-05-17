import json
import time


def cm_to_inches(cm):
    return cm * 0.393701


while True:
    try:
        with open('height_input.txt', 'r') as file:
            data = json.load(file)
            cm = data['cm']

        inches = cm_to_inches(cm)

        with open('height_output.txt', 'w') as file:
            json.dump({'inches': inches}, file)

        # Add a delay of 1 second
        time.sleep(1)

    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"An error occurred: {error}. Waiting for valid input...")


