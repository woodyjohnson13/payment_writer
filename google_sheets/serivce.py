import gspread
import os
from google.oauth2.service_account import Credentials

current_directory = os.path.dirname(os.path.abspath(__file__))
credential = os.path.join(current_directory, "testing_creds.json")

class GoogleSheet:
    def __init__(self):
        # Define the scope of access
        self.scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
        
    
    def create_sheet(self,spreadsheet_id,sheet_name):
        credentials = Credentials.from_service_account_file(credential)
        scoped_credentials = credentials.with_scopes(self.scope)
        client = gspread.authorize(scoped_credentials)
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        return sheet
            
        
    def add_row(self, sheet, data):
        column_mapping = {'M': 13, 'AJ': 36, 'AL': 38,'AK':37,'Z': 26}  # Extend for more columns

        last_row = len(sheet.get_all_values())

        for column, value in data.items():
            column_index = column_mapping.get(column.upper(), None)  # Handle non-existent columns gracefully

            if column_index:
                sheet.update_cell(last_row + 1, column_index, value)
            else:
                # Handle case where column is not found in the mapping (optional)
                print(f"Warning: Column '{column}' not found in mapping.")


# google=GoogleSheet()
# my_sheet=google.create_sheet("154wOj16F5j_YvMRcw0rRE6_u_Hi4qBZCwdejWD_bWMU","test1")

# data = {'C': "C", 'D': "D"}
# google.add_row(my_sheet,data)

