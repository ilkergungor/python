import os, shutil

source = 'C:\\PY\\test.txt'
empty_path= 'C:\\PY\\empty_folder'
folderDir= 'folder'

try:
      shutil.rmtree(folderDir)
      os.remove(source)
      os.rmdir(empty_path) #! DELETES DIRECTORY
except FileNotFoundError as e:
      print(e)
except PermissionError as e:
      print(e)
except OSError as e:
      print(e)  
else:
      print('Successfully deleted')


      
      