#!/usr/bin/env python3

import os
import sys
import time
import subprocess
import random

class TerminalQuest:
    def __init__(self):
        self.player = {"name": "", "level": 1, "xp": 0}
        self.levels = [
            {
                "name": "File Explorer",
                "description": "Learn to navigate the file system",
                "tasks": [
                    {"command": "ls", "description": "List files in the current directory"},
                    {"command": "cd", "description": "Change directory"},
                    {"command": "pwd", "description": "Print working directory"}
                ]
            },
            {
                "name": "File Manipulator",
                "description": "Master file creation and modification",
                "tasks": [
                    {"command": "touch", "description": "Create a new file"},
                    {"command": "cp", "description": "Copy a file"},
                    {"command": "mv", "description": "Move or rename a file"}
                ]
            }
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        self.clear_screen()
        print("=" * 50)
        print("Terminal Quest - Master the Linux Command Line")
        print("=" * 50)
        print(f"Player: {self.player['name']} | Level: {self.player['level']} | XP: {self.player['xp']}")
        print("=" * 50)

    def get_player_name(self):
        self.print_header()
        self.player["name"] = input("Enter your name, brave terminal explorer: ")

    def show_main_menu(self):
        while True:
            self.print_header()
            print("\nMain Menu:")
            print("1. Start Quest")
            print("2. View Character")
            print("3. Exit Game")
            choice = input("\nEnter your choice (1-3): ")

            if choice == "1":
                self.start_quest()
            elif choice == "2":
                self.view_character()
            elif choice == "3":
                print("Thank you for playing Terminal Quest. Goodbye!")
                sys.exit()
            else:
                input("Invalid choice. Press Enter to try again.")

    def start_quest(self):
        current_level = self.levels[self.player["level"] - 1]
        self.print_header()
        print(f"\nCurrent Quest: {current_level['name']}")
        print(f"Description: {current_level['description']}")
        print("\nTasks:")
        for i, task in enumerate(current_level['tasks'], 1):
            print(f"{i}. {task['description']} (use '{task['command']}')")

        input("\nPress Enter to start the quest...")

        for task in current_level['tasks']:
            self.print_header()
            print(f"\nTask: {task['description']}")
            print(f"Use the '{task['command']}' command to complete this task.")

            user_input = input("\nEnter your command: ")
            if user_input.strip() == task['command']:
                print("Great job! Task completed successfully.")
                self.player['xp'] += 10
            else:
                print(f"Oops! The correct command was '{task['command']}'. Try again next time!")

            input("\nPress Enter to continue...")

        self.player['level'] += 1
        print(f"\nCongratulations! You've completed the '{current_level['name']}' quest!")
        print(f"You've advanced to level {self.player['level']}!")
        input("\nPress Enter to return to the main menu...")

    def view_character(self):
        self.print_header()
        print("\nCharacter Information:")
        print(f"Name: {self.player['name']}")
        print(f"Level: {self.player['level']}")
        print(f"XP: {self.player['xp']}")
        input("\nPress Enter to return to the main menu...")

    def run(self):
        self.get_player_name()
        self.show_main_menu()

if __name__ == "__main__":
    game = TerminalQuest()
    game.run()
