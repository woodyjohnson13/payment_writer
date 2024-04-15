from dotenv import load_dotenv
import os

from db.db import Database
from db.models import Payment  
from google_sheets.serivce import GoogleSheet
import datetime

# Load dotenv files
load_dotenv(override=True)

db_url = os.getenv('DB_URL')


current_directory = os.path.dirname(os.path.abspath(__file__))
credential = os.path.join(current_directory, "google_sheets/testing_creds.json")


def main():
    my_db = Database(db_url)
    my_google=GoogleSheet()

    #fill hasmap with payments
    payments_with_status_0 = my_db.get_payments_with_status_0()
    payments_hashmap = {}
    for payment in payments_with_status_0:
        payment_info = {
            "id":payment.id,
            "status": payment.status,
            "date":payment.date,
            "amount":payment.amount,
            "lead_id":payment.lead_id,
            "payment_message":payment.payment_message,
            "chat_id":payment.chat_id,
            "reply_message":payment.reply_message} 
        
        payments_hashmap[payment.id] = payment_info
    
    
    for item in payments_hashmap:
        mapping=my_db.get_mapping(payments_hashmap[item]['payment_message'],payments_hashmap[item]['chat_id'])
                     
        row_data = {
            mapping['date_today']:datetime.datetime.now().strftime('%d.%m.%Y'),
            mapping['payment_column']:payments_hashmap[item]["amount"],
            mapping['payment_date']: payments_hashmap[item]['date'],
            mapping['payment_message']: payments_hashmap[item]['payment_message'],
            mapping['reply_message']: payments_hashmap[item]['reply_message']}
        
        sheet=my_db.get_sheet_id(payments_hashmap[item]['chat_id'])
        
        my_sheet=my_google.create_sheet(sheet["sheet_id"],"test")
        my_google.add_row(my_sheet,row_data)
        print('succes')
        my_db.set_status_to_1(payments_hashmap[item]['id'])
        print('status set to 1')


        
    

if __name__ == '__main__':
    main()
