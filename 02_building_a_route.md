## Exercise

Work through the following in `app.py` in your `hello_web_project` project.

Create a new route that responds to requests sent with:
  * A method `POST`
  * A path `/submit`
  * Body parameters `name` and `message`

Here's the expected behaviour of this route:

```
# Request:
POST /submit

# With body parameters:
name=Leo
message=Hello world

# Expected response (2OO OK):
Thanks Leo, you sent this message: "Hello world"
```

Make sure your server is running — then, using `curl` and Postman, check the
route is working.



## Challenge

Work through the following in `app.py` your `hello_web_project` project.

Create a new route that responds to requests sent with:
  * A method `GET`
  * A path `/wave`
  * A query parameter `name`

It should return the text `'I am waving at [NAME]'`, where `[NAME]` is replaced
by the value of the `name` _query parameter_.

```
# Request:
GET /wave?name=Leo

# Expected response (200 OK):
I am waving at Leo
```

Make sure your server is running — then, using `curl` and Postman, check the
route is working.