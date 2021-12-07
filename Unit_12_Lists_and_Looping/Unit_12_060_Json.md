# 12.060 JSON

## What is JSON?

JSON stands for JavaScript Object Notation.  It is a string representation of a JavaScript object.  

Even though it was developed from JavaScript, JSON has become a standard method of exchanging data between computer systems.  Most languages have the ability to read and write JSON data.

## Simple JSON notation

When most people think of JSON they think of a structure like this one:

```json
{ 
    "title" : "Eye of the World",
    "author" : "Robert Jordan",
    "year" : 1990,
    "pages" : 814
}
```

Some important points about the above.

* The object is surrounded with {curly braces}.
* The fields are organized in "key:value" pairs.
* The key is surrounded by "quotation marks."
* Strings are in quotes
* Numeric data does not have quotes
* Comma is a separator between fields

Note that the comma is a *separator.*  It is not an end-of-line marker.  The comma goes between fields.  There is no comma after the last field.

### Minified vs Beautified

JSON may be minified to compress any unnecessary white space.

```json
{"title":"Eye of the World","author":"Robert Jordan","year":1990,"pages":814}
```

The opposite of minified is usually called "pretty" or "beautified."  

Websites like [https://codebeautify.org/](https://codebeautify.org/)  provide a lot of services such as minifying, beautifying, and validating JSON.  They can also convert json to other formats.
### Arrays

JSON may be used to represent arrays.  [Square brackets] are used for arrays.  For example, the minified `["Chris","Pat","Marty"]` can be beautified to 

```json
[
  "Chris",
  "Pat",
  "Marty"
] 
```

### Single Values

Technically JSON may consist of a single value.  However, a lot of applications have trouble dealing with single values.

## Nesting

* Objects may be nested inside objects.
* Objects may contain arrays
* Arrays may contain objects.

Generally, when objects or arrays are nested inside objects the nested object must be given a key to identify it.

```json
{
  "iss_position": {
    "latitude": "45.9788",
    "longitude": "-74.2322"
  },
  "timestamp": 1637281945,
  "message": "success"
}
```

Arrays may contain objects without assigning them names:

```json
[
    { 
        "title" : "Eye of the World",
        "author" : "Robert Jordan",
        "year" : 1990,
        "pages" : 814
    },
    { 
        "title" : "The Dragon Reborn",
        "author" : "Robert Jordan",
        "year" : 1991,
        "pages" : null
    }
]
```

## JSON and the Internet

When css is transmitted over the Internet it is often minimized.  This saves bandwidth.  

Here is a curl statement to fetch some minified JSON.

```bash
curl -s http://api.open-notify.org/iss-now.json
```

## `jq`

The `jq` command is an extremely powerful command for handling JSON data.  It contains an entire programming language within it.

`jq` "filters" incoming data from a stream or a file.  Output from one filter may be piped to other filters. It can get complicated.

The simplest filter is just a period.  I don't find anything that identifies what the period represents, but after playing with jq for a while I believe that that the period represents the "root" of the json structure.

```bash
curl -s http://api.open-notify.org/iss-now.json | jq '.'
{
  "iss_position": {
    "longitude": "-49.9521",
    "latitude": "-10.3959"
  },
  "timestamp": 1637431248,
  "message": "success"
}
```

To recover the timestamp we can specify the .timestamp field

```bash
curl -s http://api.open-notify.org/iss-now.json | jq '.timestamp'
1637431538
```

The ISS data has a field "iss_postion" which is an object.  To "drill down" we separate the fields by blanks.

```bash
curl -s http://api.open-notify.org/iss-now.json | jq '.iss_position .latitude'
```

Here is a command that finds the current price of bitcoin. (Remove the filter to see what is actually happening)

```bash
curl -s https://api.coindesk.com/v1/bpi/currentprice.json | jq '.bpi .USD .rate'
"57,959.3451"
```

## Working with arrays in jq

This URL contains data about states.  Note that it is an array of objects.  [https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json](https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json)

```bash
# Get the array broken into elements (which are objects)
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '.[]'

# print the capital of each state
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '.[] .capital_city'

# takes the basic array '.' then filters it through sort_by(.capital_city) 
# and then just prints the capital city
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '. | sort_by(.capital_city) | .[] .capital_city'
```

It is possible to make arrays and new objects from existing JSON.  It is also possible to merge two different JSON objects.  But that is mostly beyond what we are going to do here. 

curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '.[] | {capital_city,  state}' 


## Sample Commands

These are some commands I ran while investigating.  They are kind of like my working notes.

```bash
curl -s http://api.open-notify.org/iss-now.json
curl -s https://api.coindesk.com/v1/bpi/currentprice.json | jq '.bpi .USD .rate'
curl -s https://api.github.com/repos/noynaert/csc274handouts/commits?per_page=5
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq .
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '.[49]'
curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '.[49] .capital_city'
curl -s https://cat-fact.herokuapp.com/facts | jq . | less

curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq '.[] | {capital_city,  state}' 
Create objects: curl -s https://raw.githubusercontent.com/CivilServiceUSA/us-states/master/data/states.json | jq 'sort_by(.capital_city) | .[] | {  capital_city,  state }' 

Some other sources:
https://jsonplaceholder.typicode.com/users/
https://ipapi.co/150.200.28.11/json/
```

## References

* [https://stedolan.github.io/jq/tutorial/](https://stedolan.github.io/jq/tutorial/)
* [https://www.baeldung.com/linux/jq-command-json](https://www.baeldung.com/linux/jq-command-json)
