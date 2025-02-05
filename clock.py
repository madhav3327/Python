import tkinter as tk
import time
import math

# Function to update the clock
def update_clock():
    # Get the current time
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate the angles for the clock hands
    sec_angle = math.radians(seconds * 6 - 90)
    min_angle = math.radians(minutes * 6 - 90)
    hour_angle = math.radians((hours * 30 + minutes * 0.5) - 90)

    # Update the second hand
    x2_sec = 150 + 100 * math.cos(sec_angle)
    y2_sec = 150 + 100 * math.sin(sec_angle)
    canvas.coords(sec_hand, 150, 150, x2_sec, y2_sec)

    # Update the minute hand
    x2_min = 150 + 80 * math.cos(min_angle)
    y2_min = 150 + 80 * math.sin(min_angle)
    canvas.coords(min_hand, 150, 150, x2_min, y2_min)

    # Update the hour hand
    x2_hour = 150 + 50 * math.cos(hour_angle)
    y2_hour = 150 + 50 * math.sin(hour_angle)
    canvas.coords(hour_hand, 150, 150, x2_hour, y2_hour)

    # Repeat every 100 milliseconds
    root.after(100, update_clock)

# Create the main window
root = tk.Tk()
root.title("Analog Clock")

# Create the canvas for the clock
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Draw the clock face
canvas.create_oval(50, 50, 250, 250, outline="black", width=2)  # Clock border
for i in range(12):  # Hour markers
    angle = math.radians(i * 30 - 90)
    x_start = 150 + 90 * math.cos(angle)
    y_start = 150 + 90 * math.sin(angle)
    x_end = 150 + 100 * math.cos(angle)
    y_end = 150 + 100 * math.sin(angle)
    canvas.create_line(x_start, y_start, x_end, y_end, fill="black", width=2)

# Create clock hands
sec_hand = canvas.create_line(150, 150, 150, 50, fill="red", width=1)
min_hand = canvas.create_line(150, 150, 150, 70, fill="blue", width=2)
hour_hand = canvas.create_line(150, 150, 150, 90, fill="black", width=4)

# Start the clock update
update_clock()

# Run the Tkinter event loop
root.mainloop()