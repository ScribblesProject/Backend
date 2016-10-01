# Django Quick Start

**WAIT!!** If you are new to Django, please visit the `design.md` file in this folder to understand how Django is layed out. Then come here.

## Entry Points

Traffic enters at the /project/urls.py file. Then is directed to their respective application urls file.

For example:

A GET call to the /api/status/ endpoint will take the following route:

1. project/urls.py
2. api/urls.py
3. api/views/status.py
4. The Status class is then displayed.

## Models

Models are handled through the interaction of classes. To create a model, format a class which inherits from the Django model class. Then add the fields as variables. The framework will take care of the rest.

To get objects from a method, include the model object at the top then do any of the following:

```
# Fetch everything
Asset.objects.all()

# Filter
Asset.objects.filter(id=1234)
```
