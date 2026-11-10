# Solution 1 to count Digits in number
class CountDigits:

    def __init__(self, number):
        self.number = number

    def count(self):
        num = self.number
        count = 0
        while num > 0:
            num = num // 10 
            count = count + 1
        return count

one = CountDigits(12345)
print(one.count())


#Soiution 2 to count Digits in number
class CountDigits2:

    def __init__(self, number):
        self.number = number

    def count(self):
        count = len(str(self.number))
        return count


two = CountDigits2(3456789)
print(two.count())


