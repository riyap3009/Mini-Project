
import matplotlib.pyplot as plt

students= ['A','B','C','D','E']
marks=[80,65,90,75,85]
colors= ['green','light blue','red','yellow','pink']
plt.title("Student Grades")
plt.xlabel("Students")
plt.ylabel=("Marks")
plt.bar(students, marks, color=colors)

plt.show()
