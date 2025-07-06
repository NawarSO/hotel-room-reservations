# "hotel-room-reservations" 
Welcome to our simple project.
In this project you can find system analysis for room reservation system including srs and UMLs
# To install the libraries 
you can find a file named 'requirements.txt' it include the libraries you need to run the project.
You can install them using the command :
python install -r requirements.txt
# To run the project:
At first you need to migrate the data base using the commands:
python manage.py makemigrations
python manage.py migrate
Now you can run the server using the command :
python manage.py runserver
the server now will run on http://localhost:8000/
# Api documentation 
you can find api documentation on http://localhost:8000/swagger/
you will find a list with all the crud operations and endpoints that you can access to.

# Important Note 
in the views.py for more security you must to change the 'AllowAny' to 'IsAuthenticated'  or 'IsAdminUser' it shows in views.py
In this way only the register users or employees will access the endpoint.



