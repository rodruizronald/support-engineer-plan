# Week 2 — Answers: Binary, Bytes, and How Data Is Represented

Answer each question below in your own words. Don't copy-paste definitions — explain them as if to a friend.

## Part A — Bits, bytes, and the number bases

### Q1. What is a bit and what is a byte? Why is a byte 8 bits, and how many distinct values can one byte represent?

_Your answer:A computer is made of millions of tiny switches called transistors. Since each switch can only have two states (on or off), the computer represents those states with 0 and 1. Each of those values is called a bit. Because a single bit can store very little information, eight bits are grouped together to form a byte, which can represent 256 different values._

### Q2. What does the "base" of a number system mean? Explain binary, decimal, and hex. Why do programmers lean on hex, and why does one byte fit in exactly two hex digits?

_Your answer: The base of a number system is the number of different symbols that can be used to write numbers. We use the decimal system (base 10) because it has ten symbols (0 through 9) Computers use binary system (base2) because their transistor can only be on or off, wich are represented as 1 and 0. Programmers use the hexadecimal system (base 16) because it is a shorter and easier way to read binary numbers. Instead of writing long sequences of zeros and ones, they can use the numbers 0–9 and the letters A–F. One byte has 8 bits and can be divided into two groups of 4 bits. Since each group of 4 bits has 16 possible combinations, each group can be represented by a single hexadecimal digit. That is why one byte is always represented by two hexadecimal digits._ 
### Q3. How is a whole number stored in a fixed number of bits? Signed vs unsigned, and what is overflow / wraparound? Give a real example of a counter or timestamp that overflowed.

_Your answer:Whole numbers are stored in binary using a fixed number of bits, such as 8, 16, 32, or 64. Each bit can only contain a 0 or a 1, and a number is represented by combining those bits. Counting works similarly to the decimal system, but using only two values. The system always adds 1 to the rightmost bit; if that bit is already 1, it changes back to 0 and carries 1 to the bit on the left. For example, with 2 bits the sequence is 00 = 0, 01 = 1, 10 = 2, and 11 = 3. If you add 1 to 11, it becomes 00 because there is no more space to store a larger value. This is called overflow or wraparound. Unsigned numbers can only represent positive values, while signed numbers use some of the available bit combinations to represent negative values, so they have a smaller positive range._ 
_A real example of overflow is the Year 2038 problem, where some systems that store time as a signed 32-bit integer will reach their maximum value and the counter will overflow._

### Q4. How does a computer store "A", "é", and an emoji? Explain ASCII vs Unicode vs an encoding like UTF-8. Why is one character not the same as one byte?

_Your answer:A computer does not store letters directly. Instead, it stores numbers that represent each character. ASCII was an early standard that assigned numbers to common letters and symbols, but it mainly supported English characters. Later, Unicode was created to assign a unique number to characters from all languages, including emojis. UTF-8 is an encoding that converts Unicode characters into bytes so they can be stored in files or sent over the Internet. One character is not always one byte because, in UTF-8, some characters use 1 byte, while others use 2, 3, or even 4 bytes._

### Q5. KB vs KiB (and MB vs MiB): why does a "1 TB" drive show as ~931 GB? Bits vs bytes: why does a "100 Mbps" connection download at ~12 MB/s?

_Your answer:The difference between KB and KiB is that KB uses multiples of 1,000 bytes, while KiB uses multiples of 1,024 bytes, which is how computers work internally. That is why a drive sold as 1 TB appears as about 931 GiB in the operating system. Both show the same number of bytes, but they group them differently. Also,, one byte is made up of 8 bits. Internet providers advertise speed in megabits per second (Mbps), while downloads are usually shown in megabytes per second (MB/s). That is why a 100 Mbps connection downloads at about 12.5 MB/s, because you divide by 8._

## Part B — How Python represents that data

### Q6. In Python, what's the difference between a `str` and a `bytes`? When you save text to a file or send it over a network, which one travels, and what step converts between them?

_Your answer:In Python, a str represents text, while a bytes object represents data in the format that a computer can store or transmit. When we save text to a file or send it over the Internet, what is actually stored or transmitted is bytes. To convert a str into bytes, we use the .encode() method. To convert bytes back into text, we use .decode(). These processes allow text to be stored correctly and later read again._

### Q7. What is a `UnicodeDecodeError`, and in terms of encodings what has gone wrong? Why can the same file open fine in one program and show mojibake in another?

_Your answer: A UnicodeDecodeError happens when Python tries to convert bytes into text using the wrong encoding and cannot interpret them correctly. The problem is not with the bytes themselves, but with the fact that they are being read using the wrong rules. Sometimes an error is not raised, but strange characters such as cafÃ© appear instead. This is known as mojibake._

### Q8. Why does `0.1 + 0.2` not equal `0.3`? In terms of bits, what can't a float represent exactly, and why should you never store money as a float?

_Your answer:0.1 + 0.2 does not equal exactly 0.3 because floating-point numbers (float) are stored in binary using a limited number of bits. Some decimal numbers, such as 0.1, cannot be represented exactly in binary, so they are stored as approximations. When calculations are performed using these approximations, small errors can appear, such as 0.30000000000000004. For this reason, float should not be used to represent money. Instead, Python provides Decimal, which stores decimal values more accurately._

### Q9. Where have you seen hex (pick two: memory addresses, color codes, bytes in a log, error codes)? What do the digits mean there, and how do you convert a hex string to a number and back?

_Your answer:I had not really paid attention to it before, but I learned that hexadecimal is commonly used in color codes. The hexadecimal system uses the numbers 0–9 and the letters A–F, where A represents 10 and F represents 15. In Python, you can convert a decimal number to hexadecimal using hex(), and you can convert a hexadecimal number back to decimal using int(value, 16)._

### Q10. (Tie-back to Week 1.) A 4-byte integer and a 1000-character UTF-8 string both live in RAM and may hit disk or the network. Using the latency hierarchy, why does knowing the byte size of your data matter for all three components?

_Your answer:The size of data in bytes is important because it determines how much RAM is needed and how long it takes to read data from the disk or send it over the network. A 4-byte integer takes up very little space and can be moved quickly, while a 1,000-character string uses many more bytes and takes longer to store or transmit. Since RAM, disk, and the network all operate at different speeds, moving a larger amount of data makes these operations slower._
