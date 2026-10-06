import random
class VacuumEnvironment():

    def __init__(self):
        self.status = {}
        for i in range(16):
            self.status["loc_" + chr(ord('A') + i)] = random.choice(['Clean', 'Dirty'])

    def execute_action(self, agent, action):
        if action == 'Up':
            pass
        elif action == 'Down':
            pass
        elif action == 'Left':
            pass
        elif action == 'Right':
            pass
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                self.status[agent.location] = 'Clean'

    def default_location(self, thing):
        choices = []
        for i in range(16):
            choices.append("loc_" + chr(ord('A') + i))
        return random.choice(choices)

vacuum_env = VacuumEnvironment()
print("State of the Environment: {}.".format(vacuum_env.status))