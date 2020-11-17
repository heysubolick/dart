from tkinter import *


class GUI():
    def __init__(self):
        self.tkhandler = Tk()
        self.tkhandler.geometry("280x500")
        self.tkhandler.title("버디버디")

        self.label_title = Label(self.tkhandler, text="내 친구(0/0)")

        # 배치 - 한 줄씩 쌓인다. : pack()
        self.label_title.pack()

        self.btn = Button(self.tkhandler, text='메시지 전송', width=30)
        self.btn.pack()

    def run(self):
        self.tkhandler.mainloop()


g = GUI()
g.run()
