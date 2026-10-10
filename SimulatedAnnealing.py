import random
import math
import vacuum
class SimulatedAnnealing(vacuum.vacuum):
    def choose_move(self, current, neighbors, t):
        #get T
        T = self.schedule(t)
        print("T =", T)

        #if T is 0, end loop
        if T == 0:
            return('Highest Found')
        
        #get random neighbor
        next_dir = random.choice(list(neighbors.items()))
        print("Random direction picked:", next_dir[0])

        #if random neighbor is greater than current, move that direction
        delta_E = next_dir[1] - current
        if delta_E > 0:
            print(next_dir[1], "is better than", current)
            return next_dir[0]
        #otherwise, get a probability from T and return that direction if in bounds
        else:
            prob = math.exp(delta_E / T)
            rand_val = random.random()
            if rand_val < prob:
                print(next_dir[0], "selected with probability", prob)
                return next_dir[0]
            #if not, do nothing
            else:
                print(next_dir[0], "rejected with probability", prob)
                return 'NoOp'
    
    def schedule(self, t):
        return max(10 - 0.1*t, 0)
