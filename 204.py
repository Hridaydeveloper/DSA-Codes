class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        else:
            prime = [True] * (n + 1)

            prime[0] = False
            prime[1] = False

            p = 2

            while p*p <= n:
                if prime[p]:

                    for mul in range(p*p, n + 1, p):
                        prime[mul] = False
                p += 1
            count = 0
            for i in range(2, n):
                if prime[i]:
                    count += 1
        return count



        
