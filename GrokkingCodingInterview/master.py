import os.path
import sys
def do():
    signature = input('Enter signature here:\n').lstrip().rstrip()
    signature = signature.split("->")[0].rstrip()
    signature = signature.replace("self, ","")
    signature = signature.replace(": str","")
    signature = signature.replace(": int","")
    signature = signature.replace(": ListNode","")
    signature = signature.replace(": List[int]","")
    signature = signature.replace(": List[str]","")
    filename = signature.split()[1]
    filename = filename[:filename.index('(')]
    print("Enter problem description:")
    problem =sys.stdin.readlines()
<<<<<<< HEAD
    save_path = '/Users/nbhushan/OneDrive - Adobe/Nidhi Folder/Study/Python/MyPythonWS/GrokkingCodingInterview'

=======
    save_path = '/Users/nbhushan/OneDrive - Adobe/Nidhi Folder/N - Personal/Study/Python/MyPythonWS/GrokkingCodingInterview'
>>>>>>> 88bf0bda88764f957d7d0656826c2ad9033373ba
    filepath = os.path.join(save_path, filename+'.py')
    f = open(filepath, "a")
    print(filepath)
    f.write("'''")
    f.write(''.join(problem))
    f.write("'''\n\n")
    f.write("from collections import Counter\n")
    if "head" in signature or "node" in signature:
        f.write("\nclass ListNode(object):\n")
        f.write("\tdef __init__(self, val, next=None):\n")
        f.write("\t\tself.val = val\n")
        f.write("\t\tself.next = next\n\n")
<<<<<<< HEAD
        f.write("\tdef printList(self):\n")
        f.write("\t\twhile self:\n")
        f.write("\t\t\tprint(self.val, end='->')\n")
        f.write("\t\t\tself = self.next\n")
        f.write("\t\tprint('None')\n\n")
        f.write(signature+":\n    pass\n\n")
        f.write("head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))")
        f.write("\n"+signature[4:len(signature)])
        f.write("\nhead.printList()")
    else:
        f.write(signature+":\n    pass\n\n")
        f.write("\nprint("+signature[4:len(signature)]+")")
        f.close()
=======
    f.write(signature+":\n    pass\n\n")
    f.write("\nprint("+signature[4:len(signature)]+")")
    f.close()
>>>>>>> 88bf0bda88764f957d7d0656826c2ad9033373ba

do()