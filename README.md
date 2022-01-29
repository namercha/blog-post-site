## Demonstrating jinja
This small program is to demonstrate the usage of Flask and the jinja templating language. 
The user can enter their name in the url and the site will return their predicted age and gender. 
Age and gender predictions are derived using the [Agify](https://agify.io/) and [Genderize](https://genderize.io/) APIs.

Example:
```
http://127.0.0.1:5000/guess/nabil
```
will return a predicted age and gender of the name `nabil`. 