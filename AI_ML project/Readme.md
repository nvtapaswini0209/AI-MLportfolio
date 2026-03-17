# AI Resume Analyzer – AWS Serverless Project

## Project Overview
The AI Resume Analyzer is a serverless cloud application built on AWS that automatically analyzes resumes and extracts insights such as detected skills, entities, and resume scores.

The system processes uploaded resume files using AWS serverless services and Natural Language Processing (NLP).

---

## Architecture

The application follows an event-driven serverless architecture.

User uploads resume → Amazon S3 → AWS Lambda → Amazon Comprehend → DynamoDB → CloudWatch

### Architecture Diagram
![Architecture](architecture/architecture-diagram.png)

---

## AWS Services Used

Amazon S3 – Stores uploaded resume files

AWS Lambda – Processes resumes automatically when files are uploaded

Amazon Comprehend – Performs NLP analysis to detect entities and key phrases

Amazon DynamoDB – Stores resume analysis results

Amazon CloudWatch – Logs and monitors Lambda execution

---

## Workflow

1. User uploads a resume text file into the S3 bucket.
2. The S3 event automatically triggers the Lambda function.
3. Lambda reads the resume text file.
4. The text is sent to Amazon Comprehend for NLP analysis.
5. Comprehend detects entities and key phrases.
6. Lambda calculates a resume score based on detected skills.
7. Results are stored in DynamoDB.
8. CloudWatch records logs for monitoring.

---

## Example Resume Input

Name: John Doe  
Skills: Python, AWS, SQL, Machine Learning  
Experience: Software Engineer working on cloud infrastructure

---

## Example Output

Resume Score: 84

Detected Skills
- AWS
- Python
- SQL

Entities
- AWS
- Python

Key Phrases
- cloud infrastructure
- data pipelines

---

## Project Features

Serverless architecture  
Event-driven processing  
Automatic resume analysis  
Skill detection using NLP  
Cloud monitoring and logging  

---

## Challenges

The AWS sandbox environment restricted Amazon Textract access.

To overcome this limitation, the architecture was modified to process text-based resumes instead of PDF files.

---

## Future Improvements

Add Textract for PDF resume parsing  
Add Bedrock for AI feedback generation  
Build a frontend interface for uploading resumes  
Add CI/CD pipeline using AWS CodePipeline

---

## Skills Demonstrated

AWS Cloud Architecture  
Serverless Computing  
Natural Language Processing  
Event-Driven Systems  
Cloud Monitoring

---

## Author
Venkata Tapaswini Nallana