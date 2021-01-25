'''Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
'''

from collections import Counter
def checkConflict(appointments):
    appointments.sort(key=lambda x:x[0])
    end = appointments[0][-1]
    for i in range(1, len(appointments)):
        if appointments[i][0]<end:
            return False
        end = appointments[i][-1]
    return False
appointments = [[1,4], [2,5], [7,9]]
print(checkConflict(appointments))
