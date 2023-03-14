import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os


def main():
    """ Judul Aplikasi """
    st.title("Circle Detection App")
    st.text("loremdsadasdasdasd")
    maxRadiusInput = st.sidebar.slider(
        'Select a range of values',
        0, 100, 25)
    param1 = st.sidebar.slider(
        'Select a param1 of values',
        0, 100, 25)
    param2 = st.sidebar.slider(
        'Select a param2 of values',
        0, 100, 25)
    # tipe=type(maxRadiusInput)
    st.write('Max Radius:', maxRadiusInput)
    uploaded_file = st.sidebar.file_uploader("", type=['jpg','png','jpeg'])

    #Add 'before' and 'after' columns
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.sidebar.image(uploaded_file)
        converted_img = np.array(image.convert('RGB'))
        gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
        # img = cv2.medianBlur(gray_scale, 5)
        gray_scale = cv2.medianBlur(gray_scale, 5)
        rows = gray_scale.shape[0]
        circles = cv2.HoughCircles(gray_scale, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                param1=param1, param2=param2,
                                minRadius=0, maxRadius=maxRadiusInput)


        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(converted_img, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(converted_img, center, radius, (255, 0, 255), 3)


        st.image(converted_img)

if __name__ == '__main__':
    main()