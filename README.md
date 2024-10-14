This is "home" for the future "htag demo". It will be a docker app (because my free hosting provider will shutdown my free account, if many people use the online version at the same time)

It will be a lot simpler to intanciate it, on demand ;-)

**IMPORTANT** : Currently, I'm working on this (the demo is not finnished, and bug a little)

# Test on your own

    docker run -p 8111:8000 ghcr.io/manatlan/htagdemo:latest

or 

    docker build -t test https://github.com/manatlan/htagdemo.git && docker run -p 8111:8000 --rm test

And surf to http://localhost:8111


# Test locally (on your host):

    git clone https://github.com/manatlan/htagdemo.git 
    cd htagdemo
    ./runLocal.sh

It will open the demo in your browser ;-)

## build and run once

    git clone https://github.com/manatlan/htagdemo.git 
    cd htagdemo
    docker build -t htagdemo . && docker run -p 8000:8000 --rm htagdemo

And surf to http://localhost:8000

# Test online

[htagdemo on render](https://htagdemo.onrender.com/)

**note** : The docker is hosted on **render.com** (in a free account) : so, it may take 50sec to start on-demand, be patient ;-)


