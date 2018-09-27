from random import getrandbits
def makeBiasedCoin(odds):
    # binary expansion of 1/3 is 0.0101010101....
    # To obtain a random boolean with half probability of true and half probability of false
    #         b = bool(getrandbits(1))
    # Your code here
    odds_bits = odds
    count = 0
    for bit in odds_bits:
        count = count + 1
        if getrandbits(1) != bit:
            return {'result':bool(bit), 'tosses':count}
    return {'result':False, 'tosses':count}

def generateBinaryDigits(num):
    binary = list()
    max_iter = 0
    while num != 0.0 and max_iter < 30:
        num = num*2
        binary.append(int(num))
        num = num%1
        max_iter = max_iter+1
    return binary

count=0
t = 0
nTrials = 5000000
odds_bits = generateBinaryDigits(21/64)
print(odds_bits)
tosses = list()
for i in range(nTrials):
    coin = makeBiasedCoin(odds_bits)
    print(i)
    tosses.append(coin['tosses'])
    if coin['result']:
        count = count + 1
print('Count = ', count, ' probability est = ', count/nTrials, 'Tosses = ', sum(tosses)/len(tosses))
