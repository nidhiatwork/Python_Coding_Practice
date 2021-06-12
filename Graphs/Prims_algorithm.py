'''In an ocean, there are n islands some of which are connected via bridges with some cost attaced with it. Find bridges in such a way that all islands are connected with minimum cost of travelling.
'''
import heapq
def get_minimum_cost_of_connecting(num_islands, bridge_config):
    adj_list = []
    for _ in range(num_islands+1):
        adj_list.append([])
    for config in bridge_config:
        adj_list[config[0]].append([config[1], config[2]])
        adj_list[config[1]].append([config[0], config[2]])
    visited = set()
    h = []
    total_cost=0
    heapq.heappush(h, (0, bridge_config[0][0]))
    while len(h)>0:
        cost,island = heapq.heappop(h)
        if island in visited:
            continue
        visited.add(island)
        total_cost +=cost
        for neighbor,edge_cost in adj_list[island]:
            if neighbor not in visited:
                heapq.heappush(h,(edge_cost, neighbor))
    return total_cost

def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)