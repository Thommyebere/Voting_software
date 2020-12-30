from users import database


class Vote_process(object):
    def __init__(self):
        pass
    @staticmethod
    def voting():
        elections = []
        election_name = database.select_election_name()
        for election in election_name:
            elect_name = "".join(election)
            elections.append(elect_name)
        unique_election_name = set(elections)
        for elect_names in unique_election_name:
            print(elect_names)

# tyy=Vote_process()
# tyy.voting()
