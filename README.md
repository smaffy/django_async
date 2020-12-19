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

