import random
from tkinter import *
import os
from winsound import *
import json

class mainapplication:
    def __init__(self, para):
        self.master = para
        self.menu_canvas = Canvas(para, width=800, height=600, bg='black')
        self.menu_canvas.place(x=0, y=0)
        # adding all the images
        self.quit_img = PhotoImage(file='quit1.png')
        self.leaderboard_img = PhotoImage(file='leaderboard-wbg.png')
        self.pause_img = PhotoImage(file="pause.png")
        self.image = PhotoImage(file="lms (1).png")
        self.option_img = PhotoImage(file='menu-button.png')
        

        # Actual Background Images Size: 800x600
        self.bg_img = PhotoImage(file="bg.png")
        self.bg_img2 = PhotoImage(file="gamebg1.png")
        self.bg_img3 = PhotoImage(file="gamebg2.png")
        # Images for Background Choice Size: 200x150
        self.bg_choice1 = PhotoImage(file="bgchoice1.png")
        self.bg_choice2 = PhotoImage(file="bgchoice2.png")
        self.bg_choice3 = PhotoImage(file="bgchoice3.png")

        # Images for Char Choice Size 250x150
        self.char1 = PhotoImage(file="charchoice1.gif")
        self.char2 = PhotoImage(file='charchoice2.png')
        self.char3 = PhotoImage(file='charchoice3.gif')
        # character frames for animations
        self.charFrames1 = [PhotoImage(file="frame_0_char1.png"), PhotoImage(file="frame_1_char1.png")]
        self.charFrames2 = [PhotoImage(file="frame_0_char2.png"), PhotoImage(file="frame_1_char2.png")]
        self.charFrames3 = [PhotoImage(file="frame_0_char3.png"), PhotoImage(file="frame_1_char3.png")]

        self.fireball_img = PhotoImage(file='bullet.png')
        self.special_img = PhotoImage(file='specialprompt.png')
        # speeds of the character and the obstacle
        self.char_speed = 15
        self.speed = -5
        self.value = True

        self.up = True
        self.jump = True
        
        self.score = 0
        self.powers_available = 1
        self.power_in_use = False
        # default controls
        self.bkey = "b"
        self.skey = "s"
        self.jumpkey = "space"

        # creating the mainmenu

        self.signin_screen()

    def signin_screen(self):
        self.username = StringVar()
        self.menu_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
        self.headerText = self.menu_canvas.create_text(400, 100, font="Timesnewroman 50 bold", fill='dodger blue',
                                                       text='Enter your Name')
        self.user_entry = Entry(text="ehat is ", bd=0, font="Times 20", textvariable=self.username)
        self.user_entry.place(x=250, y=300)
        self.user_entry.insert(0, 'Guest')
        self.shape1 = self.menu_canvas.create_polygon(240, 315, 220, 295, 220, 335, fill='black')

        self.signin_button = Button(self.master, text="Sign in", command=self.create_mainmenu, font="Times 20",
                                    fg="white", bg="green", activebackground="lightgreen")
        self.signin_button.place(x=350, y=350)

    def create_mainmenu(self):
        global myname
        self.signin_button.destroy()
        self.user_entry.destroy()
        self.menu_canvas.delete(self.shape1)
        
        myname=self.username.get()

        self.menu_canvas.itemconfig(self.headerText, text='DINO JUMPER')
        self.quit_button = Button(self.menu_canvas, image=self.quit_img, width=70, height=70, anchor='se',
                                  command=self.master.destroy)
        self.quit_button.place(x=720, y=520)
        if os.path.isfile(f"{myname}.txt"):
            self.start_button = Button(self.menu_canvas, text="LOAD GAME", relief='ridge', width=25, bd=2,
                                   font='Helvitica 20', fg='white', bg='dark green', activebackground='seagreen',
                                   command=self.LoadGame)
            self.start_button.place(x=400, y=460, anchor='center')
        self.option_button = Button(self.menu_canvas, image=self.option_img, width=70, height=70, anchor='se',
                                    relief='ridge', command=self.options_menu)
        self.option_button.place(x=720, y=435)
        self.start_button = Button(self.menu_canvas, text="BEGIN VENTURE!!", relief='ridge', width=25, bd=2,
                                   font='Helvitica 20', fg='white', bg='dark green', activebackground='seagreen',
                                   command=self.thegame)
        self.start_button.place(x=400, y=300, anchor='center')
        self.leaderboard_button = Button(self.menu_canvas, text="Leaderboards", relief='ridge',
                                         width=15, bd=2, font='Helvitica 20', fg='white',
                                         bg='dark green', activebackground='seagreen', command=self.leaderboard)
        self.leaderboard_button.place(x=400, y=380, anchor='center')
        

    # -------------------Options menu----------------------------
    def options_menu(self):
        self.option_canvas = Canvas(self.master, width=800, height=600, bg='black')
        self.option_canvas.place(x=0, y=0)
        self.option_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
        self.option_canvas.create_text(60, 25, text='Personalise your Experience',
                                       font='Times 30 italic', fill='black',
                                       anchor='nw')

        self.char_button = Button(self.option_canvas, text="Change\nCharacter", relief='ridge',
                                  width=15, bd=2, font='Helvitica 20', fg='white',
                                  bg='dark green', activebackground='seagreen',
                                  command=self.char_choice)
        self.char_button.place(x=60, y=100)
        self.option_canvas.create_text(400, 100, anchor='nw', font='Times 20',
                                       fill='white', text='| SELECT YOUR JUMPER')

        self.bg_button = Button(self.option_canvas, text="Change\nLevel", relief='ridge',
                                width=15, bd=2, font='Helvitica 20', fg='white',
                                bg='dark green', activebackground='seagreen',
                                command=self.bg_choice)
        self.bg_button.place(x=60, y=250)
        self.option_canvas.create_text(400, 250, anchor='nw', font='Times 20',
                                       fill='white', text='| SELECT YOUR SETTING')

        self.controls_button = Button(self.option_canvas, text="Help", relief='ridge',
                                      width=15, bd=2, font='Helvitica 20', fg='white',
                                      bg='dark green', activebackground='seagreen',
                                      command=self.help_button)
        self.controls_button.place(x=60, y=400)
        self.option_canvas.create_text(400, 400, anchor='nw', font='Times 20',
                                       fill='white', text='| LEARN TO PLAY')

        self.back_button = Button(self.option_canvas, text="Back To Main Menu", relief='ridge',
                                  bd=2, font='Helvitica 20', fg='white',
                                  bg='dark green', activebackground='seagreen',
                                  command=lambda: self.return_mainmenu(self.option_canvas))
        self.back_button.place(x=500, y=530)

    # ------------choice for the character--------------------
    def char_choice(self):

        self.char_canvas = Canvas(self.master, width=800, height=600, bg='black')
        self.char_canvas.place(x=0, y=0)
        self.char_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
        self.char_canvas.create_text(10, 80, font='Arial 30 bold', fill='white',
                                     text='Choose Character', anchor='w', tags='my_tag')
        self.char_canvas.create_text(710, 580, font='Arial 10 bold', fill='white',
                                     text='*only changes in-game.')

        self.radiovar = IntVar()
        self.radiovar.set(1)

        self.radio1 = Radiobutton(self.char_canvas, width=200, height=150, image=self.char1,
                                  variable=self.radiovar, value=1)
        self.radio1.place(x=10, y=150)
        self.radio2 = Radiobutton(self.char_canvas, width=200, height=150, image=self.char2,
                                  variable=self.radiovar, value=2)
        self.radio2.place(x=290, y=150)
        self.radio3 = Radiobutton(self.char_canvas, width=200, height=150, image=self.char3,
                                  variable=self.radiovar, value=3)
        self.radio3.place(x=570, y=150)

        def char_button_click():
            global char_radio_value
            char_radio_value = self.radiovar.get()
            self.char_canvas.destroy()

        self.char_choice_button = Button(self.char_canvas, text='OK', anchor='center', fg='white',
                                         padx=100, pady=15, bg='sea green', relief='ridge', bd=2,
                                         font='Arial 20 bold',
                                         command=char_button_click)
        self.char_choice_button.place(x=290, y=400)

    # -------------choice for the terrain---------------------
    def bg_choice(self):
        global bg_canvas
        bg_canvas = Canvas(width=800, height=600)
        bg_canvas.place(x=0, y=0)

        bg_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')

        bg_canvas.create_text(10, 80, font='Arial 30 bold', fill='white', text='Choose Track', anchor='w',
                              tags='my_tag')

        bg_canvas.create_text(710, 580, font='Arial 10 bold', fill='white', text='*only changes in-game.')
        self.radiovar = IntVar()
        self.radiovar.set(1)
        self.radio1 = Radiobutton(bg_canvas, width=200, height=150, image=self.bg_choice1, variable=self.radiovar,
                                  value=1)
        self.radio1.place(x=10, y=150)

        self.radio2 = Radiobutton(bg_canvas, width=200, height=150, image=self.bg_choice2, variable=self.radiovar,
                                  value=2)
        self.radio2.place(x=290, y=150)

        self.radio3 = Radiobutton(bg_canvas, width=200, height=150, image=self.bg_choice3, variable=self.radiovar,
                                  value=3)
        self.radio3.place(x=570, y=150)

        def bg_button_click():
            global bg_radio_value
            bg_radio_value = self.radiovar.get()
            bg_canvas.destroy()

        self.bg_button = Button(bg_canvas, text='OK', anchor='center', fg='white', padx=100, pady=15, bg='sea green',
                                relief='ridge', bd=2, font='Arial 20 bold', command=bg_button_click)
        self.bg_button.place(x=290, y=400)

    # --------------help button----------------------------------
    def help_button(self):
        self.help_canvas = Canvas(root, width=800, height=600, bg='black')
        self.help_canvas.place(x=0, y=0)
        self.help_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
        self.help_canvas.create_text(25, 20, text='Jump Over Obstacles\nSurvive to Score',
                                     font='Times 35 italic', fill='black', anchor='nw')
        self.help_canvas.create_text(25, 120, text='Keep Playing To Discover Powers',
                                     font='Times 35 italic', fill='black', anchor='nw')
        self.help_canvas.create_rectangle(15, 15, 780, 175, width=2)
        self.help_canvas.create_rectangle(15, 230, 780, 480, width=2)
        self.help_canvas.create_text(780, 200, text='Controls',
                                     font='Times 35 bold', fill='black', anchor='e')
        self.help_canvas.create_text(25, 260, text=f'| BOSS KEY : {self.bkey}',
                                     font='Times 30', fill='khaki', anchor='w')
        self.help_canvas.create_text(25, 320, text=f'| SPECIAL POWER : {self.skey}',
                                     font='Times 30', fill='khaki', anchor='w')
        self.help_canvas.create_text(25, 380, text='| PAUSE/PLAY : ESCAPE',
                                     font='Times 30', fill='khaki', anchor='w')
        self.help_canvas.create_text(25, 440, text=f'| JUMP : {self.jumpkey}',
                                     font='Times 30', fill='khaki', anchor='w')
        back_button = Button(self.help_canvas, text='OK', anchor='center', fg='white',
                             padx=100, pady=15, bg='dark green', relief='ridge', bd=2,
                             font='Arial 20 bold', command=lambda: self.return_mainmenu(self.help_canvas))
        back_button.place(x=100, y=500)
        controls_button = Button(self.help_canvas, text='Change controls', anchor='center', fg='white',
                                 padx=60, pady=15, bg='dark green', relief='ridge', bd=2,
                                 font='Arial 20 bold', command=self.change_controls)
        controls_button.place(x=400, y=500)

    def change_controls(self):
        self.help_canvas.destroy()
        self.control_canvas = Canvas(width=800, height=600)
        self.control_canvas.place(x=0, y=0)
        self.control_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
        back_button = Button(self.control_canvas, text='OK', anchor='center', fg='white',
                             padx=100, pady=15, bg='dark green', relief='ridge', bd=2,
                             font='Arial 20 bold', command=self.return_to_help)
        back_button.place(x=290, y=500)

        self.change1 = Entry(self.control_canvas, width=5, background="black", fg="white", font="Times 20 bold")
        self.change1.place(x=400, y=250)
        self.control_canvas.create_text(250, 260, text="Boss key", font="Times 20 bold")
        self.change1.insert(END, f"{self.bkey}")
        self.change1.bind("<FocusIn>", lambda e: self.metastate(key=1))

        self.change2 = Entry(self.control_canvas, width=5, background="black", fg="white", font="Times 20 bold")
        self.change2.place(x=400, y=300)
        self.control_canvas.create_text(250, 310, text="Special key", font="Times 20 bold")
        self.change2.insert(END, f"{self.skey}")
        self.change2.bind("<FocusIn>", lambda e: self.metastate(key=2))

        self.change3 = Entry(self.control_canvas, width=5, background="black", fg="white", font="Times 20 bold")
        self.change3.place(x=400, y=350)
        self.control_canvas.create_text(250, 360, text="Jump", font="Times 20 bold")
        self.change3.insert(END, f"{self.jumpkey}")
        self.change3.bind("<FocusIn>", lambda e: self.metastate(key=3))

    def return_to_help(self):
        self.control_canvas.destroy()
        self.help_button()

    def metastate(self, key, event=None):
        if key == 1:
            self.change1.delete(0, END)
            self.change1.insert(END, "???")
            self.change1.bind("<Key>", lambda e: self.newkey(e, 1))
        elif key == 2:
            self.change2.delete(0, END)
            self.change2.insert(END, "???")
            self.change2.bind("<Key>", lambda e: self.newkey(e, 2))
        elif key == 3:
            self.change3.delete(0, END)
            self.change3.insert(END, "???")
            self.change3.bind("<Key>", lambda e: self.newkey(e, 3))

    def newkey(self, event, key):
        if key == 1:
            self.change1.delete(0, END)
            self.bkey = event.keysym
        elif key == 2:
            self.change2.delete(0, END)
            self.skey = event.keysym
        elif key == 3:
            self.change3.delete(0, END)
            self.jumpkey = event.keysym
        self.control_canvas.destroy()
        self.change_controls()
    # -------------when user starts the game-------------------
    def thegame(self):
        global game_canvas, b, c
        self.score = 00
        self.updated = False
        ourScore = "Score:" + str(self.score)

        game_canvas = Canvas(width=800, height=600, bg='black')
        game_canvas.place(x=0, y=0)
        
        
        c = 0
        game_canvas.bind_all(f"<{self.bkey}>", self.boss_key)
        # creating the binding for pause menu
        game_canvas.bind_all(f"<{self.skey}>", self.special_key)
        game_canvas.bind_all("<e><n><j>", self.cheatCode1)
        game_canvas.bind_all("<c><a><l><m>", self.cheatCode2)
        b = 0
        game_canvas.bind_all("<Escape>", self.pause)
        self.pause_button = Button(image=self.pause_img, command=self.pause, height=60, width=60)
        self.pause_button.place(x=0, y=10)

        if bg_radio_value == 1:
            game_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
        elif bg_radio_value == 2:
            game_canvas.create_image(0, 0, image=self.bg_img2, anchor='nw')
        elif bg_radio_value == 3:
            game_canvas.create_image(0, 0, image=self.bg_img3, anchor='nw')

        if char_radio_value == 1:
            self.toanimate = self.charFrames1
        elif char_radio_value == 2:
            self.toanimate = self.charFrames2
        elif char_radio_value == 3:
            self.toanimate = self.charFrames3

        game_canvas.create_rectangle(290, 2, 460, 45, fill='green', width=3)
        self.scoreText = game_canvas.create_text(375, 23, text=ourScore, font="Times 30 italic", fill='black')
        

        # creating the binding for jumping
        game_canvas.bind_all(f"<{self.jumpkey}>", self.press)

        

        self.character = game_canvas.create_image(200, 490, image=self.toanimate[0])
        self.power_prompt = game_canvas.create_text(780, 20, anchor='e',
                                                    text=self.powers_available, font='Times 15')
        game_canvas.create_image(750, 20, anchor='e', image=self.special_img)
        game_canvas.create_text(765, 20, anchor='e', text='x', )

        a = 0
        
        self.animation(a)
        self.enemies()
        self.movement()
        
    # -------------------Creating the puase menu------------------------------
    def pause(self, e=None):
        self.pause_button.destroy()
        global obstacle, b, pos_char, pos_enemy, stop, timer, pause
        
        if b % 2 == 0:

            pos_char = game_canvas.coords(self.character)
            pos_enemy = game_canvas.coords(obstacle)
            game_canvas.delete(self.character)
            game_canvas.delete(obstacle)
            b = b + 1
            game_canvas.unbind_all(f"<{self.jumpkey}>")
            pause = game_canvas.create_text(400, 100, font="Timesnewroman 50 bold", fill='dodger blue',
                                            text='PAUSE MENU')
            self.return_to_menu_button = Button(game_canvas, text="Return\nto Main menu", relief='ridge', width=15,
                                                bd=2, font='Helvitica 20',
                                                fg='white', bg='dark green', activebackground='seagreen',
                                                command=lambda: self.return_mainmenu(game_canvas, None))
            self.return_to_menu_button.place(x=300, y=200)

            self.continuegame = Button(game_canvas, text="CONTINUE", relief='ridge', width=15, bd=2,
                                       font='Helvitica 20',
                                       fg='white', bg='dark green', activebackground='seagreen',
                                       command=lambda: self.pause(None))
            self.continuegame.place(x=300, y=300)

            self.retry_button = Button(game_canvas, text="Retry", relief='ridge', width=15, bd=2, font='Helvitica 20',
                                       fg='white', bg='dark green', activebackground='seagreen',
                                       command=lambda: self.return_thegame(game_canvas))
            self.retry_button.place(x=425, y=400, anchor='center')
            self.save_button = Button(game_canvas, text="Save Game", relief='ridge', width=15, bd=2, font='Helvitica 20',
                                       fg='white', bg='dark green', activebackground='seagreen',
                                       command=self.SaveGame)
            self.save_button.place(x=425, y=500, anchor='center')
        else:
            self.return_to_menu_button.destroy()
            self.retry_button.destroy()
            self.continuegame.destroy()
            self.save_button.destroy()
            game_canvas.delete(pause)
            self.value = False
            self.character = game_canvas.create_image(pos_char[0], pos_char[1], image=self.toanimate[0])
            obstacle = game_canvas.create_image(pos_enemy[0], pos_enemy[1], image=self.enemy_img)

            self.three = game_canvas.create_text(400, 300, font="Timesnewroman 50 bold", fill='dodger blue', text="")
            self.timer = 3
            self.countdownTimer()

    def countdownTimer(self):
        global b
        if self.timer == 3:

            game_canvas.itemconfig(self.three, text="On your keys!")
            self.timer -= 1
            self.ctimer = game_canvas.after(1000, self.countdownTimer)
        elif self.timer == 2:

            game_canvas.itemconfig(self.three, text="Get set")
            self.timer -= 1
            self.ctimer = game_canvas.after(1000, self.countdownTimer)
        elif self.timer == 1:
            game_canvas.itemconfig(self.three, text="GO!")
            self.timer -= 1
            self.countdownover = True
            self.ctimer = game_canvas.after(1000, self.countdownTimer)
        elif self.timer == 0:
            game_canvas.delete(self.three)
            if pos_char[1] < 490:
                self.jump = True
            else:
                self.jump = False
            self.value = True
            self.press(None)
            self.jump = True
            game_canvas.bind_all(f"<{self.jumpkey}>", self.press)
            b = b + 1
            self.pause_button = Button(image=self.pause_img, command=self.pause, height=60, width=60)
            self.pause_button.place(x=0, y=10)
            self.movement()
            self.value = True
            a = 0
            self.animation(a)
    #------------------Save/load functions--------------------------
    def SaveGame(self):
        
        
        print("Saved successfully")
        #f=open(f'{myname}.txt','a') #appending name and score in a file
        contents = {"user":myname ,"enemy":self.randomEnemy, "score":self.score, "char_pos":pos_char, "enemy_pos":pos_enemy, "char_choice":str(char_radio_value), "background":str(bg_radio_value)}
        with open(f'{myname}.txt', 'w') as userfile:
            json.dump(contents, userfile)
        f.close()

    def LoadGame(self):
        global game_canvas,obstacle, b,c
        f=open(f'{myname}.txt','r') #appending name and score in a file
        
        try:
            with open(f'{myname}.txt', 'r') as userfile:
                data = json.load(userfile)
                f.close()
        except:
            pass
        score = data["score"]
        self.randomEnemy=data["enemy"]
        pos_char = data["char_pos"]
        pos_enemy = data["enemy_pos"]
        char_choice = data["char_choice"]
        background = data["background"]

        self.score = int(score)
        self.updated = False
        ourScore = "Score:" + str(self.score)

        
        
        game_canvas = Canvas(width=800, height=600, bg='black')
        game_canvas.place(x=0, y=0)
        
        c = 0
        game_canvas.bind_all("<b>", self.boss_key)
        # creating the binding for pause menu
        game_canvas.bind_all("<s>", self.special_key)
        game_canvas.bind_all("<e><n><j>", self.cheatCode1)
        game_canvas.bind_all("<c><a><l><m>", self.cheatCode2)
        b = 0
        game_canvas.bind_all("<Escape>", self.pause)
        self.pause_button = Button(image=self.pause_img, command=self.pause, height=60, width=60)
        self.pause_button.place(x=0, y=10)
        

        if background == "1":
            game_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
        elif background =="2":
            game_canvas.create_image(0, 0, image=self.bg_img2, anchor='nw')
        elif background == "3":
            game_canvas.create_image(0, 0, image=self.bg_img3, anchor='nw')

        if char_choice == "1":
            self.toanimate = self.charFrames1
        elif char_choice == "2":
            self.toanimate = self.charFrames2
        elif char_choice == "3":
            self.toanimate = self.charFrames3

        # creating the binding for jumping
        game_canvas.bind_all("<space>", self.press)
        game_canvas.create_rectangle(290, 2, 460, 45, fill='green', width=3)
        self.scoreText = game_canvas.create_text(375, 23, text=ourScore, font="Times 30 italic", fill='black')

        self.character = game_canvas.create_image(pos_char[0], pos_char[1], image=self.toanimate[0])
        self.power_prompt = game_canvas.create_text(780, 20, anchor='e',
                                                    text=self.powers_available, font='Times 15')
        game_canvas.create_image(750, 20, anchor='e', image=self.special_img)
        game_canvas.create_text(765, 20, anchor='e', text='x', )

        self.enemy_img = PhotoImage(file=self.randomEnemy)
        obstacle = game_canvas.create_image(pos_enemy[0], pos_enemy[1], image=self.enemy_img)
        if pos_char[1] < 490:
            self.jump = True
        else:
            self.jump = False
        self.value = True
        self.press(None)
        self.jump = True

        a = 0
        self.animation(a)
        self.movement()

    def animation(self, a):
        if self.value == True:
            if a % 2 != 0:
                a = a + 1
                game_canvas.itemconfig(self.character, image=self.toanimate[0])
            else:
                a = a + 1
                game_canvas.itemconfig(self.character, image=self.toanimate[1])
            game_canvas.after(90, lambda: self.animation(a))

            # ------------------------------cheat code--------------------------------------

    def cheatCode1(self, event):
        self.score += 40

    def cheatCode2(self, event):
        self.speed += 1

    # ------------------------------boss key-----------------------------------------

    def boss_key(self, e):
        global obstacle, c, pos_char, pos_enemy, boss_canvas
        if c % 2 == 0:

            pos_char = game_canvas.coords(self.character)
            pos_enemy = game_canvas.coords(obstacle)
            game_canvas.delete(self.character)
            game_canvas.delete(obstacle)
            c = c + 1
            game_canvas.unbind_all(f"<{self.jumpkey}>")
            boss_canvas = Canvas(width=800, height=600)
            boss_canvas.place(x=0, y=0)
            boss_canvas.create_image(0, 0, image=self.image, anchor='nw')
        else:
            boss_canvas.destroy()
            self.character = game_canvas.create_image(pos_char[0], pos_char[1], image=self.toanimate[0])
            obstacle = game_canvas.create_image(pos_enemy[0], pos_enemy[1], image=self.enemy_img)
            c = c + 1
            if pos_char[1] < 490:
                self.jump = True
            else:
                self.jump = False
            self.value = True
            self.press(None)
            self.jump = True
            game_canvas.bind_all(f"<{self.jumpkey}>", self.press)
            self.movement()

    def press(self, e):
        if self.jump:
            PlaySound("jump_sound.wav", SND_ASYNC)
            self.character_movement()

    def special_key(self, event):
        global fireball

        if self.powers_available > 0 and self.power_in_use is False:
            fireball = game_canvas.create_image(200, 480,
                                                image=self.fireball_img)
            self.special_movement()
            self.powers_available -= 1
            game_canvas.itemconfigure(self.power_prompt, text=self.powers_available)

    def special_movement(self):
        global obstacle, fireball

        ballpos = game_canvas.coords(fireball)
        obspos = game_canvas.coords(obstacle)
        
        if ballpos[0] < obspos[0]:
            game_canvas.move(fireball, 5.5, 0)
            game_canvas.after(10, self.special_movement)
            self.power_in_use = True
        else:
            game_canvas.delete(obstacle)
            game_canvas.delete(fireball)
            self.updateScore()
            self.enemies()
            self.power_in_use = False

    # -----------movemennt of character------------
    def character_movement(self, event=None):
        try:
            self.jump = False
            if self.up:
                game_canvas.move(self.character, 0, -self.char_speed)
                if game_canvas.coords(self.character)[1] <= 320:
                    self.up = False

            else:
                game_canvas.move(self.character, 0, self.char_speed)
                if game_canvas.coords(self.character)[1] > 490:
                    self.up = True
                    self.jump = True
                    game_canvas.coords(self.character, 200, 490)
                    self.updated = False

            if not self.jump:
                pos1 = game_canvas.coords(obstacle)
                pos2 = game_canvas.coords(self.character)
                # updating the score

                while pos1[0] > 180 and pos1[0] < 240 and self.updated == False and not self.collision(pos2, pos1):
                    self.updateScore()
                game_canvas.after(20, self.character_movement)
        except:
            pass

    # --------------------Collision control------------------------------
    def collision(self, pos1, pos2):
        if pos2[0] > 180 and pos2[0] < 240 and pos1[1] > 420:
            return True

        elif pos2[0] > 180 and pos2[0] < 240 and pos1[1] == pos2[1]:
            return True
        return False

    # -----------movemennt of obstacles--------------
   
        
    def enemies(self):
        global obstacle,coin

        if bg_radio_value == 1:
            enemyList = ["polar bear.gif", "gorilla.gif", "snowman.png", "chipkali.png"]
        elif bg_radio_value == 2:
            enemyList = ["camel.png", "eagle.png", "scorpion.png"]
        elif bg_radio_value == 3:
            enemyList = ["tesla.png", "toyota.png", "honda.png"]
        self.randomEnemy = random.choice(enemyList)
        self.enemy_img = PhotoImage(file=self.randomEnemy)
        obstacle = game_canvas.create_image(799, 480, image=self.enemy_img)
        
    def movement(self):
        global charpos, obspos

        game_canvas.move(obstacle, self.speed, 0)
        
        # Ye try except isliye daala kiun ke pause karke obstacle delete hota hai, aur phir move karne pe error deta
        try:
            if game_canvas.coords(obstacle)[0] <= -50:
                game_canvas.delete(obstacle)
                self.enemies()

            movingEnemy = game_canvas.after(10, self.movement)

            # checking if the obstacle collided with the character
            if self.collision(game_canvas.coords(self.character), game_canvas.coords(obstacle)):
                game_canvas.unbind_all(f"<{self.jumpkey}>")
                game_canvas.unbind_all(f"<{self.bkey}>")
                game_canvas.unbind_all(f"<{self.skey}>")
                game_canvas.create_text(400, 300, fill="white", font="Times 20 italic bold",
                                        text="Better luck next time!")
                
                game_canvas.after_cancel(movingEnemy)
                
                self.pause_button.destroy()
                PlaySound('oh_no.wav', SND_FILENAME)
                
                self.result_file = open("results.txt", "a")
                self.result_file.write(f"\t{self.username.get()}\t\t{self.score}\n")
                self.result_file.close()
                self.return_to_menu_button = Button(game_canvas, text="Return\nto Main menu", relief='ridge', width=15,
                                                    bd=2, font='Helvitica 20',
                                                    fg='white', bg='dark green', activebackground='seagreen',
                                                    command=lambda: self.return_mainmenu(game_canvas))
                self.return_to_menu_button.place(x=100, y=440)

                self.leaderboard_button = Button(game_canvas, text="Leaderboards", relief='ridge', width=15, bd=2,
                                                 font='Helvitica 20',
                                                 fg='white', bg='dark green', activebackground='seagreen',
                                                 command=self.leaderboard)
                self.leaderboard_button.place(x=450, y=450)

                self.retry_button = Button(game_canvas, text="Retry", relief='ridge', width=25, bd=2,
                                           font='Helvitica 20',
                                           fg='white', bg='dark green', activebackground='seagreen',
                                           command=lambda: self.return_thegame(game_canvas))
                self.retry_button.place(x=400, y=250, anchor='center')
                game_canvas.after_cancel(self.moving_coins)
        except:
            pass
    
    # -------------------function to return to mainmenu and to retry-----------------------
    def return_mainmenu(self, todestroy=None, startfrom=None):
        if startfrom != None:
            startfrom.destroy()
            try:
                self.return_to_menu_button.destroy()
                self.leaderboard_Text.destroy()

            except:
                self.return_to_menu_button.destroy()
                self.continuegame.destroy()
                self.retry_button.destroy()
        if todestroy != None:
            todestroy.destroy()
        self.create_mainmenu()
        self.speed = -5

    def return_thegame(self, todestroy):
        todestroy.destroy()
        self.speed = -5
        self.char_speed = 15
        self.thegame()
        self.powers_available = 1
        game_canvas.itemconfigure(self.power_prompt, text=self.powers_available)

    # -------------------Setting the leaderboards-----------------------
    def leaderboard(self):
        leaderboard_canvas = Canvas(width=800, height=600)
        leaderboard_canvas.place(x=0, y=0)

        if bg_radio_value == 1:
            leaderboard_canvas.create_image(0, 0, image=self.bg_img, anchor='nw')
        elif bg_radio_value == 2:
            leaderboard_canvas.create_image(0, 0, image=self.bg_img2, anchor='nw')
        elif bg_radio_value == 3:
            leaderboard_canvas.create_image(0, 0, image=self.bg_img3, anchor='nw')
        leaderboard_canvas.create_text(410, 50, text="Leaderboards", font="Timesnewroman 30 bold", fill='darkgreen')
        self.leaderboard_Text = Text(leaderboard_canvas, bg="forestgreen", fg="white", height=10, width=40,
                                     font="Calibri 20")
        self.leaderboard_Text.place(x=150, y=90)
        self.sorting()

        if os.path.isfile("results.txt"):
            for i in range(len(self.mainList)):
                self.leaderboard_Text.insert(END, "\t\t" + str(self.mainList[i][0]) + ":\t" + str(
                    self.mainList[i][1]) + "\n")
        else:
            self.leaderboard_Text.insert(END, "No scores to display")
        if "game_canvas" not in globals():
            self.return_to_menu_button = Button(self.master, text="Return\nto Main menu", relief='ridge', width=15,
                                                bd=2, font='Helvitica 20',
                                                fg='white', bg='dark green', activebackground='seagreen',
                                                command=lambda: self.return_mainmenu(startfrom=leaderboard_canvas))
            self.return_to_menu_button.place(x=300, y=470)
        else:
            self.return_to_menu_button = Button(self.master, text="Return\nto Main menu", relief='ridge', width=15,
                                                bd=2, font='Helvitica 20',
                                                fg='white', bg='dark green', activebackground='seagreen',
                                                command=lambda: self.return_mainmenu(game_canvas, leaderboard_canvas))
            self.return_to_menu_button.place(x=300, y=470)

    # ---------------------Sorting the leaderboard-------------------------------------
    def sorting(self):
        s = ''
        n = ''
        t = 0
        self.mainList = []
        with open('results.txt', 'r') as file:
            for line in file:
                for i in line:
                    if i == "\t":
                        t += 1
                    elif i.isdigit() and t == 3:
                        s += i
                    elif i != "\n" and i != "\t":
                        n += i
                self.mainList.append((n, int(s)))
                s = ''
                n = ''
                t = 0

        self.mainList = sorted(self.mainList, key=lambda a: a[1], reverse=True)

    # ----------------when called, the function updates the score-------------------
    def updateScore(self,score = None):
        global powers_available
        if score != None:
            self.score+=20
        else:
            self.score += 10
        ourScore = "Score:" + str(self.score)
        game_canvas.itemconfig(self.scoreText, text=ourScore)
        self.updated = True
        # updating the speed if the score reaches a certain value
        if self.score == 100:
            self.powers_available = 2
            game_canvas.itemconfigure(self.power_prompt, text=self.powers_available)

            self.levelup_text = game_canvas.create_text(400, 300, fill="white", font="Times 20 italic bold",
                                                        text="Congrats! Level up.\n You are now a runner")
            self.speed -= 3
            game_canvas.after(2000, self.update_speed)
        elif self.score == 300:
            self.powers_available = 3
            game_canvas.itemconfigure(self.power_prompt, text=self.powers_available)
            self.levelup_text = game_canvas.create_text(400, 300, fill="white", font="Times 20 italic bold",
                                                        text="Congrats! Level up.\n You are now an athlete")
            self.speed -= 3
            game_canvas.after(2000, self.update_speed)
        elif self.score == 800:
            self.powers_available = 4
            game_canvas.itemconfigure(self.power_prompt, text=self.powers_available)

            self.levelup_text = game_canvas.create_text(400, 300, fill="white", font="Times 20 italic bold",
                                                        text="Congrats! Level up.\n You are now an Usain Bolt")
            self.speed -= 3
            game_canvas.after(2000, self.update_speed)

    def update_speed(self):
        game_canvas.delete(self.levelup_text)


# --------------------------------------------------------#
root = Tk()
root.title("T.Rex Retro")
root.iconbitmap('icon.ico')
width = 800
height = 600
width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()
x = (width_screen / 2) - (width / 2)
y = (height_screen / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
bg_radio_value = 1
char_radio_value = 1
m = mainapplication(root)
root.mainloop()
