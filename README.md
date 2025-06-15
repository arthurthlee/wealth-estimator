Model Considerations:
face-recognition library in Python vs DeepFace
From researching online, it seems like the face-recognition library is decent for basic tasks, and is easy to set up, requiring fewer dependencies and lower hardware requirements compared to a more robust model such as InsightFace. Since it is mentioned that accuracy is less important compared to robustness, we can go with the face-recognition library, as we are not sure about where the project will be deployed (Mobile? Super fast AWS EC2 instance with GPU? Office computer?)

Pydantic:
Ensures that inputs to the model are of a consistent structure

Need to install CMAKE