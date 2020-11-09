Unit 13.030 Moving Files

There are several ways to move files.  We will focus on SFTP becaus of its general usefulness.

## ```ssh```

We have been using ssh all semester without talking about it very much.

ssh establishes a secure connection between computers.  All the data flowing back and forth is encrypted.  

The main things we have pushed through the connection were characters typed on our local computer and results sent back from woz.

### Tunneling

It is possible to pass other things besides text through the SSH connection.  This is called either "Tunneling" or "Forwarding"

We have already briefly seen passing X communications between systems.

Another thing we can use tunnels for is to transfer files.

There are both command line interfaces and gui interfaces.  

* push
* get
* ls (also dir)
* cd, mkdir


### Why not just ```ftp```

FTP does not use encryption.  It also does not encrypt passwords.  They are sent across the network in clear text.  Therfore anyone along the route may use tcpdump or wireshark to capture your password.