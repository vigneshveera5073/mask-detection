#linux open cv install ->sudo apt-get install opencv
import cv2

video = cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count = 0

while True:
	ret, frame = video.read()
	faces = facedetect.detectMultiScale(frame, 1.3, 5)
	for x, y, w, h in faces:
		count = count + 1
#detect image save file port
		name = '~/python/Face_Mask_Detection-Using-Python--main/face_without_mask' + str(count) + '.jpg'
		print("Creating Images........." + name)
		cv2.imwrite(name, frame[y:y+h, x:x+w])
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
		#cv2.rectangle(frame, (x, y-40), (x + w, y), (0, 255, 0), -1)
		cv2.putText(frame, "No Mask", (x+15 , y-15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, (0, 0, 255), 1)

	cv2.imshow("WindowFrame", frame)
	cv2.waitKey(50)
#minime five hundred image save file
	if count > 500:
		break
cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()
