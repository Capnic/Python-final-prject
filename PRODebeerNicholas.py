#have to multiply the assignments by the weight they have before dividing
# by the total average

#Project Final
#gradebook program with GUI
#need 7 assignments/exam entries with different weights
#8 frames needed for that
#3 more needed; for the buttons and then the grade it shows with the letter
#lets get to it

import tkinter as tk


class Grade_avg:
    def __init__(self):
        #create main window
        self.main_window= tk.Tk()

        #create 11 frames 
        self.label_frame= tk.Frame(self.main_window)
        self.discussions_frame= tk.Frame(self.main_window)
        self.quiz_frame= tk.Frame(self.main_window)
        self.program_frame= tk.Frame(self.main_window)
        self.mylab_frame= tk.Frame(self.main_window)
        self.exam1_frame= tk.Frame(self.main_window)
        self.exam2_frame= tk.Frame(self.main_window)
        self.final_frame= tk.Frame(self.main_window)
        self.button_frame= tk.Frame(self.main_window)
        self.average_frame= tk.Frame(self.main_window)
        self.letter_frame= tk.Frame(self.main_window)

        #widgets and pack for label frame
        
        self.msg_label= tk.Label(self.label_frame,
                            text="Enter the scores for the following assignments and exams: ")
        self.msg_label.pack(side='left')
        #discussion frame

        self.discussions_label= tk.Label(self.discussions_frame,
                                text="Discussions (5% of Total):")
        self.discussions_entry= tk.Entry(self.discussions_frame,
                                     width=15)
        self.discussions_label.pack(side='left')
        self.discussions_entry.pack(side='left')

        #quiz frame
        self.quiz_label= tk.Label(self.quiz_frame,
                                  text="Quizzes (15% of Total):")
        self.quiz_entry= tk.Entry(self.quiz_frame,
                                  width=15)
        self.quiz_label.pack(side='left')
        self.quiz_entry.pack(side='left')

        # program frame
        self.program_label= tk.Label(self.program_frame,
                                     text="Programs/Project (15% of Total):")
        self.program_entry= tk.Entry(self.program_frame,
                                     width=15)
        self.program_label.pack(side='left')
        self.program_entry.pack(side='left')

        # labs frame

        self.mylab_label= tk.Label(self.mylab_frame,
                                   text="MyLabs (15% of Total):")
        self.mylab_entry= tk.Entry(self.mylab_frame,
                                   width=15)
        self.mylab_label.pack(side='left')
        self.mylab_entry.pack(side='left')

        #exam1 frame
        self.exam1_label= tk.Label(self.exam1_frame,
                                   text="Exam1 (10% of Total):")
        self.exam1_entry= tk.Entry(self.exam1_frame,
                                   width=15)
        self.exam1_label.pack(side='left')
        self.exam1_entry.pack(side='left')

        #exam 2 frame

        self.exam2_label= tk.Label(self.exam2_frame,
                                   text="Exam2 (10% of Total):")
        self.exam2_entry= tk.Entry(self.exam2_frame,
                                   width=15)
        self.exam2_label.pack(side='left')
        self.exam2_entry.pack(side='left')

        #final exam frame
        self.final_label= tk.Label(self.final_frame,
                                   text="Final Exam (30% of Total):")
        self.final_entry= tk.Entry(self.final_frame,
                                   width=15)
        self.final_label.pack(side='left')
        self.final_entry.pack(side='left')

        #button frame
        self.calc_button= tk.Button(self.button_frame,
                                     text="Calculate Average/Letter Grade",
                                     command=self.calc_avg)
                                            
                                    
        self.quit_button= tk.Button(self.button_frame,
                                    text="Quit",
                                    command= self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        #average frame
        self.avg_label= tk.Label(self.average_frame,
                                 text="Average:")
        self.value= tk.StringVar()
        self.avgV_label= tk.Label(self.average_frame,
                                  textvariable=self.value)
        self.avg_label.pack(side='left')
        self.avgV_label.pack(side='left')

        #letter frame
        
        self.letter_label= tk.Label(self.letter_frame,
                                    text="Letter Grade:")
        self.lettervalue= tk.StringVar()
        self.letterV_label= tk.Label(self.letter_frame,
                                     textvariable=self.lettervalue)
        self.letter_label.pack(side='left')
        self.letterV_label.pack(side='left')

        #all of the widgets are set for the frames and packed...now to pack the frames
        self.label_frame.pack()
        self.discussions_frame.pack()
        self.quiz_frame.pack()
        self.program_frame.pack()
        self.mylab_frame.pack()
        self.exam1_frame.pack()
        self.exam2_frame.pack()
        self.final_frame.pack()
        self.button_frame.pack()
        self.average_frame.pack()
        self.letter_frame.pack()
        

        #start the mainloop
        tk.mainloop()
    #need to have the calc_avg called as 'value' and letter grade as 'lettervalue
    def calc_avg(self):
        #need to get all the values first

        self.discussions=float(self.discussions_entry.get())
        self.quizzes=float(self.quiz_entry.get())
        self.program=float(self.program_entry.get())
        self.mylab=float(self.mylab_entry.get())
        self.exam1=float(self.exam1_entry.get())
        self.exam2=float(self.exam2_entry.get())
        self.final_exam=float(self.final_entry.get())

        #now i can do the calculation with weights
        self.avg = (.05*self.discussions)+(.15*self.quizzes)+(.15*self.program)+(.15*self.mylab)+(.1*self.exam1)+(.1*self.exam2)+(.3*self.final_exam)

        

        self.value.set(self.avg)
        # i should of done another function for the letter grades however
        # i couldnt get it to work. super function it is

        if self.avg >= 89.45:
            lettervalue= "A"
        elif self.avg <89.45 and self.avg >= 79.45:
            lettervalue= "B"
        elif self.avg <79.45 and self.avg >= 69.45:
            lettervalue= "C"
        elif self.avg <69.45 and self.avg >= 59.45:
            lettervalue = "D"
        else:
            lettervalue = "F"

        self.lettervalue.set(lettervalue)

        
        return        
                              
grades=Grade_avg
grades()
                            
