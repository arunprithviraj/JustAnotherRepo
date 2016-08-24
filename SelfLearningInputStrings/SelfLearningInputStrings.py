KingName = ''
QueenName = ''
PrinceName = ''
KingdomName = ''
KingDiedBy = ''
#Get the input from the user to form the story  
KingName = input('Enter the name of the King in the story : ')
QueenName = input('Enter the name of the Queen in the story : ')
PrinceName = input('Enter the name of the Prince in the story : ')
KingdomName = input('Enter the name of the Kingdom in the story : ')
KingDiedBy = input('How the king died : ')

#Check whether King Name has Manu which is not allowed
ManuAvailable = KingName.find('Manu')
print(KingName.find('Manu'))
print(KingName)
if (ManuAvailable != -1):
     KingName = input('Manu not allowed, Enter the name of the King in the story : ')

#The story is formed by the input from user
print('\nOnce upon time in ' + KingdomName + ' there lived a king named ' + KingName + ', he had a lovely wife '+ QueenName +'.')
print(' Once the young prince ' + PrinceName + ' grew old enough, the king died by ' + KingDiedBy.upper())