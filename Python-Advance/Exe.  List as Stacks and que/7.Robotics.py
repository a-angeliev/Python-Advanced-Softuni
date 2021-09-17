import re
import datetime
robots = input()
robots = re.split(';|-', robots)
robots_names= []
str_robots_proc = []
robots_time = []
products = []

start_time = [int(x) for x in input().split(":")]
start_time = start_time[2]+ start_time[1]*60 + start_time[0] * 60 * 60

for index in range(0,len(robots),2):
    robots_names.append(robots[index])
    str_robots_proc.append(robots[index+1])
    robots_time.append(0)
robots_proc = [int(x) for x in str_robots_proc]
command = input()
while not command == "End":
    products.append(command)
    command=input()
# products.reverse()
# is_taken = False
while products:
    for index in range(len(robots_time)):
        if not robots_time[index] == 0:
            robots_time[index] -= 1
    start_time+=1
    if start_time == 86400:
        start_time = 0
    for i in range(len(robots_time)):
        if robots_time[i] == 0:
            robots_time[i] = robots_proc[i]
            item = products.pop(0)
            displayed_time = str(datetime.timedelta(seconds=start_time))
            if start_time <= 35999:
                print(f"{robots_names[i]} - {item} [0{displayed_time}]")
            else:
                print(f"{robots_names[i]} - {item} [{displayed_time}]")
            is_taken = 1
            break
    if not is_taken == 1:
        # products = products[1:] + products[:1]
        item = products.pop(0)
        products.append(item)
    is_taken = 2






