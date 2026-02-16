import tkinter as tk
import random

root = tk.Tk()
root.title("Royal Surprise 👑")
root.geometry("900x650")
root.configure(bg="black")

canvas = tk.Canvas(root, width=900, height=650, bg="black", highlightthickness=0)
canvas.pack()

# ---------------- FLOATING HEARTS ----------------
hearts = []

def create_heart():
    x = random.randint(50, 850)
    heart = canvas.create_text(x, 650, text="💖", font=("Arial", 20))
    hearts.append(heart)

def animate_hearts():
    for heart in hearts:
        canvas.move(heart, 0, -2)
        pos = canvas.coords(heart)
        if pos and pos[1] < 0:
            canvas.delete(heart)
            hearts.remove(heart)
    if len(hearts) < 15:
        create_heart()
    root.after(100, animate_hearts)

# ---------------- WELCOME ----------------
canvas.create_text(450, 200, text="Welcome Malkin Jii 👑",
                   fill="gold", font=("Georgia", 40, "bold"))
canvas.create_text(450, 260, text="Bihari Jii ❤️",
                   fill="white", font=("Georgia", 28, "bold"))

def show_popup():
    popup = tk.Toplevel(root)
    popup.geometry("300x120+350+300")
    popup.configure(bg="black")
    popup.overrideredirect(True)
    label = tk.Label(popup, text="my love ❤️",
                     font=("Arial", 22, "bold"),
                     fg="#ff4d6d", bg="black")
    label.pack(expand=True)
    root.after(1000, popup.destroy)

root.after(2000, show_popup)

# ---------------- CAKE SCENE ----------------
def show_cake_scene():
    canvas.delete("all")
    canvas.configure(bg="#ffe6f2")

    animate_hearts()

    canvas.create_text(450, 80,
                       text="Royal Rajma Chawal Cake 🎂",
                       font=("Georgia", 30, "bold"),
                       fill="darkred")

    canvas.create_rectangle(300, 350, 600, 400, fill="white")
    canvas.create_rectangle(300, 300, 600, 350, fill="#7b0000")

    draw_girl()

    cut_btn = tk.Button(root, text="Cut Cake 🎂",
                        font=("Arial", 14, "bold"),
                        command=cut_cake)
    cut_btn.place(x=400, y=580)

# ---------------- GIRL DRAW ----------------
def draw_girl():
    global left_eye, right_eye, hair, hand

    hair = canvas.create_arc(670, 260, 740, 340,
                             start=0, extent=180,
                             fill="black")

    canvas.create_oval(680, 280, 730, 330, fill="#ffe0bd")

    left_eye = canvas.create_oval(695, 300, 700, 305, fill="black")
    right_eye = canvas.create_oval(710, 300, 715, 305, fill="black")

    canvas.create_arc(695, 310, 715, 325,
                      start=200, extent=140, style=tk.ARC)

    canvas.create_line(705, 330, 705, 420, width=4)

    hand = canvas.create_line(705, 350, 660, 370, width=3)
    canvas.create_line(705, 350, 750, 370, width=3)

    canvas.create_polygon(680, 420, 730, 420, 705, 480,
                          fill="#ff66b2")

    blink()
    move_hair()

# ---------------- BLINK ----------------
def blink():
    canvas.itemconfig(left_eye, state="hidden")
    canvas.itemconfig(right_eye, state="hidden")

    def open_eyes():
        canvas.itemconfig(left_eye, state="normal")
        canvas.itemconfig(right_eye, state="normal")
        root.after(random.randint(2000,4000), blink)

    root.after(200, open_eyes)

# ---------------- HAIR MOVE ----------------
def move_hair():
    canvas.move(hair, 2, 0)

    def back():
        canvas.move(hair, -2, 0)
        root.after(2000, move_hair)

    root.after(200, back)

# ---------------- CUT ----------------
slice_piece = None

def cut_cake():
    global slice_piece
    slice_piece = canvas.create_polygon(
        450, 300, 520, 350, 450, 350,
        fill="#7b0000"
    )

    eat_btn = tk.Button(root, text="Eat Cake 🍰",
                        font=("Arial", 14, "bold"),
                        command=eat_cake)
    eat_btn.place(x=400, y=580)

# ---------------- EAT ----------------
def eat_cake():
    move_slice()

def move_slice():
    coords = canvas.coords(slice_piece)
    if coords and coords[0] < 660:
        canvas.move(slice_piece, 6, -2)
        canvas.move(hand, 2, -1)  # hand moves while eating
        root.after(30, move_slice)
    else:
        canvas.delete(slice_piece)
        fade_background()

# ---------------- BACKGROUND FADE ----------------
def fade_background():
    colors = ["#330000", "#550000", "#770000", "#990000", "#000000"]
    def fade(i=0):
        if i < len(colors):
            canvas.configure(bg=colors[i])
            root.after(400, fade, i+1)
        else:
            typewriter_effect()
    fade()

# ---------------- TYPEWRITER ----------------
def typewriter_effect():
    canvas.delete("all")
    canvas.configure(bg="black")

    message = """Thankyou for being huge part of my life
I enjoyed every moment with you

Khair jab kisi ki nazar lagg jaye
to ache se ache bonds toot jaate hain

And yes,
Thanksalot ❤️
Jazaak Allah
Tysm

I do love you a lot
even if I don't show it."""

    text_obj = canvas.create_text(
        450, 320,
        text="",
        fill="gold",
        font=("Georgia", 22, "bold"),
        justify="center"
    )

    def animate(i=0):
        if i <= len(message):
            canvas.itemconfig(text_obj, text=message[:i])
            root.after(40, animate, i+1)
        else:
            fireworks()

    animate()

# ---------------- FIREWORKS ----------------
def fireworks():
    for i in range(25):
        x = random.randint(100,800)
        y = random.randint(100,500)
        canvas.create_text(x, y, text="✨", font=("Arial", 20))

# ---------------- AUTO ----------------
root.after(5000, show_cake_scene)

root.mainloop()
