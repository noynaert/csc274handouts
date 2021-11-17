# 12.060 JSON

## What is JSON?

JSON stands for JavaScript Object Notation.  It is a string representation of a JavaScript object.  

Even though it was developed from JavaScript, JSON has become a standard method of exchanging data between computer systems.  Most languages have the ability to read and write JSON data.

```bash
curl -s http://api.open-notify.org/iss-now.json
curl -s https://api.coindesk.com/v1/bpi/currentprice.json | jq '.bpi .USD .rate'
curl -s https://api.github.com/repos/noynaert/csc274handouts/commits?per_page=5
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq .
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '.[49]'
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '.[49] .capital_city'
```


## References

* [https://stedolan.github.io/jq/tutorial/](https://stedolan.github.io/jq/tutorial/)
* [https://www.baeldung.com/linux/jq-command-json](https://www.baeldung.com/linux/jq-command-json)
