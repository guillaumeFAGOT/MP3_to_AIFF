# petite fonction python a utiliser sur machine qui supporte python (de base sur machine issus de Linux.)
# on importe les libraires python
import os
import os.path
# recuperation des fichiers dans le repertoire
chemin = os.listdir("/home/guillaume/ITW")
for ligne in chemin:
	# liste des fichiers existants
	print (ligne)
	# verification de la commande ffmpeg
	print ('ffmpeg -y -i ' + '~/Bureau/ITW/'+ligne + ' '  '~/Bureau/ITW/'+ ligne.split('mp3')[0]+'aiff')
	# lancement de la commande
	os.system('ffmpeg -y -i ' + '~/Bureau/ITW/'+ligne + ' '  '~/Bureau/ITW/'+ ligne.split('mp3')[0]+'aiff')		
