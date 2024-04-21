
n = int(input("Enter the no of the sides of the polygon : ")) 
  
l = int(input("Enter the length of the sides of the polygon : ")) 
import turtle 
  
t = turtle.Turtle() 
  

  
  
for i in range(n): 
    turtle.forward(l) 
    turtle.right(360 / n)
turtle.mainloop()