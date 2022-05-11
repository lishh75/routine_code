import os
def files(path,rt=False):
    '''
	list file's names or return its
    '''
    files=os.listdir(path)
    if not rt:
    	for i in files:
        	print(i)
    else: return files
