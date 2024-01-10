import random


def gameWin(comp,you):
    if comp== "s" and you== "p":
        return False
    if comp== "p" and you== "s":
        return True
    if comp== "r" and you== "p":
        return True
    if comp==you:
        return None
    if comp== "p" and you== "r":
        return False
    if comp== "r" and you== "s":
        return False
    if comp== "s" and you== "r":
        return True

print("Computer Turn: Rock(r) Paper(p) or Scissor(s)?")
RandomInput= random.randint(1,3)
if RandomInput==1:
    comp = "p"
elif RandomInput==2:
    comp = "r"
elif RandomInput== 3:
    comp= "s"  
you= input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")
a= gameWin(comp,you)    
print(f"computer choose {comp}")
if a==None:
    print("This is a tie")
elif a:
    print("Congratulations, You win!!")    
else:
    print("Sorry, You loose")    


