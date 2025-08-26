# 🫁 Chest X-ray Cancer Classification (Normal vs Adenocarcinoma)

This repository contains an **end-to-end Deep Learning project** for classifying **chest X-rays** into **Normal** and **Adenocarcinoma** categories.  
The project is designed with a **modular, production-ready pipeline**, integrating tools like **DVC**, **MLflow**, and **Dagshub** for experiment tracking, reproducibility, and scalability.

---

## 📌 Problem Statement
Early and accurate diagnosis of **lung cancer adenocarcinoma** from chest X-rays can improve patient outcomes.  
The challenge is to build a robust model that can differentiate between **normal** and **adenocarcinoma** cases.

- Current dataset: **198 Adenocarcinoma** + **148 Normal** samples (small dataset).  
- To improve generalization, the dataset can be extended with **Kaggle chest X-ray datasets** and trained for more epochs.  

---

## 🚀 Approach

1. **Transfer Learning with VGG16**  
   - Used **VGG16 pretrained on ImageNet** as the base model.  
   - Implemented **transfer learning** for feature extraction and fine-tuning.  

2. **Modular Pipeline**  
   - Each component is implemented separately:
     - **Data Ingestion**
     - **Prepare Base Model**
     - **Model Training**
     - **Evaluation**

3. **Configuration Driven**  
   - All **file paths** are managed in `config.yaml`.  
   - All **hyperparameters** are defined in `params.yaml`.  

4. **Best Practices**  
   - Used **`dataclasses`** in `entity.py`.  
   - **Configuration Manager** handles object creation and dependency management.  
   - **Training pipeline** (`main.py`) orchestrates all components.  

5. **Experiment Tracking**  
   - **DVC** used for pipeline reproducibility.  
     - `dvc.yaml` defines all steps.  
     - `dvc repro` reruns only modified components.  
   - **MLflow + Dagshub** used to log experiments, metrics, and parameters.  

6. **Deployment**  
   - Flask-based **User Interface** (HTML + CSS) to upload X-rays and get predictions.  
   - Dockerize the App and deploy in AWS.  

---

### 📂 Project Structure
```

├── .github
│   └── workflows
│       └── .gitkeep
├── src
│   └── Chest_cancer_classification
│       ├── __init__.py
│       ├── components
│       │   └── __init__.py
│       ├── utils
│       │   └── __init__.py
│       ├── config
│       │   ├── __init__.py
│       │   └── configuration.py
│       ├── pipeline
│       │   └── __init__.py
│       ├── entity
│       │   └── __init__.py
│       └── constants
│           └── __init__.py
├── config
│   └── config.yaml
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── setup.py
├── research
│   └── trials.ipynb
├── templates
│   └── index.html
├── static
│   └── css
│       └── style.css
├── App.py
└── main.py
```

## ⚙️ Tech Stack

- **Python** 🐍  
- **TensorFlow / Keras** (Deep Learning)  
- **VGG16** (Transfer Learning)  
- **DVC** (Pipeline & Data Versioning)  
- **MLflow + Dagshub** (Experiment Tracking)  
- **Flask** (User Interface)  
- **Docker** (Containerization)  
- **AWS** (Deployment)  

---

## 📊 Results

- Trained on a **small dataset** (198 Adenocarcinoma, 148 Normal).  
- Achieved **promising results** with VGG16 Transfer Learning.  
- Performance is expected to **improve with larger datasets** (e.g., from Kaggle) and extended training.  

---

## 🛠️ How to Run Locally

**Clone the repository**
   ```bash
   git clone https://github.com/yourusername/chest-xray-classification.git
   cd chest-xray-classification
```

**Create virtual environment and activate it**
```bash
python -m venv venv
source venv/bin/activate    # on Mac/Linux
venv\Scripts\activate       # on Windows
```

### Install requirements

```bash
pip install -r requirements.txt
```

### 🚀 Run Pipeline

```bash
python main.py
```

### 🔄 Reproduce with DVC

```bash
dvc repro
```

### 🖥️ Launch the Flask App (UI development in progress)

```bash
python App.py
```
# AWS CICD Deployment with GitHub Actions

## 1. Login to AWS Console
Log in to your AWS account to start the setup.

---

## 2. Create IAM User for Deployment
Create a new IAM user with **specific access**:

- **EC2 Access:** For managing virtual machines.  
- **ECR Access:** Elastic Container Registry to save your Docker images in AWS.

---
## Create ECR Repository

Create an **ECR repository** to store/save your Docker images.

- Save the repository URI for later use:  905418209639.dkr.ecr.eu-north-1.amazonaws.com/cancer-proj
---

## 4. Description: About the Deployment
The deployment workflow:

1. Build Docker image of the source code.  
2. Push your Docker image to ECR.  
3. Launch your EC2 instance.  
4. Pull your image from ECR on EC2.  
5. Launch your Docker image in EC2.

---

## 4. Policy
Attach the following policies to your IAM user:

- `AmazonEC2ContainerRegistryFullAccess`  
- `AmazonEC2FullAccess`
---

## 5. Create EC2 Machine
- Use **Ubuntu** as the operating system.

---
## Configure EC2 as Self-Hosted Runner

1. Go to your GitHub repository **Settings → Actions → Runners → New self-hosted runner**.  
2. Choose your **operating system**.  
3. Follow the instructions and run the commands on your EC2 instance **one by one** to register it as a self-hosted runner.
---

## 7. Install Docker on EC2
**Optional:**
```bash
sudo apt-get update -y

sudo apt-get upgrade -y
#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

## Setup GitHub Secrets

In your GitHub repository, configure the following secrets:

- `AWS_ACCESS_KEY_ID` = *your AWS access key ID*
- `AWS_SECRET_ACCESS_KEY` = *your AWS secret access key*
- `AWS_REGION` = *Region*
- `AWS_ECR_LOGIN_URI` = `905418209639.dkr.ecr.eu-north-1.amazonaws.com/cancer-proj`
- `ECR_REPOSITORY_NAME` = ``



