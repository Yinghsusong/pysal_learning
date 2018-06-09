import matplotlib.pyplot as plt 

x = [0.000426,0.001279,0.002559,0.003198,0.00661,0.033689,0.092537,0.247548,
0.504691,0.782942,0.829211,0.921962,0.947548,0.973987,0.981663,0.984222,0.989126,0.995522,1]

y = [0.00561,0.013399,0.022576,0.025677,0.031864,0.095686,0.196072,0.491475,
0.76991,0.952089,0.971259,0.995486,0.99633,0.997108,0.997829,0.998329,0.999106,0.999389,1]


plt.plot(x,y)
plt.scatter(x,y)
plt.title('The ROC curve of the result')

plt.show()