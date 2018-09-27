import random

logins = {'MrMulla':'Password123','admin':'admin','example':'WeakPassword'}
songs = [line.replace('\n','').split('-') for line in open("songsList.txt", "r")]
open("songsList.txt", "r").close()
carryOn, points = 1, 0

username = input('User Name: ')
if username in logins and logins[username] == input('password: '):
  while carryOn == 1:
    randNum = random.randint(0,len(songs)-1)
    print('\nGuess the song:\n%s - %s' %(songs[randNum][0],''.join(word[0] for word in songs[randNum][1].split()).upper()))
    if input('').upper() == songs[randNum][1].upper():
      points += 3
      print('\nCorrect!\n+3 points\nYou have %s points' %(points))
    elif input('\nIncorrect,\nTry Again:\n').upper() == songs[randNum][1].upper():
      points += 1
      print('\nCorrect!\n+1 point\nYou have %s points' %(points))
    elif True:
      print('\nIncorrect again!\nThe correct answer was: %s\nFinal points: %s\n\nScore Chart:' %(songs[randNum][1],points))
      scoresFile = open("scores.txt", "r+")
      scoresFile.writelines('\n%s-%s'%(username, points))
      scores = sorted([line.replace('\n','').split('-') for line in scoresFile],key=lambda l:l[1], reverse=True)
      for line in scores[0:5]:
        print('%s %s' %(line[1],line[0]))
      scoresFile.close()
      carryOn = 0
else:
  print('\nincorrect username or password')