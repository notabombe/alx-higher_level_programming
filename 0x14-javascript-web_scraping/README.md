# 0x14. Javascript - Web scraping

      window.dataLayer = window.dataLayer || \[\]; dataLayer.push({"userId":173838,"visitorType":"student","batch":{"id":51,"fullNameWithC":"LOS-0922 (C#10)","schoolLocation":{"id":3,"name":"Lagos"}},"curriculum":{"id":1,"name":"SE Foundations"}}); window.gtm\_user\_custom\_event = function (name, options) { if (typeof name === 'undefined') { return; } window.dataLayer.push({ customEventOptions: typeof options !== 'undefined' ? options : {}, event: name, }); } (function(w,d,s,l,i){w\[l\]=w\[l\]||\[\];w\[l\].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)\[0\], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-N4C8MF2'); Project: 0x14. JavaScript - Web scraping | Lagos Intranet          Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);  #\_copy{align-items:center;background:#4494d5;border-radius:3px;color:#fff;cursor:pointer;display:flex;font-size:13px;height:30px;justify-content:center;position:absolute;width:60px;z-index:1000}#select-tooltip,#sfModal,.modal-backdrop,div\[id^=reader-helper\]{display:none!important}.modal-open{overflow:auto!important}.\_sf\_adjust\_body{padding-right:0!important}.super\_copy\_btns\_div{position:fixed;width:154px;left:10px;top:45%;background:#e7f1ff;border:2px solid #4595d5;font-weight:600;border-radius:2px;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Helvetica Neue,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol;z-index:5000}.super\_copy\_btns\_logo{width:100%;background:#4595d5;text-align:center;font-size:12px;color:#e7f1ff;line-height:30px;height:30px}.super\_copy\_btns\_btn{display:block;width:128px;height:28px;background:#7f5711;border-radius:4px;color:#fff;font-size:12px;border:0;outline:0;margin:8px auto;font-weight:700;cursor:pointer;opacity:.9}.super\_copy\_btns\_btn:hover{opacity:.8}.super\_copy\_btns\_btn:active{opacity:1}body, div, a, p, span{ user-select: text !important; }p, h1, h2, h3, h4, h5, h6{ cursor: auto; user-select: text !important; }::selection{ background-color: #338FFF !important; color: #fff !important; }

Toggle navigation[

](https://intranet.alxswe.com/)

*   [
    
    My Planning
    
    ](https://intranet.alxswe.com/planning/me)
*   [
    
    Projects
    
    ](https://intranet.alxswe.com/projects/current)
*   [
    
    QA Reviews I can make
    
    ](https://intranet.alxswe.com/corrections/to_review)
*   [
    
    Evaluation quizzes
    
    ](https://intranet.alxswe.com/dashboards/my_current_evaluation_quizzes)

* * *

*   [
    
    Curriculums
    
    ](https://intranet.alxswe.com/dashboards/my_curriculums)
*   [
    
    Concepts
    
    ](https://intranet.alxswe.com/concepts)
*   [
    
    Conference rooms
    
    ](https://intranet.alxswe.com/dashboards/video_rooms)
*   [
    
    Servers
    
    ](https://intranet.alxswe.com/servers)
*   [
    
    Sandboxes
    
    ](https://intranet.alxswe.com/user_containers/current)
*   [
    
    Tools
    
    ](https://intranet.alxswe.com/dashboards/my_tools)
*   [
    
    Video on demand
    
    ](https://intranet.alxswe.com/dashboards/videos)

* * *

*   [
    
    Peers
    
    ](https://intranet.alxswe.com/users/peers)
*   [
    
    Captain's Logs
    
    ](https://intranet.alxswe.com/dashboards/my_captain_log)

* * *

*   [
    
    Slack
    
    ](https://alx-students.slack.com/)
    
    [
    
    My Profile
    
    ](https://intranet.alxswe.com/users/my_profile)
    

[

](https://intranet.alxswe.com/)

*   [
    
    My Planning
    
    ](https://intranet.alxswe.com/planning/me)
*   [
    
    Projects
    
    ](https://intranet.alxswe.com/projects/current)
*   [
    
    QA Reviews I can make
    
    ](https://intranet.alxswe.com/corrections/to_review)
*   [
    
    Evaluation quizzes
    
    ](https://intranet.alxswe.com/dashboards/my_current_evaluation_quizzes)

* * *

*   [
    
    Curriculums
    
    ](https://intranet.alxswe.com/dashboards/my_curriculums)
*   [
    
    Concepts
    
    ](https://intranet.alxswe.com/concepts)
*   [
    
    Conference rooms
    
    ](https://intranet.alxswe.com/dashboards/video_rooms)
*   [
    
    Servers
    
    ](https://intranet.alxswe.com/servers)
*   [
    
    Sandboxes
    
    ](https://intranet.alxswe.com/user_containers/current)
*   [
    
    Tools
    
    ](https://intranet.alxswe.com/dashboards/my_tools)
*   [
    
    Video on demand
    
    ](https://intranet.alxswe.com/dashboards/videos)

* * *

*   [
    
    Peers
    
    ](https://intranet.alxswe.com/users/peers)
*   [
    
    Captain's Logs
    
    ](https://intranet.alxswe.com/dashboards/my_captain_log)

* * *

*   [
    
    Slack
    
    ](https://alx-students.slack.com/)
    
    [
    
    My Profile
    
    ](https://intranet.alxswe.com/users/my_profile)
    

0x14. JavaScript - Web scraping
===============================

ScriptingAPIJavaScript

*   By: Guillaume, CTO at Holberton School
*   Weight: 1
*   Ongoing second chance project - started May 23, 2023 6:00 AM, must end by May 25, 2023 6:00 AM
*   An auto review will be launched at the deadline

#### In a nutshell…

*   **Auto QA review:** 0.0/67 mandatory & 0.0/20 optional
*   **Altogether:**  **0.0%**
    *   Mandatory: 0.0%
    *   Optional: 0.0%
    *   Calculation:  0.0% + (0.0% \* 0.0%)  == **0.0%**

Resources
---------

**Read or watch**:

*   [Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A "Working with JSON data")
*   [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA "The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco")
*   [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ "request module")
*   [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g "Modern JS")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/yZIL5HK-2hHAP-RJF6yInQ "explain to anyone"), **without the help of Google**:

### General

*   Why JavaScript programming is amazing
*   How to manipulate JSON data
*   How to use `request` and fetch API
*   How to read and write a file using `fs` module

### Copyright - Plagiarism

*   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
*   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
*   You are not allowed to publish any content of this project.
*   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/node`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should be `semistandard` compliant. [Rules of Standard](https://intranet.alxswe.com/rltoken/W9rASrTqkF-xXjcwomrMLw "Rules of Standard") + [semicolons on top](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg "semicolons on top"). Also as reference: [AirBnB style](https://intranet.alxswe.com/rltoken/NZR55f9vk1dZXj5q7UI5mQ "AirBnB style")
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   You are not allowed to use `var`

More Info
---------

### Install Node 10

    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    

### Install semi-standard

[Documentation](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg "Documentation")

    $ sudo npm install semistandard --global
    

### Install `request` module and use it

[Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ "Documentation")

    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules
    

**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

Tasks
-----

### 0\. Readme

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a script that reads and prints the content of a file.

*   The first argument is the file path
*   The content of the file must be read in `utf-8`
*   If an error occurred during the reading, print the error object

    guillaume@ubuntu:~/0x14$ cat cisfun
    C is super fun!
    guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
    C is super fun!
    
    guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
    { Error: ENOENT: no such file or directory, open 'doesntexist'
        at Error (native)
      errno: -2,
      code: 'ENOENT',
      syscall: 'open',
      path: 'doesntexist' }
    guillaume@ubuntu:~/0x14$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x14-javascript-web_scraping`
*   File: `0-readme.js`

Done?! Help Check your code Get a sandbox QA Review

### 1\. Write me

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a script that writes a string to a file.

*   The first argument is the file path
*   The second argument is the string to write
*   The content of the file must be written in `utf-8`
*   If an error occurred during while writing, print the error object

    guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
    guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
    Python is cool
    guillaume@ubuntu:~/0x14$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x14-javascript-web_scraping`
*   File: `1-writeme.js`

Done?! Help Check your code Get a sandbox QA Review

### 2\. Status code

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a script that display the status code of a `GET` request.

*   The first argument is the URL to request (`GET`)
*   The status code must be printed like this: `code: <status code>`
*   You must use the module `request`

    guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
    code: 200
    guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
    code: 404
    guillaume@ubuntu:~/0x14$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x14-javascript-web_scraping`
*   File: `2-statuscode.js`

Done?! Help Check your code Get a sandbox QA Review

### 3\. Star wars movie title

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

*   The first argument is the movie ID
*   You must use the [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA "Star wars API") with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
*   You must use the module `request`

    guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
    A New Hope
    guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
    Attack of the Clones
    guillaume@ubuntu:~/0x14$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x14-javascript-web_scraping`
*   File: `3-starwars_title.js`

Done?! Help Check your code Get a sandbox QA Review

### 4\. Star wars Wedge Antilles

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

*   The first argument is the API URL of the [Star wars API](https://intranet.alxswe.com/rltoken/HwLU2L7tJ4TEjzfTBc7zTA "Star wars API"): `https://swapi-api.alx-tools.com/api/films/`
*   Wedge Antilles is character ID `18` - your script **must** use this ID for filtering the result of the API
*   You must use the module `request`

    guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
    3
    guillaume@ubuntu:~/0x14$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x14-javascript-web_scraping`
*   File: `4-starwars_count.js`

Done?! Help Check your code Get a sandbox QA Review

### 5\. Loripsum

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a script that gets the contents of a webpage and stores it in a file.

*   The first argument is the URL to request
*   The second argument the file path to store the body response
*   The file must be UTF-8 encoded
*   You must use the module `request`

    guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
    guillaume@ubuntu:~/0x14$ cat loripsum
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>
    
    <p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>
    
    <p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>
    
    <p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>
    
    guillaume@ubuntu:~/0x14$ 
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x14-javascript-web_scraping`
*   File: `5-request_store.js`

Done?! Help Check your code Get a sandbox QA Review

### 6\. How many completed?

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a script that computes the number of tasks completed by user id.

*   The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
*   Only print users with completed task
*   You must use the module `request`

    guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
    { '1': 11,
      '2': 8,
      '3': 7,
      '4': 6,
      '5': 12,
      '6': 6,
      '7': 9,
      '8': 11,
      '9': 8,
      '10': 12 }
    guillaume@ubuntu:~/0x14$
    

**Repo:**

*   GitHub repository: `alx-higher_level_programming`
*   Directory: `0x14-javascript-web_scraping`
*   File: `6-completed_tasks.js`

Done?! Help Check your code Get a sandbox QA Review

Copyright © 2023 ALX, All rights reserved.

×

#### Students who are done with "0. Readme"

×

#### Correction of "0. Readme"

**Congratulations!** All tests passed successfully!  
You are ready for your next mission!

Start a new test Close

* * *

#### Result:

##### Commit used:

*   **URL:** [Click here](https://github.com/notabombe/alx-higher_level_programming/tree/38e09bc84a03508fc128f96f53c1586373ecfa4b)
*   **ID:** `38e09bc84a03508fc128f96f53c1586373ecfa4b`
*   **Author:** GitHub
*   **Subject:** _Update README.md_
*   **Date:** 2023-04-15 17:42:09 +0100

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

×

#### 0\. Readme

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Students who are done with "1. Write me"

×

#### Correction of "1. Write me"

**Congratulations!** All tests passed successfully!  
You are ready for your next mission!

Start a new test Close

* * *

#### Result:

##### Commit used:

*   **URL:** [Click here](https://github.com/notabombe/alx-higher_level_programming/tree/38e09bc84a03508fc128f96f53c1586373ecfa4b)
*   **ID:** `38e09bc84a03508fc128f96f53c1586373ecfa4b`
*   **Author:** GitHub
*   **Subject:** _Update README.md_
*   **Date:** 2023-04-15 17:42:09 +0100

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

×

#### 1\. Write me

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Students who are done with "2. Status code"

×

#### Correction of "2. Status code"

**Congratulations!** All tests passed successfully!  
You are ready for your next mission!

Start a new test Close

* * *

#### Result:

##### Commit used:

*   **URL:** [Click here](https://github.com/notabombe/alx-higher_level_programming/tree/38e09bc84a03508fc128f96f53c1586373ecfa4b)
*   **ID:** `38e09bc84a03508fc128f96f53c1586373ecfa4b`
*   **Author:** GitHub
*   **Subject:** _Update README.md_
*   **Date:** 2023-04-15 17:42:09 +0100

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

×

#### 2\. Status code

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Students who are done with "3. Star wars movie title"

×

#### Correction of "3. Star wars movie title"

**Congratulations!** All tests passed successfully!  
You are ready for your next mission!

Start a new test Close

* * *

#### Result:

##### Commit used:

*   **URL:** [Click here](https://github.com/notabombe/alx-higher_level_programming/tree/38e09bc84a03508fc128f96f53c1586373ecfa4b)
*   **ID:** `38e09bc84a03508fc128f96f53c1586373ecfa4b`
*   **Author:** GitHub
*   **Subject:** _Update README.md_
*   **Date:** 2023-04-15 17:42:09 +0100

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

×

#### 3\. Star wars movie title

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Students who are done with "4. Star wars Wedge Antilles"

×

#### Correction of "4. Star wars Wedge Antilles"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

×

#### 4\. Star wars Wedge Antilles

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Students who are done with "5. Loripsum"

×

#### Correction of "5. Loripsum"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

×

#### 5\. Loripsum

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Students who are done with "6. How many completed?"

×

#### Correction of "6. How many completed?"

Start a new test Close

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

Skipped - Previous check failed

×

#### 6\. How many completed?

##### Commit used:

*   **User:** \---
*   **URL:** Click here
*   **ID:** `---`
*   **Author:** \---
*   **Subject:** _\---_
*   **Date:** \---

×

#### Recommended Sandbox

Running only

### 1 image(0/2 Sandboxes spawned)

### Ubuntu 14.04 - NodeJS 10

Ubuntu 14.04 with NodeJS 10

Run

×

#### Markdown Guide

#### Emphasis

\*\***bold**\*\*
\*_italics_\*
~~strikethrough~~

#### Headers

\# Big header
## Medium header
### Small header
#### Tiny header

#### Lists

\* Generic list item
\* Generic list item
\* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item

#### Links

\[Text to display\](http://www.example.com)

#### Quotes

\> This is a quote.
> It can span multiple lines!

#### Images

CSS style available: `width, height, opacity`

!\[\](http://www.example.com/image.jpg)
!\[\](http://www.example.com/image.jpg | width: 200px)
!\[\](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)

#### Tables

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

_Or without aligning the columns..._

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |

#### Displaying code

\`var example = "hello!";\`

_Or spanning multiple lines..._

\`\`\`
var example = "hello!";
alert(example);
\`\`\`

This project involved practicing file I/O on Node.js and using the NPM request
framework to interact with the [Star Wars](https://swapi.co/),
[JSONplaceholder](https://jsonplaceholder.typicode.com), and
[Twitter](https://developer.twitter.com/en/docs/api-reference-index) API's.

## Tasks :page_with_curl:

* **0. Readme**
  * [0-readme.js](./0-readme.js): JavaScript script that reads and prints the
  contents of a file.
  * Usage: `./0-readme.js <file path>`.

* **1. Write me**
  * [1-writeme.js](./1-writeme.js): JavaScript script that writes a string to a
  file.
  * Usage: `./1-writeme.js <file path> <string to write>`.

* **2. Status code**
  * [2-statuscode.js](./2-statuscode.js): JavaScript script that displays the
  stauts code of a `GET` request using the `request` framework.
  * Usage: `./2-statuscode.js <URL to GET>`.
  * Output: `code: <status code>`.

* **3. Star wars movie title**
  * [3-starwars_title.js](./3-starwars_title.js): JavaScript script that uses the
  Star Wars API to print the title of the Star Wars movie with a given integer episode
  number.
  * Usage: `./3-starwars_title.js <3-starwars_title.js>`.

* **4. Star wars Wedge Antilles**
  * [4-starwars_count.js](./4-starwars_count.js): JavaScript script that uses the
  Star Wars API to print the number of movies featuring the character "Wedge Antilles".
  * Usage: `./4-starwars_count.js http://swapi.co/api/films/`.

* **5. Loripsum**
  * [5-request_store.js](./5-request_store.js): JavaScript script that stores the
  contents of a webpage in a file.
  * Usage: `./5-request_store.js <URL to get> <file path to store content in>`.

* **6. How many completed?**
  * [6-completed_tasks.js](./6-completed_tasks.js): JavaScript script that uses the
  JSONPlaceholder API to compute the number of tasks completed per user ID.
  * Usage: `./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos`.

* **7. Who was playing in this movie?**
  * [100-starwars_characters.js](./100-starwars_characters.js): JavaScript script
  that uses the Star Wars API to print all characters featured in a given movie.
  * Usage: `./100-starwars_characters.js <movie ID>`.

* **8. Right order**
  * [101-starwars_characters.js](./101-starwars_characters.js): JavaScript script
  that uses the Star Wars API to print all characters featured in a given movie in
  the same order as they are listed in the `characters` list of the `/films/` response.
  * Usage: `./101-starwars_characters.js <movie ID>`.

* **9. Twitter Auth**
  * [102-search_twitter.js](./102-search_twitter.js): JavaScript script that sends
  a search request to the Twitter API with a given search string.
  * Usage: `./102-search_twitter.js <consumer  key> <consumer secret> <search string>.
  * Outputs 5 results in the format `[<Tweet ID>] <Tweet text> by <Tweet owner name>`.
