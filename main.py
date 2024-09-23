# main.py
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format to include the day of the week, date, and time
formatted_time = now.strftime("%A, %Y-%m-%d %H:%M:%S")

# Print the formatted time
print("Current Date, Time and Day: ", formatted_time)
