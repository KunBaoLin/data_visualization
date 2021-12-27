import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]


plt.scatter(x_values,y_values, s=200)
plt.title("square numbers", fontsize =24)
plt.xlabel('values', fontsize = 14)
plt.ylabel('square of values', fontsize = 14)
plt.tick_params(axis='both', which = 'major', labelsize =14)


plt.show()