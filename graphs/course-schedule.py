def canFinish(numCourses, prerequisites):
    # 1.  Initialize a dictionary to store the courses as keys, prerequisites as values
    # 2.  Initialize a set to store visited courses to prevent cycles
    # 3.  DFS for each course
    # 3a. If that course has a prerequisite, visit it until it doesnt
    # 3b. If that course path doesn't end up having an ending course without a prerequisite, return false

    course_map = { i:[] for i in range(numCourses) } # 1.
    course_set = set() # 2.

    for course, prerequisite in prerequisites:
        course_map[course].append(prerequisite)

    for course in range(numCourses):
        if not dfs(course_map, course_set, course):
            return False

    return True

def dfs(course_map, course_set, course):
    # 1.  Base cases

    if course in course_set:
        return False
    elif course_map[course] == []:
        return True

    # About to start traversing, so add to set
    course_set.add(course)

    for prerequisite in course_map[course]:
        if not dfs(course_map, course_set, prerequisite):
            return False
        
    # Successfully traversed, remove prerequisites and remove from set
    course_set.remove(course)
    course_map[course] = []

    return True

numCourses = 5
prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]

print(canFinish(numCourses, prerequisites))