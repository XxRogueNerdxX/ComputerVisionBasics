import cv2 
import numpy as np 


#importing image 
'''
img = cv2.imread(r'C:\\ComputerVision\\OpenCV\\Basics\\lena.jpg')
print(img)
cv2.imshow('image', img)
k = cv2.waitKey(0)   waitKey(0) : infinite display else ms
if k == ord('s'):
    cv2.destroyAllWindows()
'''


'''
#video capture 
cap = cv2.VideoCapture(0) #Could add video path 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))


while(True):
    ret, frame = cap.read()
    if ret:
        out.write(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
       
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('Wrong')
        break
cap.release()
out.release()
cv2.destroyAllWindows()
'''


#adding geomenttry 
'''
img = cv2.imread(r'C:\\ComputerVision\\OpenCV\\Basics\\lena.jpg')
print(img)
img = np.zeros([512, 512, 3], np.uint8)
img = cv2.line(img, (0,0), (255, 255), (0,0,0), 10)  #image_variable, start_pix, end_pix, color(BGR), thickness
img = cv2.line(img, (0,255), (255, 255), (0,0,0), 10)
img = cv2.rectangle(img, (348, 0), (510, 128), (0,255,0), 3) #rectangle 
img = cv2.circle(img, (447, 63), 63, (0,0,255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''



#Changing video aspect and adding geomentry 
'''
cap = cv2.VideoCapture(0) #Could add video path 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = cv2.line(frame, (0,0), (255, 255), (0,0,0), 10) adding line to video 
        cv2.imshow('frame', frame)
       
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print('Wrong')
        break
cap.release()
cv2.destroyAllWindows()
'''

#mouse Recog        #CHECK YOUR WAY !!!!!!!!
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)
'''
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 1, (255,255,255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('imag', img)

points = []
img = np.zeros([512, 512, 3], dtype = np.uint8)
cv2.imshow('imag', img)
cv2.setMouseCallback('imag', click_event )
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
#get image color in new window
'''
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 1, (25   5,255,255), -1)
        b = img[x,y,0]
        g = img[x,y,1]
        r = img[x,y,2]
        print(b,g,r)
        colorimg = np.zeros((512, 512, 3), np.uint8)
        colorimg[:] = [b, g, r]
        cv2.imshow('color', colorimg)



img = cv2.imread(r'C:\\ComputerVision\\OpenCV\\Basics\\lena.jpg')
cv2.imshow('imag', img)
cv2.setMouseCallback('imag', click_event )
cv2.waitKey(0)
cv2.destroyAllWindows()


'''