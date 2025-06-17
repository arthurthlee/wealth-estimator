Here's a more readable and polished version of your README formatted for GitHub:

---

# 💰 Wealth Estimator API

This project estimates a user's potential net worth based on a selfie, and returns the top 3 most visually similar wealthy individuals along with similarity scores.

---

## 📸 What It Does

* Accepts a selfie image as input
* Returns:

  * An **estimated potential net worth**
  * A **list of the top 3 most similar wealthy individuals** (with similarity scores)

---

## 🚀 Getting Started

### 🐳 Run Locally in Docker

1. Clone the repo:

   ```bash
   git clone https://github.com/your-repo/wealth-estimator.git
   cd wealth-estimator
   ```

2. Make sure [Docker](https://www.docker.com/products/docker-desktop/) is installed and running.

3. Build and run the container:

   ```bash
   docker build -t wealth-estimator .
   docker run -p 80:80 wealth-estimator
   ```

4. Open your browser to [http://localhost/docs](http://localhost/docs)

5. Try it out:

   * Click on the `POST /predict` endpoint
   * Click **"Try it out"**
   * Upload an image and set the `top_n_similar` value
   * Click **"Execute"** to see the results

---

### 🧪 Running Unit Tests

1. Install [CMake](https://cmake.org/download/) and ensure it's added to your system `PATH` (required by `face_recognition`)

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies and run tests:

   ```bash
   pip install -r requirements/dev.txt
   pytest
   ```

---

### 🖥️ Running Locally Without Docker

Once CMake and dependencies are installed, run:

```bash
python scripts/run_locally.py --image_path tests/test_data/warren_buffett.jpg
```

---

## 🧠 Adding New Data

To add new wealthy individuals:

1. Add their image to: `scripts/data/pictures/`
2. Add their net worth to: `scripts/data/net_worths.csv`

Then generate the updated embeddings:

```bash
python scripts/create_embeddings.py
```

This creates a new `data.json` in: `wealth_estimator/data/`

---

## 🧰 Project Structure

```
scripts/
├── data/
│   ├── pictures/              # Images of wealthy individuals
│   └── net_worths.csv         # CSV of net worths
├── create_embeddings.py       # Generates embeddings from images and net worths
└── run_locally.py             # Run prediction locally with a sample image

wealth_estimator/
├── app/
│   ├── main.py                # FastAPI app with /predict endpoint
│   ├── models.py              # Response models for the API
│   ├── logic.py               # Logic for similarity and matching
│   └── utils.py               # Embedding extraction functions
├── requirements.txt
├── Dockerfile
├── setup.py
└── README.md
```

Only the `wealth_estimator/` app and data folders are included in the Docker container. The `scripts/` folder is excluded since it's not required at inference time.

---

## 🤖 Model Considerations

* **Library**: [`face_recognition`](https://github.com/ageitgey/face_recognition)
* **Why**: Easy to use, minimal dependencies, and good enough accuracy for the project scope
* **Deployment Flexibility**: Suitable for various environments (local machine, cloud, etc.)

---

## 📏 Similarity Metric

* **Metric Used**: Cosine Similarity
* **Reason**: More robust to changes in image brightness or contrast compared to Euclidean distance, making it ideal for comparing facial features regardless of lighting conditions.

---

## 🏗️ Deployment Architecture

* Deployed on **AWS ECS Fargate** using the **Free Tier**
* Docker image is pushed to **Amazon ECR**
* No manual EC2 configuration required

---

## 🌱 Future Improvements

* Create Jupyter notebooks for `create_embeddings.py` and `run_locally.py`
* Implement a full training/testing pipeline
* Modularize model selection (e.g., integrate HuggingFace models)
* Make config file which can determine logging levels for dev, stg, prd, model endpoints, etc

---
