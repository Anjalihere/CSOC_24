I found and analyzed the save file of the popular mobile game `Temple Run`. I did some research to found out that in the earlier version of this game, a save file `gamedata.txt` used to be there which was vulnerable to changes. But, the new version I have is very secure to these changes.


![img](https://video-images.vice.com/articles/610a7c706de2b4009bf4168a/lede/1628179209216-new-project-16.jpeg?crop=1xw:1xh;center,center&resize=1200:*)


I connected my phone to PC to see all the files of games. I found Temple Run in `Internal Storage/Android/Data/com.imangi.templerun` and the important files were in `files` folder.
This folder contained a lot of `.dat` files in different locations which was a bit confusing to determine which is the true `save file` . 


Looking through each of them, I got to know that `recordmanager.dat` may contain `saved data` of game. Because `global-metadata.dat`, `System.Data.dll-resources.dat `, `mscorlib.dll-resources.dat`…these files contain a lot of data, some seemed to be `base-64` though, they were truly not. 

<img width="479" alt="Screenshot 2024-07-15 at 10 30 03 PM" src="https://github.com/user-attachments/assets/3f0e9c5e-320d-4c77-a071-0e066480c8f5">

Also when I compared them after playing one and then another game, there was no difference seen. 


(Note that `recordmanager.dat` and `ALT_recordmanager.dat` contained same data.)

<img width="499" alt="Screenshot 2024-07-15 at 10 30 59 PM" src="https://github.com/user-attachments/assets/13448854-96c3-4de6-ba6a-f38eed562fae">

But when I compared `recordmanager.dat` files after another game, a lot of difference were noticed which confirmed of it being the save file. 

<img width="578" alt="Screenshot 2024-07-15 at 10 40 43 PM" src="https://github.com/user-attachments/assets/8ce62d77-5462-40ac-ba4b-d7c3b89fa87b">

I put `hexdump` of two games in two different files using `xxd` then compared them using `diff`. A lot of amall and big differences were noticed at different offsets which couldn't confirm the location `coins` value
Which I was looking for.

<img width="572" alt="Screenshot 2024-07-15 at 10 41 00 PM" src="https://github.com/user-attachments/assets/e6eb6fa0-b1a5-463f-ba32-74dce028f399">

In the first game, I had `1124` (`0x464`) coins and in the next game, I got `1192` (`0x4a8`) coins. `grep` these coins' hex values in these save files didn't give a useful offset where the coin data could be present. Also, same happened with `score` parameter.

<img width="410" alt="Screenshot 2024-07-15 at 10 48 29 PM" src="https://github.com/user-attachments/assets/b6114b4b-4bed-4374-8061-b46ced36aba2">


This analysis clearly points towards that the save file is `obfuscated` very badly that it won't let access anyway. Online editors also doesn't work on these files.



