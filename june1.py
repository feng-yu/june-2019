"""
[Medium]
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

Solution:

For example, consider a quadrant (circular sector) inscribed in a unit square. Given that the ratio of their areas is
π/4, the value of π can be approximated using a Monte Carlo method:[11]

Draw a square, then inscribe a quadrant within it
Uniformly scatter a given number of points over the square
Count the number of points inside the quadrant, i.e. having a distance from the origin of less than 1
The ratio of the inside-count and the total-sample-count is an estimate of the ratio of the two areas,
π/4. Multiply the result by 4 to estimate π.
"""
import random

def find_pi(N):
    in_circle_count = 0;
    for _ in range(N):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1:
            in_circle_count += 1
    pi = in_circle_count * 1000 // N * 4 / 1000  #Estimate π to 3 decimal places
    return pi


def main():
    for _ in range(20):
        N = 500000
        pi = find_pi(N)
        print(pi)

main()
