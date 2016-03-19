# LearnServer
Learn how server runs and advantages and disadvantages of different implementations.

**simple_server**

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
 
**cgi_server**

* Using cgi way to solve the problem that accept and recv block each other.
* Split accept and recv in different process.

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