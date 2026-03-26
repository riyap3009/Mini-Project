
import matplotlib.pyplot as plt

activites= ['Study','Sleep','Entertainment','Other']
hours=[6,8,4,6]
colors=['yellow','blue','green','purple']
plt.xlabel("Actions")
plt.ylabel("Hours spent")
plt.title("Daily Activites")
plt.bar(activites, hours,color=colors)

plt.show()
