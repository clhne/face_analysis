from PIL import Image
import face_recognition
img = face_recognition.load_image_file("wang.jpg")
face_locations = face_recognition.face_locations(img)
face_landmarks_list = face_recognition.face_landmarks(img)

for face_location in face_locations:
    top, right, bottom, left = face_location
    face_img = img[top:bottom,left:right]
    pil_img = Image.fromarray(face_img)
    pil_img.save("imggroup_face.jpg")
