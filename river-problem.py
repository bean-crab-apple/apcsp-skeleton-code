import copy

# Define a function that takes in a state as a dictionary and returns True if the state meets the conditions and False if it does not
def isValid(state):
    if state["wolf"] == state["goat"] and state["wolf"] != state["person"]:
        return False
    elif state["goat"] == state["cabbage"] and state["goat"] != state["person"]:
        return False
    else:
        return True
# DONE
    

# Define a function that takes in a state as a dictionary and returns a list of all valid states that can be reached from 1 move of the input state
# This function will need to call the function isValid(state)
def get_next_states(state):
    next_states = []
    same_side = []
    for entity in state:
        if state[entity] == state["person"] and entity != "person":
            same_side.append(entity)
    for entity in same_side:
        temp_state = copy.deepcopy(state)
        temp_state[thing] = not state[thing]
        temp_state["person"] = not state["person"]
        if isValid(temp_state) == True:
            next_states.append(temp_state)
            # append for seen later
    just_person = copy.deepcopy(state)
    just_person["person"] = not just_person["person"]
    if isValid(just_person) == True:
        next_states.append(just_person)
        # append for seen later
    return next_states


# Define a recursive function that takes in a current_state and win_state and returns the path to those states using the Depth First Search algorithm
# This function will need to call the function get_next_states(state), as well as itself
def dfs(current_state, win_state):
    Test
    
# Test your code! Does it solve the river crossing riddle?
initial_state = {
    "wolf": False,
    "goat": False,
    "cabbage": False,
    "person": False
}

win_state = {
    "wolf": True,
    "goat": True,
    "cabbage": True,
    "person": True
}

visited_states = [initial_state]
path = []

if dfs(initial_state, win_state):
    for index, step in enumerate(path):
        print("After move", index+1, "the state is ", step)
else:
    print("No solution found.")

