'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

S=input()
S1=[*S]
for i in range(2):
    S1.pop()
S1="".join(reversed(S1))
S1=S1.replace('h','n')
print(S1)
