# Project Structure & Design

Django is designed such that each part of the website is compartmentalized from other parts.

There are 2 Django apps that I have created and really only 1 is of any significance.

1. `/api` - This is the meat of this project. It contains the models and api endpoints.
2. `/website` -  The initial webpage that a visitor sees when they visit the server's base url

The applications are setup such that the main `/project/urls.py` file redirects all traffic to the application specific `/api/urls.py` file if the `/api` directory is used on the base url. This is to say that if I call `http://tams-142602.appspot.com/api/` all traffic will be further routed through the `/api/urls.py` file.

## Views (How responses are generated)

- All view controllers are stored in the `/views` folder inside the app directory.
- Every view inherits from a `ViewRequestDispatcher`, stored in `dispatcher.py`. This will intercept all method calls going to a view and check for exceptions. If an exception occurs, the dispatcher will handle it gracefully rather than simply showing status 500.
- Every view also inherits (through the `ViewRequestDispatcher`) from Django's base view class. This means that when you define the view class, you set the methods of that class corresponding to the methods of the request: get, push, put, delete, update, etc.
- If the `urls.py` class specifies that the url should include a parameter. The parameter is passed into these view methods as a function parameter.
- Every view in the `/api` application will simply dump JSON into the response at the end of the view methods.

## Errors

All errors are generated from the classes in `/common/error.py`. Simply initialize one of the error classes with the message and return to an exception throw.

## Models   

- All models are stored in the `/models` directory inside the app directories.
- Models are represented as classes. Each class inherits from a base model class. The name of the class corresponds to the name of the model. The attributes of the class correspond to the attributes of the model.

> NOTE: Since the project uses Google App Engine's NoSQL database, there is no need to `makemigrations` and `migrate`. These commands initialize a regular SQL database with the relationships and manages any migrations from model versions.

I have built an ERD diagram to illustrate the relationships between models. [View The Entity Relationship Diagram (ERD)](./ERD.pdf)

## User Model

A non standard user model is used. This will make it much easier to add attributes to a user profile. The user model is stored in `/models/user.py`.
