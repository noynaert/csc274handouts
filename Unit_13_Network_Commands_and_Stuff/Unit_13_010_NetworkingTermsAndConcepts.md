# Unit 13.010 Networking Commands

This summarizes some of the most important commands for networking.  I realize networking is not a 
prerequisite for this course.  Here is a quick and dirty introduction to networking terms  and concepts you need to know.  You may skip
this page and video if you understand the basics of networking.

## IP Addresses

Every Computer on the Internet has to have an IP address.  In theory, each computer must have a unique address.  But we do have some cheats that allow some duplication of addresses.

### IPv4 Addresses

IP addresses are usually written as 4 decimal numbers separated by periods.  150.200.1.1 would be an example of an IP address.
The decimal numbers are each 0 through 255.

The addressing scheme developed for the Internet was created when there were only mainframe and minicomputers.  Mainframes
cost millions, and minicomputers were costing $50,000 to $100,000, and that was in 1970 dollars!  32 bits allowed 
a theoretical 4 billion computers.  That was considered to be excessive.  Computers were expensive and rare, and it was unlikely
that all of the computers would be connected.  There was going to be a lot of "wasted" addresses, but still the assumption was
that they had allowed for a ridiculously large number of addresses.

And then microcomputers happened.  Basically, they were running out of addresses because there were so many computers.

#### NAT to the rescue

"Network Address Translation" or NAT was invented to help stretch the supply of IP addresses.  NAT allowed a large number of computers to share the same IP address.  

##### 192.168.0.0 

Your home probably has an IP address supplied by your network provider (commonly Suddenlink or AT&T in St. Joseph).  

All the computers and printers in a typical home are connected to a router in the home.  Your router has the IP address from Suddenlink
or another provider.  The Router actually does address translation.  To the outside world all the computers in your home appear to be on the same IP address.  But within your home everything appears to be on a network that starts with 192.168.  

Larger commercial networks use a different NAT system, but the concepts are about the same.  They use the address 10.

### IPv6

It was obvious that even with NAT and other tricks the Internet was going to run out of IPv4 addresses.  So IPv6 addresses
were developed.  At least in the US most systems still use IPv4 addresses.  The Internet was developed in the US, and so the bulk
of the addresses were reserved for US use.

IPv6 has some advantages besides allowing a larger domain of IP addresses.  It offers some security and efficiency boosts. It is
also easier for a device to move between different networks without needing as much network reconfiguration.  

Cell phones were obviously going to be a problem that would even blow through the US allocation of IPv4 addresses.  So most cell phones operate with IPv6 addresses except when they connect to a local wifi.  And even then many of them stay on IPv6.

An example of an IP address would be fe80::7d53:273:a6e2:6c3a.  It is a hexadecimal number.  The address shown is actually a shorthand.  The :: indicates several zeros were eliminated.

## Network Interfaces

The network interface is the hardware that allows the computer to connect to the Internet.  If you are plugging an ethernet cable into the computer you are using the network interface.  If you are using wireless, then the network interface is the thing that controls the radio.  Every Network Interface in the world has a unique number burned into the device.  

The Internet Address is also known as a "MAC Address."  An example would be b0:83:fe:a4:5b:cb.

## DNS

The Domain Name System (DNS) assigns names to IP addresses.  For example, the computer named "noynaert.com" has an IP address of 216.239.34.21
