# template for "Stopwatch: The Game"

# define global variables
import simplegui

counter_x = 0
counter_y = 0
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t // 600
    seconds = t / 10 % 60
    miliseconds = t % 10
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
    return str(minutes) + ":" + str(seconds) + "." + str(miliseconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_clock():
    timer.start()
    
def stop_clock():
    global counter_x, counter_y
    if timer.is_running(): # check if timer is running
        counter_y = counter_y + 1
# check if stopwatch was stopped at 0 miliseconds
# if miliseconds == 0 was giving bad results sometimes
        if (time % 10) == 0:
            counter_x = counter_x +1
    timer.stop()

def reset_clock():
    global time, counter_x, counter_y
    time = 0
    counter_x = 0
    counter_y = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time = time + 1

# adds a counter for number of stops
def counter():
    global counter_x, counter_y
    counter = str(counter_x) + "/" + str(counter_y)
    return counter

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [60, 90], 36, "White")
    canvas.draw_text(counter(), [150, 30], 18, "Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 200, 120)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
start_button = frame.add_button("Start", start_clock, 100)
stop_button = frame.add_button("Stop", stop_clock, 100)
reset_button = frame.add_button("Reset", reset_clock, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
