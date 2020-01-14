import sqlite3
import random

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

class Game:
    def __init__(self):
        self.stooopid=0

    def setup_questions(self):
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM questions")
        result = cur.fetchone()[0]
        question_list = list(range(1,result+1))
        random.shuffle(question_list)
        return question_list

    def get_question(self, conn, wantedquestion):
        questionanswers = []
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions WHERE id=?", (wantedquestion,))
        question = cur.fetchone()[1]
        questionanswers.append(question)
        cur.execute("SELECT answer, correct_answer FROM answers WHERE question=?", (wantedquestion,))
        answers = cur.fetchall()
        questionanswers.append(answers)
        return questionanswers

if __name__ == '__main__':
    conn = create_connection(r"pythonsqlite.db")
    questionair = Game()
    questionslist = questionair.setup_questions()
    get_question = questionair.get_question(conn, questionslist[0])
    print(get_question[0])
    
    print(get_question[1][2])