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