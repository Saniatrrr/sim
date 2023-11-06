import random
import os
import time

logo = """
████╗░░░███╗░█████╗░██╗░░██╗██████╗░██╗░░░██╗██████╗░
████╗░████║██╔══██╗██║░░██║██╔══██╗██║░░░██║██╔══██╗
██╔████╔██║███████║███████║██████╦╝██║░░░██║██████╦╝
██║╚██╔╝██║██╔══██║██╔══██║██╔══██╗██║░░░██║██╔══██╗
██║░╚═╝░██║██║░░██║██║░░██║██████╦️╚██████╔️██████╦️
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════️╚═════️
-----------------------------------------------------------
-----------------------------------------------------------

Author   :  Mahabub
Github   :  Saniatrr
Facebook : ⭐⭐⭐⭐
Contact : 01643655880
-----------------------------------------------------------
-----------------------------------------------------------
"""


class Main:
    def __init__(self):
        os.system("clear")
        print(logo)
        print("\n [1] NEPAL NUMBER")
        print(" [2] INDIAN NUMBER\n")
        choice = input(" Choose: ")
        if choice in ["1", "01"]:
            self.nepal()
        elif choice in ["2", "02"]:
            self.generate_indian_sim_number()
        else:
            print("Select correctly.")
            time.sleep(1)
            Main()

    def nepal(self):
        # Generate a random 10-digit number
        os.system("clear")  # Corrected this line
        print(logo)
        sim_number = "+977" + str(random.randint(9800000000, 9899999999))

        # List of ANSI escape codes for different text colors
        text_colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"]

        # Randomly select a text color
        random_text_color = random.choice(text_colors)

        # Create the border with the random text color
        border = random_text_color + '+' + '-' * (len(sim_number) + 2) + '+' + "\033[0m"

        print(border)
        print(f'| {sim_number} |')
        print(border)

        print("Press 1 to go back")
        choice = input()
        if choice == "1":
            self.__init__()

    def generate_indian_sim_number(self):
        os.system("clear")  # Corrected this line
        print(logo)
        # Generate a random 10-digit number
        sim_number = "+91" + str(random.randint(7000000000, 9999999999))

        # List of ANSI escape codes for different text colors
        text_colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m"]

        # Randomly select a text color for the number
        random_text_color = random.choice(text_colors)

        # Create a blue border
        border = "\033[94m" + '+' + '-' * (len(sim_number) + 2) + '+' + "\033[0m"

        print(border)
        print(f"{random_text_color}{sim_number}\033[0m")
        print("Press 1 to go back")
        choice = input()
        if choice == "1":
            self.__init__()

Main()
