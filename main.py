from dotenv import load_dotenv
import os 

from db.db import Database


#loading dotenv files
load_dotenv(override=True)

db_url = os.getenv('DB_URL')


def main():
  my_db=Database(db_url)
  print(my_db.get_payments_with_status_0)


if __name__ == '__main__':
    main()
