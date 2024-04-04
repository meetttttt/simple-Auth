"""
This is the utils file where we will write our utilities function, which is needed to run the projects.
"""
# Imports are written here
import os
import logging
import mysql.connector
from dotenv import load_dotenv

# loading env
load_dotenv()

# Set up logging
logging.basicConfig(filename=os.getenv("LOG_FILE"),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def user_auth(userName: str, userPassword: str, userID=None, sessionID=None) -> bool:
    """
    This function will do the authentication from the db
    :param userName: Name of the user
    :param userPassword: Password of the user
    :param userID: ID of the user
    :param sessionID: User Session ID
    :return: bool whether the user is authenticated or not.
    """
    try:
        # Connect to MySQL
        logging.info(f"Starting with connection")
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DBNAME")
        )
        # Create cursor
        cursor = conn.cursor()

        logging.info(f"Data for auth: {userName, userPassword}")
        # Execute query
        query = "SELECT * FROM user_auth WHERE username = %s AND password = %s"
        cursor.execute(query, (userName, userPassword))

        # Fetch results
        result = cursor.fetchone()
        # Close cursor and connection
        cursor.close()
        conn.close()

        if result:
            logging.info(f"User Auth Success: {userName}")
            return True
        else:
            logging.info(f"User Auth Failed: {userName}")
            return False
    except Exception as e:
        logging.info(f"Error[utils.py]: {e}")
        return False




