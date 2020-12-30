from users import database


class Results(object):
    def __init__(self):
        pass

    def election_results(self):
        elections = []
        election_name = database.select_election_name()
        for election in election_name:
            elect_name = "".join(election)
            elections.append(elect_name)
        unique_election_name = set(elections)
        for elect_names in unique_election_name:
            print(elect_names)
        election_choice = input("What elections results do you want to see?  ")
        category = database.selection_election_one(election_choice)
        category_list = []
        for category_names in category:
            category_list.append(category_names)
        unique_category_set = set(category_list)
        for returned_voted in unique_category_set:
            vote_category = (''.join(map(str, returned_voted)))
            print("For the post of {}, these are the results".format(vote_category))
            results = database.get_election_results(election_choice, vote_category)
            for first_name, last_name, vote in results:
                print("{:5}| {:5}| {:5} ".format(first_name, last_name, vote))



