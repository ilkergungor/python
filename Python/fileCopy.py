import shutil

shutil.copyfile('test.txt', 'copied.txt') #!COPIES CONTENT OF THE FILE (SRC, DST)

shutil.copy('test.txt', 'copied.txt') #! copyfile() + PERMISSION MODE DST CAN BE DIRECTORY (SRC, DST )

shutil.copy2('test.txt', 'copied.txt') #! copy() + COPIES METADATA (CREATION AND MODIFY TIMES) (SRC, DST )



