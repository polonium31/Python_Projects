with open("Input/Names/invited_names.txt","r") as name:
    names = name.readlines()
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for i in names:
        place_holder = "[name]"
        stripped = i.strip()
        new_letter = letter_contents.replace(place_holder, i)
        with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt","w") as complete_letter:
            complete_letter.write(new_letter)