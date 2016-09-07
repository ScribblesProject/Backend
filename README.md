# TAMS Backend

Welcome to the TAMS backend project. 


## Installation

Please see [Installation Instructions](./docs/install.md)

## Other Documentation

- [Django Quick Start Guide](./docs/django.md)
- [Project Structure & Design](./docs/design.md)

## Methodology - Why things are the way they are?

### Language

Python/Django - All Django projects follow a similar structure which makes it easier for someone else to come in and continuously maintain it. 

Django pros:
- Follows MVC pattern
- Easily build out new features
- Easy to locate areas to maintain
- PHP sucks

Django cons:
- There is an initial learning curve
- Python is technically slower in compute time. But for this project thats negligable and is not really a factor.

Sites built in Django:
- Pinterest
- Instagram
- Bitbucket
- Mozilla Support
- Nasa
- Washington Post
- The Onion
- Disqus
- Many more...

For those with rails experience, the learning curve will likely be less.

#### Why does PHP Suck?

PHP sucks because:
- No formal structure for websites. Not MVC unless MVC is programmed in by the developer. This hinders maintainability.
- Object oriented design is an after thought. This does not lend well to MVC
- Because PHP can be, and often is, embedded directly into HTML it makes it more difficult to figure out whats going on.
- Ancient. This language was cool over 10 years ago, but now is primarily used by legacy code. 

For a better, more complete reason why PHP sucks: [READ THIS ANSWER](http://programmers.stackexchange.com/questions/263389/why-is-php-so-hated)

### Hosting

- CSUS does not offer hosting for sites other than PHP (PHP sucks)
- [Google App Engine](https://cloud.google.com/appengine/) offers free hosting that is scalable, reliable and easy to use. Its what manny sites such as Khan Academy are using. 
    - Emphasis on easy to use. 

**Email me at**: danielmj@me.com to gain access

### Database

To make Google App Engine completely free, a NoSQL database is used. To enable a nosql on Django, a highly integrated framework was utilized called [Djangae](http://djangae.org).

This framework maintains the notion of a relational database. But implements it in NoSQL behind the scenes. Nothing really changes from how you use Django. There just may be some added middleware and applications to support this kind of use case. 

NoSQL Pros:
- More scalable
- Easier to maintain

NoSQL Cons:
- Tables require indexing prior to fetching.



