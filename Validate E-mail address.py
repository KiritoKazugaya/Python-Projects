email = input (" Enter your Email : ")
#min criteria is a@a.in and the min length is therefore 6 characters atleast
def error():
    print("You have entered wrong email!")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha(): #checks for alphabets
        if "@ in email" and (email.count("@") == 1):
            if(email[-4]==".") ^ (email[-3]=="."): #XOR operator gives true for atleast 1 true
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    error()
                else:
                    error()
            else :
                error()
        else:
            error()
    else:
        error()
else:
    error()

