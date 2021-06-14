import cv2 
import numpy as np 

class helper(): 
    def __init__(self, numTracker, range): 
        self.numTracker = numTracker
        self.range = range
    
    def nothing(self, x):
        pass
   
    def tracker(self):
        cv2.namedWindow('img')
        for i in range(self.numTracker):
            cv2.createTrackbar(str(i), 'img', 
            self.range[i][0], self.range[i][1], 
            self.nothing)
    
    def trackpos(self,img): 
        while True: 
            val =np.zeros(self.numTracker)
            for i in range(self.numTracker):
                val[i] = cv2.getTrackbarPos(str(i),'img')
            cv2.imshow("img")
            #insert code here 
            print(val)
            k = cv2.waitKey(0)
            if k == ord('q'):
                cv2.destroyAllWindows()
                break 



