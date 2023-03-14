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
        # converted_img = np.array(image.convert('RGB'))
        gray_scale = cv2.cvtColor(uploaded_file, cv2.COLOR_RGB2GRAY)
        output = image.copy()


        st.image(output)

        
        # col1, col2 = st.columns( [0.5, 0.5])
        # with col1:
        #     st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)

        # with col2:
        #     st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)


if __name__ == '__main__':
    main()