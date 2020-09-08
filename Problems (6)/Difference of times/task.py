# put your python code here
hour_start = int(input())
min_start = int(input())
sec_start = int(input())

hour_finish = int(input())
min_finish = int(input())
sec_finish = int(input())

res_hours = (hour_finish - hour_start) * 3600
res_minutes = (min_finish - min_start) * 60
res_seconds = (sec_finish - sec_start)

res_time = res_hours + res_minutes + res_seconds

print(res_time)
