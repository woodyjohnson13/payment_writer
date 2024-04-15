from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db.models import BotTransfer,Chat,Payment
import mysql.connector


from dotenv import load_dotenv
import os

load_dotenv(override=True)

db_url = os.getenv('DB_URL')



Base = declarative_base()




class Database:
        def __init__(self, db_url):
            self.engine = create_engine(db_url,echo=True)
            self.Session = sessionmaker(bind=self.engine)
            
        def get_session(self):
            return self.Session()
                              
                              
        def get_payments_with_status_0(self):
            session = self.get_session()
            try:
                payments = session.query(Payment).filter_by(status=0).all() 
                return payments
            finally:
                session.close() 
                
        def set_status_to_1(self, id):
            session = self.get_session()
            try:
                payment = session.query(Payment).filter_by(id=id).first()
                if payment:
                    payment.status = 1
                    session.commit()
                    return payment
                else:
                    return None
            except Exception as e:
                session.rollback()
                print(f"Error setting payment status: {e}")
                return None
            finally:
                session.close()

        def get_sheet_id(self,chat_id):
            session = self.get_session()
            try:
                sheet_id = session.query(Chat).filter_by(chat_id=chat_id).first()
                if sheet_id:
                        return {
                            'sheet_id': sheet_id.sheet_id, 
                        }
                else:
                        return {}  #
            except Exception as e:
                    print(f"Error")
                    return None  
            finally:
                    session.close()
   
        def get_mapping(self, message, chat_id):
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="8121974",
                    database="payemnt_bot"
                )
                cursor = conn.cursor(dictionary=True)

                query = """
                    SELECT *
                    FROM bot_transfer
                    WHERE chat_id = %s
                    AND %s LIKE CONCAT('%', key_phrase, '%')
                    LIMIT 1
                """
                cursor.execute(query, (chat_id, message))
                mapping = cursor.fetchone()

                if mapping:
                    return {
                        'date_today': mapping['date_today'],
                        'payment_date': mapping['payment_date'],
                        'payment_message': mapping['payment_message'],
                        'reply_message': mapping['reply_message'],
                        'chat_id': mapping['chat_id'],
                        'payment_column': mapping['payment_column']
                    }
                else:
                    return None
            except Exception as e:
                print(f"Error determining transfer: {e}")
                return None
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()

