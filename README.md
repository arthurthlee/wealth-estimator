
This wealth estimator project will:
Accept a selfie image as input.
Returns:
- An estimated potential net worth for the user
- A list of top 3 most similar wealthy individuals and their similarity scores


Installation instructions:
To run this locally in a container, make sure that you have installed Docker, and it is currently running on your machine.
Run the following lines in a console:
`docker build -t wealth-estimator .`
`docker run -p 80:80 wealth-estimator`

Then, open a browser and go to the url http://localhost/docs
Click on the POST /predict endpoint, and click "Try it out"
Type in whatever top N value you desire


Need to install CMAKE

Model Considerations:
face-recognition library in Python
From researching online, it seems like the face-recognition library is decent for basic tasks, and is easy to set up, requiring fewer dependencies and lower hardware requirements compared to a more robust model such as InsightFace. Since it is mentioned that accuracy is less important compared to robustness, we can go with the face-recognition library, as we are not sure about where the project will be deployed (Mobile? Super fast AWS EC2 instance with GPU? Office computer?)

Similarity Considerations:
I primarily weighed cosine similarity versus euclidean distance. Cosine similarity measures the cosine of the angle between two vectors, regardless of vector length. For image recognition, this is more desirable, as this would focus on the actual content of the image, regardless of brightness or contrast, whereas Euclidean distance would take the magnitude of the vectors in account, making brightness and contrast more heavily affect the predicted result (something we wouldn't want in this scenario, as our image could be dark or washed out)