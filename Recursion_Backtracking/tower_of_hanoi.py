def tower_of_Hanoi(num_disks, s, a, d):
    if num_disks==0:
        return
    if num_disks==1:
        # d.append(s[-1])
        # s.pop()
        print("{} {}".format(s, d))

    else:
        tower_of_Hanoi(num_disks-1, s, d, a)
        print("{} {}".format(s, d))
        tower_of_Hanoi(num_disks-1, a, s, d)

# tower_of_Hanoi(3, 'S', 'A', 'D')

def tower_of_Hanoi1(num_disks, s, a, d):
    if num_disks==0:
        return
    if num_disks==1:
        d.append(s[-1])
        s.pop()
        # print("{} {}".format(s, d))

    else:
        tower_of_Hanoi1(num_disks-1, s, d, a)
        # print("{} {}".format(s, d))
        tower_of_Hanoi1(num_disks-1, a, s, d)

s = [1,2,3]
a = []
d = []
tower_of_Hanoi1(3, s, a, d)
