Unit 13.020 Networking Commands

Remember the man pages!

On most of the following I am only giving a brief introduction.  Be sure to check out the man pages.

## ```ping```

```ping``` is mainly used for diagnosing network problems.  It sends out a packet of information to the server and measures the time it takes to get a response.  

It is a test to see if the other system is there.  It can also measure "latency" or the delay in getting messages exchanged.  

You do not have to ping just end computers.  You may also ping routers.  Sometimes I ping my gateway just to see if a signal is getting that far (more on how to find your gateway later)

On most *nix systems the ping command runs until it is stopped with Ctrl-C.  Therefore it is usually a good idea to run ping with the -c option.  I usually set up ```ping='ping -c'``` as an alias.

```bash
ping -c4 www.whitehouse.gov
ping 104.126.196.63
```

### Milliseconds

Ping reports its time in milliseconds.  I expect you to know what a millisecond is.

A millisecond is 1/1000 of a second.

Milliseconds | Seconds
:---: | :---:
100 ms | a tenth of a second
250 ms | a quarter of a second
500 ms | a half a second
1000 ms | a second

As a side note, the MWSU great firewall blocks ip traffic from off campus.  Therefore pinging systems like evan.cs.missouriwestern.edu or woz.cs.missouriwestern.edu typically shows them as being unavailable.  However, woz is inside the great firewall.  So if you are logged into woz you may ping other computers on campus.

## ```ip```

The ```ip``` command is fairly new.  It is intended to replace the ```ifconfig``` and ```route``` commands.

* ```ip addr``` This may be the most used of the ip commands.  It shows information about how the network is accessed.  
  * It usually gives the "mac" address and labels it /link/ether.
  * It also gives the ip address in ipv4 and ipv6 and labels them "inet" and "inet6"
* ```ip route``` This gives the routing table.  This is an important command for routers.  However, your laptop and woz are not routers.  For these systems ```ip route``` is important because it usually only has one entry.  That entry is labeled "default" and is the address of the subnet's ***gateway*** to the Internet.  If you lose network control the first thing you want to do is ping the gateway.  That will tell you whether your computer can get across the local area network.

## ```traceroute```

Traceroute shows each router the message travels over from the client to the server.  It usually gives travel times.  That makes it possible for a network administrator to identify where bottlenecks may exist.

There are various reasons information might not be returned.  When information is unavailable and asterisk * is placed in the data field.

## ```nslookup```

```nslookup``` gives information about dns information.  It works in both interactive and noninteractive modes.  

Noninteractive happens when you give a host name.  It prints some basic information.

```text
$ nslookup www.missouriwestern.edu
Server:         10.65.0.1
Address:        10.65.0.1#53

Non-authoritative answer:
Name:   www.missouriwestern.edu
Address: 150.200.1.43
``` 
If you don't supply a domain name it goes interactive.  See the man page.

## ```nmap```

```nmap``` got star treatment in the movie *The Matrix*

It basically scans the network.  It gives the ip addresses of systems it finds.  It also tries to find open ports. Run times can take several minutes.  If you are on your home network you could run the following command and find all your local systems including laptops, printers, and anyone on the local wifi.

```
$ nmap -sn 192.168.0.0/16
```
nmap is not installed on woz.  Running it would set off alarm bells in the IT department because it could signify that the network is under attack.


## ```netstat```

This is another command that returns information about network interfaces and the amount of traffic flowing through each of them.

I like it because it is clean.  Here is a run on my home system.

```text
$ netstat -i
Kernel Interface table
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
enp1s0    1500 10211170      0     31 0       6688715      0      0      0 BMRU
lo       65536  1824449      0      0 0       1824449      0      0      0 LRU
tun0      1500  4690012      0      0 0       2954260      0  13938      0 MOPRU
```

I have one network interface (enpls0) that is an ehternet connection connected by a router.

lo is the loopback address

tun0 is a tunnel.  I assume it is there because I am connected to the Internet via a VPN.

## ```tcpdump```

```tcpdump``` lists raw data from packets sent across a network link.  It is not installed on woz because of security issues.

## ```dig```

```dig`` queries dns servers about entries in the dns database

## ```wget```

```wget``` fetches files.  It may get data from http, https, and ftp sites.  The big difference between ftp/sftp and wget is that wget is not interactive.  That makes it better for fetching data in scripts or as a background process.

wget also works when the environment is unstable.  If a download fails wget will keep trying.  