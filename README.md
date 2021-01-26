# shopNsing Backend

To run the application manually:<br>
```
1. Create virtual environment
    - virtualenv venv
2. Activate
    On Mac:
        - source venv/bin/activate
    On Windows:
        - venv\Scripts\activate
3. Install dependencies
    - pip install -r requirements.txt
4.Run development server
    - python manage.py runserver
    
<b>Endpoints </b><br>
POST API to validate a slot with a finite set of values.
 1. category?category={}
 Requires the category for which tracks will be returned
