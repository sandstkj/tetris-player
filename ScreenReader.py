import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()

red = (0, 0, 255);
black = (0, 0, 0);

boardwidth = 10;
boardheight = 20;
blocklength = 26;

startx = 807;
starty = 380; #390
endx = startx + (blocklength+1) * boardwidth;
endy = starty + (blocklength+1) * boardheight;

while(True):
	printscreen_pil = ImageGrab.grab(bbox=(startx, starty, endx, endy))
	#printscreen_numpy = np.array(printscreen_pil.getdata()), dtype='uint8')
	
	print('loop took {} seconds'.format(time.time()-last_time))
	last_time = time.time()
	#x = (startx + endx) / 2;
	#y = (starty + endy) / 2;
	
	row = ""
	for y in range(blocklength, endy - starty, blocklength):
		print(row)
		row = ""
		
		for x in range(blocklength, endx - startx, blocklength):
			if printscreen_pil.getpixel((x,y)) == black:
				row = row + " "
			else:
				row = row + ("X")
		
			printscreen_pil.putpixel((x, y), red);
		#print(printscreen_pil.getpixel((x,y)));
			
	
	print(row)
	print("----------------------------------")
			
	cv2.imshow('window', np.array(printscreen_pil))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break