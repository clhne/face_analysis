import face_recognition
jobs_img = face_recognition.load_image_file("../images/jobs.jpg")
obama_img = face_recognition.load_image_file("../images/obama.jpg")
test_img = face_recognition.load_image_file("../images/test_jobs.jpeg")

jobs_encoding = face_recognition.face_encodings(jobs_img)[0]
obama_encoding = face_recognition.face_encodings(obama_img)[0]
test_encoding = face_recognition.face_encodings(test_img)[0]

results = face_recognition.compare_faces([jobs_encoding,obama_encoding],test_encoding)
labels = ['jobs','obama']

print 'results:'+str(results)

for i in range(0,len(results)):
    if results[i] == True:
        print 'The person is:'+labels[i]


