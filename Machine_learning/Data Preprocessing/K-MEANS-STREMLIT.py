import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Title
st.title("Customer Segmentation using K-Means")

# File uploader
uploaded_file = st.file_uploader("Upload Mall_Customers.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    # Select features
    X = df.iloc[:, [3, 4]].values

    # Elbow Method
    st.subheader("Elbow Method")

    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    fig1, ax1 = plt.subplots()
    ax1.plot(range(1, 11), wcss, marker='o')
    ax1.set_title('The Elbow Method')
    ax1.set_xlabel('Number of clusters')
    ax1.set_ylabel('WCSS')
    st.pyplot(fig1)

    # Select number of clusters
    k = st.slider("Select number of clusters", 2, 10, 5)

    # Apply KMeans
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    # Plot clusters
    st.subheader("Cluster Visualization")

    fig2, ax2 = plt.subplots()

    colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown']

    for i in range(k):
        ax2.scatter(
            X[y_kmeans == i, 0],
            X[y_kmeans == i, 1],
            s=100,
            c=colors[i],
            label=f'Cluster {i+1}'
        )

    # Plot centroids
    ax2.scatter(
        kmeans.cluster_centers_[:, 0],
        kmeans.cluster_centers_[:, 1],
        s=300,
        c='yellow',
        label='Centroids'
    )

    ax2.set_title('Clusters of Customers')
    ax2.set_xlabel('Annual Income (k$)')
    ax2.set_ylabel('Spending Score (1-100)')
    ax2.legend()

    st.pyplot(fig2)

    # Add cluster column
    df['Cluster'] = y_kmeans

    st.subheader("Clustered Data")
    st.write(df)

    # Download option
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Clustered Data", csv, "clustered_customers.csv", "text/csv")

else:
    st.info("Please upload a CSV file to proceed.")