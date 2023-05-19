import tkinter as tk

def create_vector(size):
    return [None] * size

def set_value(vector, index, value):
    vector[index] = value

def get_value(vector, index):
    return vector[index]

def update_word_label(word_label, guessed_letters):
    word_label.config(text=" ".join([letter if letter else "_" for letter in guessed_letters]))

def hangman_game():
    word = "rogerio"  
    word_length = len(word)
    guessed_letters = create_vector(word_length)

    attempts = 6
    guessed_all_letters = False

    def guess_letter():
        nonlocal attempts, guessed_all_letters
        guess = guess_entry.get().lower()
        guess_entry.delete(0, tk.END)

        if len(guess) != 1:
            result_label.config(text="Please enter a single letter.")
            return

        if guess in guessed_letters:
            result_label.config(text="You already guessed that letter.")
            return

        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    set_value(guessed_letters, i, guess)
        else:
            attempts -= 1
            result_label.config(text="Incorrect guess! Attempts left: " + str(attempts))

        update_word_label(word_label, guessed_letters)

        if all(letter is not None for letter in guessed_letters):
            guessed_all_letters = True
            result_label.config(text="Congratulations! You guessed the word: " + word)

        if attempts == 0:
            result_label.config(text="Game over! The word was: " + word)

    window = tk.Tk()
    window.title("Hangman Game")

    word_label = tk.Label(window, text=" ".join(["_" for _ in range(word_length)]), font=("Arial", 24))
    word_label.pack(pady=20)

    guess_frame = tk.Frame(window)
    guess_frame.pack()

    guess_entry = tk.Entry(guess_frame, font=("Arial", 14))
    guess_entry.pack(side=tk.LEFT, padx=5)
    guess_button = tk.Button(guess_frame, text="Guess", font=("Arial", 14), command=guess_letter)
    guess_button.pack(side=tk.LEFT)

    result_label = tk.Label(window, text="", font=("Arial", 14))
    result_label.pack(pady=20)

    window.mainloop()

hangman_game()
