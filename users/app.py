from users.first import Voting
from users import database

database.create_table()
opp = Voting()
opp.choices()
