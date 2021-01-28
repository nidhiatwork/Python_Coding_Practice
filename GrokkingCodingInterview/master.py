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
    save_path = '/Users/nbhushan/OneDrive - Adobe/Nidhi Folder/Study/Python/MyPythonWS/GrokkingCodingInterview'

    filepath = os.path.join(save_path, filename+'.py')
    f = open(filepath, "a")
    print(filepath)
    f.write("'''\n")
    f.write(''.join(problem).strip())
    f.write("\n'''\n\n")
    f.write("from collections import Counter\n")
    if "root" in signature or "tree" in signature:
        f.write("\nclass TreeNode(object):\n")
        f.write("\tdef __init__(self, val, left=None, right=None):\n")
        f.write("\t\tself.val = val\n")
        f.write("\t\tself.left = left\n")
        f.write("\t\tself.right = right\n\n")
        f.write(signature+":\n    return\n\n")
        f.write("root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5, TreeNode(10), TreeNode(11))), TreeNode(3, TreeNode(6, TreeNode(12), TreeNode(13)), TreeNode(7, TreeNode(14), TreeNode(15))))")
        f.write("\nroot = "+signature[4:len(signature)])
    elif "head" in signature or "node" in signature:
        f.write("\nclass ListNode(object):\n")
        f.write("\tdef __init__(self, val, next=None):\n")
        f.write("\t\tself.val = val\n")
        f.write("\t\tself.next = next\n\n")
        f.write("\tdef printList(self):\n")
        f.write("\t\twhile self:\n")
        f.write("\t\t\tprint(self.val, end='->')\n")
        f.write("\t\t\tself = self.next\n")
        f.write("\t\tprint('None')\n\n")
        f.write(signature+":\n    return\n\n")
        f.write("head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))")
        f.write("\nhead = "+signature[4:len(signature)])
        f.write("\nhead.printList()")
    else:
        f.write(signature+":\n    pass\n\n")
        f.write("\nprint("+signature[4:len(signature)]+")")
        f.close()

do()
