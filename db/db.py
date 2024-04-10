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
                payments = session.query(Payment).filter_by(status=0).all()  # Use filter_by for clarity
                return payments
            finally:
                session.close()  # Ensure session is closed







