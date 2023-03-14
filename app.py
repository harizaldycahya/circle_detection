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


        # image = cv2.imread(args["image"])
        output = image.copy()
        gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)


        # tambahan
        # detect circles in the image
        circles = cv2.HoughCircles(gray_scale, cv2.HOUGH_GRADIENT, 1.2, 100)
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)


        st.image(output)

        
        # col1, col2 = st.columns( [0.5, 0.5])
        # with col1:
        #     st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)

        # with col2:
        #     st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)


if __name__ == '__main__':
    main()