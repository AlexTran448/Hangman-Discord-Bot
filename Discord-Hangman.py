import discord
import random
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
            
        if message.content.startswith('!hangman'):
            await message.channel.send("Welcome to hangman!"+"\n"+"Here is a list of the difficulties you can choose from:"+"\n"+"-"+"\n"+"(1)Rookie - 15 lives for words of lengths 3-5 letters"+"\n"+"(2)Standard - 12 lives for words of lengths 4-8 letters"+"\n"+"(3)Intermediate - 8 lives for words of 6-9 letters"+"\n"+"(4)Insane - 8 lives for words of 10-20 letters"+"\n"+"(5)Extreme - 3 lives for words of 10-20 letters"+"\n"+"(6)Overkill - 2 lives for words of 16-20 letters"+"\n"+"Which difficulty would you like to choose? (1/2/3/4/5/6)")


            def CurrentRevealed(CurrentUserGuess, CurrentDashes, CurrentWord):
              Update = ""
              for i in range(len(CurrentWord)):
                  if CurrentWord[i] == CurrentUserGuess:
                      Update = Update + CurrentUserGuess
                  else:
                      Update = Update + CurrentDashes[i]
              return Update



            x = True
            while x:
                def is_correct(m):
                    return m.author == message.author and m.content.isdigit()
                try:
                    Dif = await self.wait_for('message', check=is_correct, timeout=10.0)
                except asyncio.TimeoutError:
                    return await message.channel.send("Sorry, you took too long")
                if Dif.content == ("1"):
                    x = False
                    file = open("english2.txt")
                    wordlist = file.readlines()
                    ChosenLives = 15
                    SecretWord = ("s")
                    while len(SecretWord) < 3 or len(SecretWord) > 5:
                        SecretWord = SecretWord.rstrip()
                        SecretWord = random.choice(wordlist)
                        SecretWord = SecretWord.rstrip()
                elif Dif.content == ("2"):
                    x = False
                    file = open("english2.txt")
                    wordlist = file.readlines()
                    ChosenLives = 12
                    SecretWord = ("s")
                    while len(SecretWord) < 4 or len(SecretWord) > 8:
                        SecretWord = SecretWord.rstrip()
                        SecretWord = random.choice(wordlist)
                        SecretWord = SecretWord.rstrip()
                elif Dif.content == ("3"):
                    x = False
                    file = open("english2.txt")
                    wordlist = file.readlines()
                    ChosenLives = 8
                    SecretWord = ("s")
                    while len(SecretWord) < 6 or len(SecretWord) > 9:
                        SecretWord = SecretWord.rstrip()
                        SecretWord = random.choice(wordlist)
                        SecretWord = SecretWord.rstrip()
                elif Dif.content == ("4"):
                    x = False
                    file = open("english2.txt")
                    wordlist = file.readlines()
                    ChosenLives = 8
                    SecretWord = ("s")
                    while len(SecretWord) < 10 or len(SecretWord) > 20:
                        SecretWord = SecretWord.rstrip()
                        SecretWord = random.choice(wordlist)
                        SecretWord = SecretWord.rstrip()
                elif Dif.content == ("5"):
                    x = False
                    file = open("english2.txt")
                    wordlist = file.readlines()
                    ChosenLives = 3
                    SecretWord = ("s")
                    while len(SecretWord) < 10 or len(SecretWord) > 20:
                        SecretWord = SecretWord.rstrip()
                        SecretWord = random.choice(wordlist)
                        SecretWord = SecretWord.rstrip()
                elif Dif.content == ("6"):
                    x = False
                    file = open("english2.txt")
                    wordlist = file.readlines()
                    ChosenLives = 2
                    SecretWord = ("s")
                    while len(SecretWord) < 16 or len(SecretWord) > 20:
                        SecretWord = SecretWord.rstrip()
                        SecretWord = random.choice(wordlist)
                        SecretWord = SecretWord.rstrip()
                else:
                    message.channel.send("Please choose a valid option!")

            validinput = 0
            Dashes = ("-" * len(SecretWord))
            await message.channel.send("The length of the chosen word is " + str(len(SecretWord))+"\n"+"You start with " + str(ChosenLives) + " Lives." + "\n" + Dashes + "\n" + "Guess a letter you think it is in the word: ")
            while ChosenLives > 0 and Dashes != SecretWord:
                line = ""
                UserGuess = await self.wait_for('message')
                if UserGuess.content == "!quit":
                    await message.channel.send("Hangman bot leaving!")
                    return
                if len(UserGuess.content) != 1:
                    validinput = 0
                elif UserGuess.content.isalpha():
                    UserGuess = UserGuess.content.lower()
                    if UserGuess in SecretWord:
                        line = "Good Guess! " + UserGuess + " is in the word. :)" + "\n"
                        Dashes = CurrentRevealed(UserGuess, Dashes, SecretWord)
                        validinput = 1
                    else:
                        line = "I'm afraid " + UserGuess + " isn't in the word. :(" + "\n"
                        ChosenLives -= 1
                        validinput = 1
                    line = line + "You have " + str(ChosenLives) + " lives currently left."
                else:
                    validinput = 0
                if validinput == 1:
                    line = line + "\n" + Dashes + "\n"+"Guess a letter you think it is in the word: "
                    print(line)
                    await message.channel.send(line)
            if ChosenLives == 0:
                await message.channel.send("Game Over! The word was " + SecretWord + ".")
            else:
                await message.channel.send("You win! The answer was " + SecretWord + ".")
                


client = MyClient()
client.run('NjM1ODk3NjQ4MDExOTM1Nzk0.Xa4PqA.cdAsV6BvfjXIl_3ebf__uj7P1bU')
