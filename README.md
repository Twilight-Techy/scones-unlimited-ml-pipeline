# 🚦 Scones Unlimited: Image Classification Workflow on AWS

## 📌 Project Overview
Scones Unlimited is a serverless, event-driven workflow for **image classification of delivery vehicles**. It uses **AWS Step Functions**, **Lambda**, and a deployed **machine learning model** to classify incoming images (e.g., bicycles, motorcycles).  
This project demonstrates how to build a scalable ML pipeline that ingests input images, classifies them using an inference endpoint, and routes results accordingly.  

---

## 🛠️ Tech Stack
- **AWS Lambda** – serverless compute functions  
- **AWS Step Functions** – workflow orchestration  
- **Amazon SageMaker** – ML model endpoint for inference  
- **Amazon S3** – input/output data storage  
- **Amazon SNS** *(optional)* – notifications on errors or events  
- **Python** – Lambda function code  

---

## ⚙️ Workflow Architecture
1. **Image Ingestion** – Input images are uploaded as Base64 strings.  
2. **Preprocessing Lambda** – Decodes and prepares the image for inference.  
3. **Inference Lambda** – Sends image to SageMaker endpoint for prediction.  
4. **Postprocessing Lambda** – Interprets predictions and decides next steps.  
5. **Fan-out Support (Optional)** – Workflow can process multiple images in parallel.  
6. **Visualization** – Model predictions are visualized with test data.  

<p align="center">  
  <img src="docs\Screenshot 2025-09-15 001524.png" alt="Step Function Workflow" width="600"/>  
</p>  

---

## ✨ Features
- ✅ Event-driven architecture with AWS Step Functions  
- ✅ ML inference using SageMaker deployed model  
- ✅ Parallel fan-out workflow (optional challenge)  
- ✅ Data visualization for predictions *(extra)*  
- ✅ Error handling with Step Function + SNS notifications (optional)  
- ✅ Scalable, serverless deployment  

---

## 📊 Visualization Example
Here’s an example of the model output visualization with CIFAR-10 vehicle classes:  

<p align="center">  
  <img src="visualization_screenshots/Screenshot 2025-09-15 103457.png" alt="Model Prediction Visualization" width="500"/>  
</p>  

---

## 🚀 Getting Started
### Prerequisites
- AWS account with access to Lambda, Step Functions, S3, SageMaker  
- Python 3.8+  
- IAM roles configured for Lambda & Step Functions  

### Setup
1. Deploy Lambda functions (`lambda_function.py`)  
2. Create SageMaker endpoint with trained CIFAR model  
3. Define Step Function using `state_machine.json`  
4. Test with sample images  

---

## 📂 Project Structure

``` markdown
├── lambda.py
├── CIFARStateMachine.asl.json
├── visualization_screenshots/
│   └── [visualization images]
├── starter.ipynb
├── test.lst
├── train.lst
└── README.md
```

---

## 📝 Results & Learnings
Through building this project, I was able to:
- Learn how to design **event-driven architectures** with AWS Step Functions.  
- Understand how to **chain multiple Lambda functions** into a production-style workflow.  
- Deploy and query a **SageMaker inference endpoint** for real-time ML predictions.  
- Visualize model outputs to monitor confidence and ensure threshold compliance.  
- Explore **optional challenges** like parallel fan-out workflows, error notifications with SNS, and scaling the workflow with more classes.  

**Key Takeaway:**  
This project reinforced the importance of combining **machine learning** with **cloud-native serverless design** to create systems that are not only accurate, but also scalable, maintainable, and production-ready.  

---

## 🔮 Optional Enhancements
- Add more classes from CIFAR dataset (cars, trucks, airplanes, etc.)  
- Build a dummy/test data generator for continuous image input  
- Use Step Functions fan-out for parallel image processing  
- Add SNS topic for error notifications  

---

## 📸 Demo Screenshots
*(Insert screenshots of your Step Function running successfully, Lambda logs, and predictions here)*  

---

## 📖 Acknowledgements
This project is part of the **Udacity Machine Learning Engineer Nanodegree**.  
Built with ❤️ using **AWS** services.