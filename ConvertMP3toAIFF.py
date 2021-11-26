import os
import os.path
chemin = os.listdir("/home/guillaume/Bureau/ITW")
for ligne in chemin:
	print (ligne)
	print ('ffmpeg -y -i ' + '~/Bureau/ITW/'+ligne + ' '  '~/Bureau/ITW/'+ ligne.split('mp3')[0]+'aiff')	
	os.system('ffmpeg -y -i ' + '~/Bureau/ITW/'+ligne + ' '  '~/Bureau/ITW/'+ ligne.split('mp3')[0]+'aiff')		
