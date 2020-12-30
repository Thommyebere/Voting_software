from users import database
import datetime
from users.vote_terminal import Vote_process
from users.election_results import Results


class Voting(object):

    def __init__(self):
        print("What do you wanna do? ")
        choice = """
        1.Press 1 to CREATE AN ELECTION POLL
        2.Press 2 to VOTE AMONGST ELECTION CATEGORY
        3.PRESS 3 to VIEW THE RESULTS OF A PARTICULAR ELECTION
        """
        self.mychoice = int(input(choice))

    def choices(self):
        if self.mychoice == 1:
            self.election()
        elif self.mychoice == 2:
            Vote_process.voting()
        elif self.mychoice == 3:
            result=Results()
            result.election_results()
        else:
            Voting()

    @staticmethod
    def election():
        print("<-------------WELCOME--------------->")
        name_election = input("Enter name of election:  ")
        num_category = int(input("How many election categories do you want to create:  "))
        counter = 1
        category_choice = 1
        while counter <= num_category:
            name_category = input("Enter name for category {}:  ".format(counter))
            votes = int(input("How many persons do you have for the {} category:  ".format(name_category)))
            while category_choice <= votes:
                vote_first_name = input("Enter first name for the {} position: ".format(name_category))
                vote_last_name = input("Enter last name for the {} position:  ".format(name_category))
                vote_count = 0
                date = datetime.datetime.now()
                database.insert_into_election(vote_first_name, vote_last_name, name_election, name_category, vote_count,
                                              date)
                category_choice = category_choice + 1
                print("Enter for the next category: ")

            else:
                category_choice = 1
                counter = counter + 1
        else:
            print("Thanks for creating a category")
            Voting()



