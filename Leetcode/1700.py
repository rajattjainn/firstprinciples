class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        new_students = []
        while len(students)>0:
            std = students.pop(0)
            if sandwiches[0] == std:
                sandwiches.pop(0)
            else:
                new_students.append(std)
            
        if len(new_students) == 0:
            return 0
        
        if sum(new_students) == len(new_students) and sandwiches[0] == 0:
            return len(new_students)
        
        if sum(new_students) == 0 and sandwiches[0] == 1:
            return len(new_students)
        
        return self.countStudents(new_students, sandwiches)


students = [1,1,1,0,0,1]

sandwiches = [1,0,0,0,1,1]


print (Solution().countStudents(students, sandwiches))
