'''
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
'''

def getImportance_1(employees, id):
    emps = {employee[0]: employee for employee in employees}
    total_imp = emps[id][1]
    sub = emps[id][2]
    if not sub:
        return total_imp
    while sub:
        emp_id = sub.pop()
        total_imp += emps[emp_id][1]
        for item in emps[emp_id][2]:
            sub.append(item)
    return total_imp

def getImportance_2(employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        emps = {employee[0]: employee for employee in employees}
        def dfs(id):
            subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id][2]])
            return subordinates_importance + emps[id][1]
        return dfs(id)

employees, id = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# employees, id = [[1,2,[2]], [2,3,[]]], 2
print(getImportance_1(employees, id))
