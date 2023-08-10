from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle win the race? Enter a colour: ?")
turtle_colour = ["red", "green", "black", "blue", "pink", "silver"]
y_position = [-70, -40, -10, 20, 50, 80]
is_race_on = False
turtles = []

for turtle in range(len(turtle_colour)):
    turtle_obj = Turtle(shape="turtle")
    turtle_obj.color(turtle_colour[turtle])
    turtles.append(turtle_obj)
    turtle_obj.penup()
    turtle_obj.goto(x=-230, y=y_position[turtle])


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_obj_single in turtles:
        if turtle_obj_single.xcor() > 230:
            is_race_on = False
            winning_colour = turtle_obj_single.pencolor()
            if winning_colour == user_bet:
                print(f"you won !! winning turtle colour is {winning_colour}")
            else:
                print(f"you loose and winning turtle colour is {winning_colour}")

        random_distance = random.randint(0, 10)
        turtle_obj_single.forward(random_distance)


screen.exitonclick()


