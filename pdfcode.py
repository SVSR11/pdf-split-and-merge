import os
from PyPDF2 import PdfWriter, PdfReader
import time
from tkinter.filedialog import askopenfilename

start=time.time()
# Get the list of all files and directories
#path = askopenfilename(filetypes=[("Pdf Files", "*.pdf"), ("All Files", "*.*")])
path = "C://Users//dell//Desktop//project pdf//New folder"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
print(dir_list)
allname=[]
name10=[]
name0_9=[]
for name in dir_list:
    a=name.split('_')
    onlyname=a[0]
    
    allname.append(a[0])



for b in allname:
    for c in range(len(b)):
        if b[c].isdigit():
            if b[c+1].isdigit():
                index_=allname.index(b)
                name10.append(dir_list[index_])
                break
            else:
                index_=allname.index(b)
                name0_9.append(dir_list[index_])
                break


for filename in name10:
    name0_9.append(filename)

'''
count=0
quesrange=["1-2,6-6","1-3,6-8"]

#quesrange=[5,5,2,1,1,1,2,1,2,2]
ansrange=[]
writer = PdfWriter()
for pdfname in name0_9:
    
    pdfpath=path+'//'+pdfname
    reader = PdfReader(pdfpath)
    
    portion=quesrange[count]
    rang1=portion.split(",")
    for i in rang1:
        rangefinal=i.split('-')
        for j in range(int(rangefinal[0])-1,int(rangefinal[1])):
             writer.add_page(reader.pages[j])
    count+=1
    
    
'''# for i in range(quesrange[count]):
         #writer.add_page(reader.pages[i])
    
'''
    
 
# write to document-output.pdf
with open("PyPDF2-output.pdf", "wb") as fp:
    writer.write(fp)

end=time.time()
print("Time:-",
      ((end-start) * 10**3)/1000, "sec")
      
'''