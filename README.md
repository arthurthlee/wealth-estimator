
This wealth estimator project will:
Accept a selfie image as input.
Returns:
- An estimated potential net worth for the user
- A list of top 3 most similar wealthy individuals and their similarity scores


Installation instructions:
To run this locally in a container, git clone the repo, and make sure that you have installed Docker, and it is currently running on your machine.
Run the following lines in a console:
`docker build -t wealth-estimator .`
`docker run -p 80:80 wealth-estimator`

Then, open a browser and go to the url http://localhost/docs
Click on the POST /predict endpoint, and click "Try it out"
Type in whatever top N value you desire
Click "Execute", and view the Server response box below


To run unit tests, first install CMAKE and make sure that it is part of your PATH (CMAKE used by face_recognition library in Python)
Then, create a virtual env if you'd like, by typing
`python -m venv .venv`
`.venv/Scripts/activate` on Windows, or `.venv/bin/activate` on Mac/Linux

Then install the requirements and run pytest:
`pip install -r requirements/dev.txt`
`pytest`

After installing CMAKE and the requirements, you can also run it locally without using Docker by running this command from the project folder:
`python .\scripts\run_locally.py --image_path .\tests\test_data\warren_buffett.jpg`


Model Considerations:
face-recognition library in Python
From researching online, it seems like the face-recognition library is decent for basic tasks, and is easy to set up, requiring fewer dependencies and lower hardware requirements compared to a more robust model such as InsightFace. Since it is mentioned that accuracy is less important compared to robustness, we can go with the face-recognition library, as we are not sure about where the project will be deployed (Mobile? Super fast AWS EC2 instance with GPU? Office computer?)

Similarity Considerations:
I primarily weighed cosine similarity versus euclidean distance. Cosine similarity measures the cosine of the angle between two vectors, regardless of vector length. For image recognition, this is more desirable, as this would focus on the actual content of the image, regardless of brightness or contrast, whereas Euclidean distance would take the magnitude of the vectors in account, making brightness and contrast more heavily affect the predicted result (something we wouldn't want in this scenario, as our image could be dark or washed out)

Architectural Considerations:
I've hosted the model on an AWS free tier account. I've added the Docker image to ECR, and I am hosting it on ECS Fargate, so I don't need to manually configure an EC2 instance. 


scripts/
├── data/                       
│   ├── pictures/             # Pictures of various wealthy people
|   └── net_worths.csv        # Net worths of each person
├── create_embeddings.py      # Script to create an data.json embeddings file for the pictures and net_worths in the scripts/data folder
└── run_locally.py            # Script to run the program locally, by passing in the local path of an image and the number of matches to return
wealth-estimator/
├── app/
│   ├── main.py               # Contains the main FastAPI /predict endpoint
│   ├── models.py             # Contains the definitions of the endpoint response
│   ├── logic.py              # Contains the function for finding the top N matches, given a user image embedding
│   ├── utils.py              # Contains a utility function to extract face embeddings given image bytes. Used for creating a new dataset of embeddings of wealthy people, and also for creating embeddings of the user image
├── requirements.txt
├── Dockerfile
├── setup.py
└── README.md

With this structure, I'm only including the wealth_estimator app and data folders into the Dockerfile, since the files and data in scripts/ are not necessary for inference time (unless we decide to make an endpoint/UI to be able to create new embeddings for new people)

Improvements:
- Add logging