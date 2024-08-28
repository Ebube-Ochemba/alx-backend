# 0x02-i18n

> This project was on Internationalization and Localization **[i18n]**

## Summary

I learnt about how to parametrize Flask templates to display different languages, how to infer the correct locale based on URL parameters, user settings or request headers, and how to localize timestamps.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/0-app.py): Setup a basic Flask app.
    - [templates/0-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/0-index.html): A simple template to be rendered.
- [x] [1-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/1-app.py): Create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`. 
    - [templates/1-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/1-index.html): A simple template to be rendered.
- [x] [2-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/2-app.py): Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.
    - [templates/2-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/2-index.html): A simple template to be rendered.
- [x] [3-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/3-app.py): Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.
    - [templates/3-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/3-index.html): A simple template to be rendered.
- [x] [4-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/4-app.py): Implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.
    - [templates/4-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/4-index.html): A simple template to be rendered.
- [x] [5-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/5-app.py): Creating a user login system is outside the scope of this project.
    - [templates/5-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/5-index.html): A simple template to be rendered.
- [ ] [6-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/6-app.py):
    - [templates/6-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/6-index.html): A simple template to be rendered.
- [ ] [7-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/7-app.py):
    - [templates/7-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/7-index.html): A simple template to be rendered.
- [ ] [-app.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/-app.py):
    - [templates/-index.html](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x02-i18n/templates/-index.html): A simple template to be rendered.


> [templates](./templates): A folder of html templates files to illustrate tasks.
