# LearnServer
Learn how server runs and advantages and disadvantages of different implementations.

Python2/3 could run these scripts well. And the HTTP performance test uses wrk as test tool, python3.5.1 as test environment.

## simple_server

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

## cgi_server

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

## cgi_threading_server

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