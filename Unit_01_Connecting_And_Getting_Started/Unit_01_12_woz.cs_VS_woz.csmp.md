# 01.12 woz.cs VERSUS woz.csmp

Originally the URL of Woz was woz.cs.missouriwestern.edu.  However, in August 2022 the url was changed to woz.csmp.missouriwestern.edu.

I have tried (and I am trying) to fix change woz.cs to woz.csmp wherever it occurs in the course.  I can guarantee that I have missed some.

Therefore, please just make a mental note that when you see woz.cs it should probably be woz.csmp.

## More information than you probably wanted

If you are interested in the reason for the change, it has to do with the SSL certificate.   Previously woz had provided https services by using a free "Let's Certify" certificate.  This was adequate for the security needs of woz.

However, we have other servers in the department that needed a stronger security certificate.  Therefore we obtained a "wildcard" certificate for csmp.missouriwestern.edu.  It made sense to change the domain of woz to the higher level certificate.

As of this writing, I don't have the new certificate installed, but it is on my todo list.