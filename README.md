# TAMS Backend

## Installation

1. Install the Google App Engine SDK for Python. This should come with the GoogleAppEngineLauncher application
2. Open the launcher. Click file and add an existing project.
3. Navigate to the project directory and select it
4. Now just press the play button. This will run a local deployment on your system. 
5. To deploy, ensure that you have access to deploy and click deploy.

## Methodology - Why are things the way they are?

### Language

Python/Django - Because all projects follow a similar structure which makes it easier for someone else to come in and continue maintaining it.
- Follows MVC
- Easily build out new features
- Also because PHP just sucks

### Hosting

- CSUS does not offer hosting for sites other than PHP.
- Google App Engine offers free hosting that is scalable, reliable and easy to deploy.

**Email me at**: danielmj@me.com to gain access

### Database

To make Google App Engine completely free, a nosql database is used. To enable a nosql on Django, a highly integrated framework was used: Djangae. 