## mysite
A simple Todo List App developed using Django Web Framework. Allows filtering of the activities based on day, week, month, year.
Also allows sorting based on the activity status.

## How to deploy the Django web app on PythonAnywhere

# Step 1: Fork
Fork the mysite repository to create your own copy of mysite Django App

# Step 2: Upload your code to PythonAnywhere
Use bash console on PythonAnywhere to upload your code from github repository
for example:
```
$ git clone https://github.com/myusername/mysite.git
```

# Step 3: Create a virtualenv
Create a virtualenv by mentioning your project name and the version of python you want to use
``` 
$ mkvirtualenv --python=/usr/bin/python3.4 mysite-virtualenv 
```

# Step 4: Install Django
```
(mysite-virtualenv)$ pip install django
```

# Step 5: Create a Web app with Manual Config
Head over to the Web tab and create a new web app, choosing the "Manual Configuration" option and the right version of Python 
(the same one you used to create your virtualenv).

# Step 6: Enter your virtualenv name
Once that's done, enter the name of your virtualenv in the Virtualenv section on the web tab and click OK. 
You can just use its short name "mysite-virtualenv", and it will automatically complete to its full path in /home/username/.virtualenvs.

# Step 7: Edit your WSGI file
Delete everything except the Django section. Your WSGI file should look something like this:

+++++++++++ DJANGO +++++++++++
```
import os
import sys

path = '/home/myusername/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
# Step 8: Save the file, hit reload button for your domain.
Visit your site and the web app should be live


## License
[MIT License](https://github.com/ShreyaPrabhu/mysite/blob/master/LICENSE.md)





 
