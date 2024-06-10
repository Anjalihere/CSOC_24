# Challenge #1
## information
> Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/149ab4b27d16922142a1e8381677d76f/cat.jpg)
>
> Hint_1: Look at the details of the file
> 
> Hint_2: Make sure to submit the flag as picoCTF{XXXXX}

Looking at the image...umm..nothing so special. Let's look for the file type using  ` file ` command. Nothing suspicious...it is a ` JPEG ` file. Now let's use ` exiftool ` to get the detailed information about the file.
Here we found some ambiguous ` base64 encoded ` string in the  ` License ` section. Let's decode it and here we found our flag :)

` picoCTF{the_m3tadata_1s_modified} `

<img width="1018" alt="information_picoctf" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/c3463d97-1145-4e19-83b0-b677c50833c1">

## Matryoshka doll
> Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/1b70cffdd2f05427fff97d13c496963f/dolls.jpg)
>
> Hint_1: Wait, you can hide files inside files? But how do you find them?
>
> Hint_2: Make sure to submit the flag as picoCTF{XXXXX}

Looking at the image..just a doll image. The name ` Matryoshka ` indeed seem intriguing. ` Google ` said that it is also known as stacking or ` nesting ` dolls...that rings a bell. I remembered ` binwalk ` looked for 
embedded files and executable code in a binary image. So, I did ' binwalk ' and found this ` 2_c.jpg ` file (offo...again a doll)...maybe more embeddings. Again, did ` binwalk ` and found ` 3_c.jpg ` file and again, 
found ` 4_c.jpg ` and one last time and found the flag in ` flag.txt ` file.

` Tip : ` Look for these handy commands [here](https://trailofbits.github.io/ctf/forensics/) 

` picoCTF{bf6acf878dcbd752f4721e41b1b1b66b} `


<img width="1100" alt="Screenshot 2024-06-09 at 3 44 18 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/14296686-a63b-434a-abe0-f375a33b30f4">

<img width="1100" alt="Screenshot 2024-06-09 at 3 54 00 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/73efccc5-28c6-40ac-b531-ddc79b353391">

<img width="1100" alt="Screenshot 2024-06-09 at 3 51 12 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/a1156cba-20de-4bb9-83e8-c02d61daffd8">

<img width="1100" alt="Screenshot 2024-06-09 at 3 45 50 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/5bf190ec-01c0-4306-b6c1-f096753eb5c8">

<img width="1100" alt="Screenshot 2024-06-09 at 3 46 55 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/d6e4d048-53e6-49b8-a958-aceffd8b7bfc">

## tunn3l v1s10n
> We found this [file](https://mercury.picoctf.net/static/21c07c9dd20cd9f2459a0ae75d99af6e/tunn3l_v1s10n). Recover the flag.
>
> Hint: Weird that it won't display right...

` file ` command just said ` data `. Doing ` exiftool `, I found it is a ` bmp(bitmap) ` that too ` 24-bit bitmap ` file. Then, I opened it in [hexed.it](https://hexed.it/) and looked for the ` BITMAP ` file format on 
google. Going through ` Wikipedia ` page, I found the ` DIB header ` of the file was messed up. 

<img width="780" alt="Screenshot 2024-06-08 at 7 39 34 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/ae78ae73-7a56-4f1c-abd5-b7fe8f1eac64">

So, I changed the ` 15th byte ` of file from ` BA D0 ` to ` 28 00 ` and got a ` fake flag ` image. 

<img width="576" alt="Screenshot 2024-06-08 at 7 40 33 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/99100db9-5426-4a44-bf8c-000c84930e9a">

It seemed like we should increment the height of image. So, I changed the ` height ` byte of image to same as ` width ` of image i.e., to ` 6E 04 ` and found the flag :)

` picoCTF{qu1t3_a_v13w_2020} `

<img width="681" alt="Screenshot 2024-06-09 at 5 25 55 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/8008814d-3c51-49a5-97ed-9543606a98e2">


<img width="567" alt="Screenshot 2024-06-08 at 7 41 35 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/c3c6d9e3-f6f3-47c8-995b-58812d303b36">

## MacroHard WeakEdge
> I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/c00c449c3b08daaccacca6f9d5c55d49/Forensics%20is%20fun.pptm)
>

Have heard of ` ppt ` files but ` pptm `...let's search. OK! ` zip ` rings a bell. Let's try to ` unzip ` it and there we see a ` hidden ` file at last. Let's ` cat ` it and some string...maybe ` base64 `, decode and 
got the flag :)

` picoCTF{D1d_u_kn0w_ppts_r_z1p5} `

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/62f656ec-72b9-40df-9bfd-497eaf8b6678)

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/ddf2e84d-d9d5-4669-83be-962eb7130c4d)
![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/7879d4ed-aaa2-4f55-85f8-323d58f8fb64)

## Enhance!
> Download this image file and find the flag.
>
> [Download image file](https://artifacts.picoctf.net/c/102/drawing.flag.svg)

This ` SVG ` file opened in chrome and that was a large black circle. Since, it opened in chrome I just did ` View Page Source `. At first, I didn't notice it. But, as soon as I saw the last part of flag 
` c 3 d _ d 0 a 7 5 7 b f } ` which was hard to go unnoticed, I found the flag with other parts being before ` </tspan><tspan ` in some lines of last part of code.

` picoCTF{3nh4nc3d_d0a757bf} `

<img width="742" alt="Screenshot 2024-06-09 at 5 59 37 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/f5caf166-0f26-4585-b767-489ab77063d8">

## advanced-potion-making
> Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!
>
> Download [advanced-potion-making](https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making)

Judging by the description of the challenge, it seems the file is corrupted. Let's open it in hexeditor, looking through the [file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures), the initial bytes 
point towards a ` PNG ` file. So, I searched for ` PNG wiki ` page and found the file header structure. And, I saw that many bytes of the file are corrupted. 

<img width="933" alt="Screenshot 2024-06-09 at 7 45 50 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/3b65d2f8-f850-48d2-a069-677f347fb666">
<img width="690" alt="Screenshot 2024-06-09 at 7 54 43 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/10bb3850-40c7-47d9-8e6d-7c8396a924d1">

So, I fixed them on hexeditor and got a whole red image.

<img width="1152" alt="Screenshot 2024-06-09 at 7 40 26 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/97bd79d1-2350-431f-b5c3-a936576d8179">

All red?...maybe it has something to do with colours. I tried to edit it using this [image editor](https://www.online-image-editor.com/) and just when I color changed it to ` Black&White ` Boom! Got the flag :)

<img width="1259" alt="Screenshot 2024-06-09 at 7 40 04 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/a9e11027-cdf5-4c61-95ac-b270fd34a06c">

` picoCTF{w1z4rdry} `

## hideme
> Every file gets a flag.
>The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/262/flag.png).
>

` exiftool ` yielded nothing but when I ` binwalked ` the file, I found another embedded file ` flag.png ` into this file. So, I extracted it and there is the flag in ` flag.png ` image.

` picoCTF{Hiddinng_An_imag3_within_@n_ima9e_82101824} `

<img width="1049" alt="Screenshot 2024-06-09 at 6 09 01 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/6829a0d3-445a-4cf3-a33b-c2e1b0fb112c">

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/03a7daea-c569-4a5e-8f74-fb4f63ac5c42)

## MSB
> This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
>
> Download the image [here](https://artifacts.picoctf.net/c/302/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)
> 
> Hint_1: What's causing the 'corruption' of the image?

Hmm..MSB ` Most Significant Bit `, we can guess from the title that the challenge is related to ` MSB `.  So, I searched for some ` MSB Steganography tools ` and found a ` git repository ` and then cloned it. After that,
I read the ` README.md ` to know the requirements and usage of ` sigBits.py ` file and installed ` Pillow `. When I ran it with arguments ` --type=Msb ` and ` image file `, I got ` outputSB.txt ` file which has a lot and lot of long text lines, 
therefore, using just ` grep ` wasn't getting me flag. So, I had to use ` cat outputSB.txt | tr " " "\n" | grep -oE "picoCTF{.*?}" ` and got the flag :)
Also, ` tr " " "\n" `: Replaces each space with a newline, splitting the sentence into individual words on separate lines

` picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_ea7deb4c} `


<img width="1049" alt="Screenshot 2024-06-09 at 6 57 58 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/a045ee76-1ee6-4b5e-b029-491b4fff4a87">
<img width="1049" alt="Screenshot 2024-06-09 at 6 58 14 PM" src="https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/0dd48460-e6e2-491a-9939-0c03d67b85e4">

## extensions
> This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?
>
> Hint_1: How do operating systems know what kind of file it is? (It's not just the ending!
>
> Hint_2: Make sure to submit the flag as picoCTF{XXXXX}

As the name suggests, this has something to do with file ` extensions `. It says ` .txt ` but when I used ` file ` command, I got to know that it is actually ` PNG ` image file. So, I just changed the extension from ` .txt ` to ` .png ` and got the 
image which has the flag :)

` picoCTF{now_you_know_about_extensions} `

![image](https://github.com/Anjalihere/Week0_COPS-INFOSEC/assets/146505430/e18ed0ac-d6d8-4b51-806d-c41ac5b2b3b9)






  
