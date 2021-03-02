# Title: Mr.A
# Hint: Xor might be useful
# The idea of this challenge is to use the XOR operator in each of the numbers with ord(A)

text = """14, 36, 42, 97, 53, 56, 53, 97, 40, 36, 97, 44, 52, 35, 35, 96, 97, 54, 
36, 36, 53, 97, 59, 36, 51, 96, 97, 56, 37, 55, 58, 11, 25, 16, 11, 102, 8, 
30, 12, 25, 16, 11, 30, 16, 2, 30, 11, 16, 3, 0, 24, 5, 22, 30, 16, 19, 4, 10, 11, 96, 96, 60"""

output = ""
xoring_value = ord('A')
for i in text.split(", "):
    output += chr(int(i) ^ xoring_value)
print(output)

# Oek tyt ie mubb! weet zer! ydv{JXQJ'I_MXQJ_QC_JQBAYDW_QREKJ!!}
# Then decoding it with caesar cipher

# You did so well! good job! inf{THAT'S_WHAT_AM_TALKING_ABOUT!!}
