import tkinter  as tk

root= tk.Tk()
root.title("Simple Quiz")
root.geometry("700x600")

#intial score
score=0

#-----functions----------
def show_frame(frame): # function to operate frames
    frame.tkraise()

def check_answers():
    global score # making funtion belong to check answers
    score=0

    feedback= ""

    if q1_entry.get() == "Nile": 
        score += 1 
        feedback += "Q1 Correct\n\n" 
    else: 
        feedback += "Q1 Wrong\n\n" 

    if q2_entry.get().lower() == "Pacific Ocean": 

        score += 1 

        feedback += "Q2 Correct\n\n" 

    else: 

      feedback += "Q2 Wrong\n\n" 
    if q3_entry.get() == "John Snow": 

        score += 1 

        feedback += "Q3 Correct\n\n" 

    else: 

        feedback += "Q3 Wrong\n\n"
        
    if q4_entry.get() == "Zagreb":
        score +=1
        feedback += "Q4 Correct\n\n"
    else:
        feedback += "Q4 Wrong\n\n"

    if q5_entry.get() == "Vatican city":
        score+=1
        feedback += "Q5 Correct\n\n"
    else:
        feedback += "Q5 Wrong\n\n"

    if q6_entry.get() == "France":
        score+=1
        feedback += "Q5 Correct\n\n"
    else:
        feedback += "Q5 Wrong\n\n"

    if q7_entry.get() == "Spain":
        score+=1
        feedback += "Q5 Correct\n\n"
    else:
        feedback += "Q5 Wrong\n\n"

    if q8_entry.get() == "Caspian Sea":
        score+=1
        feedback += "Q5 Correct\n\n"
    else:
        feedback += "Q5 Wrong\n\n"

    if q9_entry.get() == "Greenland":
        score+=1
        feedback += "Q5 Correct\n\n"
    else:
        feedback += "Q5 Wrong\n\n"

    result_text.set(feedback + "\nScore: " + str(score) + "/9") 

  

    show_frame(result_frame)  
# ---------- FRAMES And their Placement---------- 

welcome_frame = tk.Frame(root) 

quiz_frame = tk.Frame(root) 

result_frame = tk.Frame(root) 

# -----------Frames in the grid and their position in the cell. 

welcome_frame.grid(row=0, column=0, sticky="nsew") 

quiz_frame.grid(row=0, column=0, sticky="nsew") 

result_frame.grid(row=0, column=0, sticky="nsew") 

# ---------- WELCOME SCREEN ---------- 

title = tk.Label(welcome_frame, text="Welcome to the Quiz", font=("Arial", 16)) 

title.grid(row=0, column=0, pady=20) 

  

start_button = tk.Button( 

    welcome_frame, 

    text="Start Quiz", 

    command=lambda: show_frame(quiz_frame) 

) 

start_button.grid(row=1, column=0, pady=20) 

  

  

# ---------- QUIZ SCREEN ---------- 

q1 = tk.Label(quiz_frame, text="1. What is the name of the longest river: ") 

q1.grid(row=0, column=0, sticky="w", padx=20, pady=20) 

  

q1_entry = tk.Entry(quiz_frame) 

q1_entry.grid(row=0, column=1) 

#--------------------------------------------------------------------------

q2 = tk.Label(quiz_frame, text="2. What is the name of the largest ocean: ") 

q2.grid(row=1, column=0, sticky="w", padx=20,pady=20) 

  

q2_entry = tk.Entry(quiz_frame) 

q2_entry.grid(row=1, column=1)

#---------------------------------------------------------------------------
q3= tk.Label(quiz_frame, text="3. Who solved the 1854 cholera outbreak in London: ")
q3.grid(row=2, column=0, sticky= "w", pady=20, padx=20)

q3_entry= tk.Entry(quiz_frame)
q3_entry.grid(row=2, column=1)
#--------------------------------------------------------------------------
q4=tk.Label(quiz_frame, text="4.What is the capital of Croatia: ")
q4.grid (row=3, column=0,  sticky="w", padx=20, pady=20)
q4_entry= tk.Entry(quiz_frame)
q4_entry.grid(row=3, column=1)
#--------------------------------------------------------------------------
q5 = tk.Label(quiz_frame, text="5.What country has the lowest population: ")
q5.grid (row=4, column=0,  sticky="w", padx=20, pady=20)
q5_entry= tk.Entry(quiz_frame)
q5_entry.grid(row=4, column=1)

#-------------------------------------------------------------------------------
q6 = tk.Label(quiz_frame, text="6..Which country has the most time zones: ")
q6.grid (row=5, column=0,  sticky="w", padx=20, pady=20)
q6_entry= tk.Entry(quiz_frame)
q6_entry.grid(row=5, column=1)
#--------------------------------------------------------------------------------
q7 = tk.Label(quiz_frame, text="7.Which country is opposite of New Zealand: ")
q7.grid (row=6, column=0,  sticky="w", padx=20, pady=20)
q7_entry= tk.Entry(quiz_frame)
q7_entry.grid(row=6, column=1)

#---------------------------------------------------------------------------------
q8 = tk.Label(quiz_frame, text="8.What is the largest inland body of water:: ")
q8.grid (row=7, column=0,  sticky="w", padx=20, pady=20)
q8_entry= tk.Entry(quiz_frame)
q8_entry.grid(row=7, column=1)
#--------------------------------------------------------------------------------
q9 = tk.Label(quiz_frame, text="9. What is the world’s largest island: ")
q9.grid (row=8, column=0,  sticky="w", padx=20, pady=20)
q9_entry= tk.Entry(quiz_frame)
q9_entry.grid(row=8, column=1)

#----------------------------------------------------------------------------------

submit_button = tk.Button(quiz_frame,text="Submit", command=check_answers) 
submit_button.grid(row=9, column=0, columnspan=2, pady=20) 

  

  

# ---------- RESULT SCREEN ---------- 

result_text = tk.StringVar()  # StringVar is a special Tkinter variable that can update widgets automatically. 

  

result_label = tk.Label(result_frame, textvariable=result_text, font=("Arial", 12)) 

result_label.grid(row=0, column=0, pady=20) 

  

home_button = tk.Button( result_frame,text="Back to Home", command=lambda: show_frame(welcome_frame)) 

home_button.grid(row=5, column=0, pady=20) 

  

  

# Start program with welcome screen 

show_frame(welcome_frame) 

  

root.mainloop() 

