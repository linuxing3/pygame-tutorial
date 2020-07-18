
# math for pygame

## rotate

```python
# Import math Library
import math

# Return the arc tangent of y/x in radians
arc = math.atan2(2, 2)
print(arc) 

angle =  360 - arc * 180 / math.pi
print(angle)

print (math.sin(arc))
print (math.cos(arc))

```

```txt
0.7853981633974483
315.0
0.7071067811865475
0.7071067811865476
```