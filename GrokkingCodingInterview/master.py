import os.path
import sys
def do():
    signature = input('Enter signature here:\n').lstrip().rstrip()
    signature = signature.split("->")[0].rstrip()
    signature = signature.replace("self, ","")
    signature = signature.replace(": str","")
    signature = signature.replace(": List[int]","")
    filename = signature.split()[1]
    filename = filename[:filename.index('(')]
    print("Enter problem description:")
    problem =sys.stdin.readlines()
    save_path = '/Users/nbhushan/OneDrive - Adobe Systems Inc/Nidhi Folder/N - Personal/Study/Python/MyPythonWS/GrokkingCodingInterview'
    filepath = os.path.join(save_path, filename+'.py')
    f = open(filepath, "a")
    f.write("'''")
    f.write(''.join(problem))
    f.write("'''\n\n")
    f.write(signature+":\n    pass\n\n")
    f.write("\n"+signature[4:len(signature)])
    f.close()

do()