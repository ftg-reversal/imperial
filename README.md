# Imperial

## Usage
```
$ docker pull reversal/imperial
$ docker run -it --rm -e NICOVIDEO_ID=*** -e NICOVIDEO_PASS=*** -p 80:80 reversal/imperial
$ curl http://localhost/80/100/sm*** | jq .
```
