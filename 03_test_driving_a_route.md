## Exercise One

_Work in the same project directory `hello_web_project` for the following
exercises._

Add these tests to `tests/test_app.py` and use them to test-drive the
implementation of a `POST /count_vowels` route.

```python
# File: tests/test_app.py

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'
```


## Exercise Two

Use [this Design Recipe](../resources/plain_route_recipe_template.md) to
test-drive a new route `POST /sort-names` which receives a list of names (as a
comma-separated string) and return the same list, sorted in alphabetical order.

Here's a description of the expected behaviour:

```
# Request:
POST http://localhost:5001/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe
```
<details>
  <summary>:confused: What do you mean a 'list of names', that's a string with commas in it!</summary>

  ---

  Well spotted. HTTP requests transfer everything as strings, both requests
  and responses, so cannot transmit lists or other data structures directly.
  
  Here we've used commas to represent a list of items. You'll need to take the
  string `"Joe,Alice,Zoe,Julia,Kieran"` and somehow transform it into a Python
  list. You'll also need to do the reverse to transmit it back in the response.

  In industry, there are various standardised formats to represent lists and
  dictionaries as strings. One is called JSON, which you may want to research
  if you are interested.

  ---

</details>

# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Request:
POST http://localhost:5001/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /home
#  Expected response (200 OK):
"""
This is my home page!
"""

# GET /wave?name=Leo
#  Expected response (200 OK):
"""
I am waving at Leo
"""

# GET /wave
#  Expected response (200 OK):
"""
I am waving at no one!
"""

# POST /submit
#  Parameters:
#    name: Leo
#    message: Hello world
#  Expected response (200 OK):
"""
Thanks Leo, you sent this message: "Hello world"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""

# POST /sort-names
#  Parameters: names=Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK): 
"""
Alice,Joe,Julia,Kieran,Zoe
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'


"""
POST /sort-names
  Parameters:
    names: Joe,Alice,Zoe,Julia,Kieran
  Expected response (200 OK):
  "Alice,Joe,Julia,Kieran,Zoe"
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"
```




## Challenge

This is a process feedback challenge. That means you should record yourself
doing it and submit that recording to your coach for feedback.

Use the Design Recipe to test-drive the following route:

```
# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
```

You should assert that the response status code is `200` and that the response
body is the correct string.

<details>
  <summary>:magnet: I want an extra challenge.</summary>

  ---

  For an extra challenge, add multiple names and sort them alphabetically.

  ```
  # Request:
  GET /names?add=Eddie,Leo

  # Expected response (2OO OK):
  Alice, Eddie, Julia, Karim, Leo
  ```

  ---
</details>

After you're done, submit your recording