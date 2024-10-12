#!/bin/bash
sleep 3 && xdg-open http://localhost:8000 &
docker build -t htagdemo . && docker run -p 8000:8000 --rm htagdemo
