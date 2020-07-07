# a dice rolling program
import PySimpleGUI as sg
from random import randint


# class for dice object
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        total = randint(1, self.sides)
        return total


# function to generate rolls
def generate_roll(num, type, extra):
    # set default to 1 dice if 0 or <
    if num < 1:
        num = 1
        window['-NUM-'].update(1)
    n = num
    # roll totals
    rolled = []
    # roll num times
    while num > 0:
        # create the dice and roll it
        d = Dice(type).roll_dice()
        # add it to rolled list then remove obj
        rolled.append(d)
        del d
        num -= 1

    # output

    
    # negative value in extra
    if extra < 0:
        print(f"Rolling {n}d{type}{extra}")
    # 0 or >
    else:
        print(f"Rolling {n}d{type}+{extra}")
    print(rolled)
    print(f"Total: {sum(rolled) + extra}")


sg.theme('SystemDefault1')

layout = [

    [
        sg.InputText(size=(5, 1), default_text=1,
                     enable_events=True, key='-NUM-'),
        sg.Text(text="dice to roll"),
    ],
    [
        sg.Text(text="+/- "),
        sg.InputText(size=(5, 1), default_text=0,
                     enable_events=True, key='-EXTRA-'),
        sg.Text(text="to add to roll"),
    ],
    [
        sg.Text(text="Click dice when ready")
    ],
    [
        sg.Button("d2"),
        sg.Button("d4"),
        sg.Button("d6"),
        sg.Button("d8"),
        sg.Button("d10"),
        sg.Button("d12"),
        sg.Button("d20"),
        sg.Button("d100"),
    ],
    [
        sg.Output(size=(60, 5), key='-OUTPUT-')
    ],
    [
        sg.Button("Clear"),
    ],

]

# create the window
window = sg.Window("pydice roller", layout)


def clear_output():
    window['-OUTPUT-'].update("")


# create event loop
while True:
    event, values = window.read()

    if event == "d2":
        clear_output()
        generate_roll(int(values["-NUM-"]), 2, (int(values["-EXTRA-"])))
    if event == "d4":
        clear_output()
        generate_roll(int(values["-NUM-"]), 4, (int(values["-EXTRA-"])))
    if event == "d6":
        clear_output()
        generate_roll(int(values["-NUM-"]), 6, (int(values["-EXTRA-"])))
    if event == "d8":
        clear_output()
        generate_roll(int(values["-NUM-"]), 8, (int(values["-EXTRA-"])))
    if event == "d10":
        clear_output()
        generate_roll(int(values["-NUM-"]), 10, (int(values["-EXTRA-"])))
    if event == "d12":
        clear_output()
        generate_roll(int(values["-NUM-"]), 12, (int(values["-EXTRA-"])))
    if event == "d20":
        clear_output()
        generate_roll(int(values["-NUM-"]), 20, (int(values["-EXTRA-"])))
    if event == "d100":
        clear_output()
        generate_roll(int(values["-NUM-"]), 100, (int(values["-EXTRA-"])))

    if event == "Clear":
        window['-NUM-'].update(1)
        window['-EXTRA-'].update(0)
        clear_output()

    if event == sg.WIN_CLOSED or event == 'Quit':
        break


window.close()
