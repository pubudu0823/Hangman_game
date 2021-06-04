import os;

while True :

    x = 0;
    while x < 5 :
        word = input('Enter the word (Alphabetic characters only): ')
        if word.isalpha() == True :
            break;
        else :
            print("Only alphabetic characters are allowed")
            x += 1;
    if x == 5 :
        print("Too many invalid inputs. Exiting the program...")
        exit();

    os.system("cls");

    #word = 'experiment';

    ShowWord = list(word);
    WordCopy = list(word);
    ErrorCount = 0;

    for i in range(0,len(ShowWord)):
        ShowWord[i] = "__ ";

    GuessedLetters = {}

    for j in range(0,len(ShowWord)+10):

        print("")
        guess = input('Guess a letter: ')
        guess = guess[0:1];
        print("Your input is " + guess)
        k = 0;
        while k < 10 :
            if guess in GuessedLetters or guess.capitalize() in GuessedLetters:
                print("You've already tried this letter. Try something else!")
                guess = input('Guess a Letter: ')
                guess = guess[0:1];
                print("Your input is " + guess)
            else :
                GuessedLetters[guess.capitalize()] = "null"
                break;
            k += 1;

        MatchedLetters = [];

        LetterMatched = 99
        for i in range(0,len(WordCopy)):
            if guess.capitalize() == WordCopy[i].capitalize():
                MatchedLetters.append(i);
                LetterMatched = 1

        if LetterMatched != 1 :
            ErrorCount += 1

        if ErrorCount == 6 :
            print("You lost :(")
            print("The word is " + word)
            break;

        print("You've made " + str(ErrorCount) + " errors so far");

        for key in GuessedLetters :
            print(key, end = " ");

        for i in range(0,len(ShowWord)):
            if i in MatchedLetters :
                ShowWord[i] = guess;

        print("")
#        print(ShowWord);

        for i in range(0, len(ShowWord)):
            print(ShowWord[i], end = " ");

        if "__ " not in ShowWord :
            print("")
            print("You Won!!!")
            break;