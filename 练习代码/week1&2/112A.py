#prepare for string_1
string_1 = input().lower()
split_1 = list(string_1)
ascii_1 = [ord(char) for char in split_1 ]

#prepare for string_2
string_2 = input().lower()
split_2 = list(string_2)
ascii_2 = [ord(char) for char in split_2 ]
num=0

#compare
for i in range(len(string_1)):
    if ascii_1[i] < ascii_2[i]:
        print('-1')
        break
    elif ascii_1[i] > ascii_2[i]:
        print('1')
        break
    else:
        num += 1

if num == len(string_1):
    print('0')

#or you can compare directly ---official
#line1 = input()
#line2 = input() 
#if line1.lower() > line2.lower(): 
#    print(1) 
#elif line1.lower() < line2.lower(): 
#    print(-1) 
#else: 
#    print(0)