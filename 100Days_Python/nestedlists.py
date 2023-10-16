print("welcome to vishnu's grocery store!")
fruits=['apple','orange','manderin','peach','blue berry','banana','lemon','grapes']
vegetables=['cucumber','carrot','beetroot','tomato','ginger','turmeric']
greens=['spinach','celery','mint']
diary=['milk','curd','butter milk','butter','ghee','paneer']
nuts=['cashews','almonds','pumpkin seeds','sunflower seeds','dates','raisins']
sweetners=['jaggery','honey']
protein=['eggs','chicken','urad dal']
carbs=['brown bread','brown rice','wheat bran','oats']
groceries=[fruits,vegetables,diary,nuts,sweetners,protein,carbs]
print('choose 0 for fruits\nchoose 1 for vegetables\nchoose 2 for greens\nchoose 3 for diary\nchoose 4 for nuts\nchoose 5 for sweeteners\nchoose 6 for protein\nchoose 7 for carbs ')
choice=int(input('enter your choice:'))
print(f'here you go,choose from the following {groceries[choice]}')
