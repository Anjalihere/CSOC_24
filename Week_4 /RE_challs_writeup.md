### Description
> Find password for Chall_1, Chall_2 and Chall_5 .
>
> Write a keygen for Chall_3 and Chall_4.
# Chall_1
> Password: 1234900000
>

Running `file` command tells that it is `ELF 64-bit LSB executable file`. Running the program, it prompts for the password and on taking the input tells whether it is correct or incorrect. `strings` command doesn't help much in getting the password.  

Let's decompile the file using this [decompiler explorer](https://dogbolt.org/) where you can experiment with a lot of reverse engineering tools like Ghidra, Hex rays, angr and so on and compare their results to see which one is giving more appropriate result.

`GDB` shows two important functions - `main` and `check`. Let's see through these functions in the decompiler Ghidra.

In the `main` function, a character array `local_118` is declared to store user input. The program prompts the user to enter a password, reads the input using fgets, and stores it in local_118. It then removes any newline character from the input using strcspn. The check function is called to verify the password. 


<img width="467" alt="Screenshot 2024-07-10 at 11 01 29 AM" src="https://github.com/Anjalihere/CSOC_24/assets/146505430/202d8b14-2678-4966-9ace-90987bcdd84d">


The `check` functions checks if the `input length is 10 characters`, the `first character is '1'`, and the `fifth character is '9'`. If these conditions are met, check returns 1, indicating the password is correct, and the program prints **Correct** otherwise, it prints **Incorrect** 


<img width="568" alt="Screenshot 2024-07-10 at 11 01 42 AM" src="https://github.com/Anjalihere/CSOC_24/assets/146505430/d7d55383-ee18-471b-b6b2-646a477f7c1c">

Given the specified conditions, there can be many passwords of the form `1 _ _ _ 9 _ _ _ _ _` and putting any of them will work. Let's put `1234900000` and woohoo! we cracked the password :)

# Chall_2
> Password: cracked
>
Again, the file is `LSB executable`. `strings` doesn't tell much. Binary Ninjas will give this decompiled code. I have put the functionality of each parameter in comments.

```cpp
// Analysis of main function

// String Initialization and Input Handling
std::string::string(&__str);  // Initializes __str for user input
std::ostream::operator<<(std::operator<<<std::char_traits<char>>(&std::cout, "Enter the password:"),
                         std::endl<char>);  // Outputs "Enter the password:"
std::getline<char>(&std::cin, &__str);  // Reads user input into __str

// Password Checking and Output
void var_38;
if (checkPassword(&var_38, r12) == 0) {
    __s = "Login failed";  // Sets login failure message
} else {
    __s = "Login successful";  // Sets login success message
}
std::ostream::operator<<(std::operator<<<std::char_traits<char>>(&std::cout, __s), std::endl<char>);  // Outputs login result

// Cleanup
std::string::~string(&var_38);  // Destructs var_38 to free memory
std::string::~string(&__str);  // Destructs __str to free memory
```

The `main` function manages user input and validation by prompting for a password, verifying it using `checkPassword` function against a preset pattern (var_48), and indicating login success or failure based on the validation result.


```cpp
// Analysis of checkPassword function

// Variable Initialization
int64_t var_10 = arg2;  // Initializes var_10 with arg2 (possibly a return value)

// String Initialization and Length Comparison
std::allocator<char>::allocator(&var_25);  // Allocates memory for local variables
std::string::string(&var_48, &data_2005);  // Initializes var_48 with predefined data
std::allocator<char>::~allocator(&var_25);  // Frees memory allocated by var_25
int32_t var_20 = 0xfffffff9;  // Sets var_20 to -7 (possibly for length comparison)
int32_t rax = std::string::length(&var_48);  // Gets length of var_48
int64_t rax_5;  // Variable for storing length comparison result

// String Manipulation and Comparison
rax_5 = std::string::length(arg1) == -(var_20);  // Compares length of arg1 with -7
int32_t rbx_2;  // Result variable for password validation
if (rax_5 != 0) {
    std::string::string(&var_68);  // Initializes var_68 for constructing password pattern
    for (int32_t i = 0; i < rax; i = (i + 1)) {
        if (i == (rax - 1)) {
            std::string::operator+=(&var_68);  // Appends characters to var_68
            std::string::operator+=(&var_68);  // Appends characters to var_68
        }
        std::string::operator+=(&var_68, *std::string::at(&var_48, i));  // Appends characters from var_48 to var_68
    }
    std::string::iterator rax_13 = std::string::end(arg1);  // Gets end iterator of arg1
    std::reverse<__normal_iterator<char*, std::string> >(std::string::begin(arg1), rax_13);  // Reverses arg1
    if (_ZSteqIcEN9__gnu_cxx11__enable_ifIXsrSt9__is_charIT_E7__valueEbE6__typeERKNSt7__cxx1112basic_stringIS3_St11char_traitsIS3_ESaIS3_EEESE_(arg1, &var_68) == 0) {
        rbx_2 = 1;  // Sets rbx_2 to 1 if password validation fails
    } else {
        arg2 = 1;  // Sets arg2 to 1 (possibly indicating successful validation)
        rbx_2 = 0;  // Sets rbx_2 to 0 indicating successful validation
    }
    std::string::~string(&var_68);  // Destructs var_68 to free memory
}

// Final Validation and Cleanup
if ((rax_5 == 0 || (rax_5 != 0 && rbx_2 == 1))) {
    arg2 = 0;  // Resets arg2 to 0 indicating successful validation
}
std::string::~string(&var_48);  // Destructs var_48 to free memory

// Return Validation Result
return arg2;  // Returns arg2 as the validation result
```
Here in this function, we have few unknown data which can be seen on the decompiler and these are the hidden data string which is constructing the password.

<img width="480" alt="Screenshot 2024-07-10 at 12 57 53 PM" src="https://github.com/Anjalihere/CSOC_24/assets/146505430/e60ecef6-2aeb-43f7-bcf6-85ddc2a5d658">

```
data_2005: 64 65 63 00 dec.
data_2009: 6b 00 k.
data_200b: 63 61 72 00 car.
```
The `checkPassword` functions compares the length of the user-input string (arg1) with the negative of a predefined negative value (-7). 
If the lengths match, `var_48` is constructed by appending 'd' and 'c', followed by 'k' and 'car', forming the string `dekcarc`. This constructed string is then compared with the user-input string after it has been reversed and hence becomes `cracked` which is the password.


# Chall_3
# Chall_4
Ghidra gives reveals these two functions- `Entry` and `verify` function.

```cpp
void processEntry entry(void)

{
  uchar *in_RCX;
  size_t siglen;
  size_t siglen_00;
  size_t siglen_01;
  uchar *sig;
  EVP_PKEY_CTX *ctx;
  size_t in_R8;
  long in_R13;
  long in_R15;
  
  syscall();
  ctx = (EVP_PKEY_CTX *)0x0;
  sig = &password;
  syscall();
  _verify((EVP_PKEY_CTX *)0x0,&password,0x10,in_RCX,in_R8);
  _verify(ctx,sig,siglen,in_RCX,in_R8);
  _verify(ctx,sig,siglen_00,in_RCX,in_R8);
  _verify(ctx,sig,siglen_01,in_RCX,in_R8);
  if ((in_R13 == 0x42e) && (in_R15 + 0xb == in_R15)) {
    _correct();
  }
                    // WARNING: Subroutine does not return
  _incorrect();
}
```
**processEntry function**

* It initializes some variables (`ctx` and `sig`) and calls `_verify` 4 times with different parameters.
* It performs conditional checks (if statement) using parameters `in_R13` and `in_R15` `(in_R13 == 0x42e and in_R15 + 0xb == in_R15)` but the disassembly says different. It tells `in_R13 == 0x42e and in_R12 + 0xb == in_R15` which also makes more sense than former.
* Depending on the conditional check, it either calls _correct (for success) or _incorrect (for failure).

<img width="216" alt="Screenshot 2024-07-10 at 11 16 50 PM" src="https://github.com/Anjalihere/CSOC_24/assets/146505430/d58c38ff-6aa7-4d5e-93cb-d5ed10de9bbe">

```cpp
int _verify(EVP_PKEY_CTX *ctx,uchar *sig,size_t siglen,uchar *tbs,size_t tbslen)

{
  int in_EAX;
  long lVar1;
  
  lVar1 = 0;
  do {
    lVar1 = lVar1 + 1;
    in_EAX = in_EAX + 1;
  } while (lVar1 != 4);
  return in_EAX;
}
```
**_verify function**

* This function takes several parameters: `ctx` (EVP_PKEY_CTX pointer), `sig` (uchar pointer), `siglen` (size_t), `tbs` (uchar pointer), and `tbslen` (size_t).
* It initializes a loop counter `lVar1` and iterates 4 times.
* Inside the loop, it increments lVar1 and `in_EAX`.
* After the loop, it returns the value of in_EAX, which is always `4` in this case.

Hmmm...this provided code doesn't give much information about the password. Let's look at the disassembly. Starting with `entry` function since not much happening in `verify` function.

```
00401000  mov     eax, 0x1
00401005  mov     edi, 0x1
0040100a  mov     rsi, question  {"Enter your password: Wrong passw…"}
00401014  mov     edx, 0x15
00401019  syscall 
0040101b  mov     eax, 0x0
00401020  mov     edi, 0x0
00401025  mov     rsi, password
0040102f  mov     edx, 0x10
00401034  syscall
```
The program prints `Enter your password` using the sys_write syscall. It then reads up to `16 characters` of user input into the password buffer using the sys_read syscall. 

**First Call to verify**
```
00401036  mov     rax, password
00401040  call    _verify
00401045  mov     r12, r15
```
* The password is moved to `RAX` and passed to the `verify` function.
* The result from verify is stored in `R15` and then copied to `R12`.

**Second Call to verify**
```
00401048  mov     rax, data_402040
00401052  call    _verify
00401057  cmp     r12, r15
0040105a  jne     _jmpwrong
```

* The value at `data_402040` is moved to RAX and passed to the verify function.
* The result is compared with the previously stored value in `R12`. If they are not equal, the program jumps to _jmpwrong (indicating a wrong password).

**Third Call to verify**
```
0040105c  mov     rax, data_40203c
00401066  call    _verify
0040106b  mov     r14, r15
```
* The value at `data_40203c` is moved to `RAX` and passed to the verify function.
* The result is stored in `R15` and then copied to `R14`.
  
**Fourth Call to verify**
```
0040106e  mov     rax, data_402044
00401078  call    _verify
0040107d  cmp     r14, r15
00401080  jne     _jmpwrong
```
* The value at `data_402044` is moved to RAX and passed to the verify function.
* The result is compared with the previously stored value in R14. If they are not equal, the program jumps to _jmpwrong (indicating a wrong password).

**Final Checks**
```
00401082  cmp     r13, 0x42e
00401089  jne     _jmpwrong
0040108b  add     r12, 0xb
0040108f  cmp     r12, r15
00401092  jne     _jmpwrong
```
* The value in `R13` is compared with `0x42e`(1070). If they are not equal, the program jumps to _jmpwrong.
* `R12` is incremented by `11`(0xb) and compared with `R15`. If they are not equal, the program jumps to `_jmpwrong`.

**Password Determination**

Given the results from the verify function and the comparisons in _start, we can deduce:

###### Comparing R12 and R15 after the first verify call:

The value at data_402040 must produce the same result as the password in the first 4 bytes i.e., bytes at position `[0, 3]` must be equal to bytes at position `[8,11]`.

###### Comparing R14 and R15 after the third and fourth verify calls:

The values at data_40203c and data_402044 must match in terms of their result from verify i.e., ytes at position `[4, 7]` must be equal to bytes at position `[12,15]`.

###### Final Check Comparisons:

* The `R13` value must be 0x42e (1070)
* `R12` (which is 4) incremented by 11 must be equal to `R15` (which is also 4), meaning `4 + 11 = 15` and `R15 = 15`.

Here is the keygen script:

```python
import string
import random

def generate_keygen():
    # Generate two pairs of characters
    pair1 = random.choice(string.ascii_letters)   # First character for both pairs
    pair2 = random.choice(string.ascii_letters)   # Second character for both pairs
    
    # Create the password based on the given conditions
    password = [pair1]*4 + [pair2]*4 + [pair1]*4 + [pair2]*4
    
    return ''.join(password)

# Generate and print the keygen
keygen = generate_keygen()
print("Generated keygen:", keygen)
```
This will generate a lot of passwords. I will use `eeeeNNNNeeeeNNNN`

# Chall_5
> Password: 0xJam3z
>

The challenge seems pretty complicated but its really easy if we observe patiently. When we execute `strings chall_5` we can find the password string somewhere in the beginning. But, for the sake of difficulty of challenge, let's get to the low-level of program.

<img width="263" alt="Screenshot 2024-07-10 at 7 00 52 PM" src="https://github.com/Anjalihere/CSOC_24/assets/146505430/a90a1b5e-fb4e-484c-b34f-22778d74b903">

Putting the program in `Binary Ninjas`, these two important functions can be found - `obfuscatePassword` and `main` function.

```cpp
char* obfuscatePassword(char* arg1)
{
    // Initialize variables
    void var_39;
    void* var_38 = &var_39;

    // Initialize string with "0xJam3z"
    std::string::string<std::allocator<char>>(arg1, "0xJam3z", rsi);

    // XOR obfuscation with 0x6d
    char var_19 = 0x6d;
    int64_t var_48 = std::string::begin();
    int64_t var_50 = std::string::end();
    while (true) {
        if (operator!=<char*, std::string>(&var_48, &var_50) == 0)
            break;
        
        // XOR each character with 0x6d
        char* rax_6 = __normal_iterator<char*, std::string>::operator*(&var_48);
        *rax_6 = *rax_6 ^ 0x6d;
        __normal_iterator<char*, std::string>::operator++(&var_48);
    }

    return arg1;
}
```
This `obfuscatePassword` function takes a character array `arg1` as input, initializes it with the string `0xJam3z`, and then obfuscates each character in arg1 by `XORing` it with `0x6d`('m').

```cpp
__main()
{
    // Initialize variables
    void var_58;
    obfuscatePassword(&var_58);  // Obfuscate user input

    // Output prompt and read user input
    std::cout << "Enter the password: ";
    void var_78;
    std::cin >> &var_78;

    // Initialize another string (var_98) with user input
    void var_98;
    std::string::string(&var_98, &var_78);

// XOR obfuscation of user input
char var_19 = 0x6d;                      // Initialize var_19 with 0x6d (which is 109 in decimal, 'm' in ASCII)
void* var_28 = &var_98;                  // var_28 points to the memory address of var_98 (presumably a std::string)
int64_t var_a0 = std::string::begin(&var_98); // var_a0 is the beginning iterator of std::string var_98
int64_t var_a8 = std::string::end(&var_98);   // var_a8 is the end iterator of std::string var_98

// Iterate over the string var_98
while (true) {
    // Check if the current iterator var_a0 is equal to the end iterator var_a8
    if (operator!=<char*, std::string>(&var_a0, &var_a8) == 0)
        break; // Exit the loop if iterators are equal
    
    // Dereference the iterator var_a0 to get the current character pointer rax_4
    char* rax_4 = __normal_iterator<char*, std::string>::operator*(&var_a0);
    
    // XOR the current character pointed by rax_4 with var_19 (0x6d)
    *rax_4 = *rax_4 ^ 0x6d;
    
    // Move to the next character in the string by incrementing the iterator var_a0
    __normal_iterator<char*, std::string>::operator++(&var_a0);
}

```
The `main` function begins by obfuscating user input using the obfuscatePassword function. It then prompts the user to enter a password, reads it, and stores it in `var_78`. This input is subsequently copied to `var_98` and obfuscated similarly to the predefined string **0xJam3z**. After obfuscation, it checks if the obfuscated input matches **0xJam3z**.

If the input matches **0xJam3z**, it prints **Correct** and executes a command (e.g., opening a calculator using system(_Command: `calc`)) otherwise prints **Incorrect**.

Therefore, our superhidden password is `0xJam3z`

