c,n,h,f,a=0,0,0,0,0
while(c<200):    
    print("1. Nikhil")
    print("2. Armaan")
    print("3. Faisal")
    print("4. Hasnain")
    print("5. Results")
    print("6. Exit")
    ch=int(input("Enter your vote: "))
    if ch==1:
        print("Thanks for your vote!")
        n+=1
    elif ch==2:
        print("Thanks for your vote!")
        a+=1
    elif ch==3:
        print("Thanks for your vote!")
        f+=1
    elif ch==4:
        print("Thanks for your vote!")
        h+=1
    elif ch==5:
        if n>a and n>f and n>h:
            print(f"The winner is Nikhil with {n} votes!")
            break
        elif (a>n) and (a>f) and (a>h):
            print(f"The winner is Armaan with {a} votes!")
            break
        elif (f>a) and (f>n) and (f>h):
            print(f"The winner is Faisal with {f} votes!")
            break
        else:
            print(f"The winner is Hasnain with {h} votes!")
            break
    elif ch==6:
        print("Exiting...")
        exit()
        break
    else:
        print("Enter a valid choice")
    c+=1
