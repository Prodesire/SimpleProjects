# Tail
Using Python to realize the 'tail -f filename' function of Linux. Only runs on Python3 only. 

When running this, it will read 5 lines(if there are equal or more than 5 lines) from the file by default, then read the following new lines in real time. If there is no new line, it will sleep for 1 second and try to read line again.