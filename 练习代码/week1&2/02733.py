a=int(input('What is the year'))
if a%4==0:
    if a%100==0:
        if a%400==0:
            #if a%3200==0:   cheat:3200>3000
            #    print('N')
            #else:
                print('Y')
        else:
            print('N')
    else:
        print('Y')
else:
    print('N')