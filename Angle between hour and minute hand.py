hour,minutes = [int(i) for i in input().split()]
hour=hour+minutes/60
minutes = minutes/5
ans = (max(hour,minutes)-min(hour,minutes))*30
print(min(ans,360-ans))
