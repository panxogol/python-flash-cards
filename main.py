# --- IMPORTS ---
import tkinter as tk
from config import *


# --- FUNCTIONS ---
def main():
    # --- Inner Functions ---
    # --- UI Setup ---
    # Window
    window = tk.Tk()
    window.title(WINDOW_TITLE)
    window.config(bg=BACKGROUND_COLOR, padx=WINDOW_PAD_X, pady=WINDOW_PAD_Y)

    # Images
    front_card_img = tk.PhotoImage(file="./images/card_front.png")
    back_card_img = tk.PhotoImage(file="./images/card_back.png")
    right_img = tk.PhotoImage(file="./images/right.png")
    wrong_img = tk.PhotoImage(file="./images/wrong.png")

    # Cards
    canvas = tk.Canvas(width=800, height=526)
    canvas.create_image(400, 263, image=front_card_img)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=1, column=1)

    # Words
    lb_language = canvas.create_text(
        LB_LANG_X, LB_LANG_Y,
        text=LB_LANG_TEXT,
        font=(
            LB_LANG_FONT,
            LB_LANG_FONT_SIZE,
            LB_LANG_FONT_STYLE
        )
    )

    lb_word = canvas.create_text(
        LB_WORD_X, LB_WORD_Y,
        text=LB_WORD_TEXT,
        font=(
            LB_WORD_FONT,
            LB_WORD_FONT_SIZE,
            LB_WORD_FONT_STYLE
        )
    )

    # Buttons


    # --- MAINLOOP ---
    window.mainloop()


# --- RUN ---
if __name__ == '__main__':
    main()
