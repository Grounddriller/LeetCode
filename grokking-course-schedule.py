from collections import deque

def can_finish(num_courses, prerequisites):
    in_degree = [0] * num_courses
    graph = [[] for _ in range(num_courses)]

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque()
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)

    completed = 0

    while queue:
        current = queue.popleft()
        completed += 1

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses
