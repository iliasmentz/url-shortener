Shorty
======================

Shorty is an application that receives your long, ugly urls and ask its provider to make it smaller and prettier.

## What Providers are? 

Providers are external services that specialize in url shortening. When you ask Shorty to shorten your url, Shorty sends a request to one of those providers in order to shorten. 

You can either choose which provider Shorty should use or let Shorty pick one for you.

  
## Cool, how to run it? 😎

You can run it locally either with `python with virtualenv` or with `docker`

### To run it with `virtualenv` :

#### Requirements: `virtualenv`, `python3`, `pip3`

```bash
$ ./run_with_virtual_env.sh
```

### To run it with `docker` :

#### Requirements: `docker` obviously 😅

```bash
# build docker image
$ docker built -t shorty:latest .

# run the docker image
$ docker run -p <the-port-you-want>:5000 shorty
```

## Okay, I did it! 🎉 Now, do I use it? 

Great job! Now you just need to send to Shorty some requests to execute. 
The request should look like the above

```json
{
  "url": "the url you want to shorten",
  "provider": "the provider that will shorten the url (optional)"
}
```

If you send a valid request the response would look something like this:

```json
{
  "data": {
    "url": "https://example.com",
    "link": "https://bit.ly/8h1bka",
  }
}
```

If you make any invalid request, Shorty will try his best to let you know what needs to be done.
The error format looks like this:

```json
{
  "error": {
    "status": "http status code",
    "code": "application specific error code",
    "detail": "detail message for the error"
  }
}
```

## How do I know if Shorty works?

Just run the tests 😅
To run the test just execute:
```bash
$ py.test
```

## How was Shorty build? 👷‍

Shorty's architecture is based on Robert's C. Martin Clean Architecture.

The `/postlink` executes the `ShortenUseCase` with the given request.
In the execution, the use case checks if the request is valid and if it is, 
it just retrieves the provider from the provider factory and the provider does 
the shortening. 

If any errors arise during the shorten use case, the appropriate
shorty exception will be raised and returned.
 

Resources
---------

1. `Flask`: http://flask.pocoo.org/
2. `pytest`: http://pytest.org/latest/
3. `virtualenvwrapper`: https://virtualenvwrapper.readthedocs.io/en/latest/
4. `HTTP statuses`: https://httpstatuses.com/

