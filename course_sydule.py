import collections

courses = [[0,1],[0,2]]

course_leng = 3
def can_complet(courses,course_leng):
    adjList = collections.defaultdict(list)
    for course,pre in courses:
        adjList[pre].append(course)

    def dfs(node,track):
        track[node] = True
        for n in adjList[node]:
            if n in track or dfs(n,track):
                return True
        return False


    for n in range(course_leng):
        track = {}
        if dfs(n,track):
            return False
    return True

print(can_complet(courses,course_leng))
