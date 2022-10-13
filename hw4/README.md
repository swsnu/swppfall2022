# Homework 4 - Django

**Due: 11/02 (Wed) 18:00 (This is a hard deadline)**

**ANY KIND OF CHEATING IS NOT ALLOWED FOR THE HOMEWORK. Please be aware that we run software plagiarism detection tools.**

## Django

In this assignment, you will implement a backend service for the blog frontend that you have created in homework 3.
This is an **individual** assignment.

Through this assignment, you are expected to:

- Build a RESTful API server with Django (4.1.2)
- Understand how communication between the client and the server occurs
- Test your Django application

## Environment

The grading will be conducted in a docker container so that all students' assignments run in the same environment.
Thus, you should work on your homework using `snuspl/swpp:hw4` image that we uploaded to the dockerhub. Run docker container with the following command. We will use one unified container for frontend and backend. 
```
docker run --rm -it \
    --ipc=host \
    --name "$container_name" \
    -p 0.0.0.0:8000:8000\
    -v ${PWD}:/home \
    snuspl/swpp:hw4
```
(Note that with docker, you have to run server with command `python manage.py runserver 0.0.0.0:8000`)

### Comments on files

Our `myblog` project consists of a single app, `blog`.
Because we provide the url routing and setting of the project already, you are expected to update the `blog` app mainly.

### Features

As you have seen in homework 3, our blog has three models: User, Article, and Comment.

- Each user should be able to sign up, sign in and sign out.
- Only those users who are signed in are allowed to read or write articles and comments.
- Users should be able to update or delete articles and comments only which they have created.

For the user model, you **must** use the [Django default user model](https://docs.djangoproject.com/en/4.1/topics/auth/) and the django authentication system to manage user authentication.
In homework 3, we didn't cover the real user authentication process.
Now with a proper backend, we can manage user sessions and authentication supported by Django.

For articles, you need to create a model named as `Article` that consists of following fields:

| Field name             | Type |
|------------------------|-----|
| `title`                | Char Field (max_length=64) |
| `content`              | Text Field |
| `author`               | Foreign Key |

The author must be a (foreign) key referring a User.

For comments, you need to create a model named as `Comment` that consists of following fields:

| Field name             | Type |
|------------------------|-----|
| `article`              | Foreign Key |
| `content`              | Text Field |
| `author`               | Foreign Key |

The article and author must be a (foreign) key referring an Article and a User.

To check whether you implemented your model correctly or not, please check the following code works well with your model implementation (in your test code or somewhere else).

``` python
from django.contrib.auth.models import User
from .models import Article, Comment

new_user = User.objects.create_user(username='swpp', password='iluvswpp')  # Django default user model
new_article = Article(title='I Love SWPP!', content='Believe it or not', author=new_user)
new_article.save()
new_comment = Comment(article=new_article, content='Comment!', author=new_user)
new_comment.save()
```

Detailed specifications of RESTful APIs are as following:

**IMPORTANT NOTE: Make sure you include trailing slash(`/`) at the end of each API. If you do not include, your codes will not be graded correctly.**

| API                    | GET | POST | PUT | DELETE |
|------------------------|-----|------|-----|--------|
| `/api/signup/`              | X | Create new user | X | X |
| `/api/signin/`              | X | Log in | X | X |
| `/api/signout/`             | Log out | X | X | X |
| `/api/article/`             | Get article list | Create new article | X | X |
| `/api/article/:article_id/`         | Get specified article | X | Edit specified article | Delete specified article |
| `/api/article/:article_id/comment/` | Get comments of specified article | Create comment on specified article | X | X |
| `/api/comment/:comment_id/`         | Get specified comment | X | Edit specified comment | Delete specified comment |

Note that the APIs are slightly different from that of homework 3. Since we have used simple json server backend, APIs were limited in homework 3.
In this assignment, we will implement a more RESTful API.

POST and PUT requests should contain data using the JSON format in the body of the request.
For each model, the JSON format should look like:

- User : `{username: string, password: string}`
- Article : `{title: string, content: string}`
- Comment : `{content: string}`

Also, the user information will be included in the `request` automatically. Check `request.user`.

For each API you should respond with the appropriate HTTP response code.
The list of response codes you should use is as follows:

- `200` (Ok) : Request was responded successfully.
- `201` (Created) : Request has created new resources successfully.
- `204` (No Content) : Request was responded successfully but without any content.
- `400` (Bad Request) : Failed to decode request body or failed to retrieve necessary key-value from json (`KeyError`).
- `401` (Unauthorized) : Request requires authentication. This should be returned if you are requesting without signing in.
- `403` (Forbidden) : Request is forbidden. This should be returned if your request tries to modify resources of which you are not the owner.
- `404` (Not Found) : Requested resource is not found. 
- `405` (Method not allowed) : Requested URL does not allow the method of the request.

Please make sure to implement your request methods under the following global specifications:

- For all non-allowed requests (X marked in the API table), response with `405` (and any information must not be modified).
- For all requests about article and comment without signing in, response with `401` (and any information must not be modified).
- For all requests about non-existing article and comment, response with `404` (and any information must not be modified).
- For all PUT and DELETE requests from non-author, response with `403` (and any information must not be modified). 

Among these global specifications, the prior specification has the higher priority. For example, if someone requests for a non-existing article without signing in, response with `401` instead of `404`.

Also, please make sure to implement your request methods under the following detailed specifications (in your `views.py`). When the server successfully handles a request, it responds with a JSONResponse for GET(except `/api/signout/`) and responds with a HTTPResponse for POST, PUT, and DELETE. 

**IMPORTANT NOTE: Make sure you include trailing slash(`/`) at the end of each API. If you do not include, your codes will not be graded correctly.**

- POST `/api/signup/`:
  Create a user with the information given by request JSON body and response with `201`

- POST `/api/signin/`:
  Authenticate with the information given by request JSON body. If success, log-in (the authentication info should be changed properly) and response with `204`. If fail, response with `401`.

- GET `/api/signout/`:
  If the user is authenticated, log-out (the authentication info should be changed properly) and response with `204`. If not, response with `401`.

- GET `/api/article/`:
  Response with a JSON having a list of dictionaries for each article's `title`, `content`, and `author`. The value of the `author` must be the `id` of the author but not her `username`. You don't need to include the id of each article to the response. 

- POST `/api/article/`:
  Create an article with the information given by request JSON body and response with `201`. Posted article (with it's assigned id) should be included in response's content as JSON format.

- GET `/api/article/:article_id/`:
  Response with a JSON having a dictionary for the target article's `title`, `content`, and `author`. The value of the `author` must be the `id` of the author but not her `username`. You don't need to include the id of the article to the response. 

- PUT `/api/article/:article_id/`:
  Update the target article with the information given by request JSON body and response with `200`. Updated article (with it's id) should be included in response's content as JSON format.

- DELETE `/api/article/:article_id/`:
  Delete the target article and response with `200`. When deleting an article, all comments under the target article (but not any comments under other articles, of course) **must** be deleted also.

- GET `/api/article/:article_id/comment/`:
  Response with a JSON having a list of dictionaries for each comment's `article`, `content`, and `author`. The value of the `article` and the `author` must be the `id` of the article and the author but not the `title` and her `username`. You don't need to include the id of each comment to the response. 

- POST `/api/article/:article_id/comment/`:
  Create a comment with the information given by request JSON body and response with `201`. Posted comment (with it's assigned id) should be included in response's content as JSON format.

- GET `/api/comment/:comment_id/`:
  Response with a JSON having a dictionary for the target comment's `article`, `content`, and `author`. The value of the `article` and the `author` must be the `id` of the article and the author but not the `title` and her `username`. You don't need to include the id of the comment to the response. 

- PUT `/api/comment/:comment_id/`:
  Update the target comment with the information given by request JSON body and response with `200`. Updated comment (with it's id) should be included in response's content as JSON format.

- DELETE `/api/comment/:comment_id/`:
  Delete the target comment and response with `200`. When deleting a comment, other users, articles and comments **must** not be deleted also.

### Testing

You should also write tests to verify that your blog backend is implemented correctly.
Your tests should reach **100%** of both the statement coverage and the branch coverage.

You can run tests and gather coverage data by:

- Statement coverage : `coverage run --source='./blog' manage.py test`
- Branch coverage : `coverage run --branch --source='./blog' manage.py test`

Use `coverage report -m` to report on the results. 
Use `coverage html` for a nicer presentation.

### Tips

In Django, it is rather complex to send request other than GET method with RESTful API due to the [CSRF token](https://docs.djangoproject.com/en/4.1/ref/csrf/).
To successfully handle such requests, try the following steps:

1. Before sending the request, send GET request to `/api/token/`. The response will come with an empty content and will set the cookie `csrftoken` in your browser.
2. Send the POST request with a header containing `HTTP_X_CSRFTOKEN` as the value of the `csrftoken`.

For more detail, see `test_csrf` of the `blog/test.py` file in the skeleton code.
You may change this part if you have a better way of handling the CSRF token, but disabling the protection itself is **NOT** permitted.

## Grading

This assignment is composed of a total of 80 points.
We will test your Django code under Python 3.9, and Django 4.1.2. (You can check your Django version with `pip freeze | grep Django`)

- User APIs (15 points)
- Article APIs (20 points)
- Comment APIs (20 points)
- Django Testing (25 points)

Like HW 3, if some basic features are not implemented properly, many other test cases can fail. 
For example, if the signing-in process works badly, most of the cases above will fail.
We'll try to give some partial points in this case, but it might not be enough.

## FAQs from past SWPP courses

Q1. What is the priority for the error status codes?     
A1. The priority between error status codes is 405 > 401 > 404 > 403. **However**, you do not need to worry about cases that are combinations of 400 + (405, 401, 404, 403). That is, we do not test cases in which the user sent un-decodable payload with not allowed HTTP request.

Q2. If there is an empty list of Articles or Comments, what should be the return code and value?    
A2. If your Django API server received GET request to /api/article/ and the article list is empty, then the API server should return an empty list with 200 status code. If the API server received GET request to /api/article/:article_id/comment/ and the comment list of the article_id is empty, then the server should return an empty list with 200 status code. Please note that these two cases are different from cases where the request gets sent to non-existing article. Regarding requests to non-existing resources, the API server should return 404 status code.

Q3. Any tips for how to tackle CSRF related issues?       
A3. Please refer to this [github issue](https://github.com/swsnu/swppfall2020/issues/164).

Q4. Should we also check user authentication when handling requests for article or comment?   
A4. Yes, you should. Regarding requests related to article and comments, please check user authentication and return 401 when authentication fails. 

Q5. I cannot see information contained at cookie when using POSTMAN.    
A5. Please use the POSTMAN app instead of chrome extension. 

Q6. Should we handle 400 bad request?  
A6. Handling 400 bad request is a good practice, and we've covered how to catch KeyError and JSONDecodeError during practice session. We recommend you to handle 400 for the better code quality of your DJango API server. **However**, we do not test 400 for this HW. That is, you may assume that frontend always sends well-formatted data.

## Submission

**Due: 11/02 (Wed) 18:00 (This is a hard deadline)**

We will check the snapshot of the default(e.g. main) branch of your Github repository at the deadline and grade it.
Please name your repository as `swpp-hw4-YOUR_USERNAME`, and replace YOUR_USERNAME with you own GitHub username.
Refer to HW1 to create another **private** repository. (Make sure to push your work on Github on time and add `swpp-tas` as a collaborator in your repository settings.)
Also, make sure to push your work on Github on time. 
You won't need to send us an email for submission, but we will pull each repositories at the time specified.

Please put your django projects in the root folder (not inside another `hw4` or `skeleton` folder) appropriately.
Your directory hierarchy should look like this:

``` bash
repository_root/
  README.md (this file)
  blog/
    ...
  myblog/
    ...
  manage.py
  ...
```

You can include unnecessary files(e.g. .vscode) in `.gitignore` if you want.
