# cv2.findContours()

#  cv2.drawContours() 


# Here's the step-by-step approach to detecting shapes:

    # Import module done 
    # Import image  done 
    # Convert it to grayscale image
    # Apply thresholding on image and then find out contours.

    # Run a loop in the range of contours and iterate through it.


    # In this loop draw a outline of shapes Using drawContours() and find out center point of shape.
    # Classify the detected shape on the basis of a number of contour points it has and put the detected shape name at the center point of shape



# contours_approximation:

#     cv.CHAIN_APPROX_NONE It will store all the boundary points.
#     cv.CHAIN_APPROX_SIMPLE It will store number of end points (eg.In case of rectangle it will store 4)


# Return value: list of contour points

# 100 → 0 (black)
# 130 → 255 (white)
# 200 → 255 (white)


# cv.DrawContours(src, contour, contourIndex, colour, thickness)

# cv2.findContours(src, contour_retrieval, contours_approximation)


import cv2
import numpy as np
from matplotlib import pyplot as plt
 
image = cv2.imread("/home/rawan/Desktop/object-color-detection-/test.jpg")
print (image is None )

resized = cv2.resize(image, (800, 600)) 


grayscale_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

threshold = cv2.adaptiveThreshold(grayscale_image, 255, 
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                  cv2.THRESH_BINARY, 37, 9)



# contour 
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



for i, contour in enumerate(contours):
    if i == 0:
        continue

    # Approximate contour shape
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)

    # Draw contour
    cv2.drawContours(resized, [contour], 0, (0, 0, 255), 5)

    # Find center
    M = cv2.moments(contour)
    if M['m00'] != 0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

    slides = len(approx)

    print("Contour", i, "Vertices:", len(approx))

    if (slides == 3 ):
        label = "triangle"
    elif(slides == 4 ):
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h

        if 0.95 <= aspect_ratio <= 1.05: 
          label  = "square"

        else:
          label  = "rectangle"
    else :
       label = "circle "
        

    # Label the shape
    cv2.putText(resized, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 2)
cv2.imshow("shapes", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


    

# ////////////////////////////////color detection ////////////////////////////////////
