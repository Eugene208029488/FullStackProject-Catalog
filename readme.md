#Item Catalog
Build a web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users should have the ability to post, edit, and delete their own items.

#Technology used:
1. Python Webserver (BaseHTTPServer, cgi)
2. SQLAlchemy - ORM for Python
3. Sqlite - database
4. Flask framework to build web application
	* Routing
	* Jinja2 template
	* Form request and redirect
	* message flashing
	* RESTful API -JSON endpoint
5. OAuth 2.0 - Google+ and Facebook Third party Auth Provider

#Instructions to setup and launch the application
1. Launch Vagrant VM (type Vagrant Up)
1. Login to vagrant
  * type '*vagrant ssh*'
  * cd /vagrant/catalog
2. Create a new SQLite database and its table using SQLAlchemy.
  * type "*python database_setup.py*"
3. Load test data
  * type "*python loadgrocery.py*"
4. Run application
  * type "*python catalog.py*"

#Instructions for the catalog application
1. Open browser and type "*http://localhost:5000"
  * Homepage displays all current categories with the latest added items.
  * Click "Catalog App" to go to homepage.
  * Selecting a specific category shows you all the items available for that category.
  * Selecting a specific item shows you specific information about that item.
  * Can use either Google+ or Facebook to authenticate and login user.
  * After logging in, a user has the ability to add, update, or delete item information. Users should be able to modify only those items that they themselves have created.
  * Click logout to logout user.

2. Provide an RESTful API JSON enpoint
  * Type http://localhost:5000/catalog.json - will return all category and its items
  * Type http://localhost:5000/catalog/[category_name]/json - ex. http://localhost:5000/catalog/Fruits/json - will return all items for Fruits category