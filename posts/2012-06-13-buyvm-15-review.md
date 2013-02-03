BuyVM 128MB OpenVZ VPS Review ($15/year)

If you are looking for an affordable VPS provider, many people will recommend 
BuyVM. They are famous on sites like LowEndBox, LowEndTalk, and WebHostingTalk.
BuyVM is notoriously known for their high server performance, high reliability, 
dirt cheap prices, and very, very low stock. Their servers are located in San 
Jose, California at a Coresite datacenter. The stock for the 128MB OVZ is in 
such high demand that BuyVM is forced to release stock in batches. Eager 
buyers (like me) refresh the BuyVM page every 4:00 and 13:00 PST for a chance 
to grab one. I would call them the "Apple" of virtual private server providers.

I was finally able to snatch a $15/year 128MB OpenVZ VPS. I threw on Debian 
Squeeze 64bit as soon as I got the SSH information (1 hour after I ordered). 
I installed Nginx, PHP-FPM, and MySQL. I planned to have this server host my 
blog, main website, and a couple other small projects.

After I logged in, I was surprised to see that I actually had 256MB of RAM 
available for use instead of 128MB. I guess that's what 'Burst RAM' means.

According to /proc/cpuinfo, I'm running on a node with an Intel(R) Xeon(R) CPU 
L5520 @ 2.27GH processor. I have access to one core as described on the order 
page.

BuyVM recently added something called "SSD caching" to all their nodes for 
caching applications that temporarily need access to a fast hard drive. 

### Some quick tests

Here's a dd test:

```generic
$ dd if=/dev/zero of=test bs=64k count=16k conv=fdatasync
16384+0 records in
16384+0 records out
1073741824 bytes (1.1 GB) copied, 3.619 s, 297 MB/s```

BuyVM has all their VPS's on a GigE line so transfer speeds can be very fast. 
Routing is decent to the east coast. It all depends on the mood of the server 
at a specific time of day.

```generic
wget cachefly.cachefly.net/100mb.test -O /dev/null
--2012-07-08 18:51:57--  http://cachefly.cachefly.net/100mb.test
Resolving cachefly.cachefly.net... 205.234.175.175
Connecting to cachefly.cachefly.net|205.234.175.175|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 104857600 (100M) [application/octet-stream]
Saving to: “/dev/null”

100%[===================================================>] 104,857,600 23.0M/s   in 4.5s    

2012-07-08 18:52:01 (22.2 MB/s) - “/dev/null” saved [104857600/104857600]```

### Summary

I've been using the VPS for about a month. It feels very fast and is able 
to run all my applications perfectly at a VERY low cost ($1.25/m). They also 
have IPv6 running perfectly (ping6 pumpkin6.huang.mx). The value is great 
and the I couldn't be happier.

I hear BuyVM will be adding a new datacenter in Atlanta Buffalo very soon 
and if they do, I will be buying another VPS the second it comes out!

### Update 6/14/12

Oh the irony. A couple of hours after writing this great review, my VPS went 
offline for 1 hour 40 minutes (according to buyvmstatus) or 2 hours (according 
to Pingdom). My uptime this month is now 99.7%. I will be updating this post as 
I continue to be using this VPS.

### Update 7/12/12

There's been some lengthy downtime over the past month. Once it was even up to 
two hours. I believe it was because of a bad kernel or something on the node 
my VPS is on. The problem seems to have been fixed because now my VPS is doing 
fine. It's been up for 13 days and still going strong. I'm running both a 
node.js app and Python app (this blog) perfectly while only using half of my 
256MB of RAM.