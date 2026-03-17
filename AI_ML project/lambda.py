import json
import boto3
import urllib.parse
from datetime import datetime

s3 = boto3.client("s3")
comprehend = boto3.client("comprehend")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ResumeAnalysis")

def calculate_score(text):
    score = 50
    text_lower = text.lower()

    keywords = {
        "aws": 10,
        "python": 10,
        "sql": 8,
        "machine learning": 10,
        "docker": 8,
        "kubernetes": 8,
        "testing": 6,
        "selenium": 6,
        "react": 6,
        "javascript": 6,
        "ci/cd": 8,
        "terraform": 8,
        "linux": 6
    }

    matched_skills = []

    for keyword, points in keywords.items():
        if keyword in text_lower:
            score += points
            matched_skills.append(keyword)

    if score > 100:
        score = 100

    return score, matched_skills

def lambda_handler(event, context):

    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])

    response = s3.get_object(Bucket=bucket, Key=key)
    file_content = response["Body"].read().decode("utf-8")

    comprehend_response = comprehend.detect_entities(
        Text=file_content[:4500],
        LanguageCode="en"
    )

    entities = [entity["Text"] for entity in comprehend_response.get("Entities", [])]

    key_phrases_response = comprehend.detect_key_phrases(
        Text=file_content[:4500],
        LanguageCode="en"
    )

    key_phrases = [phrase["Text"] for phrase in key_phrases_response.get("KeyPhrases", [])]

    score, matched_skills = calculate_score(file_content)

    item = {
        "resume_id": key,
        "uploaded_at": datetime.utcnow().isoformat(),
        "resume_text": file_content,
        "entities": entities,
        "key_phrases": key_phrases,
        "matched_skills": matched_skills,
        "score": score
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "resume_id": key,
            "score": score,
            "matched_skills": matched_skills
        })
    }