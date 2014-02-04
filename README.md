Python based http server that logs raw http queries and headers. Useful for testing http clients.

Listen to specified port for HTTP queries.  
When a HTTP query is received it will log the raw request line and headers.   
If the HTTP query is a POST it will log the form fields.


Example:

    curl --data "param1=value1&param2=value2" http://127.0.0.1:8000

will show:

    127.0.0.1 - - [04/Feb/2014 17:15:36] "POST / HTTP/1.1" 200 -
    HEADERS:
    --------
    User-Agent: curl/7.35.0
    Host: 127.0.0.1:8000
    Accept: */*
    Content-Length: 27
    Content-Type: application/x-www-form-urlencoded
    
    POST FIELDS:
    ------------
    param1 = value1
    param2 = value2