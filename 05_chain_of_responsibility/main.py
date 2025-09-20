from chain import Chain
from team_member import TeamMember
from president import President
from vice_president import VicePresident
from manager import Manager
from secretary import Secretary
from worker import Worker

my_chain = Chain()
my_chain.chain.append(President())
my_chain.chain.append(VicePresident())
my_chain.chain.append(Manager())
my_chain.chain.append(Secretary())
my_chain.chain.append(Worker())
my_chain.chain.append(TeamMember())

tasks = [
    "write back",
    "meet president",
    "meet customer",
    "do work",
    "drive"
]

for task in tasks:
    my_chain.run_task(task)