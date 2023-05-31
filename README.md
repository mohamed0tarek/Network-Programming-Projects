![Language](https://img.shields.io/badge/language-Python%20-yellow.svg) ![Language](https://img.shields.io/badge/language-Tkinter%20-orange.svg)


# Socket Programming with Python

This repository contains various projects related to socket programming using Python. The projects are organized into two main directories: **"Chat Projects"** and **"Games"**.

## Chat Projects

The **"Chat Projects"** directory consists of three subdirectories:

### Simple Chat
This directory contains a simple chat application implemented using socket programming in Python. It allows two users to exchange messages with each other by connecting through a shared port on the localhost. The chat functionality is achieved using the **`server.py`** and **`client.py`** files.

### Chat Room
The **"Chat Room"** directory contains a more advanced chat application that simulates a chat room environment. Multiple users can connect to the chat room through a common port on the localhost by running the **`server.py`** file. Once connected, they can exchange messages and participate in group conversations.

### Chat Room with GUI
In this directory, you'll find a chat room application with a graphical user interface (GUI) created using Tkinter. Users can connect to the chat room by running the **`server.py`** file. The GUI provides an intuitive interface for sending and receiving messages in the chat room.

## Games

The **"Games"** directory consists of two subdirectories:

### Rock-Paper-Scissors
This directory contains a simple implementation of the classic game **"Rock-Paper-Scissors"** using socket programming in Python and implemented with a graphical user interface (GUI) created using Tkinter. Users can connect to the game server through a specified port on the localhost and play against each other. The server functionality is implemented in the **`server.py`** file.

### Tic-Tac-Toe
In this directory, you'll find an implementation of the popular game **"Tic-Tac-Toe"** using socket programming and implemented with a graphical user interface (GUI) created using Tkinter. Multiple users can connect to the game server by running the **`server.py`** file and take turns playing the game on a shared board.

## Getting Started

To run any of the projects in this repository, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the desired project directory.
3. Make sure you have Python and Tkinter installed on your system.
4. Run the Python script associated with the project (e.g., `python server.py`, `python client.py`).
5. Connect to the specified port on the localhost using the corresponding client(s) or GUI.

Note: Each project may have specific dependencies. If required, please refer to the project's individual README file for additional setup instructions.

## Contributions

Contributions to this repository are welcome! If you have any bug fixes, improvements, or new features to add, please follow the guidelines outlined in the CONTRIBUTING.md file.

## License

This repository is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as per the license terms.
