# 12.060 JSON


```bash
curl -s http://api.open-notify.org/iss-now.json
curl -s https://api.coindesk.com/v1/bpi/currentprice.json | jq '.bpi .USD .rate'

curl -s https://api.github.com/repos/noynaert/csc274handouts/commits?per_page=5
```


## References

* [https://stedolan.github.io/jq/tutorial/](https://stedolan.github.io/jq/tutorial/)
* [https://www.baeldung.com/linux/jq-command-json](https://www.baeldung.com/linux/jq-command-json)
