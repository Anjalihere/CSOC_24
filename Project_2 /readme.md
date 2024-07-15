# Web of Vulnerabilities


I made this website with full of vulnerabilities and crafted it in the form of a storyline or game such that exploiting one vulnerability will lead to another one and so on.  
I have given hints for next level in order to make it a little easier and fun although real-world challenge don't involve such hints.

## Getting Started
Running `app.py` will get us to this page which is explaining the storyline. The story is about Healer - a skilled night messenger who is framed for the murder of `Park Deong-cheol`. Being on the run, he needs to collect evidence which is the `fingerprint` of murderer in order to prove his innocence. Our challenge is to help him get the real culprit.

<img width="981" alt="Screenshot 2024-07-15 at 4 06 34 PM" src="https://github.com/user-attachments/assets/92b4a036-0dbb-43e6-a5cf-71de9fe416ef">

The image on the webpage tells that this image contain some information about next step. Let's click on the image...Ta-da! we have our next page.

<img width="796" alt="Screenshot 2024-07-15 at 4 07 13 PM" src="https://github.com/user-attachments/assets/f7d8f0b1-393d-49a5-b507-63f09157a87f">


## Path Traversal:

The first vulnerability I introduced is of ` Path Traversal` . There is a hint in title  **Hidden in `Cascades`** which is directly pointing to some `css` file. And inspecting through source code…there is a `secrets.css` file which contain the path to `login` page. 

<img width="894" alt="Screenshot 2024-07-15 at 4 07 55 PM" src="https://github.com/user-attachments/assets/7d8ecf04-1661-4f55-adb5-a7f65b7a818a">



<img width="358" alt="Screenshot 2024-07-15 at 4 08 39 PM" src="https://github.com/user-attachments/assets/546b0c59-3045-4636-aa67-14c75631fa48">



<img width="623" alt="Screenshot 2024-07-15 at 4 08 13 PM" src="https://github.com/user-attachments/assets/3ef46aa0-626a-4423-9bcb-bd42e5cc15c6">


## Authentication Bypass:

Getting to the login page, some  `message` is displayed. We are asked `email`, `username` and `password` which is pointing towards some vulnerability related to `Authentication Bypass`. Observing carefully, we can see some `morse code` (a hint). Decode it and it says there is a `logical flaw` and `emails are checked only` . 

<img width="690" alt="Screenshot 2024-07-15 at 9 35 11 PM" src="https://github.com/user-attachments/assets/fb602712-8909-4758-aba9-cc6753b85f10">


<img width="740" alt="Screenshot 2024-07-15 at 4 42 04 PM" src="https://github.com/user-attachments/assets/774f80a3-0ff5-4483-ba27-43b21facaa30">



Since admin access is needed in such cases. Let's put `admin@moebius.com`...Oh no! this isn't the one. Remember the message says **the CEO of company is called `b0ss`**. So, we need `b0ss` access. Just put email as `b0ss@moebius.com` and username or password can be anything. There you go!


<img width="358" alt="Screenshot 2024-07-15 at 4 10 03 PM" src="https://github.com/user-attachments/assets/ecacfd34-ca4f-4ce4-b34f-9b2c171579ca">


We get a database of criminals and their crimes. The search bar says `Search by crimes..`. Since we are looking for a `murder` case…let's put that.


<img width="1242" alt="Screenshot 2024-07-15 at 9 36 33 PM" src="https://github.com/user-attachments/assets/42056359-dbeb-4c7a-ba55-d69e0e62f5e4">


Bingo! You get the culprit details but we also needed `fingerprint` of the culprit. Click on ` View Fingerprint` and another one.


<img width="1280" alt="Screenshot 2024-07-15 at 4 10 51 PM" src="https://github.com/user-attachments/assets/5506561c-c300-4375-8dd1-d08734d045a4">

## Cookies:

<img width="560" alt="Screenshot 2024-07-15 at 4 11 14 PM" src="https://github.com/user-attachments/assets/b6130ce5-c079-4ea5-80c5-bac07c55075c">

This is a `Cookies Manupulation` challenge. The hints on the webpage clearly points towards `cookies`. 
Checking cookies, it contained the name `b0ss` and key is some weird string. 

<img width="504" alt="Screenshot 2024-07-15 at 4 12 41 PM" src="https://github.com/user-attachments/assets/786d07ce-5c48-4dcb-b87a-c9551cb256ca">

But the next hint said `favourite number - not 64` which means `not base-64 encoding`. It can easily be checked on [CyberChef](https://gchq.github.io/CyberChef/) that it's a `base 62` and it says `admin`.


<img width="500" alt="Screenshot 2024-07-15 at 4 43 29 PM" src="https://github.com/user-attachments/assets/c88edf6a-076d-4f56-8503-b72c16d6b4b8">

But isn't the `b0ss` our admin so, take base-62 encoded string of b0ss and put it in the value of cookie and refresh.

<img width="500" alt="Screenshot 2024-07-15 at 4 43 51 PM" src="https://github.com/user-attachments/assets/fdd4f729-0e5f-4711-9124-aa7022fbc384">

<img width="504" alt="Screenshot 2024-07-15 at 4 11 51 PM" src="https://github.com/user-attachments/assets/f46729bc-870e-4323-95a5-90d79b22b4ef">



Eureka!!! We have got the most confidential information - the `fingerprint of culprit`.

<img width="917" alt="Screenshot 2024-07-15 at 4 12 59 PM" src="https://github.com/user-attachments/assets/a9036efb-b05e-4eac-85a7-3e377ed1c7ca">

Okay then! THIS WAS IT :)
