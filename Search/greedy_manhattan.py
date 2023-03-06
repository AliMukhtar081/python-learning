import heapq

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i*3+j]
            if tile != -1:
                goal_x = (tile - 1) % 3
                goal_y = (tile - 1) // 3
                distance += abs(j - goal_x) + abs(i - goal_y)
    return distance

def is_goal(state, goal_state):
    return state == goal_state or state == tuple([-1] * len(goal_state))

def successors(current_state):
    blank_index = current_state.index(-1)
    successor_states = []
    moves = {1: -3, 2: 3, 3: -1, 4: 1}
    for move, offset in moves.items():
        new_offset = blank_index + offset
        if move == 1 and blank_index >= 3:
            new_state = list(current_state)
            new_state[blank_index], new_state[new_offset] = new_state[new_offset], new_state[blank_index]
            successor_states.append((tuple(new_state), 1))
        elif move == 2 and blank_index <= 5:
            new_state = list(current_state)
            new_state[blank_index], new_state[new_offset] = new_state[new_offset], new_state[blank_index]
            successor_states.append((tuple(new_state), 1))
        elif move == 3 and blank_index % 3 != 0:
            new_state = list(current_state)
            new_state[blank_index], new_state[new_offset] = new_state[new_offset], new_state[blank_index]
            successor_states.append((tuple(new_state), 1))
        elif move == 4 and blank_index % 3 != 2:
            new_state = list(current_state)
            new_state[blank_index], new_state[new_offset] = new_state[new_offset], new_state[blank_index]
            successor_states.append((tuple(new_state), 1))
    return successor_states

def greedy_first_search(initial_state, goal_state):
    frontier = []
    explored = set()
    heapq.heappush(frontier, (manhattan_distance(initial_state), initial_state))
    while frontier:
        state = heapq.heappop(frontier)[1]
        if is_goal(state, goal_state):
            return state
        explored.add(state)
        for successor_state, _ in successors(state):
            if successor_state not in explored:
                heapq.heappush(frontier, (manhattan_distance(successor_state), successor_state))
    return None


initial_state = (1, 2, 3, 4, 5, 6, -1, 7, 8)
goal_state = (1, 2, 3,-1, 4, 5, 6, 7, 8)
solution = greedy_first_search(initial_state,goal_state)
print(solution)
