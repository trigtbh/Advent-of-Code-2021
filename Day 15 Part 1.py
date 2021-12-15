import helper
import queue
from queue import PriorityQueue

with open(helper.nrml("day15.txt")) as f:
    contents = f.read().splitlines()

nodes = []

for y in range(len(contents)):
    for x in range(len(contents[0])):
        nodes.append((y, x))

def validate(point):
    y, x = point
    return (0 <= y < len(contents)) and (0 <= x < len(contents[0]))


def reconstruct(camefrom, current):
    total = [current]
    while current in camefrom.keys():
        current = camefrom[current]
        total = [current] + total
    return total

def h(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] + p2[1])

def astar(start, goal, h):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    came_from = {}
    g_score = {spot: float("inf") for spot in nodes}
    g_score[start] = 0
    f_score = {spot: float("inf") for spot in nodes}
    f_score[start] = h(start, goal)

    open_set_hash = {start}

    while not open_set.empty():


        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == goal:
            return reconstruct(came_from, goal)
            

        y, x = current
        valid = list(filter(validate, [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]))
        for neighbor in valid:
            ny, nx = neighbor
            temp_g_score = g_score[current] + int(contents[ny][nx])

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor, goal)
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    
                    open_set_hash.add(neighbor)

    return False

path = astar((0, 0), (len(contents) - 1, len(contents[0]) - 1), h)
print(sum([int(contents[py][px]) for (py, px) in path]) - 1)