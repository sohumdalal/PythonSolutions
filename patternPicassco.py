stars = int(input("Enter the size of your square: "))  # Convert input to integer
height_count = 0
while height_count < stars:
    row_count = 0
    line = ""  
    while row_count < stars:  
      line += "*"
      row_count += 1
    print(line) 
    height_count += 1
    
triangleLength = int(input("Enter the size of your triangle: "))  # Convert input to integer
triangleCount = 0
triangle = ""
while triangleCount < triangleLength:
  triangle += "*"
  triangleCount += 1
  print (triangle);

pyramidLength = int(input("Enter the size of your pyramid: "))  # Convert input to integer
for x in range(1, pyramidLength + 1):
  if(x % 2 == 1):
    spaces = (pyramidLength - x) // 2  
    stars = "*" * x 
    print(" " * spaces + stars)
    
diamondLength = int(input("Enter the size of your diamond: "))  # Convert input to integer
for x in range(1, diamondLength + 1):
  if(x % 2 == 1):
    spaces = (diamondLength - x) // 2  
    stars = "*" * x 
    print(" " * spaces + stars)
for y in range(diamondLength - 1, 0, - 1):
  if(y % 2 == 1):
    spaces = (diamondLength - y) // 2  
    stars = "*" * y
    print(" " * spaces + stars)
