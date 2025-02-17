class Solution:
    from collections import defaultdict, deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        numCourses: courses you have to take from 0 to numCourses - 1
        prerequisites: A list of list with [a, b] where you must take b to take a

        [3, 2], [2, 1], [3, 0], [2, 0]
        """
        def checkDependency(course, inStack):
            if course in inStack:
                return False
            if course in visited:
                return True
            dependent_courses = courseDict[course]
            checked = True
            inStack.add(course)
            visited.add(course)
            for dependent in dependent_courses:
                if not checkDependency(dependent, inStack):
                    return False
            inStack.remove(course)
            return checked

        courseDict = defaultdict(list)
        for prerequisite in prerequisites:
            course, prereq = prerequisite[0], prerequisite[1]
            courseDict[prereq].append(course)

        visited = set()
        for course in list(courseDict.keys()):
            checked = checkDependency(course, set())
            if not checked:
                return False
        return True
        
