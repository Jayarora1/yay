

import os
print("checking if file exists or not")
if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
else:
    print("This file doesnt exist")
