import matplotlib.pyplot as plt

plt.scatter(2,4, s=2000)
plt.title("square numbers", fontsize =24)
plt.xlabel('values', fontsize = 14)
plt.ylabel('square of values', fontsize = 14)
plt.tick_params(axis='both', which = 'major', labelsize =14)


plt.show()