import heapq

def uniform_cost_search(start_state, goal_state, successors):
   
    frontier = [(0, [start_state])]
    visited = set()
    while frontier:
        (priority, path) = heapq.heappop(frontier)
        state = path[-1] 
        if state == goal_state:
            return path
        if state  not in visited:
            visited.add(state)
            for (next_state, cost) in successors(state):
                if next_state not in visited:
                    next_path = path + [next_state]
                    next_priority = priority + cost
                    heapq.heappush(frontier, (next_priority, next_path))
    return None


def successors(current_state):
    blank_index = current_state.index(0)
    successor_states = []
    moves = {1: -3, 2: 3, 3: -1, 4: 1}
    for move, index_delta in moves.items():
        new_index = blank_index + index_delta
        if move == 1 and blank_index >= 3:
            new_state = list(current_state)
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            successor_states.append((tuple(new_state), 1))
        elif move == 2 and blank_index <= 5:
            new_state = list(current_state)
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            successor_states.append((tuple(new_state), 1))
        elif move == 3 and blank_index % 3 != 0:
            new_state = list(current_state)
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            successor_states.append((tuple(new_state), 1))
        elif move == 4 and blank_index % 3 != 2:
            new_state = list(current_state)
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            successor_states.append((tuple(new_state), 1))
    return successor_states


start_state = (1, 2, 3, 4, 0, 5, 6, 7, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
path = uniform_cost_search(start_state, goal_state, successors)
print(path)
