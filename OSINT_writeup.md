# Challenge #2
## Try Hack Me | Sakura Room
### INTRODUCTION
Just type in "Let's Go!" 
### TIP-OFF
> What username does the attacker go by?
> 
> SakuraSnowAngelAiko

Reading the instructions, it said to analyse the image well and that image contain a lot of information. So, I converted the ` binary ` of image into ` ASCII ` and got this ` A picture is worth 1000 words but metadata is worth far more `.

<img width="1276" alt="Screenshot 2024-06-06 at 8 08 06 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/d2040d28-b90c-48e4-8c78-a705cedc1cda">

OK! so let's look at ` metadata ` i.e., ` EXIFTOOL ` and woohoo..found the ` username ` of attacker in ` Export-filename ` section.

<img width="622" alt="Screenshot 2024-06-09 at 9 27 21 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/ac287e06-8b1e-4afb-9bbc-4877b35a7482">


### RECONNAISSANCE
> What is the full email address used by the attacker?
>
> SakuraSnowAngel83@protonmail.com

Going with Instructions, I looked for similar usernames on sites like [WhatsMyName](https://whatsmyname.app/) but couldn't find any valid user page. So, I just searched the username on google and found a ` Github ` page and a ` Twitter ` 
account. Going through the github repo of attacker, I found the repo ` PGP ` which has some public key which I thought maybe some ` base64 `. So, I put the whole key on ` CyberChef ` and BOOM! I got the attacker's email.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/13a593ad-0087-4fe2-af86-f349cf5c0a8a)

<img width="1027" alt="Screenshot 2024-06-07 at 1 51 41 AM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/2bbb6e82-279b-4978-9071-c20274b664cd">


> What is the attacker's full real name?
>
> Aiko Abe

The Twitter account revealed the full real name of user ` Aiko Abe `:)

<img width="781" alt="Screenshot 2024-06-07 at 12 55 59 AM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/ecb32561-7c41-4700-921d-5fc11d7d4d64">


### UNVEIL
> What cryptocurrency does the attacker own a cryptocurrency wallet for?
> 
> Ethereum

The instructions said to take a deeper dive into attacker's Github account and look for changes. Looking through attacker's own repositories...

<img width="1267" alt="Screenshot 2024-06-06 at 9 28 35 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/bd1958a1-3b82-4d02-a92a-51ceb56a4bcf">

I found this cryptocurrency wallet in ` ETH ` repo and searching on google, I found ` eth ` is the name of ` Ethereum ` cryptocurrency and for which attacker own a wallet.

<img width="1270" alt="Screenshot 2024-06-06 at 9 36 46 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/12940729-ad4c-443d-9a4d-4307c5ef6587">



> What is the attacker's cryptocurrency wallet address?
>
> 0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef

Going through the ` commit history ` of ` mining script `, I found a string of letters and numbers being deleted and on searching on google, I found that ` A wallet address is a string of letters and numbers from which cryptocurrencies or NFTs can be sent to and from. `
There we got the wallet address!

<img width="1257" alt="Screenshot 2024-06-06 at 9 35 18 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/ae4d6946-7dc8-4795-86bf-d7d5d0cc7021">



> What mining pool did the attacker receive payments from on January 23, 2021 UTC?
>
> Ethermine

This was somehing which can't be found on. For this, I searched for some website where I can see payment history of ` Ethereum `cryptocurrency and found this [etherscan.io](https://etherscan.io/) and when I put attacker's wallet address in search section, I got all payments history and there I found that the attacker received payments from on ` Jan 23, 2021 ` was ` Ethermine `

<img width="1266" alt="Screenshot 2024-06-06 at 9 46 43 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/6fdf842f-967f-470a-8601-e09010ad9a5d">



> What other cryptocurrency did the attacker exchange with using their cryptocurrency wallet?
>
> Tether

Similarly, looking at the history of payments in above image, it can be seen that the other cryptocurrency attacker exchanged is of ` Tether `


### TAUNT 
> What is the attacker's current Twitter handle?
>
> SakuraLoverAiko

The instructions said that the attacker messaged from another Twitter account. 

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/eba9ec0a-c0c0-4e5b-8178-b4e6401690a1)

After seeing this image, I searched ` @AikoAbe3 ` on Twitter and oh! I got the account from which I got the full name of attacker and I also got to know that this was the new account of the attacker and he had another before. Got the username ` SakuraLoverAiko ` :)

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/10694d8e-f828-45e7-9703-87d439bab02f)

> What is the URL for the location where the attacker saved their WiFi SSIDs and passwords?
>
> http://deepv2w7p33xa4pwxzwi2ps4j62gfxpyp44ezjbmpttxz3owlsp4ljid.onion

Well, the hint said about ` The Dark Web ` and one of the attacker post said ` DEEP PASTE ` in capitals but I was not able to find any website with this name or anything. So, I just used the 
screenshot given in hints for this task and there I got the url in search bar. 

<img width="1066" alt="Screenshot 2024-06-07 at 1 30 45 AM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/2f62e4a2-fe8a-4330-a547-3b83d9e468ef">




> What is the BSSID for the attacker's Home WiFi?
>
> 84:af:ec:34:fc:f8

The above screenshot shows “Home WiFi: DK1F-G Fsdf324T@@”. I went to [wigle.net](https://wigle.net) and did a ` Basic Search ` for SSID ` DK1F-G ` in Japan (I chose Japan based on other tweets that 
indicated that location). And BOOM! it showed the BSSID as ` 84:AF:EC:34:FC:F8 `.

### HOMEBOUND
> What airport is closest to the location the attacker shared a photo from prior to getting on their flight?
>
> DCA

Attacker shared this image with a building on the side and a cherry blossom tree on another. Well, reverse searching this as a image doesn't give anything useful. 

![Esh-uTvUcAc-sXC](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/c4a9359f-6756-442c-91a9-4ce76f96a6d2)

Finally, I noticed a white building in the back standing tall which was looking short, I reverse searched it and found it was not any building but ` Washington Monument `

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/e50addd1-f4ed-4937-b3a0-ef96883f07e2)

Then, I searched for ` nearest airport to WASHINGTON MONUMENT ` and yess...I got it ` Ronald Reagan Washington National Airport `, Code: ` DCA `.


> What airport did the attacker have their last layover in?
>
> HND

Reverse searching the image on google, I found it was ` Sakura Lounge, Japan Airlines ` and then I searched for its airport code and got two codes. I put both and got ` HND ` correct.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/8126ff73-cba7-44d2-acb5-18d599b88f3f)



> What lake can be seen in the map shared by the attacker as they were on their final flight home?
>
> Lake Inawashiro

Going through this map on ` Google Map ` I found this ` blue area ` which was actually a lake called ` Lake Inawashiro `.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/3cf63ec4-14e4-480a-98b0-a96de0ad8747)



> What city does the attacker likely consider "home"?
>
> Hirosaki

I got this one's answer from the screenshot which was given in hint part of ` TAUNT ` there I found the city of attacker in ` City_Wifi ` section ` Hirosaki `.


## Sofia Santos | OSINT Exercises
### OSINT Exercise 6
> On January 19, 2023, a journalist with almost 140k followers on Twitter shared an image of a destroyed vehicle amidst a large cloud of smoke and fire. The tweet said:
> “BREAKING: TTP carried out a suicide attack on a police post in Khyber city of Pakistan that killed three Pakistani police officers.“
> 
> Verify that the photo is not of the event described by the journalist.
>
Reverse searching the image I found one of this article which was a book review with this image ` dated Sept. 4, 2020 ` (before this tweet) describing this incident which happened in ` Iraq ` and not in ` Pakistan `. The culprit being ` Al-Qaeda `.

<img width="970" alt="Screenshot 2024-06-06 at 7 31 00 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/99dee494-cd9c-40d7-930f-25b3c62aa3e3">


### OSINT Exercise 4
> This is a photo of a resort located on an island.
>
> a) What is the name of the resort?
>
> b) What are the coordinates of the island?
>
> c) In which cardinal direction was the camera facing when the photo was taken?

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/6763ba2d-987d-4bd6-bc6e-fc1005bf2ccf)

Reverse searching the image on google, I got the name of the resort ` Oan Resort ` which was located on ` Oan Island, Wonip, Chuuk, Micronesia `. Then, I searched for ` Oan Resort Coordinates ` on island and it was ` 7.3626° N, 151.7563° E `

For the third part, we need some ` Google Earth ` in the game. Putting the coordinates on there and moving and moving till we get to the location from which the camera took the photo and here we got ` Northwest `.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/bf2ae893-905d-4eff-8843-c3e74ea70fba)


### OSINT Exercise 3
> In April 2017 Mohamed Abdullahi Farmaajo, the then president of Somalia, visited Turkey. A news agency published a photo where he was seen shaking hands with Recep Tayyip Erdoğan, the country’s president. The article did not disclose where
> the photo was taken. Your task is to find out the name and coordinates of the location seen below.

Reverse searching the image, I came across this official tweet by ` Villa Somalia ` which stated the place as ` Presidential Complex in Ankara `. Although, the date of tweet was different from given in challenge but the location is same.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/c4281659-2c38-4f2c-8382-7c59ad40d63a)


### OSINT Exercise 14
> The video below was recorded during an earthquake.
> Please find the answer to the following questions:
>
> a) What was the magnitude of this earthquake?
> 
> b) What are the coordinates of where the camera was likely located in order to record this scene?

Reverse searching the image, I found many posts with the same clip. Fortunately, one of the links titled ` Cutremur Chisinau 24.09.2016 `. Clicking on the link, I found that it is indeed the same clip. To get more confirmed, I searched for all earthquakes that happened in ` September 2016 `and found [List of earthquakes in 2016](https://en.wikipedia.org/wiki/List_of_earthquakes_in_2016#September) and there I found earthquakes that happened on ` 23rd or 24th September ` and there were three on each date - Japan, Burundi and Romania on the 23rd and Philippines, Tonga and Fiji on the 24th. All occurrences had links to USGS which reports the time stamps in UTC+0. So, I searched for time at which earthquake happened in Romania on ` 23rd September 2016 ` in UTC time and got this. Also, I compared by getting UTC time of other earthquakes and only the time in the video matched with ` Romania `. 

<img width="833" alt="Screenshot 2024-06-10 at 1 12 31 AM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/d69e0a6d-0724-4626-a8d7-1ba4b584f2c4">

Searching more, I found that the city ` Chisinau ` was 224km away from the epicentre. So, the magnitude of earthquake would have been somewhere between ` 5.4 ` and ` 5.6 ` from ` Wikipedia ` page. 

<img width="828" alt="Screenshot 2024-06-10 at 12 26 10 AM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/a63fd51d-cfc9-4388-9e53-4c5722d8ecf5">

Then, for the coordinates of camera, I tried to match the buildings around the house with the building on which camera was placed. One of the building was ` Atrium Shopping Mall `, other one was ` Dimitrie Cantemir Boulevard. 14 ` and nearest one was ` Chișinău `. And, yahoo..got the coordinates of camera ` 47.017518, 28.852841 `.

<img width="568" alt="Screenshot 2024-06-10 at 12 09 53 AM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/dddbe833-91e8-4e4c-993b-c787f6d1a14d">

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/04bd52ba-083b-4337-8dd8-ad683d4833ce)

## OSINT Exercise 26
> The image below shows the contents of a zip file. Inside you will find a 31-second video recorded during a train ride, and four photos of undisclosed
> locations. They were all taken by the same individual in February 2024. Despite having no useful metadata, they still contain enough information to track down > this person’s movements.
>
> Your task is to determine:
>
> a) At which train stations did the person board and alight?

