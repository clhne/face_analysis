from PIL import Image
import face_recognition
import cv2
img = face_recognition.load_image_file("../images/imggroup.jpg")
face_locations = face_recognition.face_locations(img)
face_landmarks_list = face_recognition.face_landmarks(img)
i = 0
'''
for face_location in face_locations:
    top, right, bottom, left = face_location
    face_img = img[top:bottom,left:right]
    pil_img = Image.fromarray(face_img)
    pil_img.save("imggroup_face"+str(i)+".jpg")
    i = i + 1

'''
#use python opencv
img = cv2.imread("../images/imggroup.jpg")
face_num = len(face_locations)
for i in range(0, face_num):
    top = face_locations[i][0]
    right = face_locations[i][1]
    bottom = face_locations[i][2]
    left = face_locations[i][3]

    start = (left, top)
    end = (right, bottom)
    color = (55,255,255)
    thickness = 3
    cv2.rectangle(img, start, end, color, thickness)
    cv2.imwrite("imggroup_faces.jpg",img)

#cv2.namedWindow("recognition")
#cv2.imshow("recognition",img)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

#'''
