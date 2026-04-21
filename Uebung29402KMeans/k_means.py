from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


x=[4,5,10,4,3,11,14,6,10,12]
y=[21,19,24,17,16,25,24,22,21,21]

data = list(zip(x, y))

kmeans2 = KMeans(n_clusters=2)
kmeans2.fit(data)
print("Zentren: ", kmeans2.cluster_centers_)
plt.scatter(x,y,c=kmeans2.labels_)
plt.scatter(kmeans2.cluster_centers_[0][0],kmeans2.cluster_centers_[0][1],s=100)
plt.scatter(kmeans2.cluster_centers_[1][0],kmeans2.cluster_centers_[1][1],s=100)
plt.show()


kmeans3 = KMeans(n_clusters=3)
kmeans3.fit(data)
plt.scatter(x,y,c=kmeans3.labels_)
print("Zentren: ", kmeans3.cluster_centers_)
plt.scatter(kmeans3.cluster_centers_[0][0],kmeans3.cluster_centers_[0][1],s=100)
plt.scatter(kmeans3.cluster_centers_[1][0],kmeans3.cluster_centers_[1][1],s=100)
plt.scatter(kmeans3.cluster_centers_[2][0],kmeans3.cluster_centers_[2][1],s=100)

#ODER:
# print("Zentren: ", centers)
#
# # Plot der Zentren
# plt.scatter(centers[:, 0], centers[:, 1], s=200, c='red', marker='X')

#ODER:
# centers = kmeans3.cluster_centers_
#
# for i in range(len(centers)):
#     plt.scatter(centers[i][0], centers[i][1], s=200, c='red', marker='X')
plt.show()

kmeans4 = KMeans(n_clusters=4)
kmeans4.fit(data)
plt.scatter(x,y,c=kmeans4.labels_)
plt.show()