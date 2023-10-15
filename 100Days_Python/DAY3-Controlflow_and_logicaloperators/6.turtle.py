import turtle

screen=turtle.Screen()
screen.title("U.S.States Game")
image="C:\\Users\\vishn\\Downloads\\day-25-us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state",prompt="what's another state's name?")
print(answer_state)