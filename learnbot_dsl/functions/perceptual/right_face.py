from __future__ import print_function, absolute_import
import cv2
import numpy as np
import sys, os

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
import visual_auxiliary as va

def right_face(lbot, params=None, verbose=False):
    frame = lbot.getImage()
    mat = va.detect_face(frame)
    if mat[0][2] is not 0 or mat[1][2] is not 0 or mat[2][2] is not 0:
        return True
    return False
