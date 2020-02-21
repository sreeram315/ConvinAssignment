## **Index**

1. Documentation
2. Postman Collection
3. Setup



## **Documentation**

------

Find it here: 

https://documenter.getpostman.com/view/8124575/SzKTwJyH?version=latest



## **Postman Collection**

------

Use the following link:

https://www.getpostman.com/collections/233ba565a493c17a649e

While testing please add an environmental variable call URL with value as local host domain.



## Convin Assignment backend setup

*Note: Make sure you have any version of python 3 installed before proceding to  furthur steps. To download visit https://www.python.org/downloads/*



1. Clone the code from the **git** repository into the local machine using the *git clone* command. Provide the access keys when prompted.

   ` $ git clone URL_TO_REPO FOLDER_NAME`

 For instance
  ` $ git clone https://github.com/sreeram315/ConvinAssignment root`

------

2. Navigate into the folder the code has copied into. To keep dependencies required by this project separately, create a virtual environment in the same folder.

   `$ cd root`

   `$ virtualenv -p python3 .`

   

(if you do not have *virtualenv* installed, do   `$ pip install virtualenv`)

------

3. Enter the virtual environment by executing:

   ​     `$ source bin/activate`

   on Windows OS:  

   `$ .\Scripts\activate`

if you do a   `$ pip freeze`   now, you will see that you have no packages installed.

------

4. To install all the packages required for the project (*mentioned in requirement.txt file*), do:

   `$ pip install -r requirements.txt`

Proceed when all the packages are successfully installed.

------

5. To use a local database for development purpose, replace the existing *database* to any local database.
   Here is an instance of using *sqlite* for the same.

   `open /root/asmp/settings.py`

   update the default database to following:

```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
  }
```

------

6. Make migrations to the database.

  `$ python3 manage.py migrate`

   (*make sure you are in the root folder where manage.py is present*)

------



7. Create a super user.

  `$ python3 manage.py createsuperuser`

Use the credentials for logging into Django admin interface after next step.

------

8. Start the Django server

  `$ python3 manage.py runserver`

The local server should be up and running. Happy developing.

------

9. Start Redis server, Consumer and Producer.

`$ redis-server`

`$ celery -A tasks.tasks beat --loglevel=DEBUG`

`$ celery -A asmt worker --loglevel=info`

