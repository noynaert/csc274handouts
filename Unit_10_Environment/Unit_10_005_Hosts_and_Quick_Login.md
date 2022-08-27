# Unit 10.1 Hosts and automated logins

There are 3 parts to quick login:

1. Use the hosts file
1. Use a script
1. Use key exchange for authentication rather than a password

Actually, you can kind of trade off #1 and #2. If you tweak your hosts file a script may not help that much. On the other hand, you can use a script file and make the host modifications unnecessary.

But pedagogically both are important to understand. The hosts file will be more important in networking. The script because we do scripting in this course. So we will go with overkill and do both.

Asymmetric key exchange is critical for most modern security mechanisms.

## The hosts file

- The host file is a substitute or a shortcut for Domain Name System (DNS).
- Sometimes it is used during development before the network administrator puts the host names and IP addresses in the actual DNS system.

The hosts file is checked before going out to DNS

### Location of hosts file

This is something you set on the machine you are coming from, not on woz.csmp.missouriwestern.edu

- Windows 10 – “C:\Windows\System32\drivers\etc\hosts”
- Linux – “/etc/hosts”
- Mac OS X – “/private/etc/hosts”

IPv4 addresses for woz.csmp.missouriwestern.edu (This does not matter what your OS is. Now where you are working from matters.)

From off campus:

    150.200.3.11 woz.csmp.missouriwestern.edu

From on-campus using the NAT:

    10.112.28.11  woz.csmp.missouriwestern.edu

You don't need to use the full name. You may have multiple names for the same IP address

    10.112.28.11  woz.csmp.missouriwestern.edu
    10.112.28.11  woz.csmp
    10.112.28.11  woz
    10.112.28.11  barney

## Even quicker login with a script

Put a file with the name of your choice in your ~/bin folder. Make sure it has execute permissions

```bash
     #!/usr/bin/bash
     ssh -X abyron@woz
```

## Login an ssh key exchange

- Use `ssh-keygen -t ecdsa` to generate a public-private key pair
- By default the key will be stored in ~/.ssh
- You may use the same key for multiple sites, but I prefer to generate a different pair for each server.
- `ssh-copy-id -i ~/.ssh/YOURKEYNAME.pub woz.csmp.missouriwestern.edu` to copy the public key to woz.csmp.missouriwestern.edu
