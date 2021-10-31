
In project directory
docker build --tag reaktor_rest_wb_wordcount .
docker run --publish 8000:8000 reaktor_rest_wb_wordcount

Then go to http://localhost:8000/docs
and post {"url": "https://www.goodreads.com/book/show/40701777-the-trouble-with-peace"} for example