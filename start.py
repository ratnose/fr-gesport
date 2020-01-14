import sqlite3
from sqlite3 import Error
from random import randint

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

class Questions:

    def __init__(self, question=1):
        self.question = 1

    def get_first_question(self, conn):
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM questions")
        result = cur.fetchone()[0]
        start_q = randint(1, result)
        return start_q

    def get_question(self, conn, start_question):
        cur = conn.cursor()
        cur.execute("SELECT question FROM questions WHERE id=?", (start_question,))
        result = cur.fetchone()[0]
        return result

    def get_answers(self, conn, start_question):
        cur = conn.cursor()
        cur.execute("SELECT * FROM answers WHERE question=?", (start_question,))
        result = cur.fetchall()
        return result

    def answer_correect(self, conn, action):
        cur = conn.cursor()
        cur.execute("SELECT correct_answer FROM answers WHERE question=?", (action,))
        result = cur.fetchone()[0]
        return result


if __name__ == '__main__':
    my_questionair = Questions()
    conn = create_connection(r"pythonsqlite.db")
    print (conn)
    print("Lets [s]tart!")
    while True:
        action = input("What is you answer? \n").upper()
        
        if action == 'S':
            start_question = my_questionair.get_first_question(conn)
            first_question = my_questionair.get_question(conn, start_question)
            answers = my_questionair.get_answers(conn, start_question)
            print(first_question)
            for count, answer in enumerate(answers, start=1):
                print(count, answer[2])

        if action not in ("1","2","3","4","5"):
            print("Svara med siffra mellan 1 och 5")
        else:
            print(action, answers[int(action)])
            if action != (answers[4]):
                print("Du svarade fel!")
            else:
                print("Rätt")
