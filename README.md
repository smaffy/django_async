Async Views in Django 3.1

******************
Dependencies

    Python >= 3.8
    Django >= 3.1
    Uvicorn
    HTTPX
***************************

        pip install uvicorn
        pip install httpx

Run project:

        (env)$ uvicorn django_async.asgi:application --reload

************************
the HTTP response is sent back before the first sleep call
    
    http://localhost:8000/async/

the HTTP response is sent after the loop and the request to https://httpbin.org/ completes

    http://localhost:8000/sync/
***************************

Smoking Some Meats 

run multiple operations asynchronously, aggregate the results, and return them back to the caller

    1. http://localhost:8000/smoke_some_meats/
    2. http://localhost:8000/smoke_some_meats2/
       http://localhost:8000/smoke_some_meats2/?to_smoke=ice%20cream,%20bananas,%20cheese&flavor=Gold%20Bond%20Medicated%20Powder

********************

Burnt Meats (Sync Call)

just create sync func and call in async
result = only sync

    http://localhost:8000/burn_some_meats

********************

Sync to Async
synchronous call inside an async view (like to interact with the database via the Django ORM, for example), 
use sync_to_async either as a wrapper or a decorator

*******************

Celery and Async Views

Could use an async view to send an email or make a one-off database modification, but have Celery clean out your 
database at a scheduled time every night or generate and send customer reports

**********************

In production, be sure to use Gunicorn to manage 
Uvicorn in order to take advantage of both concurrency (via Uvicorn) and parallelism (via Gunicorn workers):

    gunicorn -w 3 -k uvicorn.workers.UvicornWorker hello_async.asgi:application

********************
    https://wersdoerfer.de/blogs/ephes_blog/django-31-async/