"""
H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
Determine the angle (in degrees) of the hour hand on the clock face right now.
"""

hours: int = int(input('Hours: '))
minutes: int = int(input('Minutes: '))
seconds: int = int(input('Seconds: '))

"""
Clock is shaped like a circle and is composed of 360 degrees. There are 60 minutes in one hour, and 360 degrees divided
by 60 minutes is 6. Therefore, the minute hand moves 6 degrees per minute.

It takes 720 minutes for the hour hand to move around the clock. 360 degrees divided by 720 minutes is 0.5. 
Therefore, the hour hand moves 0.5 degrees per minute.
"""

total_hour_angle = 360 / 12  # 30° degrees per hour for hour hand
total_minutes_angle = 360 / 720  # 0.5° degrees per minute for hour hand
total_seconds_angle = 360 / 43200  # 0.0083° degrees per minute for hour hand

angle_hour = (360 / 12) * hours
angle_minute = (360 / 720) * minutes
angle_seconds = (360 / 43200) * seconds

total_hour_hand = angle_hour + angle_minute + angle_seconds

print(total_hour_hand)