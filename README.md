Custom Rich Presence (CRP) by Calamaitz

DESCRIPTION

Python script to simulate a custom Rich Presence on Discord.
Allows selecting a game, entering custom details, and continuously updating your Discord status.

FEATURES
- Game selection via dropdown menu.
- Enter custom details using a text box.
- Continuous Rich Presence updates every 15 seconds.
- Three buttons:
    - Start: start the simulation.
    - Stop: stop the Discord connection.
    - Exit: close the connection and exit the program.
- Automatically handles empty text box (uses "Playing Solo" as default).
- Smooth GUI thanks to threading.

REQUIREMENTS
- Python 3.11 or higher
- Python libraries:
    - pypresence (pip install pypresence)
    - Tkinter (included by default in Python)

HOW TO USE
1) Create your own Discord applications in the Discord Developer Portal and replace the Application IDs in the code.
2) Upload the image in the section Rich Presence > Art Assets, then name it "game_logo".
3) Add the name of the game and the application ID in the code:
    - Add your game name in the list "games".
    - Add your game name and application ID in the dictionary "games_to_IDs".
4) Download or clone the project.
5) Run the Python file: CRP.py
6) In the GUI window:
    - Select a game from the dropdown menu.
    - Optionally, enter custom details in the text box.
    - Press Start to activate Rich Presence.
    - Press Stop to disconnect from Discord.
    - Press Exit to close the program completely.

HOW IT WORKS
- Uses pypresence to connect to Discord and update your status.
- Connection and updates run in a separate thread so the GUI does not freeze.
- If the text box is empty, the default text "Playing Solo" is used.

CUSTOMIZATION
- To change the default text: modify the "Playing Solo" string.
- To change update frequency: adjust time.sleep(15) in the thread.

WARNINGS
- Make sure Discord is running when starting the script.
- Each game must be linked to a Discord application (with the same name as the game) in the Discord Developer Portal to display Rich Presence.
- Each game needs a valid Application ID to show Rich Presence correctly.
- Images used for Rich Presence (large_image) must be uploaded in the Discord Developer Portal.
