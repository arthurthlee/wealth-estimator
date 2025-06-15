Background:
In this project, you will build a machine learning service that estimates a user's potential net worth based on a submitted selfie. This project assesses your ability to:
- Make architectural and modelling decisions
- Build and deploy an API
- Write clean, production-quality code

Task:
You need to build and deploy an API with the following functionality:
- Accepts a selfie image as input.
- Returns:
- An estimated potential net worth for the user
- A list of top 3 most similar wealthy individuals and their similarity scores

You will design:
- The embedding extraction process
- The similarity computation method
- The API design and deployment approach

Note: The definition of "wealthy individuals" and the corresponding embeddings dataset must be mocked or created as part of your solution. This is a demonstration project: accuracy is less important than the robustness and clarity of your approach. You don't need to train a model from scratch.

Requirements:
- Build a working containerized API endpoint "/predict"
- Accept a selfie image file (multipart/form-data)
- Return a JSON response with:
- Estimated net worth (USD or local currency)
- Top 3 most similar wealthy profiles (name or label + similarity score)
- Host the service publicly if possible
- Include a README that explains:
- Architecture decisions
- How to run/deploy the solution
- Assumptions made

Constraints:
You may choose any:
- Pre-trained vision model
- Similarity metric
- Frameworks

We expect you to make reasonable engineering trade-offs and explain them in the README. AI tools are allowed.

Evaluation Criteria:
Category | Focus
ML Engineering | Embedding extraction, similarity logic
API Development | Correctness, robustness, input handling
Deployment | Reproducibility, scalability, thinking
Code Quality | Structure, documentation, readability
Critical Thinking | Handling assumptions

Submission
You must submit:
- Github repository link (with Dockerfile)
- Live URL of the endpoint




Model Considerations:
face-recognition library in Python vs DeepFace
From researching online, it seems like the face-recognition library is decent for basic tasks, and is easy to set up, requiring fewer dependencies and lower hardware requirements compared to a more robust model such as InsightFace. Since it is mentioned that accuracy is less important compared to robustness, we can go with the face-recognition library, as we are not sure about where the project will be deployed (Mobile? Super fast AWS EC2 instance with GPU? Office computer?)

Pydantic:
Ensures that inputs to the model are of a consistent structure

Need to install CMAKE

Similarity considerations:
I primarily weighed cosine similarity versus euclidean distance. Cosine similarity measures the cosine of the angle between two vectors, regardless of vector length. For image recognition, this is more desirable, as this would focus on the actual content of the image, regardless of brightness or contrast, whereas Euclidean distance would take the magnitude of the vectors in account, making brightness and contrast more heavily affect the predicted result (something we wouldn't want in this scenario, as our image could be dark or washed out)