from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
SERVICE_ACCOUNT_FILE = 'service_account.json'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1E0ib9Zg6o8jtsT5mmNXgvo6nQv0VLrEHftr8szThjZw'
SAMPLE_READ_RANGE_NAME = 'Data!A2:E'
credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_READ_RANGE_NAME).execute()
            
values = result.get('values', [])

if not values:
    print('No data found.')

print('Name, Major:')
for row in values:
    # Print columns A and E, which correspond to indices 0 and 4.
    print('%s, %s' % (row[0], row[4]))

SAMPLE_READ_WRITE_RANGE_NAME="Data!F13"
write_value=[["i_am_python"]]
# sheet.va
result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_READ_WRITE_RANGE_NAME,valueInputOption="USER_ENTERED",body={"values":write_value}).execute()
print(result)