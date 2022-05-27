A short code to build an api which loads an ML model and makes a prediction
everytime the data is posted. Training of the model is done elsewhere.
PostToAPI notebook contains how the data can be posted.

A docker file is also provided to build the docker image.

To build docker image:  
docker build -t praticeapiapp . 

To run docker image:  
docker run -d --name apirunning -p 8000:8001 practiceapiapp