# Unit 10.1 Hosts and automated logins

## The hosts file

The host file is a substitute or a shortcut for hosts.

The hosts file is checked before going out to DNS

### Location of hosts file

* Windows 10 – “C:\Windows\System32\drivers\etc\hosts”
* Linux – “/etc/hosts”
* Mac OS X – “/private/etc/hosts”

IPv4 addresses for woz.cs.missouriwestern.edu

From off campus:

    150.200.3.11 woz.cs.missouriwestern.edu

From on-campus using the NAT:

    10.112.28.11  woz.cs.missouriwestern.edu

You don't need to use the full name.  You may have multiple names for the same IP address

    10.112.28.11  woz.cs.missouriwestern.edu
    10.112.28.11  woz.cs
    10.112.28.11  woz
    10.112.28.11  barney

## Even quicker login with a script

Put a file with the name of your choice in your ~/bin folder.  Make sure it has execute permissions

```bash
     #!/usr/bin/bash
     ssh -X abyron@woz
```

## Login an ssh key exchange

* Use ```ssh-keygen -t edesa``` to generate a public-private key pair
* By default the key will be stored in ~/.ssh
* You may use the same key for multiple sites, but I prefer to generate a different pair for each server.
* ```ssh-copy-id -i ~/.ssh/YOURKEYNAME.pub woz.cs.missouriwestern.edu``` to copy the public key to woz.cs.missouriwestern.edu
