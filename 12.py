import cv2, time
import math
x=1
video=cv2.VideoCapture(0)
for i in range(3):
	x=str(int(i))
		
	check , frame = video.read()
 
	
	print(check)
	
	print(frame)

	cv2.imshow('capturing',frame)

	cv2.waitKey(10)
	cv2.imwrite( 'image '+ x +'.jpg',frame)
	

video.release()
print('done')

#destroy all windows 
cv2.destroyAllWindows()
