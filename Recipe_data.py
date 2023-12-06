import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set the scope and credentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('', scope)
client = gspread.authorize(creds)
# Open the specific Google Sheet by its title
sheet = client.open('Your Google Sheet Name').sheet1  # Change the sheet name accordingly

# Function to insert JSON data into the sheet
def insert_json_data(json_data):
    # Assuming JSON data is a list of dictionaries or a single dictionary
    if isinstance(json_data, list):
        # Insert headers if the first row is empty
        headers = list(json_data[0].keys())
        if not sheet.row_values(1):
            sheet.insert_row(headers, index=1)
        # Insert each dictionary as a row in the sheet
        for entry in json_data:
            values = list(entry.values())
            sheet.append_row(values)
    elif isinstance(json_data, dict):
        # Insert headers if the first row is empty
        if not sheet.row_values(1):
            sheet.insert_row(list(json_data.keys()), index=1)
        # Insert the dictionary as a row in the sheet
        values = list(json_data.values())
        sheet.append_row(values)
# Example JSON data (replace this with your JSON model)
sample_json = [
]
# Insert JSON data into the sheet
insert_json_data(sample_json)
