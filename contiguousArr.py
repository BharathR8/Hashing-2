class Problem_2:
    def EqualNumbersCount(self, arr):
        maxLength = 0
        zero = 0
        NumberIndexMap = dict()

        for index, val in enumerate(arr):

            if val == 1:
                zero += 1

            else:
                zero -= 1

            if zero == 0:
                maxLength = index + 1

            if zero in NumberIndexMap:
                if maxLength < index - NumberIndexMap[zero]:
                    maxLength = index - NumberIndexMap[zero]

            else:
                NumberIndexMap[zero] = index

        return maxLength
    
res = [1, 1, 1, 1, 0, 1, 0, 1, 0, 0]   
solution = Problem_2()
output = solution.EqualNumbersCount(res)
print(output)