import io
from flask import Flask, request, jsonify, render_template
from PIL import Image
from io import BytesIO
import boto3
import base64
import datetime

app = Flask(__name__)

rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('imageFile')
    if file:
        stream = io.BytesIO()
        image = Image.open(file)
        image.save(stream, format="JPEG")
        image_binary = stream.getvalue()
    else:
        print('No file in request')


    response = rekognition.search_faces_by_image(
            CollectionId='family_collection',
            Image={'Bytes':image_binary}                                       
            )

    for match in response['FaceMatches']:
        face = dynamodb.get_item(
            TableName='family_collection',  
            Key={'RekognitionId': {'S': match['Face']['FaceId']}}
            )

        if 'Item' in face:
            student_name = face['Item']['FullName']['S']
            attendance = dynamodb.get_item(
                TableName='attendance',
                Key={'student_id': {'S': student_name}, 'date': {'S': datetime.datetime.now().strftime("%Y-%m-%d")}}
            )
            if 'Item' in attendance:
                message = "Attendance already marked for today"
            else:
                dynamodb.put_item(
                    TableName='attendance',
                    Item={
                        'student_id': {'S': student_name},
                        'date': {'S': datetime.datetime.now().strftime("%Y-%m-%d")}
                    }
                )
                message = 'Attendance marked'
        else:
            message = 'No match found in person lookup'

    return render_template('index.html', message=message)

@app.route('/attendance', methods=['GET'])
def get_attendance():
    response = dynamodb.scan(TableName='attendance')
    attendance_records = []
    for item in response['Items']:
        record = {
            'student_id': item['student_id']['S'],
            'date': item['date']['S']
        }
        attendance_records.append(record)

    return jsonify(attendance_records)

if __name__ == '__main__':
    app.run(debug=True)
