from sqlite3 import connect

connection = connect('Votes.db')
curs = connection.cursor()

CREATE_ELECTION_TABLE = """Create table if not Exists Votes
                       (id Integer primary key,
                        first_name Text,
                        last_name Text,
                        election_name Text,
                        name_category Text,
                        votes Integer,
                        date DATE
                        );"""

INSERT_ELECTION_TABLES = """INSERT INTO Votes (first_name,last_name,election_name,name_category,votes,
                            date) Values (?,?,?,?,?,?); """

SELECT_ELECTION_NAME = """SELECT election_name FROM Votes """

SELECT_ONE_ELECTION = """SELECT name_category from Votes where election_name=?; """

SELECT_ELECTION_POSITION = """SELECT first_name, last_name from Votes where name_category=?; """

SELECT_FETCH_VOTES = """SELECT votes from Votes where first_name=? """

SELECT_ELECTION_RESULTS = """SELECT first_name, last_name, votes from Votes where election_name=? and 
                            name_category=?; """

UPDATE_VOTES_COLUMN = """UPDATE Votes SET votes=? where first_name=?"""


def create_table():
    with connection:
        curs.execute(CREATE_ELECTION_TABLE)


def insert_into_election(first_name, last_name, election_name, name_category, vote, date):
    with connection:
        curs.execute(INSERT_ELECTION_TABLES, (first_name, last_name, election_name, name_category, vote, date))


def select_election_name():
    with connection:
        curs.execute(SELECT_ELECTION_NAME)
        return curs.fetchall()


def selection_election_one(election_name):
    with connection:
        curs.execute(SELECT_ONE_ELECTION, (election_name,))
        return curs.fetchall()


def select_election_position(name_category):
    with connection:
        curs.execute(SELECT_ELECTION_POSITION, (name_category))
        return curs.fetchall()


def select_get_votes(first_name):
    with connection:
        curs.execute(SELECT_FETCH_VOTES, (first_name,))
        return curs.fetchone()


def increase_votes(voted, first_name):
    with connection:
        curs.execute(UPDATE_VOTES_COLUMN, (voted, first_name,))


def get_election_results(election_name, name_category):
    with connection:
        curs.execute(SELECT_ELECTION_RESULTS, (election_name, name_category,))
        return curs.fetchall()

