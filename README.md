# Zoo database

## App

### model folder

Contains files that is used for connecting with database.

### schema folder

is used for validating data. Using marshmellow Schema for validating input data.

Serialize app-level objects to primitive Python types. The serialized objects can then be rendered to standard formats such as JSON for use in an HTTP API.

### utils

contains db variable that has value of SQLAlchemy as the toolkit for fobject rational mapper (ORM).

### views

- GET method is used to retrieve data on a server.
- POST method is used to create new data or resources.
- PUT method is used to replace or updating an existing data or resources with the updated version data or resources.
- DELETE method is used to remove data from a database.

- SQLAlqhemy : for object relational mapper (python SQL toolkit); poetry add flask-SQLAlchemy
