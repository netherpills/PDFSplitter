import os, PyPDF2, easygui
path, data = None, None

while data is None:
    data = easygui.multenterbox('Write the next information.', 'PDF Splitter System', ["Minimum page:", "Maximum page:", "New file name:"])
    if data != None:
        break
while path is None:
    path = easygui.fileopenbox(msg='Elije un .PDF', default=r'C:\Users\Mi-Pc\Documents', filetypes = '.pdf')
    if path != None:
        break
    
def split(path : str):
    reader = PyPDF2.PdfFileReader(open(path, 'rb'))
    writer = PyPDF2.PdfFileWriter()
    for i in range(int(data[0]), int(data[1])+1):
        writer.addPage(reader.getPage(i))
    writer.write(open(str(data[2])+'.pdf', 'wb'))
    easygui.msgbox(msg='PDF created succesfully.', title='Success')
split(path)
