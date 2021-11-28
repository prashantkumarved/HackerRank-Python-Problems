import math
AB = int(input())
BC = int(input())
X = (AB/BC)
angleC = math.atan(X)  # angleC = angle MBC , because midpoint on hypotenuse divides
# right angle into two isosceles traingle, such that AM = MC = BM
print(str(round(math.degrees(angleC)))+chr(176))
