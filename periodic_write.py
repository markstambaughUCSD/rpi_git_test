# Mark Stambaugh
# 2019/11/23
# testing period commits to github

from time import time

start_time_s = time()
last_print_time_s = start_time_s

period_s = 2
run_time_s = 10

print "begin"
while time() < start_time_s + run_time_s:
	if time() > last_print_time_s + period_s:
		print time() - start_time_s
		last_print_time_s = time()

print "done"


