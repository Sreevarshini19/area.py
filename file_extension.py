ext=["py","c","cpp","txt","pdf","doc","ppt","java"]
filename=input("Enter the file name")
t=filename.split('.')
print("The extension of the filename is ")
if t[-1]==ext[0]:
    print("Python")
elif t[-1]==ext[1]:
    print("C")
elif t[-1]==ext[2]:
    print("C++")
elif t[-1]==ext[3]:
    print("Text document")
elif t[-1]==ext[4]:
    print("Portable Document Format")
elif t[-1]==ext[5]:
    print("Document")
elif t[-1]==ext[6]:
    print("Powerpoint")
elif t[-1]==ext[7]:
    print("Java")