from turtle import Turtle, Screen
import pandas
from turtle_name import StateName

screen = Screen()

# screen.title("U.S. States Game")
screen.bgpic('blank_states_img.gif')

# How to get the coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
guessed_states = []
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

while len(guessed_states) < len(all_states):
    curr_state = screen.textinput(title=f"Correct Ans. : {len(guessed_states)}/{len(all_states)}",
                                  prompt="What's another name of the State ?").title().strip()
    # missing_state = []
    if curr_state == 'Exit':
        missing_state = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv('states_to_learn.csv')
        break
    if curr_state in all_states:
        guessed_states.append(curr_state)
        state_data = data[data.state == curr_state]
        x_cord = int(state_data.x)
        y_cord = int(state_data.y)
        # print(type(state_data.state), x_cord, y_cord)
        StateName(state_data.state.item(), x_cord, y_cord)

# missing_state.to_csv('')
missing_state9 = {}
missing_state9.items()