from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Payment(Base):
    __tablename__ = 'bank'

    id = Column(Integer, primary_key=True)
    lead_id=Column(String)
    date = Column(String)
    amount = Column(String)
    checking_account=Column(String)
    payment_message=Column(String)
    reply_message=Column(String)
    chat_id=Column(String)
    status=Column(Integer)


class Chat(Base):
    __tablename__ = 'bot_chats_and_sheets'

    id = Column(Integer, primary_key=True)
    chat_id=Column(String)
    sheet_id = Column(String)
    


class BotTransfer(Base):
    __tablename__ = 'bot_transfer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_today = Column(String(255))
    cash = Column(String(255))
    semenov_card = Column(String(255))
    bmp_card = Column(String(255))
    papka_card = Column(String(255))
    tochka_bank = Column(String(255))
    other_banks = Column(String(255))
    payment_date = Column(String(255))
    payment_message = Column(String(255))
    reply_message = Column(String(255))
    chat_id = Column(String(255))
    

