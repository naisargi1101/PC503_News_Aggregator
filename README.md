# PC503-NewsAggregator with Video Chat

This project contains 2 parts.

1. News Aggregator with beautiful soup and request module.
2. Video chat with the Agora module.

## 1. News Aggregator with beautiful soup and request module.

### (a) Install required library.

```
pip install bs4
pip install requests
pip install django
```

### (b) Build the Django project

```
django-admin startproject PC503_News_Aggregator
```

Now we will create the news app for our implementation of scrapping.

```
python manage.py startapp news_home
```

Now, we'll add this news app to settings.py file in INSTALLED_APPS. So that, Django takes this app into consideration.

### (c) Implementation of the web application

Now see the files urls.py, views.py and index.html for implementation.

### (d) Run the server

```
python manage.py runserver
```

This Command shows the output as follows. It may suggest you the command for migration. If it shows the migration command copy and run that command and then again run the above command to make the application work.

```
System check identified no issues (0 silenced).
November 12, 2022 - 12:01:44
Django version 4.1.3, using settings 'PC503_News_Aggregator.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Output
![news aggregator output](D:\PC503_News_Aggregator\output_images\news_aggregator_output.PNG)