from sys import executable
from subprocess import check_call
import sqlite3


def clear_history():

    print("Cleaning database .")

    # Connects to the database
    history = sqlite3.connect(r"assets/database/history.db")

    # Sets cursor
    cursor = history.cursor()

    # Gets ready to save it to database
    cursor.execute("DELETE FROM history")
    # Saves it to database
    history.commit()
    # Terminates connection
    history.close()

    print("Database cleared.")

    # To delete all __pycache__
    check_call([executable, "-m", "pyclean", "."])

    print("Clearing Json .")

    # to clear Json history
    json = open(r"assets/json/history.json", "w")
    json.write("[]")

    print("Json history cleared.")


if __name__ == "__main__":
    clear_history()
