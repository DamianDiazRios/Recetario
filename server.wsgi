activate_this = '/home/server20/virtualenv/Recetario/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, "/home/server20/FLASK/Recetario/")


from app import app as application
