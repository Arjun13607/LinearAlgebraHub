import streamlit as st
import numpy as np
import sympy as sp

st.set_page_config(page_title="Linear Algebra Calculator", layout="centered")

st.title("📐 Linear Algebra Calculator")

st.markdown("---")

# 1) Dimension Theorem
st.header("1) Dimension Theorem")
dimV = st.number_input("Enter Dimension of Domain (V):", min_value=0, step=1)
dimKer = st.number_input("Enter Dimension of Kernel (Ker(T)):", min_value=0, step=1)

if st.button("Calculate Image Dimension"):
    if dimKer > dimV:
        st.error("Kernel dimension cannot be greater than domain dimension.")
    else:
        st.success(f"Dimension of Image (Im(T)) = {dimV - dimKer}")

st.markdown("---")

# 2) Matrix Representation
st.header("2) Matrix Representation of Linear Transformation")
matrix_input = st.text_area(
    "Enter matrix (comma separated rows, semicolon for new row):",
    "1,2;3,4"
)

if st.button("Show Matrix"):
    try:
        matrix = np.array([[float(num) for num in row.split(",")] for row in matrix_input.split(";")])
        st.write("Matrix Representation:")
        st.write(matrix)
    except:
        st.error("Invalid matrix format! Use e.g. 1,2;3,4")

st.markdown("---")

# 3) Eigenvalues and Eigenvectors
st.header("3) Eigenvalues and Eigenvectors of Linear Transformation")
eig_input = st.text_area(
    "Enter square matrix (comma separated rows, semicolon for new row):",
    "4,1;2,3"
)

if st.button("Calculate Eigenvalues & Eigenvectors"):
    try:
        eig_matrix = sp.Matrix([[float(num) for num in row.split(",")] for row in eig_input.split(";")])
        if eig_matrix.shape[0] != eig_matrix.shape[1]:
            st.error("Matrix must be square!")
        else:
            eigen_data = eig_matrix.eigenvects()
            st.subheader("Eigenvalues and Eigenvectors")
            for val, mult, vects in eigen_data:
                st.write(f"Eigenvalue: {val}")
                for v in vects:
                    st.write(f"Eigenvector: {v}")
    except:
        st.error("Invalid matrix format! Use e.g. 4,1;2,3")