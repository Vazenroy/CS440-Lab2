class VacuumEnvironment(Environment):

    def __init__(self):
        super().__init__()
        to_add = {}
        for i in range 16:
            to_add["loc_" + chr(ord('A') + i)] = random.choice(['Clean', 'Dirty'])
        self.status = to_add

    def thing_classes(self):
        return [Wall, Dirt, HillClimbingAgent]

    def percept(self, agent):
        return (agent.location, self.status[agent.location])

    def execute_action(self, agent, action):
        if action == 'Up':
            #insert action
            agent.performance -= 1
        elif action == 'Down':
            #insert action
            agent.performance -= 1
        elif action == 'Left':
            #insert action
            agent.performance -= 1
        elif action == 'Right':
            #insert action
            agent.performance -= 1
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            self.status[agent.location] = 'Clean'

    def default_location(self, thing):
        return random.choice([loc_A, loc_B])