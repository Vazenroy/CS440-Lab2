import vacuum
class HillClimbingAgent(vacuum.vacuum):

    def choose_move(self, current, neighbors):
        most_dirt = current
        best_direction = None
        for direction in neighbors:
            if neighbors[direction] > most_dirt:
                most_dirt = neighbors[direction]
                best_direction = direction

        if best_direction is None:
            return 'NoOp' # found largest amount of dirt
        return best_direction
    