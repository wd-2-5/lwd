import cv2
def callback(pos):
    print(pos)
    print("当前用户滑动了滑动条")
cv2.nanedwindow("win")
bar = cv2.createtrackbar("example","win",0,20,)