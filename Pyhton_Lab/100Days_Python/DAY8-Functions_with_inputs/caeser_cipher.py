print("welcome to vishnu's ceaser cipher")

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
should_continue=True
while should_continue:
    direction=input("Enter 'encode' for encryption of the text (or) enter 'decode' for decryption of the code.\n")
    text=input("Enter the text that is to be processed\n").lower()
    shift=int(input("Enter the number for shifting\n"))
    if direction == "decode":
        shift *= -1

    def ceaser(start_text, shift_amount , cipher_direction):
        end_text = ""
        for char in start_text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift_amount
                end_text += alphabet[new_position]
            else:
                end_text +=char
        print(f"The {cipher_direction}d text is:{end_text}")

    ceaser(start_text=text,cipher_direction=direction,shift_amount=shift)

    result=input("If you want to continue, enter 'yes' else enter 'no'\n")
    if result=="no":
        should_continue=False
        print("Good Bye 👋")




