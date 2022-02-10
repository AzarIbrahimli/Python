def encrypt(message, step): 
    new=""
    a=0
    length=len(alphabet)
    for letter in message:
        not_included=True
        if step>=length:
            step=step-length   
        for i in range(length):    # i= number of letter 
            if letter==alphabet[i]:
                if (i+step)>=length:
                    a=(i+step)-length
                    new+=alphabet[a]                
                    not_included=False
                else:
                    not_included=False                    
                    new+=alphabet[i+step]
        if not_included==True:
            new+=letter
    print(f"The ended code is {new}")

def decrypt(message,step):
    new=""
    for letter in message:
        if (letter in alphabet):
            position=alphabet.index(letter)
            if position-step<0:
                position=26-(step-position)
                new+=alphabet[position]                
            else: 
                new+=alphabet[position-step]
        else:
            new+=letter
    print(f"The ended code is {new}")  

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction=="encode":
    encrypt(message=text,step=shift)
elif direction=="decode":
    decrypt(message=text,step=shift)
else:
    print("Again please")
