# Simulated swarm of agents
agents = [lambda x: x + 1, lambda x: x * 2, lambda x: x - 3]

def swarm_process(input_val):
    result = input_val
    for agent in agents:
        result = agent(result)
    return result

print("Swarm Output:", swarm_process(5))  # Output: 9
