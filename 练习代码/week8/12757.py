number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninty': 90}
times = {'hundred': 100, 'thousand': 1000, 'million': 1000000}

def pro(string): 
    num = 0
    res = 0
    for ele in string:
        if ele in ['thousand', 'million']:
            res += num*times[ele]
            num = 0
        elif ele == 'hundred':
            num *= 100
        else:
            num += number[ele]
    return res + num

word = list(input().split())
if word[0] == 'negative':
    del word[0]
    print(- pro(word))
else:
    print(pro(word))