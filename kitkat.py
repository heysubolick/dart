from tkinter import *


class GUI():
    def __init__(self):
        self.tkhandler = Tk()
        self.tkhandler.geometry("280x500")
        self.tkhandler.title("고양이 후원하기.exe")

        self.label_title = Label(self.tkhandler, text="킷캣 / 1살 / 여아")

        # 배치 - 한 줄씩 쌓인다. : pack()
        self.label_title.pack()

        self.btn = Button(self.tkhandler, text='50,000원 후원하기', width=30)
        self.btn.pack()

    def run(self):
        self.tkhandler.mainloop()


g = GUI()
g.run()
