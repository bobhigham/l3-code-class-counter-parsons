count = 0

def on_forever():
    global count
    if input.button_is_pressed(Button.A):
        count += 1
        basic.show_number(count)
    if input.button_is_pressed(Button.B):
        count += -1
        basic.show_number(count)
basic.forever(on_forever)
