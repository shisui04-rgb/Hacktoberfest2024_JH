import time

def countdown(t):
    """Countdown timer."""
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time Up!!')

print("Countdown Clock")
t = input("Enter the number of seconds for the countdown: ")
countdown(int(t))
