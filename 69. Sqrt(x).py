# Sqrt(x).py
class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 0:
            raise ValueError("Cannot calculate the square root of a negative number")
        if x == 0:
            return 0

        guess = x / 2.0
        epsilon = 0.000001

        while abs(guess * guess - x) > epsilon:
            guess = (guess + x / guess) / 2.0

        return int(guess // 1 )   
