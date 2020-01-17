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
        question = []
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions WHERE id=?", (wantedquestion,))
        questionfetch = cur.fetchone()[1]
        question.append(questionfetch)
        
        return question

    def get_answers(self, conn, question):
        send_answers = []
        cur = conn.cursor()

        cur.execute("SELECT answer FROM answers WHERE question=?", (question,))
        send_answersfetch = cur.fetchall()
        
        for answer in send_answersfetch:
            
            send_answers.append(answer[0])

        return send_answers

    def checkAnswer(self, conn, question, answer):
        cur = conn.cursor()
        print("In value: {} - {}".format(question, answer))
        cur.execute("SELECT correct_answer FROM answers WHERE question = ? AND id = ?", (question, answer,))
        checked_answer = cur.fetchone()
        print("db: {}".format(checked_answer))
        
        return checked_answer

if __name__ == '__main__':
    conn = create_connection(r"pythonsqlite.db")
    theGame = Game()
    questionslist = theGame.setup_questions() #Slumpmässig lista av det som finns i db
    questions = len(questionslist) #Hur länge ska det hålla på?
    game = 0

    while questions > 0:    
        get_question = theGame.get_question(conn, questionslist[game])
        print("Frågor: {}".format(get_question[0]))

        get_answers = theGame.get_answers(conn, questionslist[game])
        for num, answer in enumerate(get_answers, start=1):
            print("{} - {}".format(num, answer))

        action = input("What is you answer? \n")
        #Behöver frågams nummer... inte strängen... numret blir för högt?!
        print(questionslist[game])
        check_answer = theGame.checkAnswer(conn, questionslist[game], int(action))
        print("-- {}".format(check_answer))

        game += 1
        questions -= 1