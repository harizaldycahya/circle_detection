import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os


def main():
    """ Judul Aplikasi """
    st.title("Circle Detection App")
    st.text("loremdsadasdasdasd")

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
        circles = cv.HoughCircles(gray_scale, cv.HOUGH_GRADIENT, 1, rows / 8,
                                param1=100, param2=30,
                                minRadius=1, maxRadius=30)
        st.image(gray_scale)

if __name__ == '__main__':
    main()