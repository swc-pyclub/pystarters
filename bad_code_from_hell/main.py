#!/usr/bin/env python
# -*- coding: utf-8 -*-
from skimage.exposure import rescale_intensity


def mk_background(vname, n=1000, from_frame=0):
    '''
    Creates a backround image from the average of 'n' frames
    from video 'vname'.

    Returns an array of the same size as each frame in vname.
    '''
    my_vid = cv2.VideoCapture(vname)
    my_vid.set(cv.CV_CAP_PROP_POS_FRAMES, from_frame)
    my_y, my_x = (int(my_vid.get(cv.CV_CAP_PROP_FRAME_HEIGHT)), int(my_vid.get(cv.CV_CAP_PROP_FRAME_WIDTH)))
    buf = np.empty( (my_y, my_x, n), dtype=np.uint8 )
    for i in range(n):
        ret_val, img = my_vid.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        buf[:,:,i]=img
    my_vid.release()
    return buf.mean(2).astype(np.uint8)

def playVid(video, vidName):
    """
    Play the video
    """
    cv.NamedWindow(vidName, 1)
    while True:
        ret_val, frame = video.read()
        if ret_val is False: break
        cv2.imshow(vidName, frame)
        if (cv2.waitKey(30) != -1):
            cv.DestroyWindow(vidName)
            break

def getMindur(duration):
    '''
    Returns total duration in string format min:sec
    '''
    return '{:02}:{:02}'.format(int(duration // 60.), int(duration % 60.))


## === Set variables === ##

videoFile    = './videos/teleporter.h264'  # The file to load
background = "00:11"
start    = '00:27'  # When we track from
end      = "1:53"  # When we track to


dataFile     = 'data.tab'   # File name for ouput
writeToFile  = True         # False | True

## === End set variables === ##


## Begin.
# Threshold to create binary image. For red videos ~15 seems to
# work fine; for brighter ones set it to ~50.
#threshold = 15

MHI_DURATION = 0.1  # I don't remember 0.1 what

import os, sys, time
import cv2
from cv2 import cv
import numpy as np
from matplotlib import pyplot as plt
from skimage.segmentation import clear_border


if videoFile[len(videoFile) - 5: len(videoFile)] == '.txt':
    print "We dont' work with txt files"
    sys.exit()
if videoFile[len(videoFile) - 5: len(videoFile)] == '.doc':
    print "We dont' work with doc files"
    sys.exit()
if videoFile[len(videoFile) - 5: len(videoFile)] == '.pdf':
    print "We dont' work with doc files"
    sys.exit()
if videoFile[len(videoFile) - 5: len(videoFile)] == '.jpg':
    print "We dont' work with jpg files"
    sys.exit()
if videoFile[len(videoFile) - 5: len(videoFile)] == '.tif':  # TODO make work for tiff
    print "We dont' work with jpg files"
    sys.exit()
if videoFile[len(videoFile) - 5: len(videoFile)] == '.png':  # TODO: add eps, ai, ps, csv
    print "We dont' work with png files"
    sys.exit()


video = cv2.VideoCapture(videoFile)
print "Program starting with video" + videoFile

## Define functions.

def timeStrToFrame(timeStr, f):
    '''
    timeStr   Time string in format mm:ss.
    fps       Frames per second

    Returns the frame number that corresponds to that time.
    '''
    timeStr = [timeStr[0:timeStr.find(':')], timeStr[timeStr.find(':') + 1:]]
    if len(timeStr) == 2:
        s = int(timeStr[1]) + (int(timeStr[0]) * 60)  # The number of seconds
    else:
        raise NotImplementedError
    return s * f  # The frame

get_time = lambda: time.strftime('%Y.%m.%d %H:%M:%S')


## Initialise variables and arrays.

start = timeStrToFrame(start, int(video.get(cv.CV_CAP_PROP_FPS)));  end = timeStrToFrame(end, int(video.get(cv.CV_CAP_PROP_FPS))); bgFrameNumber = timeStrToFrame(background, int(video.get(cv.CV_CAP_PROP_FPS)))
print "Tracking from "+str(start) + "to" + str(end) + ". Background is at ".format(background)
print "Number of background frames"+str(bgFrameNumber)
currentFrame = int(video.get(cv.CV_CAP_PROP_POS_FRAMES))
vidSize = (int(video.get(cv.CV_CAP_PROP_FRAME_HEIGHT)), int(video.get(cv.CV_CAP_PROP_FRAME_WIDTH)))
mhi = np.empty(vidSize, np.float32)

if writeToFile:
    fout = open(dataFile, 'w')
    fout.writelines('{}\t{}\t{}\n'.format(\
            *['frameNum', 'centreX', 'centreY']))


## Read frames from video and detect motion.

# There seems to be a bug in opencv that prevents seeking for a
# specific frame in the video. Thus, we have to load each frame
# from the beginning and ignore the frames that are not needed.
while (currentFrame < end) == 1:
    # Read frame.
    ret, image = video.read()

    # Quit if no frame was read or the user cancels operation.
    if ((ret == 0) or (cv2.waitKey(1) != -1)):
        video.release()
        if writeToFile: fout.close()
        break

    currentFrame = int(video.get(cv.CV_CAP_PROP_POS_FRAMES))
    # Upon reading the designated background frame, convert to gray
    # display for reference.
    if (currentFrame == bgFrameNumber):
        bg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        plt.imshow(bg, plt.cm.Greys_r)
        plt.title("Background")
        plt.axis('off')        
        plt.show(block=False)

    # Ignore tracking if the current frame is not within the
    # required range.
    if (currentFrame < start):
        continue

    # Convert image to gray. Keep a colour copy for displaying.
    ctr = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Subtract background from image.
    imgsub = cv2.absdiff(image, bg)

    # Threshold image.
    ret, silh = cv2.threshold(imgsub, 15, \
                              255, cv2.THRESH_BINARY)

    # Update motion history.
    clear_border(silh)
    cv2.updateMotionHistory(silh, mhi, time.clock(), MHI_DURATION)

    # Find contours.
    mhi_int = mhi.astype(np.uint8)
    contours, hierarchy = cv2.findContours(mhi_int,\
            mode=cv2.RETR_LIST,
            method=cv2.CHAIN_APPROX_NONE)
    if (len(contours) > 0):
        cnt = contours[np.argmax([cv2.contourArea(c) for c in contours])]         # Find index of largest contour, which should be the mouse.
        # Fit an ellipse around the contour.
        cv2.drawContours(ctr, [cnt], 0, (255, 255, 255), 2)
        m = cv2.moments(cnt.astype(np.float32))
        try:
            c = [(m['m10'] / m['m00']), (m['m01'] / m['m00'])]  # Πονάει όταν πρέπει να μεταφράσεις σχόλια.
        except:
            c = [-1, -1]

            # Draw the ellipse in green on the frame for displaying
            # progress.
            # cv2.ellipse(ctr, ellipse, color=(0, 255, 0))
            #cv2.drawContours(img_colour, cnt, -1, (0,255,0))
            # Save ellipse params to text file.
            if writeToFile:
                fout.write('{}\t'.format(currentFrame))
                fout.write('{}\t{}\t'.format(*c))
    # Display progress.
    cv2.imshow(videoFile[videoFile.rfind('/')+1:len(videoFile)-5], ctr)
