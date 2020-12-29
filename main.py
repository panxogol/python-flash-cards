# --- IMPORTS ---
import tkinter as tk
from config import *
import pandas as pd
from random import choice

# --- GLOBALS ---
flip_timer = None
unknown_words = []
known_words = []
showed_words = []
words_df = None
try:
    words_df = pd.read_csv(DATA_UNLEARNED)

except FileNotFoundError:
    words_df = pd.read_csv(DATA)

finally:
    unknown_words = words_df.to_dict(orient="records")


# --- FUNCTIONS ---
def main():
    global flip_timer

    # --- Inner Functions ---
    # Known Answer
    def rightWord():
        global known_words
        current_word = randomWord()
        known_words += current_word
        unknown_words.remove(current_word)
        words_to_learn = pd.DataFrame(unknown_words)
        words_to_learn.to_csv(DATA_UNLEARNED, index=False)

    # Next card
    def randomWord():
        global flip_timer, unknown_words, showed_words
        window.after_cancel(flip_timer)
        # Variables
        current_card = choice(unknown_words)
        while current_card in showed_words:
            current_card = choice(unknown_words)
        showed_words += current_card
        language = "French"
        word = current_card[language]
        new_color = "black"

        # Configs
        canvas.itemconfig(canvas_image, image=front_card_img)
        canvas.itemconfig(lb_language, text=language, fill=new_color)
        canvas.itemconfig(lb_word, text=word, fill=new_color)

        # Flip the card after 3 sec
        flip_timer = window.after(5000, flipCard, current_card)
        return current_card

    # Flip card
    def flipCard(current_card: dict):
        new_language = "English"
        new_color = "white"
        canvas.itemconfig(canvas_image, image=back_card_img)
        canvas.itemconfig(lb_language, text=new_language, fill=new_color)
        canvas.itemconfig(lb_word, text=current_card[new_language], fill=new_color)

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
    canvas_image = canvas.create_image(400, 263, image=front_card_img)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

    # Words
    lb_language = canvas.create_text(
        LB_LANG_X, LB_LANG_Y,
        font=(
            LB_LANG_FONT,
            LB_LANG_FONT_SIZE,
            LB_LANG_FONT_STYLE
        )
    )

    lb_word = canvas.create_text(
        LB_WORD_X, LB_WORD_Y,
        font=(
            LB_WORD_FONT,
            LB_WORD_FONT_SIZE,
            LB_WORD_FONT_STYLE
        )
    )

    # Buttons
    btn_right = tk.Button(image=right_img, highlightthickness=0, command=rightWord)
    btn_right.grid(row=1, column=1)

    btn_wrong = tk.Button(image=wrong_img, highlightthickness=0, command=randomWord)
    btn_wrong.grid(row=1, column=0)

    # Initial state
    flip_timer = window.after(0, randomWord)

    # --- MAINLOOP ---
    window.mainloop()


# --- RUN ---
if __name__ == '__main__':
    main()
