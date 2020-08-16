from os import path

from flask import current_app as app
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ('https://www.googleapis.com/auth/spreadsheets',)
SHEET_ID = '1FFWIDHigL5uztBEAxVaVUpywgp9WPy4Wo3XI5EFKBug'
RANGE_NAME = 'Sheet1!A1:J20'

my_sheet = {}


def get_sheet_instance(scopes=SCOPES):
    if not my_sheet:
        cred_path = path.join(app.instance_path, 'gsapipa-1597559125165-8c2be94eb0b8.json')
        creds = service_account.Credentials.from_service_account_file(cred_path, scopes=scopes)
        service = build('sheets', 'v4', credentials=creds)
        my_sheet['sheet_instance'] = service.spreadsheets()
    return my_sheet['sheet_instance']


def get_sheet(sheet_id=None, range_name=None, body=None):
    if not sheet_id:
        sheet_id = SHEET_ID
    if not range_name:
        range_name = RANGE_NAME
    if body:
        value_input_option = 'RAW'
        result = get_sheet_instance().values().update(
            spreadsheetId=sheet_id, range=range_name, valueInputOption=value_input_option, body=body
        ).execute()
    else:
        result = get_sheet_instance().values().get(spreadsheetId=sheet_id, range=range_name).execute()
    return result


def get_response(sheet_id=None):
    if not sheet_id:
        sheet_id = SHEET_ID
    return {'link': f"https://docs.google.com/spreadsheets/d/{sheet_id}"}


def read_sheet(sheet_id=None, range_name=None):
    result = get_sheet(sheet_id, range_name)
    values = result.get('values', [])
    response = get_response(sheet_id)
    if not values:
        response['message'] = 'No data found.'
    else:
        response['data'] = values
    return response


def write_sheet(body, sheet_id=None, range_name=None):
    result = get_sheet(sheet_id, range_name, body)
    values = result.get('updatedCells')
    response = get_response(sheet_id)
    if values:
        response['message'] = f"Update count: {values}"
    else:
        response['message'] = 'No data updated'
    return response
