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
num = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for n in num:
    print(chr(n), end='')
```

`crypto{ASCII_pr1nt4bl3}`

<h4>Hex</h4>

```python
num_str = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(num_str))
```

`crypto{You_will_be_working_with_hex_strings_a_lot}`

<h4>Base64</h4>

```python
import base64

hex_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte_str = bytes.fromhex(hex_str)
enc_b64 = base64.b64encode(byte_str)
print(enc_b64)
```

`crypto/Base+64+Encoding+is+Web+Safe/`

<h4>Bytes and Big Integers</h4>

```python
from Crypto.Util.number import*
num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
num = long_to_bytes(num)
print(num)
```

`crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}`

<h3>XOR</h3>

<h4>XOR Starter</h4>

```python
str = "label"
for x in str:
  print(chr(ord(x)^13), end="")
```

`crypto{aloha}`

<h4>XOR Properties</h4>

```python
from pwn import xor
k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(k1,k2_3,flag)) 
```

`crypto{x0r_i5_ass0c1at1v3}`

<h4>Favourite Byte</h4>

```python
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
from pwn import xor 
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104') 
print(xor(flag, 'crypto{'.encode() )) 
# prints 'myXORke+y'
print(xor(flag, 'myXORkey'.encode()))
```

`crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}`

<h3>MATHEMATICS</h3>

<h4>Greatest Common Divisor</h4>

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
