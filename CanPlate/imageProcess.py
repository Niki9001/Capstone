import cv2
import numpy as np

def process_license_plate(image):
    # 高斯去噪
    image = cv2.GaussianBlur(image, (3, 3), 0)
    # 灰度处理
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # 自适应阈值处理
    ret, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)
    # 去除一些小的白点和进行形态学操作
    #kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
    #kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
    # 膨胀，腐蚀
    #thresh_image = cv2.dilate(thresh_image1, kernelX)
    #thresh_image = cv2.erode(thresh_image, kernelX)
    # 腐蚀，膨胀
    #thresh_image = cv2.erode(thresh_image, kernelY)
    #thresh_image = cv2.dilate(thresh_image, kernelY)

    # 使用cv2.RETR_TREE模式寻找轮廓
    #contours, hierarchy = cv2.findContours(thresh_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 400]

    # 绘制轮廓
    #cv2.drawContours(image, filtered_contours, -1, (255, 0, 0), 2)


    return thresh_image
