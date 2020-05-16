# get the initial time
hour_begin = int(input())
minute_begin = int(input())
second_begin = int(input())
# get the second time and convert to correct seconds
hours = (int(input()) - hour_begin) * 3600
minutes = (int(input()) - minute_begin) * 60
seconds = int(input()) - second_begin
print(hours + minutes + seconds)  # total the time
