print("Welcome to vishnu's ROCK-PAPER-SCISSORS")
import random
your_choice=int(input('choose 0 for rock,1 for paper,2 for scissors:'))
rock=''' 
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice=[rock,paper,scissors]  #you can try replacming the rock ,paper , scissors strings with the asci art
print(f'you : {choice[your_choice]}')
computer_choice=random.randint(0,2)
print(f'computer : {choice[computer_choice]}')
if your_choice==0 and computer_choice==2:
       print('congratulations 🎉 you won')
elif computer_choice==0 and your_choice==2:
       print('you lose 😔')
elif computer_choice>your_choice:
       print('you lose 😔')
elif computer_choice<your_choice:
       print('congratulations 🎉 you won')
elif computer_choice==your_choice:
       print('its a draw ⏱️')
else:
       print('you entered an invalid number, you lose.')















