# LearnServer
Learn how server runs and advantages and disadvantages of different implementations.

Python2/3 could run these scripts well. And the HTTP performance test uses wrk as test tool, python3.5.1 as test environment.


## simple_server.py

* Using socket to build a simple server.
* Accept and recv block each other, so the server cannot handle multi-request in one time.

　　HTTP Performance Test Result:  
　　　wrk http://127.0.0.1:8080  
　　　Running 10s test @ http://127.0.0.1:8080  
　　　2 threads and 10 connections  
　　　　Thread Stats   Avg      Stdev     Max   +/- Stdev  
　　　　　Latency     1.27ms   92.27us   5.45ms   95.61%  
　　　　　Req/Sec     3.83k    64.03     4.00k    81.00%  
　　　　76125 requests in 10.00s, 5.30MB read  
　　　Requests/sec:   7610.66  
　　　Transfer/sec:    542.56KB


## cgi_server.py

* Using cgi way to solve the problem that accept and recv block each other.
* Split accept and recv in different process.
* When there is a request, start a new process to handle it.

　　HTTP Performance Test Result:  
　　　wrk http://127.0.0.1:8080  
　　　Running 10s test @ http://127.0.0.1:8080  
　　　　2 threads and 10 connections  
　　　　Thread Stats   Avg      Stdev     Max   +/- Stdev  
　　　　　Latency    29.54ms    3.35ms  74.73ms   75.36%  
　　　　　Req/Sec   169.35     13.07   202.00     83.50%  
　　　　3380 requests in 10.01s, 240.96KB read  
　　　Requests/sec:    337.54  
　　　Transfer/sec:     24.06KB


## cgi_threading_server.py

* Using threading other than multiprocessing to build server, same like cgi way.
* When there is a request, start a new thread to handle it.

　　HTTP Performance Test Result:  
　　　wrk http://127.0.0.1:8080  
　　　Running 10s test @ http://127.0.0.1:8080  
　　　　2 threads and 10 connections  
　　　　　Thread Stats   Avg      Stdev     Max   +/- Stdev  
　　　　　Latency     2.55ms  190.66us   4.96ms   92.99%  
　　　　　Req/Sec     1.94k   132.20     3.73k    99.50%  
　　　　38763 requests in 10.10s, 2.70MB read  
　　　Requests/sec:   3838.05  
　　　Transfer/sec:    273.61KB  


## prefork_server.py

* **Only run in Linux.**
* Prefork many processes to handle request.

　　HTTP Performance Test Result:  
　　　wrk http://127.0.0.1:8080  
　　　Running 10s test @ http://127.0.0.1:8080  
　　　　2 threads and 10 connections  
　　　　Thread Stats   Avg      Stdev     Max   +/- Stdev  
　　　　　Latency   609.96us  301.52us   2.36ms   61.05%  
　　　　　Req/Sec     4.13k   158.06     4.60k    71.00%  
　　　　82264 requests in 10.01s, 5.73MB read  
　　　Requests/sec:   8220.92  
　　　Transfer/sec:    586.06KB


## threadpool1_server.py

* Using thread pool to handle request.
* Accept in main loop and recv and send in child threads.

　　HTTP Performance Test Result:  
　　　wrk http://127.0.0.1:8080  
　　　Running 10s test @ http://127.0.0.1:8080  
　　　　2 threads and 10 connections  
　　　　Thread Stats   Avg      Stdev     Max   +/- Stdev  
　　　　　Latency     1.73ms  106.76us   3.18ms   94.69%  
　　　　　Req/Sec     2.83k    50.54     3.06k    74.00%  
　　　　56254 requests in 10.00s, 3.92MB read  
　　　Requests/sec:   5623.53  
　　　Transfer/sec:    400.90KB


## threadpool2_server.py

* Using thread pool to handle request.
* Accept, recv and send in child threads.

　　HTTP Performance Test Result:  
　　　wrk http://127.0.0.1:8080  
　　　Running 10s test @ http://127.0.0.1:8080  
　　　　2 threads and 10 connections  
　　　　Thread Stats   Avg      Stdev     Max   +/- Stdev  
　　　　　Latency   637.33us  292.15us   4.29ms   61.94%  
　　　　　Req/Sec     4.07k   120.03     4.46k    67.50%  
　　　　81087 requests in 10.01s, 5.65MB read  
　　　Requests/sec:   8103.66  
　　　Transfer/sec:    577.70KB


## noblocking_server.py

* **Only run in Linux.**
* Accept, recv and send with noblocking.
* If there is no new connection, server will come into empty loop, which is called busy wait.

　　HTTP Performance Test Result:  
　　　wrk http://127.0.0.1:8080  
　　　Running 10s test @ http://127.0.0.1:8080  
　　　　2 threads and 10 connections  
　　　　Thread Stats   Avg      Stdev     Max   +/- Stdev  
　　　　　Latency    50.22ms   28.61ms 108.28ms   58.41%  
　　　　　Req/Sec    99.38     96.35     0.85k    92.00%  
　　　　1983 requests in 10.01s, 141.37KB read  
　　　Requests/sec:    198.14  
　　　Transfer/sec:     14.13KB


## multiplexingio_server.py

* **Only run in Linux.**
* Accept, recv and send with noblocking, but select with blocking.

　　HTTP Performance Test Result:  
　　　wrk http://127.0.0.1:8080  
　　　Running 10s test @ http://127.0.0.1:8080  
　　　　2 threads and 10 connections  
　　　　Thread Stats   Avg      Stdev     Max   +/- Stdev  
　　　　　Latency     1.41ms  111.11us   2.74ms   93.65%  
　　　　　Req/Sec     3.45k   230.10     6.62k    99.50%  
　　　　69026 requests in 10.10s, 4.81MB read  
　　　Requests/sec:   6834.32  
　　　Transfer/sec:    487.21KB