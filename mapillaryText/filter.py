import os
import shutil

for filename in os.listdir('images'):
    if os.path.getsize('images/'+filename) == 4805:
        os.remove('images/'+filename)