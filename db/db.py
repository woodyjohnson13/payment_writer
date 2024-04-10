from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db.models import BotTransfer,Chat,Payment

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
 

        def get_mapping(self,chat_id):
            session = self.get_session()
            try:
                    mapping = session.query(BotTransfer).filter_by(chat_id=chat_id).first()  # Get single object
                    if mapping:
                        return {
                            'date_today': mapping.date_today,
                            'payment_date': mapping.payment_date,
                            'payment_message': mapping.payment_message,
                            'reply_message':mapping.reply_message,
                            'cash':mapping.cash,
                            'semenov_card':mapping.semenov_card,
                            'bmp_card':mapping.bmp_card,
                            'papka_card':mapping.papka_card,
                            
                        }
                    else:
                        return {}  # Empty dictionary if no data found
            except Exception as e:
                    print(f"Error retrieving mapping for chat ID {chat_id}: {e}")
                    return None  # Return None on error
            finally:
                    session.close()





