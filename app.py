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
        # gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
        

        # Edited
        gray = cv2.cvtColor(uploaded_file, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(gray, 5)

        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1,120, param1=100, param2=30, minRadius=0, maxRadius=0)
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            # Outer Circle
            cv2.circle(uploaded_file, (i[0], i[1]), i[2], (0,255,0), 2)

            # center circle
            cv2.circle(uploaded_file, (i[0], i[1]), 2, (0,255,0), 3)
        # End Edited
        st.image(uploaded_file)

        # col1, col2 = st.columns( [0.5, 0.5])
        # with col1:
        #     st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)

        # with col2:
        #     st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)


if __name__ == '__main__':
    main()