# import datetime
# import boto3
# import io
# from PIL import Image

# rekognition = boto3.client('rekognition', region_name='us-east-1')
# dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    
# image = Image.open("AE.jpg")
# stream = io.BytesIO()
# image.save(stream,format="JPEG")
# image_binary = stream.getvalue()

# response = rekognition.search_faces_by_image(
#         CollectionId='family_collection',
#         Image={'Bytes':image_binary}                                       
#         )

# for match in response['FaceMatches']:
#     face = dynamodb.get_item(
#         TableName='family_collection',  
#         Key={'RekognitionId': {'S': match['Face']['FaceId']}}
#         )
    
#     if 'Item' in face:
#         print ("The face identified is:", face['Item']['FullName']['S'])
#         # If face is identified, check attendance
#         attendance = dynamodb.get_item(
#             TableName='attendance',
#             Key={'student_id': {'S': face['Item']['FullName']['S']}, 'date': {'S': datetime.datetime.now().strftime("%Y-%m-%d")}}
#         )
#         if 'Item' in attendance:
#             print("Attendance marked for today")
#         else:
#             print('No attendance marked for today')
#     else:
#         print ('No match found in person lookup')


# 2nd code working great
# import datetime
# import boto3
# import io
# from PIL import Image

# rekognition = boto3.client('rekognition', region_name='us-east-1')
# dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    
# image = Image.open("APJK.jpg")
# stream = io.BytesIO()
# image.save(stream,format="JPEG")
# image_binary = stream.getvalue()

# response = rekognition.search_faces_by_image(
#         CollectionId='family_collection',
#         Image={'Bytes':image_binary}                                       
#         )

# for match in response['FaceMatches']:
#     face = dynamodb.get_item(
#         TableName='family_collection',  
#         Key={'RekognitionId': {'S': match['Face']['FaceId']}}
#         )
    
#     if 'Item' in face:
#         print ("The face identified is:", face['Item']['FullName']['S'])
#         # If face is identified, check attendance
#         attendance = dynamodb.get_item(
#             TableName='attendance',
#             Key={'student_id': {'S': face['Item']['FullName']['S']}, 'date': {'S': datetime.datetime.now().strftime("%Y-%m-%d")}}
#         )
#         if 'Item' in attendance:
#             print("Attendance already marked for today")
#         else:
#             print('No attendance marked for today')
#             print('Marking attendance now...')
#             # Mark attendance
#             dynamodb.put_item(
#                 TableName='attendance',
#                 Item={
#                     'student_id': {'S': face['Item']['FullName']['S']},
#                     'date': {'S': datetime.datetime.now().strftime("%Y-%m-%d")}
#                 }
#             )
#             print('Attendance marked')
#     else:
#         print ('No match found in person lookup')

# 3rd code working great

# import datetime
# import boto3
# import io
# from PIL import Image

# rekognition = boto3.client('rekognition', region_name='us-east-1')
# dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# def print_attendance_table():
#     # Retrieve all attendance records
#     response = dynamodb.scan(TableName='attendance')

#     # Print the attendance table
#     print("\nAttendance Table:")
#     print("{:<20} {:<10}".format('Student ID', 'Date'))

#     for item in response['Items']:
#         print("{:<20} {:<10}".format(item['student_id']['S'], item['date']['S']))
    
# image = Image.open("TS.jpg")
# stream = io.BytesIO()
# image.save(stream,format="JPEG")
# image_binary = stream.getvalue()

# response = rekognition.search_faces_by_image(
#         CollectionId='family_collection',
#         Image={'Bytes':image_binary}                                       
#         )

# for match in response['FaceMatches']:
#     face = dynamodb.get_item(
#         TableName='family_collection',  
#         Key={'RekognitionId': {'S': match['Face']['FaceId']}}
#         )
    
#     if 'Item' in face:
#         print ("The face identified is:", face['Item']['FullName']['S'])
#         # If face is identified, check attendance
#         attendance = dynamodb.get_item(
#             TableName='attendance',
#             Key={'student_id': {'S': face['Item']['FullName']['S']}, 'date': {'S': datetime.datetime.now().strftime("%Y-%m-%d")}}
#         )
#         if 'Item' in attendance:
#             print("Attendance already marked for today")
#         else:
#             print('No attendance marked for today')
#             print('Marking attendance now...')
#             # Mark attendance
#             dynamodb.put_item(
#                 TableName='attendance',
#                 Item={
#                     'student_id': {'S': face['Item']['FullName']['S']},
#                     'date': {'S': datetime.datetime.now().strftime("%Y-%m-%d")}
#                 }
#             )
#             print('Attendance marked')

#         # Print the attendance table after marking attendance
#         print_attendance_table()
#     else:
#         print ('No match found in person lookup')


# 4th code working great

