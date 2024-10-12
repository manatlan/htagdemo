
# build
docker build -t htagdemo .

# run
docker run -p 8000:8000 --rm htagdemo

# test
Surf to http://localhost:8000