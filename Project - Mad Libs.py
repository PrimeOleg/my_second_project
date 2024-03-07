#******************************
# Mad Libs Project
# 07/03/2024

# WELCOME MESSAGE AND NAME
name = input("Enter your name/username: ")
print(f"Welcome {name} to mad libs game!")

# THE INPUTS FOR THE USER TO ENTER
adj1 = input("Please enter an adjective: ")
noun1 = input("Please Enter a noun: ")
verb1 = input("Please Enter a verb ending in ing: ")
adj2 = input("Please enter an adjective: ")
noun2 = input("Please enter another noun: ")
noun3 = input("Please enter another noun: ")
adj3 = input("please enter another adjective: ")
adj4 = input("Please enter another adjective: ")
noun4 = input("Please Enter another noun: ")
noun5 = input("Please Enter another noun: ")
noun6 = input("Please Enter another noun: ")
noun7 = input("Please Enter another noun: ")
noun8 = input("Please Enter another noun: ")
noun9 = input("Please Enter another noun: ")

# MESSAGES FOR BETTER USER EXPERIENCE
print("\nGenerating your Adventure story...")
print(f"Here we go {name}")

# TOTAL OUTPUT FOR THE USER'S STORY
print (f"""
       In a {adj1} land, a {noun1} with 
       {verb1} stumbled upon a {adj2} {noun2}. 
       This {noun3} led to an {adj3} journey. 
       Along the way, it faced a {adj4} dragon and a mischievous {noun4}. 
       But through {noun5} and {noun6}, it found the greatest {noun7} of all: {noun8}. 
       With hearts full of {noun9}, it returned home, forever changed.
       """)

