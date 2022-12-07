import turtle
import pandas


image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. State Game")
screen.setup(700, 700)
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed correctly.",
                                    prompt="Type names here.(Type Exit to end the game)").title()
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
print(missing_states)

turtle.mainloop()