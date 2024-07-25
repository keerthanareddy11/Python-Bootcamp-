'''def convert_to_12_hour_format(time_24):
    # Split the input string into hours, minutes, and seconds
    hours, minutes, seconds = map(int, time_24.split(':'))
    
    # Handle the special case where seconds are 60
    if seconds == 60:
        seconds = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
            if hours == 24:
                hours = 0
    
    # Determine the period (AM or PM)
    period = "AM" if hours < 12 else "PM"
    
    # Convert hours to 12-hour format
    hours_12 = hours % 12
    if hours_12 == 0:
        hours_12 = 12
    
    # Format minutes and seconds to always be two digits
    minutes_str = f"{minutes:02}"
    seconds_str = f"{seconds:02}"
    
    # Return the formatted time string
    return f"{hours_12}:{minutes_str}:{seconds_str} {period}"

# Example usage
time_24 = "23:59:60"
time_12 = convert_to_12_hour_format(time_24)
print(time_12)


h,m,s=map(int,input().split(":"))
if s==60:
    s=0
    m+=1
if m==60:
    m=0
    h+=1
if '''









time='24:60:60'
time=time.split(':')
hrs=time[0]
minutes=time[1]
sec=time[2]

if int(hrs)>=24:
    hrs=int(hrs)-24
else:
    hrs=int(hrs)-12
if int(minutes)>59:
    hrs=int(hrs)+1
    minutes=0
if int(sec)>59:
    minutes=int(minutes)+1
    sec=0
print(str(hrs)+":"+str(minutes)+":"+str(sec))