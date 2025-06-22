class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for store in range(1,n+1):
            if(store%3 == 0) and (store%5== 0):
                answer.append("FizzBuzz")
            elif store%3==0:
                answer.append("Fizz")
            elif store%5 ==0:
                answer.append("Buzz")
            else:
                answer.append(str(store))
        return answer
