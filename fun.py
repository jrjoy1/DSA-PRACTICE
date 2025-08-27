import time
import os
from colorama import init, Fore, Style

# Optional Windows beep
try:
    import winsound
    windows_beep = True
except ImportError:
    windows_beep = False

# Initialize colorama
init(autoreset=True)

# 30-minute timer
total_seconds = 30 * 60
start_time = time.time()

def progress_bar(elapsed, total, length=30):
    """Return a colored progress bar string."""
    percent = elapsed / total
    filled_length = int(length * percent)
    bar = Fore.GREEN + "█" * filled_length + Fore.RED + "─" * (length - filled_length)
    return f"[{bar}] {int(percent*100):3d}%"

while True:
    elapsed = int(time.time() - start_time)
    remaining = total_seconds - elapsed

    # Stop after total duration
    if remaining < 0:
        break

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Real-time clock
    current_time = time.strftime("%H:%M:%S")

    # Time left
    rem_hr, rem_min_sec = divmod(remaining, 3600)
    rem_min, rem_sec = divmod(rem_min_sec, 60)

    # Time passed
    pass_hr, pass_min_sec = divmod(elapsed, 3600)
    pass_min, pass_sec = divmod(pass_min_sec, 60)

    # Display
    print("⏰ Real Time:     ",
          Style.BRIGHT + Fore.GREEN + current_time)

    print("⏳ Time Left:     ",
          Style.BRIGHT + Fore.RED + f"{rem_hr:02}:{rem_min:02}:{rem_sec:02}")

    print("⏱️  Time Passed:   ",
          Style.BRIGHT + Fore.YELLOW + f"{pass_hr:02}:{pass_min:02}:{pass_sec:02}")

    print("📊 Progress:      ", progress_bar(elapsed, total_seconds))

    time.sleep(1)

# Timer finished
print("\n⏰ Time's up! 🎉")

# Beep sequence
if windows_beep:
    for i in range(3):
        winsound.Beep(1000 + i*200, 300)
        time.sleep(0.2)
else:
    for i in range(3):
        print('\a')  # Terminal bell
        time.sleep(0.2)
