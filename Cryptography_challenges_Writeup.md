# Challenge_1

`source.enc` is `base64` encoded, decoding it will give this python script:

```python
with open('flag.txt', 'r') as f:
    flag = f.read()

s = ''.join(format(ord(i), '02x') for i in flag)
e = ""

for i in range(0,len(s),4):
    e += format(int(s[i:i+2],16)^int(s[i:i+4],16), '02x')

with open('output.txt', 'w') as f:
    f.write(e)
```

`output.txt` is the output file of above python script and it contains the value of `e`. When I tried to convert `e` from hex I got some messed up string looking like this: `CO2{H4y&b56_kn _'0B?B`. As the flag is of the form `CSOC23{}`, I transformed this string to `CSO23{H4y&b56_kn _'0B?}`. Then, I ran below python script which is performing `XOR` operation and giving complete flag :)

```python
flag = "CSOC23{H4 y&b 5 6 _kn _'0B?}"
s = ''.join(format(ord(i), '02x') for i in flag)
e = "43104f0c32017b48340179266203350636025f6b6e0a5f2730423f42"
decrypted_bytes = []
for i in range(0, len(e), 4):
    # Extract the 2-byte segments from e and s
    e_segment = int(e[i:i + 4], 16)
    s_segment = int(s[i:i + 2], 16)

    # XOR the segments to get the original s_segment
    original_s_segment = e_segment ^ s_segment

    # Convert the result back to bytes and append to decrypted_bytes
    decrypted_bytes.append(original_s_segment.to_bytes(2))
    # print(decrypted_bytes[-1])

decrypted_bytes = b''.join(decrypted_bytes)
decrypted_flag = decrypted_bytes.decode('utf-8')
print("Decrypted Flag:", decrypted_flag)
```


` CSOC23{345y_ba5364_4nd_x0r?} `



# Challenge_2

Given: `01000011 01010011 01001111 01000011 00110010 33 7b 6a 75 35 37 5f ZDFmZjNyM243XzNuYw== 60 144 61 156 66 65 137 154 60 154 175`

Here, the flag is encoded using different methods: `binary`, `hex`, `base64` and `octal`. Decoding each part subsequently will give the flag :)

`Tip`: I was not able to remember what the last part is encoded in. So, I used `CyberChef` - `Magic` recipe to get which operation could help to make more sense of the string.

```python
import base64

binary_string = "01000011 01010011 01001111 01000011 00110010"
hex_string = "33 7b 6a 75 35 37 5f"
base64_string = "ZDFmZjNyM243XzNuYw=="
octal_string = [60, 144, 61, 156, 66, 65, 137, 154, 60, 154, 175]

decoded_binary = ''.join(chr(int(b, 2)) for b in binary_string.split())
decoded_hex = ''.join(chr(int(h, 16)) for h in hex_string.split())
decoded_base64 = base64.b64decode(base64_string).decode('utf-8')
decoded_octal = ''.join(chr(int(str(o), 8)) for o in octal_string)

print(f"{decoded_binary}{decoded_hex}{decoded_base64}{decoded_octal}")
```

`CSOC23{ju57_d1ff3r3n7_3nc0d1n65_l0l}`

<h1>CryptoHack Challenges</h1>

<h2>INTRODUCTION</h2>

<h4>Finding Flags</h4>

The challenge just said to submit ` crypto{y0ur_f1rst_fl4g}  ` as flag.

<h4>Great Snakes</h4>

Just run the attached [great_snakes.py](https://cryptohack.org/static/challenges/great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py) to get the flag: ` crypto{z3n_0f_pyth0n} `

<h4>Network Attacks</h4>

Connect to ` socket.cryptohack.org ` on port ` 11112 ` using ` nc socket.cryptohack.org 11112 ` then send the ` JSON ` object ` {"buy" : "flag"} ` and get the flag: 
`crypto{sh0pp1ng_f0r_fl4g5}`

<h2>GENERAL</h2>

<h3>ENCODING</h3>

<h4>ASCII</h4>

```python
# Converting given integer array to their corresponding ASCII characters using 'chr()' function
num = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for n in num:
    print(chr(n), end='')
```

`crypto{ASCII_pr1nt4bl3}`

<h4>Hex</h4>

```python
# Decoding given hex string into bytes using 'bytes.fromhex()' function
num_str = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(num_str))
```

`crypto{You_will_be_working_with_hex_strings_a_lot}`

<h4>Base64</h4>

```python
# Decoding given hex string into bytes and then encoding it into Base64 using 'base64.b64encode()' function
import base64

hex_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte_str = bytes.fromhex(hex_str)
enc_b64 = base64.b64encode(byte_str)
print(enc_b64)
```

`crypto/Base+64+Encoding+is+Web+Safe/`

<h4>Bytes and Big Integers</h4>

```python
# Converting given long integer into a message using 'long_to_bytes()' function
from Crypto.Util.number import*
num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
num = long_to_bytes(num)
print(num)
```

`crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}`

<h3>XOR</h3>

<h4>XOR Starter</h4>

```python
# XORing given string with the integer 13 using `xor()` function
str = "label"
for x in str:
  print(chr(ord(x)^13), end="")
```

`crypto{aloha}`

<h4>XOR Properties</h4>

```python
# Using Commutative, Associative, Identity and Inverse properties of XOR to obtain the flag 
from pwn import xor
k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1') # key2 ^ key3 = k2_3
flag_1_3_2 =bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# Given, flag ^ k1 ^ k3 ^ k2 = flag_1_3_2 & k3 ^ k2 = k2 ^ k3
# say,   k1 ^ (k2 ^ k3)  = k1_23 => k1 ^ k2_3 = k1_23
#        flag ^ k1_23 = flag_1_3_2
#        flag ^ (k1_23 ^ k1_23) = flag_1_3_2 ^ k1_23  => flag ^ 0 = flag = flag_1_3_2 ^ k1_23 

flag = xor(k1,k2_3,flag_1_3_2)
print(flag) 
```

`crypto{x0r_i5_ass0c1at1v3}`

<h4>Favourite Byte</h4>

```python
# Looping through every single byte and XORing to see if 'crypto' contains in the decoded string
from pwn import xor
flagBytes = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
byte = 0x00
for _ in range(256):
    flag = xor(flagBytes,byte).decode()
    if ("crypto" in flag):
        print(flag)
        break
    byte = byte + 0x01
```

`crypto{0x10_15_my_f4v0ur173_by7e}`

<h4>You either know, XOR you don't</h4>

```python
# Don't know secret key but knowing the flag format and XORing it with given hex string gives some idea of the key
# and now XORing with this key gives the flag

from pwn import xor 
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104') 
print(xor(flag, 'crypto{'.encode() )) 
# prints 'myXORke+y'
print(xor(flag, 'myXORkey'.encode()))
```

`crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}`

<h3>MATHEMATICS</h3>

<h4>Greatest Common Divisor</h4>

Find `Euclid's Algorithm` to find `GCD` [here](https://en.wikipedia.org/wiki/Euclidean_algorithm).

```python
def gcd(a,b):
    while b!=0:
           t=b
           b = a%b
           a = t

    return a

a,b = 52920,66528
print(gcd(a,b))
```
#Output: `1512`

<h4>Extended GCD</h4>

Find `Extended Euclidean algorithm` [here](https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html).

```python
def gcdExtended(a, b):
    # Initialize the coefficients for a and b
    x0, x1 = 0, 1
    y0, y1 = 1, 0
    
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    
    # a is the gcd, x0 and y0 are the coefficients
    return a, x0, y0

a, b = 26513, 32321
g, x, y = gcdExtended(a, b)
print(f"gcd({a}, {b}) = {g}, x = {x}, y = {y}")
```

#Output: `gcd(26513, 32321) = 1, x = -8404, y = 10245`  ( Here, x and y represents u and v respectively)

#Flag: `-8404`

<h4>Modular Arithmetic 1</h4>

```python
print(11%6)       # ouputs 5
print(8146798528947%17)   # outputs 4
```

#Flag: `4`

<h4>Modular Arithmetic 2</h4>

```python
print((273246787654**65536)%65537)
```

#Output: `1`

<h4>Modular Inverting</h4>

```python
def mod_inverse(g, p):
    # Using Fermat's Little Theorem to find the inverse
    return pow(g, p-2, p)

g = 3
p = 13
inverse = mod_inverse(g, p)
print(f"The multiplicative inverse of {g} modulo {p} is {inverse}")
```

#Output: `The multiplicative inverse of 3 modulo 13 is 9`

<h2>SYMMETRIC CIPHERS</h2>

<h3>HOW AES WORKS</h3>

<h4>Keyed Permutations</h4>

What is the mathematical term for a one-to-one correspondence?

#Flag: `crypto{bijection}`

<h4>Resisting Bruteforce</h4>

What is the name for the best single-key attack against AES?

Click on the red highlighted `an attack` to get the name of the attack asked here and submit `crypto{biclique}`

<h4>Structure of AES</h4>

```python
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

# Complete this function
def matrix2bytes():
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return ''.join(chr(cell) for row in matrix for cell in row)

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes())
```

`crypto{inmatrix}`

## RSA

### STARTER

#### RSA Starter 1

```python
print(pow(101,17,22663))
```

#Output: `19906`

#### RSA Starter 2

Use `pow(base, exponent, modulus)` built-in operator for next few RSA challenges.

```python
p , q = 17, 23
N = p*q
e = 65537
message = 12
print(pow(message,e,N))
```

#Output: `301`

#### RSA Starter 3

Find about `Euler totient` [here](https://leimao.github.io/article/RSA-Algorithm/)

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
n_totient = (p-1)*(q-1)
print(n_totient)
```

#Output: `882564595536224140639625987657529300394956519977044270821168`

#### RSA Starter 4

Find `private key` or `modular multiplicative inverse` of the exponent `e` modulo the totient of `N` using `Extended Euclidean algorithm` discussed above.

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
n_totient = (p-1)*(q-1)
e = 65537
d = pow(e,-1,n_totient) # exponent will be -1 since inverse is to be calculated
print(d)
```
      
#Output: `121832886702415731577073962957377780195510499965398469843281`

#### RSA Starter 5

Find more about `ciphertext`, `private key` and `public key` [here](https://leimao.github.io/article/RSA-Algorithm/))

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
n_totient = (p-1)*(q-1)
N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
d = pow(e,-1,n_totient) # As found in previous challenge
c = 77578995801157823671636298847186723593814843845525223303932
decrypted_message = pow(c,d,N)
print(decrypted_message)
```

#Output: `13371337`

#### RSA Starter 6

```python
from Crypto.Util.number import bytes_to_long
import hashlib

# from private.key
N = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689

# hash
message = "crypto{Immut4ble_m3ssag1ng}"
hash = hashlib.sha256(message.encode()).digest()
hash = bytes_to_long(hash)

# sign
sign = pow(hash, d, N)
print(sign)
```

#Output: 13480738404590090803339831649238454376183189744970683129909766078877706583282422686710545217275797376709672358894231550335007974983458408620258478729775647818876610072903021235573923300070103666940534047644900475773318682585772698155617451477448441198150710420818995347235921111812068656782998168064960965451719491072569057636701190429760047193261886092862024118487826452766513533860734724124228305158914225250488399673645732882077575252662461860972889771112594906884441454355959482925283992539925713424132009768721389828848907099772040836383856524605008942907083490383109757406940540866978237471686296661685839083475

### PUBLIC EXPONENT

#### Salty

```python
from Crypto.Util.number import long_to_bytes

n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767
e = 1
ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
pt = pow(ct,e,n)
pt_bytes = long_to_bytes(pt)
# Since e = 1, therefore ct = (m)^e mod n will become m = c (mod n)

# Decode the bytes to a string
pt_string = pt_bytes.decode('utf=8')
print(pt_string)
```

`crypto{saltstack_fell_for_this!}`


