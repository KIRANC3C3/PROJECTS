import cv2

#######################
cap = cv2.VideoCapture(1)
cap.set(3, 500)
cap.set(4, 500)
#################

count=0
minArea = 500
nplatecascade = cv2.CascadeClassifier("resourses/haarcascade_russian_plate_number.xml")
while True:

    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberplate = nplatecascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberplate:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)
            cv2.putText(img, "number plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 5)

            imgintrest = img[y:y + h, x:x + w]
            cv2.imshow("intrest", imgintrest)

    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("resourses/SCANNED/plate_"+str(count)+".jpg",imgintrest)
        cv2.rectangle(img,(0,100),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"scan saved",(150,250),cv2.FONT_HERSHEY_COMPLEX,2,(0,225,0),5)
        count+=1
        cv2.imshow("result1",img)
        cv2.waitKey(5000)

# number_plate=cv2.CascadeClassifier()
