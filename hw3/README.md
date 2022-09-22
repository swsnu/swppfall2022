# Homework 3 - React Library & Testing

#### **Due (These are hard deadlines)**
- ##### **Feature Implementation Due: 10/6 (Thu) 18:00**
- ##### **Testing Implementation Due: 10/13 (Thu) 18:00**

**ANY KIND OF CHEATING IS NOT ALLOWED FOR THE HOMEWORK. Please be aware that we run software plagiarism detection tools.**

You will implement a front-end for a blogging service using React library. This is an **individual** assignment.
This assignment will help you

- Make a simple React (version 18.2.0) application before diving into your projects
- Make test suites for the React application you implement
- Let you try out stuff we have learned in our practice sessions

## Features

Our blog will support three models: User, Articles, and Comments.
You are required to create a total of five pages as shown in the below storyboard, meeting the following requirements:

<p align="center"><img src="https://user-images.githubusercontent.com/17061663/93694736-6a6e8100-fb4a-11ea-88c3-063d817b22c5.png" width="700" alt="live server extension"></img></p>

- Log In page (`/login`)
  - You must have the following fields:
    
    | JSX Tag type | id |
    |---------------|--|
    | input | email-input |
    | input | pw-input |
    | button | login-button |

  - Users should be able to log-in by filling up the email and password inputs and hitting the log-in button.
  - As we don't have a proper backend, we don't do real, security-aware authentication yet, but users should only be able to log-in with an account with an email of 'swpp@snu.ac.kr' and password of 'iluvswpp'.
  - When a user tries to log-in with invalid inputs, the frontend should emit `Email or password is wrong` message through `alert` command (in Javascript).
  - After logging-in, users should find themselves at the article list page. (`/articles`) That is, when the user tries to go login page after logged in, the page should be redirected to article list page.
  - This is the only page that unauthorized users will have access to. Unauthorized users trying to access any other pages should be redirected to this page!     
- Article list page (`/articles`)
  - Users should be able to clearly make out the **whole** list of articles including article id, (full) article title, and author name in this page.
  - Also, user must be able to go to article create page (`/articles/create`) by hitting:
  
    | JSX Tag type | id |
    |-------------|--|
    | button | create-article-button |

  - Upon clicking on the article title, users should be able to access the article's detail page (`/articles/:id`). These article titles must be `button` but not `link`.
- Article write(create) page (`/articles/create`)
  - You must have the following fields in Write tab:
    
    | JSX Tag type | id |
    |-------------|--|
    | input or textarea | article-title-input |
    | input or textarea | article-content-input |
    | button | back-create-article-button |
    | button | confirm-create-article-button |
    | button | preview-tab-button |
    | button | write-tab-button |

  - Also, you must have the following fields in Preview tab:
  
    | JSX Tag type | id |
    |-------------|--|
    | any plain text (like h1, h3, p, …) | article-author |
    | any plain text (like h1, h3, p, …) | article-title |
    | any plain text (like h1, h3, p, …) | article-content |
    | button | back-create-article-button |
    | button | confirm-create-article-button |
    | button | preview-tab-button |
    | button | write-tab-button |
    
  - When users fill up the title and contents under Write tab and hit the confirm button (either in Preview tab or Write tab), a new article having the given title and contents should be posted.
  - The created article, of course, should be tagged with your own author id.
  - After creating the article, the user should be redirected to the created article's detail page (`/articles/:id`)
  - While creating the article, the user should be able to preview the contents (under the Preview tab by hitting `preview-tab-button`), in the way that it will be shown in the details page. The user should stay in `/articles/create` page while seeing the preview.
  - After checking the preview, the user should be able to resume writing (under the Write tab by hitting `write-tab-button`). The user should stay in `/articles/create` page after hitting the `write-tab-button`.
  - If the title or content input are empty, the confirm button should be disabled.
  - The back button will go back to the article list page (`/articles`) (also without any alert).
- Article detail page (`/articles/:id`)
  - You must have the following fields:
  
    | JSX Tag type | id |
    |-------------|--|
    | any plain text (like h1, h3, p, …) | article-author |
    | any plain text (like h1, h3, p, …) | article-title |
    | any plain text (like h1, h3, p, …) | article-content  |
    | input or textarea | new-comment-content-input |
    | button | confirm-create-comment-button |
    | button | edit-comment-button |
    | button | delete-comment-button |
    | button | edit-article-button |
    | button | delete-article-button |
    | button | back-detail-article-button |

  - Users should be able to clearly make out the title, contents, and author name of the article.
  - Also, users should be able to see the whole comments for the corresponding article including the author name and contents of each comments.
  - Simple comments functionalities (Create for everyone / Edit & Delete for the comment author through the buttons) should work.
    - When a user hits the `confirm-create-comment-button`, a new comment with the contents provided through `new-comment-content-input` and the author's name should be added to this detail page (without any alert). However, `confirm-create-comment-button` should be disabled when the `new-comment-content-input` is empty.
    - When a user hits the `edit-comment-button`, a `prompt` taking some string input should be popped up (by using Javascript `prompt` command) and initial value of the prompt should be same as current comment's content 
      - When the user fill the prompt input with new contents and confirm the pop-up, the contents of the comment should be updated with the new contents.
      - When the user confirm the pop-up with empty content, the contents should not be modified (consistent to `user cannot create empty comment`)
      - When the user canceled the pop-up, the contents should not be modified.
    - When a user hits the `delete-comment-button`, the comment should be deleted without any alert.
    - The edit and delete button for each comment must be visible for the author only.
  - Edit & Delete button for the article should work.
    - These buttons must be visible for the author only.
    - When a user hit the `edit-article-button`, the user should be redirected to the edit page (`articles/:id/edit`)
    - When a user hit the `delete-article-button`, the user should be redirected to the article list page (`articles/`) and the article should be deleted without any alert.
  - When a user hits `back-detail-article-button` button, the user should be redirected to the article list page.
- Article edit page (`/articles/:id/edit`)
  - You must have the following fields in Write tab:
  
    | JSX Tag type | id |
    |-------------|--|
    | input or textarea | article-title-input |
    | input or textarea | article-content-input |
    | button | back-edit-article-button |
    | button | confirm-edit-article-button |
    | button | preview-tab-button |
    | button | write-tab-button |

  - Also, you must have the following fields in Preview tab:
    
    | JSX Tag type | id |
    |-------------|--|
    | any plain text (like h1, h3, p, …) | article-author |
    | any plain text (like h1, h3, p, …) | article-title |
    | any plain text (like h1, h3, p, …) | article-content |
    | button | back-edit-article-button |
    | button | confirm-edit-article-button |
    | button | preview-tab-button |
    | button | write-tab-button |
    
  - Users should see similar stuffs with article create page: Write tab and Preview tab. All requirements for the plain texts and tab buttons are identical to the create page (except the url).
    - However, the `article-title-input` should contains current article's title and `article-content-input` should contains current article's content
  - When a user hits `confirm-edit-article-button`, the user should be redirected to the article detail page (`articles/:id`) and the edited title and contents should be saved. Any comment for the article should not be modified or deleted by this process.
  - When a user hits `back-edit-article-button`, the following features should be supported:
    - If the title and contents have not been modified yet but are the same as the title and contents before editing, just go back to the detail page without any alert.
    - If the title or contents has been modified modified, you should make a confirmation pop-up (through Javascript `confirm` command) with message `Are you sure? The change will be lost.`
      - If the user accept the confirmation, the user should be redirected to the detail page and the title and contents of the article should not be modified.
      - If the user dismiss the confirmation, the user should just stay on the edit page and be able to resume editing.
  - If the title or content input are empty, the confirm button should be disabled (consistent to `/create`).
- Common things for **all pages**:
  - If the user is logged-in, the user should be able to log-out from any of the pages by clicking `logout-button`. Upon logging-out, the user should end on the initial Log In page (shown as dotted lines on the storyboard).
  - The `logout-button` should not be displayed before the login. 

    
    | JSX Tag type | id |
    |---------------|--|
    | button | logout-button |

  - Each user should be able to update or delete articles and comments only which they have created.
  - **All pages/components should have proper unit tests to test its functionalities, using Jest and React Testing Library that are covered in the practice session. Your tests are expected to cover all of your code, and we will give credits according to your coverage results. You can see the coverage information of your application by using `npm test -- --coverage`. Also, all of your tests must pass.**

We provide a simple [json-server](https://github.com/typicode/json-server) backend with our skeleton code (`skeleton/api`).
Due to its simplicity, we do not go over too much into authentication and security for now, but later on (with HW4 and your project), it should be considered.

**NOTE: For Windows users**

To run the mocked json server in Windows environment, please change the following line in `skeleton/package.json`.

From:
``` json
"backend": "cp api/db.json api/_db.json && json-server --watch api/_db.json --routes api/routes.json --port 8000"
```
To:
``` json
"backend": "copy /y api￦￦db.json api￦￦_db.json && json-server --watch api￦￦_db.json --routes api￦￦routes.json --port 8000"
```

To run the server, just type following command at the root of the project
```
$ yarn install (only for the first time)
$ yarn run backend (or npm run backend)
```

You should be able to implement your redux action creators by sending appropriate http requests to the following URLs:

| API                    | GET | POST | PUT | DELETE |
|------------------------|-----|------|-----|--------|
| `api/user`        | Get user list | X | X | X |
| `api/user/1`      | Get user information containing whether or not the user is logged_in | X | Update user's `logged_in` value to log-in/log-out | X |
| `api/articles`             | Get article list | Create new article | X | X |
| `api/articles/:id`         | Get specified article | X | Edit specified article | Delete specified article |
| `api/comments`        | Get comments | Create new comment | X | X |
| `api/comments/:id`         | Get specified comment | X | Edit specified comment | Delete specified comment |

Articles should have an `id` (number), `author_id` (number), `title` (string), and `content` (string).

Comments should have an `id` (number), `author_id` (number), `article_id` (number), and `content` (string).

Users should have an `id` (number), `email` (string), `password` (string), `name` (string), and `logged_in` (boolean).

Each field names are as specified above. You should be able to implement the pages required with these APIs.

## Comments on files

Files that are created inside the `skeleton` (root) and `src` folder have been already discussed during the practice session (contents in [this link](https://github.com/facebook/create-react-app)). As we have done so in our practice sessions, you are expected to add proper components, containers, redux-store (actions, reducers) under the `src/` directory freely, according to your needs. Nicely refactored code will result in better readability and is recommended. 

The `skeleton/api` directory is added to provide simple backend for you to test out your application, and serves as specified above. **Please do not modify this directory.** You are expected to create `store` that manages redux-store by communicating using HTTP, and `containers` and `components` that produce each pages' requirements. The existing `App.tsx` is expected to be the root component of the entire application.

Also, please do not make any un-requested alerts. It will largely harm the e2e test result.

We will test your code after conducting `yarn install`, so you can import other libraries through `package.json`. However, you should not change the version of already imported dependencies.

## Tips

- Most of things have been covered in the tutorial during the lab session. Please look carefully through the slides and the tips provided.
- It might be useful and more pleasing to the eyes by using a CSS framework like [Bootstrap-React](https://react-bootstrap.github.io/) and [SemanticUI-React](https://react.semantic-ui.com/). However, this is **optional**, please proceed on your own willings. You might be needing them for your projects ahead, so it would be nice to have some head start.

## Grading

This assignment is composed of a total of 80 points. We will score your feature implementation (**lastest commit before 7 October 6:00 PM**) with our e2e test code, having 55 test cases that reflects the requirements given above. You will get 1 point for each passed test case. Also, we will check your unit test coverage (**latest commit before 14 October 6:00 PM**), which is 25 points in total. Grading details are shown below.

### Feature Implementation Score
The e2e test consist of cases about:
- Log in page features (4 points)
- Article list page features (5 points)
- Article create page features (10 points)
- Article detail page features when the user is the author of the article (14 points)
- Article detail page features when the user is not the author of the article (13 points)
- Article edit page features (9 points)

### Unit Test Score
Your unit test score will be given based on both test coverage and completeness of your feature implementation.

This is to make sure that your test code is faithful to the feature requirements.

To be more precise, your unit test score will be given as follows:  
(*score<sub>feature</sub>* denotes your feature implementation score)

| <center>Coverage</center> | <center>Points</center> |
| :-----------------------: | :---------------------: |
|       90% and above       | <center>25 * (*score<sub>feature</sub>* / 55)</center>   |
|       80% and above       | <center>20 * (*score<sub>feature</sub>* / 55)</center>   |
|       70% and above       | <center>15 * (*score<sub>feature</sub>* / 55) </center>   |
|       60% and above       | <center>10 * (*score<sub>feature</sub>* / 55) </center>   |
|         below 60%         | <center>0 </center>   |

*Note: All your test cases must pass*



Since we will automatically score your homework, **please make sure that you follow the features specification (especially, the Tag type and id of JSX fields)**.

Also, if some basic features are not implemented properly, many other test cases can fail. For example, if the logging-in process works badly, most of the cases above will fail.
We'll try to give some partial points in this case, but it might not be enough.

It's a good idea to start with the log-in page, and then implement routing features, article list pages, and other features in order.

Finally, since you have to implement many features, start early!

### Grading Environment

The grading will be conducted in a docker container so that all students' assignments run in the same environment.
Please follow [the manual](How_to_deploy_homework_in_docker.pdf) to ensure your codes execute in the grading environment before you submit.

## Submission

**Due: (These are hard deadlines)**
- **Feature Implementation Due: 10/7 (Thu) 18:00**
- **Testing Implementation Due: 10/14 (Thu) 18:00**

We will check the snapshot of the *main* branch of your Github repository at the deadline and grade it.

Please name your repository as `swpp-hw3-YOUR_USERNAME`, and replace YOUR_USERNAME with your own GitHub username. Please note that USERNAME is case-sensitive.
Refer to HW1 to create another private repository.

Also, make sure to add TA(`swpp-tas`) as your collaborator in the repository settings. 

We automatize the grading process, so your homework may not be graded properly if your directory hierarchy doesn't look like this:

```
repository_root/
  api/
  public/
  src/
    App.tsx
    App.test.tsx
    index.tsx
    ...
  package.json
  ...
```
Also, please include proper `.gitignore` file so redundant items are not be pushed to your repository (like `node_modules`).
You can use skeleton code's `.gitignore` file.

Also, make sure to push your work on Github on time. You won't need to send us an email for submission, but we will pull each repositories at the time specified.
