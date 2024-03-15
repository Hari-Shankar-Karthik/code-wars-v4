from random import randint

name = "my_script"

def ActPirate(pirate):
    if pirate.investigate_current().startswith("island"):
        return 0
    
    return randint(1, 4)

def ActTeam(team):
    pass