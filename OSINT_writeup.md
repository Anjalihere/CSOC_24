# Challenge #2
## Try Hack Me | Sakura Room
### INTRODUCTION
Just type in "Let's Go!" 
### TIP-OFF
> What username does the attacker go by?
> 
> SakuraSnowAngelAiko

Reading the instructions, it said to analyse the image well and that image contain a lot of information. So, I converted the ` binary ` of image into ` ASCII ` and got this ` A picture is worth 1000 words but metadata is worth far more `.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/080b8b33-3bba-4f9c-ae43-69b713c89644)

OK! so let's look at ` metadata ` i.e., ` EXIFTOOL ` and woohoo..found the ` username ` of attacker in ` Export-filename ` section.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/279fed76-a7d9-48f1-85b6-c980f51ef8bb)

### RECONNAISSANCE
> What is the full email address used by the attacker?
>
> SakuraSnowAngel83@protonmail.com

Going with Instructions, I looked for similar usernames on sites like [WhatsMyName](https://whatsmyname.app/) but couldn't find any valid user page. So, I just searched the username on google and found a ` Github ` page and a ` Twitter ` 
account. Going through the github repo of attacker, I found the repo ` PGP ` which has some public key which I thought maybe some ` base64 `. So, I put the whole key on ` CyberChef ` and BOOM! I got the attacker's email.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/13a593ad-0087-4fe2-af86-f349cf5c0a8a)

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/968c5bbc-5374-4492-b0b8-5ed42d4b1328)

> What is the attacker's full real name?
>
> Aiko Abe

The Twitter account revealed the full real name of user ` Aiko Abe `:)

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/115b7a2e-953a-4b93-8b22-b841c9cecf09)

### UNVEIL
> What cryptocurrency does the attacker own a cryptocurrency wallet for?
> 
> Ethereum

The instructions said to take a deeper dive into attacker's Github account and look for changes. Looking through attacker's own repositories...

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/b7f4a360-a2aa-498e-98fc-5216b92890b9)

I found this cryptocurrency wallet in ` ETH ` repo and searching on google, I found ` eth ` is the name of ` Ethereum ` cryptocurrency and for which attacker own a wallet.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/241bd457-f666-44d0-9dae-9d20c3bad43a)

> What is the attacker's cryptocurrency wallet address?
>
> 0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef

Going through the ` commit history ` of ` mining script `, I found a string of letters and numbers being deleted and on searching on google, I found that ` A wallet address is a string of letters and numbers from which cryptocurrencies or NFTs can be sent to and from. `
There we got the wallet address!

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/df62db69-7387-422a-8f17-28d69c803de9)

> What mining pool did the attacker receive payments from on January 23, 2021 UTC?
>
> Ethermine

This was somehing which can't be found on. For this, I searched for some website where I can see payment history of ` Ethereum `cryptocurrency and found this [etherscan.io](https://etherscan.io/) and when I put attacker's wallet address in search section, I got all 
payments history and there I found that the attacker received payments from on Jan 23, 2021 was ` Ethermine `

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/16ae593b-7551-4673-ab77-109cb862acde)

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

After seeing this image, I searched ` @AikoAbe3 ` on Twitter and oh! I got the account from which I got the full name of attacker and I also got to know that this was the new account of the 
attacker and he had another before. Got the username ` SakuraLoverAiko ` :)

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/10694d8e-f828-45e7-9703-87d439bab02f)

> What is the URL for the location where the attacker saved their WiFi SSIDs and passwords?
>
> http://deepv2w7p33xa4pwxzwi2ps4j62gfxpyp44ezjbmpttxz3owlsp4ljid.onion

Well, the hint said about ` The Dark Web ` and one of the attacker post said ` DEEP PASTE ` in capitals but I was not able to find any website with this name or anything. So, I just used the 
screenshot given in hints for this task and there I got the url in search bar. 

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/7be818e1-5f49-46e0-9238-8fbe4a8e3e6a)


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

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/9c801753-7024-48c8-b595-915a64b7bff2)

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

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/f41b8796-5742-429d-8477-1498f628cf41)

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
> Reverse searching the image I found one of this article which was a book review with this image ` dated Sept. 4, 2020 ` (before this tweet) describing this incident which happened in ` Iraq ` and not in ` Pakistan `. The culprit being ` Al-Qaeda `.
>
> ![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/fa96ae9a-40f7-4499-b6ca-4f8b421ce6e5)

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

For the third part, we need some ` Google Earth ` in the game. Putting the coordinates on there and moving and moving till we get to the direction from which the camera took the photo and here we got ` Northwest `.

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

Reverse searching the image, I found many posts with the same clip. Fortunately, one of the links titled ` Cutremur Chisinau 24.09.2016" `. Clicking on the link, I found that it is indeed the same clip.To get more confirmed, I searched for 
` List of earthquakes in 2016 ` and there I found earthquakes that happened on ` 24th September ` and I tried to match the time zone as given in video and found the location was ` Romania `
Then, for the coordinates of camera, I tried to match with directions of building around the house on which camera was placed.

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/0391018d-8ea8-486d-a31d-e24d0004836c)



