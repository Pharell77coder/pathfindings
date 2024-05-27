import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid):
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1

            if 0 <= neighbor[0] < len(grid):
                if 0 <= neighbor[1] < len(grid[0]):
                    if grid[neighbor[0]][neighbor[1]]:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return []


if __name__ == "__main__":
    maps = [[False, True, False, False, False, False], [False, True, False, False, True, False],
            [False, True, False, False, True, False], [False, True, False, False, True, False],
            [False, True, False, False, True, False], [False, False, False, False, True, False]]
    
    start = (0, 0)
    goal = (len(maps) - 1, len(maps[0]) - 1)
    while True:
        path = a_star(start, goal, maps)
        print(f"Path from {start} to {goal}: {path}")
        if start == goal:
            break
        start = path[1]
        print(start)
















