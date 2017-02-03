is_raining = input("Is it raining outside?")
 
if is_raining == "yes":
    have_umbrella = input("Do you have an umbrella?")
    if have_umbrella == "yes":
        print("Let's go!!!")
    else:
        print("Let's wait a moment.")
        is_raining = input("Is it still raining outside?")
        while is_raining == 'yes':
            print("Let's wait a moment.")
            is_raining = input("Is it still raining outside?")
        print("Let's go!!!")
else:
    print("Let's go!!!")