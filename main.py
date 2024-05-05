import platform
import subprocess
from pycaw.pycaw import AudioUtilities
from win11toast import toast

current_os = platform.system()
DECIBEL_THRESHOLD = 80  # This is how many decibels has to be reached for the warning to show
URGENCY = "reminder"  # Change based on priority, use "reminder" for low priority and "urgent" for high priority
COOLDOWN = 60  # This is how many seconds before the next notification can appear


def linux_notif():
    subprocess.run([
        'notify-send',
        '--expire-time=5000',
        'Volume Warning',
        f"Your computer is playing sounds at {DECIBEL_THRESHOLD} decibels, you may want to consider lowering the volume!"
    ])


def windows_notif():
    toast('Decibel Warning',
          f'Your computer is playing sounds at {DECIBEL_THRESHOLD} decibels, you may want to consider lowering the '
          f'volume',
          duration="short",
          scenario=URGENCY
          )


# TODO: DB Detection


if current_os == "Windows":
    print("Windows Section")
elif current_os == "Linux":
    print("Linux Section")
    linux_notif()

