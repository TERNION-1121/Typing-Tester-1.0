import time as t

input("Press Enter to start")
start_time = t.time()
input("Press Enter to stop")
end_time = t.time()
time_lapsed = end_time - start_time
print(time_lapsed)