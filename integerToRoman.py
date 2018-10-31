def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    digits = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    denos = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    value_in_roman = ''
    for key, value in zip (denos, digits):
        while num >= key:
            num = num-key
            value_in_roman = value_in_roman+value
    return value_in_roman

print(intToRoman(1994))
