import turtle

t = turtle.Turtle()
t.screen.bgcolor("black")
t.pensize(2)
t.color("green")
t.left(90)
t.backward(60)
t.speed("fastest")
t.shape("circle")

def tree(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.color("purple")
        t.begin_fill()  
        t.circle(3)     
        t.end_fill()    
        t.color("green")
        t.left(30)
        tree(3 * i / 4)
        t.right(60)
        tree(3 * i / 4)
        t.left(30)
        t.backward(i)

# เรียกใช้ฟังก์ชันวาดต้นไม้
tree(60)
turtle.done()
