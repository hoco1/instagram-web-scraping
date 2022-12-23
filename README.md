# Instagram Web Scraping
In this repository, with the **Request library**, I logged in to the Instagram account, got **login cookies**, and stored them in the **MongoDB** database.  
I combined this small task on **Fast API** with some features such as **Sign up** and **logging**.   
Also, clients **without authentication** can not use the **"cookies/add_cookie_cookies_post"** page, which page clients give "instagramID" and "instagramPass" for getting Instagram logging cookies.  

However, in some cases, when I want to log in by the Request library, scripts cannot go forward because Instagram gets **suspicious** and wants to send the verifying code.   
To solve that, I want to use **Selenium** instead of Request.
