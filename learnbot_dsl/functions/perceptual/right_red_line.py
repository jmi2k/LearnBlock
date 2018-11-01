from __future__ import print_function, absolute_import
import cv2
import numpy as np
import sys, os

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
import visual_auxiliary as va
def right_red_line(lbot, params=None, verbose=False):
	frame = lbot.getImage()
	rois = va.detect_red_line(frame)
	if verbose:
		print("Red points", rois)
	
	maxIndex = np.argmax(rois)
	if maxIndex==2 and rois[maxIndex]>20:
		return True
	return False
