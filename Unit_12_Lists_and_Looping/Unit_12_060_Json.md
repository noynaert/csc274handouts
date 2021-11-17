# 12.060 JSON


```bash
curl -s http://api.open-notify.org/iss-now.json
curl -s https://api.coindesk.com/v1/bpi/currentprice.json | jq '.bpi .USD .rate'
curl -s https://api.github.com/repos/noynaert/csc274handouts/commits?per_page=5
curl -s https://gist.githubusercontent.com/bradtraversy/20dee7787486d10db3bd1f55fae5fdf4/raw/2c06c44dcea55ecbb6fbf20edfd240ec6373b688/state_capitals.json | jq '.[49]'
curl -s https://gist.githubusercontent.com/bradtraversy/20dee7787486d10db3bd1f55fae5fdf4/raw/2c06c44dcea55ecbb6fbf20edfd240ec6373b688/state_capitals.json | jq '.[49] .capital' 
```


## References

* [https://stedolan.github.io/jq/tutorial/](https://stedolan.github.io/jq/tutorial/)
* [https://www.baeldung.com/linux/jq-command-json](https://www.baeldung.com/linux/jq-command-json)
