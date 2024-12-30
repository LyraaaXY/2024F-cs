habb = {'pop':1, 'no':2, 'zip':3, 'zotz':4, 'tzec':5, 'xul':6, 'yoxkin':7, 'mol':8, 'chen':9, 'yax':10, 'zac':11, 'ceh':12, 'mac':13, 'kankin':14, 'muan':15, 'pax':16, 'koyab':17, 'cumhu':18, 'uayet':19}
holly = {1:'imix', 2:'ik', 3:'akbal', 4:'kan', 5:'chicchan', 6:'cimi', 7:'manik', 8:'lamat', 9:'muluk', 10:'ok', 11:'chuen', 12:'eb', 13:'ben', 14:'ix', 15:'mem', 16:'cib', 17:'caban', 18:'eznab', 19:'canac', 0:'ahau'}

n = int(input())
print(n)
for i in range(n):
    d, m, y = input().split()
    day, month, year = int(d.replace('.', '')) + 1, habb[m], int(y)
    date = day + (month - 1)*20 + year*365
    Year = date//260
    if date%260 == 0:
        Year -= 1
    if date% 13 == 0:
        print('13 ' + holly[date%20] + ' ' + str(Year))
    else:
        print(str(date%13) + ' ' + holly[date%20] + ' ' + str(Year))