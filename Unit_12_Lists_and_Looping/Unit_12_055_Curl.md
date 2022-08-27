12.055 `curl`

`curl` is a program that fetches web pages and returns them as a stream.

## `curl` vs `wget`

Earlier this semester we use `wget` to fetch files. Both curl and wget retrieve files using the http and https protocols. The difference is `wget` generally produces files while `curl` returns a stream to the console.

```text
$ curl -s http://api.open-notify.org/iss-now.json
{"iss_position": {"longitude": "-69.9921", "latitude": "-46.1509"}, "timestamp": 1637424841, "message": "success"}noynaert@G508u:~$ curl http://woz.csmp.missouriwestern.edu
<!DOCTYPE html>
<html lang="en-us">
<head>
	<meta charset="UTF-8">
	<title>Old Jedi Mind Trick</title>
	<link href="https://fonts.googleapis.com/css2?family=Long+Cang&display=swap" rel="stylesheet">
	<style>
		body{font-family: 'Long Cang',cursive;
		   padding: 2em;}
		* {font-weight:normal;}
	</style>
</head>
<body>
	<h1>These aren't the web pages you are looking for</h1>
	<p>Nothing to see here.</p><h2>Move along</h2>
</body>
</html
```

But curl is rarely used for actual websites. There is a lot of data on the Internet that is served up using the http protocol. Use your browser to look at [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json) which shows the current location of the International Space Station. Now try the following command.

```bash
curl http://api.open-notify.org/iss-now.json
```

## The -s option

Some implementations of curl give data transfer information while the file is being downloaded as a progress bar. The -s suppresses a this output so you get the pure data from the website. Newer implementations of curl seem to suppress the progress bar, but it is pretty standard to always include it.

## More on `curl`

Curl works with a large number of protocols other than http. See the man page for a full list.

Curl is also capable of sending form data and handling logins and cookies sent by the web site.
