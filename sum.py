class Sum:
  
    def __init__(self, lst, target):
        self.lst = lst
        self.target = target

    def getSum(self):
        seen = set()
        result = []

        for num in self.lst:
            complement = self.target - num

            if complement in seen:
                result.append([complement, num])

            seen.add(num)

        return result


target = 9
lst = [2, 5, 7, 4, 8, 9]

s = Sum(lst, target)
print(s.getSum())