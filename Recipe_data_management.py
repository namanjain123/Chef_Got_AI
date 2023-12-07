import csv

# Function to read data from the CSV file
def read_data_from_csv(csv_filename):
    data = []
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Function to insert JSON data into a CSV file or edit if data exists
def insert_or_edit_json_data_to_csv(json_data, csv_filename):
    existing_data = read_data_from_csv(csv_filename)

    # Clear existing data
    if existing_data:
        existing_data.clear()

    # Write JSON data to the CSV file
    existing_data.extend(json_data)

    # Write the combined data back to the CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = existing_data[0].keys() if existing_data else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write headers
        if existing_data:
            writer.writeheader()

        # Write rows
        for entry in existing_data:
            writer.writerow(entry)
sample_json = [
]

# File name for the CSV file
csv_filename = 'data.csv'

# Insert or edit JSON data in the CSV file
insert_or_edit_json_data_to_csv(sample_json, csv_filename)
