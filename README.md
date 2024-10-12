This is "home" for the future "htag demo". It will be a docker app (because my free hosting provider will shutdown my free account, if many people use the online version at the same time)

It will be a lot simpler to intanciate it, on demand ;-)

**IMPORTANT** : Currently, it's just an [empty app](app/app.py) !
it will come soon ;-)

# Test :

    ./test.sh

# or manually :

## build and run once
docker build -t htagdemo . && docker run -p 8000:8000 --rm htagdemo

## test

Surf to http://localhost:8000