from dotenv import load_dotenv
import os


load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")



print(db_host, db_user, db_password)