import heapq

def misplaced_tiles(state):
    misplaced = 0
    for i in range(9):
        if state[i] != i+1 and state[i] != 0:
            misplaced += 1
    return misplaced

def is_goal(state,goalstate):
    return state == goalstate

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

def greedy_first_search(initial_state,goalstate):
    frontier = [(misplaced_tiles(initial_state), initial_state)]
    explored = set()
    while frontier:
        state = heapq.heappop(frontier)[1]
        if is_goal(state,goalstate):
            return state
        explored.add(state)
        for successor_state, _ in successors(state):
            if successor_state not in explored:
                heapq.heappush(frontier, (misplaced_tiles(successor_state), successor_state))
        print(state)  
    return None



initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
goalstate=(1, 2, 3, 4,0, 5, 6, 7, 8,)
solution = greedy_first_search(initial_state,goalstate)
print(solution)
