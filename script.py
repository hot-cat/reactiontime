import json
import os
import csv

def analyze_json_file(file_path):
    # Read the JSON file with the appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Perform analysis on the JSON data
    # You can customize this part according to your specific analysis requirements
    num_items = len(data)
    keys = data.keys()

    # Print the analysis results
    print(f"Number of items: {num_items}")
    print(f"Keys in the JSON file: {keys}")

    # You can perform more analysis or computations on the data here


def flanker_analyze_json_file(file_path):
    # Read the JSON file with the appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Analyze the "flanker" key
    flanker_data = data['flanker']

    # Perform analysis on the flanker data
    # You can customize this part according to your specific analysis requirements
    num_trials = len(flanker_data)
    # Perform other analysis on the flanker data

    # Print the analysis results
    print(f"Number of trials in 'flanker': {num_trials}")

    # You can perform more analysis or computations on the flanker data here


def separate_keys_to_files(file_path):
    # Read the JSON file with the appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Create a directory to store the separate JSON files
    base_directory = os.path.dirname(file_path)
    separate_files_directory = os.path.join(base_directory, 'separate_files')
    os.makedirs(separate_files_directory, exist_ok=True)

    # Separate the keys into separate JSON files
    for key, value in data.items():
        separate_file_path = os.path.join(separate_files_directory, f"{key}.json")
        with open(separate_file_path, 'w', encoding='utf-8') as separate_file:
            json.dump(value, separate_file, indent=4)

        print(f"Separate JSON file created for key '{key}': {separate_file_path}")

def analyze_flanker_trials(file_path):
    # Read the JSON file with the appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Access the "flanker" data
    flanker_data = data["flanker"]

    # Iterate over each trial
    for trial_id, trial_data in flanker_data.items():
        amount = trial_data["amount"]
        name = trial_data["name"]
        role = trial_data["role"]
        trial_trials = trial_data["data"]

        # Analyze the trial data
        num_trials = len(trial_trials)
        compatible_trials = 0
        incompatible_trials = 0
        total_response_time = 0
        total_accuracy = 0

        for trial in trial_trials:
            response_time = trial["responseTime"]
            trial_type = trial["trialType"]
            accuracy = trial["accuracy"]

            total_response_time += response_time
            total_accuracy += int(accuracy)

            if trial_type == "compatible":
                compatible_trials += 1
            elif trial_type == "incompatible":
                incompatible_trials += 1

        average_response_time = total_response_time / num_trials
        average_accuracy = (total_accuracy / num_trials) * 100

        # Print the analysis results for each trial
        print(f"Trial ID: {trial_id}")
        print(f"Amount: {amount}")
        print(f"Name: {name}")
        print(f"Role: {role}")
        print(f"Number of trials: {num_trials}")
        print(f"Number of compatible trials: {compatible_trials}")
        print(f"Number of incompatible trials: {incompatible_trials}")
        print(f"Average response time: {average_response_time} ms")
        print(f"Average accuracy: {average_accuracy}%")
        print("--------------------")

def separate_flanker_data(file_path):
    # Read the JSON file with the appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Access the "flanker" data
    flanker_data = data["flanker"]

    # Create a dictionary to store unique flanker data
    unique_flanker_data = {}

    # Iterate over each trial
    for trial_id, trial_data in flanker_data.items():
        amount = trial_data["amount"]
        name = trial_data["name"]
        role = trial_data["role"]
        trial_trials = trial_data["data"]

        # Generate a unique key for each trial based on name, role, and amount
        trial_key = f"{name}-{role}-{amount}"

        # Check if the trial is already present in the unique_flanker_data dictionary
        if trial_key in unique_flanker_data:
            continue  # Skip duplicates

        # Add the trial data to the unique_flanker_data dictionary
        unique_flanker_data[trial_key] = trial_data

    # Create a new dictionary containing only the unique flanker data
    new_data = {"flanker": unique_flanker_data}

    # Write the new JSON data to a separate file
    new_file_path = 'sorted/flanker.json'
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        json.dump(new_data, new_file, indent=4)

    print("Unique flanker data separated into a new JSON file.")


def separat_score_data(file_path):
    # Read the JSON file with the appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Access the "flanker" data
    flanker_data = data["scores"]

    # Create a dictionary to store unique flanker data
    unique_flanker_data = {}

    # Iterate over each trial
    for trial_id, trial_data in flanker_data.items():
        name = trial_data["name"]
        role = trial_data["role"]
        speed = trial_data["speed"]
        time = trial_data["time"]
        amount_circles = trial_data["amountCircles"]
        amount_track = trial_data["amountTrack"]

        # Generate a unique key for each trial based on specified fields
        trial_key = f"{name}-{role}-{speed}-{time}-{amount_circles}-{amount_track}"

        # Check if the trial is already present in the unique_flanker_data dictionary
        if trial_key in unique_flanker_data:
            continue  # Skip duplicates

        # Modify the score data
        score_data = trial_data["score"]
        if "rt" in trial_data:
            rt_values = sum(trial_data["rt"])
        else:
            rt_values = 0
        num_true = sum(int(score) for score in score_data)
        accuracy = num_true / int(amount_circles)

        modified_score_data = {
            "average_rt": rt_values / int(amount_track),
            "score": num_true,
            "accuracy": accuracy
        }

        # Add the modified score data to the trial data
        trial_data["score"] = modified_score_data

        # Add the trial data to the unique_flanker_data dictionary
        unique_flanker_data[trial_key] = trial_data

    # Create a new dictionary containing only the unique flanker data
    new_data = {"scores": unique_flanker_data}

    # Write the new JSON data to a separate file
    new_file_path = 'sorted/scores.json'
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        json.dump(new_data, new_file, indent=4)

    print("Unique score data separated into a new JSON file.")


def generate_csv(file_path, csv_file_path):
    # Read the JSON file with the appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Access the "flanker" data
    flanker_data = data["flanker"]

    # Create a list to store the rows for the CSV
    csv_rows = []

    # Iterate over each trial
    for trial_id, trial_data in flanker_data.items():
        amount = trial_data["amount"]
        name = trial_data["name"]
        role = trial_data["role"]
        trial_trials = trial_data["data"]

        # Analyze the trial data
        num_trials = len(trial_trials)
        total_response_time = 0
        total_accuracy = 0

        for trial in trial_trials:
            response_time = trial["responseTime"]
            accuracy = trial["accuracy"]

            total_response_time += response_time
            total_accuracy += int(accuracy)

        average_response_time = total_response_time / num_trials
        average_accuracy = (total_accuracy / num_trials) * 100

        # Create a row for the CSV
        csv_row = [trial_id, amount, name, role, num_trials, average_response_time, average_accuracy]

        # Add the row to the list of CSV rows
        csv_rows.append(csv_row)

    # Write the CSV data to a file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Trial ID", "Amount", "Name", "Role", "Number of Trials", "Average Response Time", "Average Accuracy"])
        writer.writerows(csv_rows)

    print(f"CSV file generated: {csv_file_path}")

def generate_scores_csv(file_path, csv_file_path):
    # Read the JSON file with the appropriate encoding
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Access the "flanker" data
    flanker_data = data["scores"]

    # Create a list to store the rows for the CSV
    csv_rows = []

    # Iterate over each trial
    for trial_id, trial_data in flanker_data.items():
        name = trial_data["name"]
        role = trial_data["role"]
        speed = trial_data["speed"]
        time = trial_data["time"]
        amount_circles = trial_data["amountCircles"]
        amount_track = trial_data["amountTrack"]

        # Check if the trial data has scores
        if "score" in trial_data:
            score_data = trial_data["score"]
            average_rt = score_data["average_rt"]
            accuracy = score_data["accuracy"]
        else:
            average_rt = 0
            accuracy = 0

        # Create a row for the CSV
        csv_row = [name, role, average_rt, accuracy, speed, time, amount_circles, amount_track]

        # Add the row to the list of CSV rows
        csv_rows.append(csv_row)

    # Write the CSV data to a file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Role", "Average RT", "Accuracy", "Speed", "Time", "Amount Circles", "Amount Track"])
        writer.writerows(csv_rows)

    print(f"CSV file generated: {csv_file_path}")

# Provide the path to your JSON file
json_file_path = 'reaciton-time-game-default-rtdb-export.json'
flanker_file_path = 'sorted/flanker.json'
socres_file_path = 'sorted/scores.json'
# Provide the desired path for the CSV file
csv_file_path = 'csv/flanker_data.csv'
scores_csv = 'csv/scores_csv.csv'
# Call the function to analyze the JSON file
# separate_flanker_data(json_file_path)

# analyze_flanker_trials(flanker_file_path)
# generate_csv(flanker_file_path, csv_file_path)

# separat_score_data(json_file_path)

generate_scores_csv(socres_file_path, scores_csv)
