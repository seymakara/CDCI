class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0

        primes = n * [True]
        primes[0] = primes[1] = False

        for i in range(4, n): #check each number if it is divided by the numbers until its half.Yarisina kadar tam bolunmediyse ondan sonra zaten bolunmez.
            for j in range(2, i//2 + 1): # +1 4 icin cunku 2 den 2 ye kadar olamaz, inclusive degil.
                if i%j == 0:
                    primes[i] = False
        return sum(primes) 
        
        # ------FASTER SOLUTION------
        if n < 2:
            return 0

        primes = n * [True]

        for i in range(2, int(n ** 0.5) + 1): # karekokunden sonrasini kontrol etmeye gerek yok. https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
            if primes[i]:
                for j in range( i ** 2, n, i): #sayinin karesinden itibaren kontrol etmeye basliyoruz cunku, oraya kadar olan kismi bu onceki sayilarin carpanlari cover ediyor. i 2 den basliyor, dolayisiyla j 2ser, 3er .. articak.
                    primes[j] = False
        return sum(primes) -2 # 0 and 1 are not prime numbers.

