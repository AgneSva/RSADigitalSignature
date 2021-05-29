from tkinter import *
from tkinter import ttk
import math
from binascii import hexlify, unhexlify
import random
# ----------FUNCTIONS----------




def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def inverse(e, phi):
    a, b, u = 0, phi, 1
    while(e > 0):
        q = b // e
        e, a, b, u = b % e, u, e, a-q*u
    if (b == 1):
        return a % phi
    else:
        print("Must be coprime!")

def generate_keypair(p, q):
 
    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key

    d = inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)

    return ((e, n), (d, n))





def generate():
    # p,q primes
    p = 823
    q = 953
    public, private = generate_keypair(p, q)
    e,n=public
    d,n=private

    #public key into file
    with open('data.txt', 'w') as f:
            f.write(str(public))


    SecondEntry.delete(0,'end')
    ThirdEntry.delete(0,'end')
    
    M=FirstEntry.get()
    M=  [ord(character) for character in M]

    
    #send over M
    ThirdEntry.insert(0,str(M))
   
    #generating signature
    S=[]
    for M in M:
     S.append( (M**d) % n)

    #send over S
    SecondEntry.insert(0,str(S))



def validate():
    M=FirstEntry.get()
    M=  [ord(character) for character in M]
    #get public key
    with open('data.txt', 'r') as f:
            public = f.read()

#convert to tuple
    ts=eval(public)
    e = int(ts[0])
    n = int(ts[1])
    

    S=SecondEntry.get()
    print("s=", S)
    S=eval(S)

    M1=[]

    for S in S:
     M1.append( (S**e) % n)


    ThirdEntry.delete(0,'end')
    ThirdEntry.insert(0,M1)
    print(M, M1)

    if M==M1:
        rez.set("parasas patvirtintas!") 
    else:
        rez.set("parasas nepatvirtintas!")



    







# ------------GUI--------
# main screen
master = Tk()
master.title('RSA DIGITAL SIGNATURE')
option = StringVar()
mode1 = StringVar()
k = StringVar()

# first field:
Label(master, text="(Pirmas laukas) x=", font=(
    "Arial", 15)).grid(row=2, sticky=W, padx=5)
FirstEntry = Entry(master)
FirstEntry.grid(row=2, column=1)

# button generate signature
button1 = Button(master, text='generuoti', width=8, command=generate)
button1.grid(row=3, column=1)

# second:
Label(master, text="(Antras laukas) s=", font=(
    "Arial", 15)).grid(row=4, sticky=W, padx=5)
SecondEntry = Entry(master)
SecondEntry.grid(row=4, column=1)


# third:
Label(master, text="(Trecias laukas) x'=", font=(
    "Arial", 15)).grid(row=6, sticky=W, padx=5)
ThirdEntry = Entry(master)
ThirdEntry.grid(row=6, column=1)

# button to get result
button3 = Button(master, text='patvirtinti', width=8, command=validate)
button3.grid(row=7, column=1)

# rezultatas:
rez=StringVar()
Label(master, textvariable= rez,text="Rezultatas", font=(
    "Arial", 12)).grid(row=8, sticky=W, padx=5)




# size of the page
master.geometry('400x400')
master.mainloop()
