import tkinter as tk
from pypresence import Presence
import threading
import time
import sys

# Game Lists
games = ["EA SPORTS FC 26", "Assassin's Creed Empire", "Grand Theft Auto VI", "Grand Theft Auto VII", "Minecraft 2"]
games_to_IDs = {
    "EA SPORTS FC 26": "1412500934629658796",
    "Assassin's Creed Empire": "1412509262428508430",
    "Grand Theft Auto VI": "1412535497779052656",
    "Grand Theft Auto VII": "1412539440294924398",
    "Minecraft 2": "1412559702251933798"
}

# Global variables for RPC connection
RPC = None
flag_running = False  # flag to stop the thread

def start_presence():
    global RPC, flag_running
    game_title = game_choice.get()
    game_ID = games_to_IDs[game_title]
    game_details = entry.get().strip()
    if not game_details:
        game_details = "Playing Solo"

    # Close any previous RPC
    if RPC is not None:
        try:
            RPC.close()
        except Exception:
            pass

    RPC = Presence(game_ID)
    RPC.connect()
    flag_running = True
    label_status.config(text = f"Discord connected to {game_title}")

    def worker():
        global flag_running
        while flag_running:
            try:
                RPC.update(
                    details = game_details,
                    large_image = "game logo",
                    large_text = game_title,
                )
            except Exception as e:
                label_status.config(text = "Error")
                flag_running = False
            time.sleep(15)

    threading.Thread(target = worker, daemon = True).start()

def stop_presence():
    global flag_running, RPC
    flag_running = False
    if RPC is not None:
        try:
            RPC.close()
            label_status.config(text = "Connection interrupted")
        except:
            pass
        RPC = None

def close_program():
    stop_presence()       # Close RPC
    window.destroy()      # Close Tkinter window
    sys.exit(0)           # End the program

# Create the main window
window = tk.Tk()
window.geometry("600x400")
window.resizable(False, False)
window.title("CRP by Calamaitz")

# Title Label
label_title = tk.Label(window, text = "Custom Rich Presence\nby Calamaitz")
label_title.place(x = 20, y = 20)

# Control variable for the drop-down menu
game_choice = tk.StringVar(window)
game_choice.set(games[0])  # Default Value

# Menu
menu = tk.OptionMenu(window, game_choice, *games)
menu.place(x = 20, y = 100)

# Game Details
entry = tk.Entry(window, width = 23)  # width in caratteri
entry.place(x = 20, y = 150)

# Start/Stop/Exit buttons
button1 = tk.Button(window, text = "Start", command = start_presence, width = 5)
button1.place(x = 20, y = 200)

button2 = tk.Button(window, text = "Stop", command = stop_presence, width = 5)
button2.place(x = 70, y = 200)

button3 = tk.Button(window, text = "Exit", command = close_program, width = 5)
button3.place(x = 120, y = 200)

# Status Label
label_status = tk.Label(window, text = "")
label_status.place(x = 20, y = 250)

# GUI
if __name__ == "__main__":
    window.mainloop()