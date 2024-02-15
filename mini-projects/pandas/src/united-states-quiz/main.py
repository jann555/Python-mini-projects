import turtle
from types import NoneType

import pandas as pd

screen = turtle.Screen()
screen.title("United States Game")

image = "../../resources/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# Load csv
states_data = pd.read_csv('../../resources/50_states.csv')
all_states = states_data.state.to_list()


def get_mouse_click_coor(x, y):
    print(x, y)


def set_state_name(state_data):
    name = turtle.Turtle()
    name.color("black")
    name.penup()
    name.hideturtle()
    name.goto(state_data.x.item(), state_data.y.item())
    name.write(f"{state_data.state.item()}", align="center", font=("Courier", 8, "normal"))


game_on = True
guesses = 0
correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f'{len(correct_answers)}/50 States Correct', prompt="What's another state "
                                                                                              "name?")
    if type(answer_state) is not NoneType:
        answer_state = answer_state.title()
        if answer_state in all_states:
            state_row = states_data[states_data.state == answer_state]
            set_state_name(state_row)
            correct_answers.append(answer_state)
            guesses += 1
        elif answer_state == "Exit":
            # Create States to learn
            missing_states = [state for state in all_states if state not in correct_answers]
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv('../../resources/states_to_learn.csv')
            print(missing_states)
            break

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
