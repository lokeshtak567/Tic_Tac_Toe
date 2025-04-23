# 🕹️ Tic Tac Toe - Python Tkinter GUI

A visually rich and interactive Tic Tac Toe game built using Python's Tkinter library. Supports both multiplayer and AI gameplay modes with custom themed graphics.

---

## 🎮 Features
- GUI built with **Tkinter**
- **Two gameplay modes**:
  - **AI Mode**: Play against a simple AI opponent
  - **Multiplayer Mode**: Play with another person
- **Custom assets**: All buttons, board, and indicators have themed images
- **Restart** and **Main Menu** options available mid-game

---

## 📁 Folder Structure
```
TicTacToe-GUI/
├── GUI.py                # Main game script
├── README.md             # Project documentation
└── images/               # All image assets used in the game
    ├── mmbg.png          # Main menu background
    ├── ai_btn.png        # AI mode button
    ├── mp_btn.png        # Multiplayer button
    ├── exit_btn.png      # Exit button
    ├── credits_btn.png   # Credits button
    ├── mpbg.png          # Multiplayer background
    ├── aibg.png          # AI background
    ├── menu_btn.png      # Menu button in-game
    ├── rst_btn.png       # Restart button
    ├── ext2_btn.png      # Exit button in-game
    ├── board.png         # Game board
    ├── playn.png         # Play button (initial)
    ├── showo.png         # O's turn indicator
    ├── showx.png         # X's turn indicator
    ├── xwon.png          # X wins
    ├── owon.png          # O wins
    ├── nwon.png          # Draw (no one wins)
    ├── playx.png         # X symbol
    ├── playo.png         # O symbol
    └── credits.png       # Credits screen
```

---

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone or download the project.
3. Make sure all images are present in the `images/` folder.
4. Run the game:

```bash
python GUI.py
```

---

## 🧠 AI Logic
The AI uses basic logic to:
- Block the opponent if they’re about to win
- Try to win if a winning move is available
- Otherwise, play a semi-random move based on game state

---

## ✍️ Credits
This game was built with passion for a Python GUI project by Lokesh Tak in 2024. All custom graphics were designed or sourced to enhance gameplay experience.

---

## 📜 License
This project is open-source for educational and personal use. Attribution appreciated!
