import turtle 
import pandas as pd

states = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)



i = 0
writnig_turtle = turtle.Turtle()
writnig_turtle.penup()
writnig_turtle.hideturtle()

guess_state = []

while i < 50:

    ask_state = screen.textinput(title = f'States correct {i}/50', prompt = "What's another state")
    ask_state = ask_state.title()

    if ask_state == 'Exit':
        break

    if ask_state in states['state'].to_list():
        guess_state.append(ask_state)
        x = states[states['state'] == ask_state]['x'].values[0]
        y = states[states['state'] == ask_state]['y'].values[0]
        print(f'x =  {x }, y =   {y}')
        writnig_turtle.goto(x, y)
        writnig_turtle.write(ask_state, align = 'center')
        i += 1



states_to_learn = set(states['state'].to_list()).difference(set(guess_state))

screen.exitonclick()
















turtle.mainloop()


