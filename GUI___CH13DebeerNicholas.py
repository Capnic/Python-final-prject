#gui program calculates gas mileage
#needs entry widgets that let user enter gallons of gas car holds
#and number of miles it can be driven on a full tank
#when calculate mpg button is clicked
#should display the mpg
#mpg is miles/gallons


import tkinter
import tkinter.messagebox

class MpgGUI:
    def __init__(self):

        # main window
        self.main_window= tkinter.Tk()

        #frames... will need maybe 3 one for all the info
        #one for displaying the calculations one for button
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame= tkinter.Frame(self.main_window)
        

        #info for top frames.
        self.prompt_label = tkinter.Label(self.top_frame,
                                         text="enter gallons tank can hold: ")
        self.gallon_entry = tkinter.Entry(self.top_frame,
                                          width=15)
        self.prompt_label2 = tkinter.Label(self.top_frame,
                                           text="miles it can be driven: ")
        self.miles_entry = tkinter.Entry(self.top_frame,
                                         width=15)
        #pack time..

        self.prompt_label.pack(side='left')
        self.gallon_entry.pack(side='left')
        self.prompt_label2.pack(side='left')
        self.miles_entry.pack(side='left')


        #calc frame
        self.mpg_label= tkinter.Label(self.middle_frame,
                                      text="MPG: ")
        self.value= tkinter.StringVar()
        self.mpgV_label= tkinter.Label(self.middle_frame,
                                       textvariable=self.value)
        #pack
        self.mpg_label.pack(side='left')
        self.mpgV_label.pack(side='left')

        #need button for bottom frame and quit

        self.Quit = tkinter.Button(self.bottom_frame,
                                   text="Quit",
                                   command=self.main_window.destroy)
        self.Calc_butt = tkinter.Button(self.bottom_frame,
                                        text="convert",
                                        command=self.calc)
        #pack
        self.Calc_butt.pack(side='left')
        self.Quit.pack(side='left')

        #give the frames a pack
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        

        


        #mainloop
        tkinter.mainloop()

    #need the calc function'
    def calc(self):
        gallon = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())

        mpg = miles/gallon
        self.value.set(mpg)

        

        

my_gui=MpgGUI()
        
