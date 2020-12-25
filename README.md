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



