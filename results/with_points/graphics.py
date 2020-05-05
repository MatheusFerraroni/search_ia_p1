import matplotlib.pyplot as plt
import numpy as np
import json

algoritmos = ["bfs", "dfs", "aos", "ats", "lbs"]
cenarios = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
metricas = ["times", "nodes", "pont", "left"]

for im in metricas:									

	tempo_maximo = 0
	tempo_max = 0

	x1 = []
	x2 = []
	x3 = []
	x4 = []
	x5 = []			

	y1 = []
	y2 = []
	y3 = []
	y4 = []
	y5 = []			
	
	y1_std = []
	y2_std = []
	y3_std = []
	y4_std = []
	y5_std = []

	for iy in algoritmos:					
		
		y = []
		y_std = []
		
		nameFile = im
		#print(nameFile)
		for ix in cenarios:				

			name = iy + "_map" + ix		
			#print(name)		
			f = open(name + ".out", "r")
			dados = json.loads(f.read())
			f.close()

			part = dados.get(im)			

			media = part.get("median")				

			tempo_max = part.get("max")				

			if tempo_max > tempo_maximo:
				tempo_maximo = tempo_max

			confianca = part.get("confidence")
			
			y.append(float(media))
			
			y_std.append(float(confianca))			
				
		if iy is "bfs":					
			y1=y
			y1_std=y_std
		if iy is "dfs":								
			y2=y
			y2_std=y_std				
		if iy is "aos":								
			y3=y
			y3_std=y_std
		if iy is "ats":								
			y4=y
			y4_std=y_std
		if iy is "lbs":								
			y5=y
			y5_std=y_std
			
	fig = plt.figure(2)
	plt.xlim(0.8, 15.2) #FOR PLR
	limitesup = tempo_maximo + tempo_maximo * 0.05
	limiteinf = -1 * tempo_maximo * 0.05
	plt.ylim(limiteinf, limitesup) #FOR PLR									
	index = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])	
	#plt.yscale('log')                                                             
	plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.90', zorder=0)    												
	plt.errorbar(index,y1, ls="-.", label='BFS',    color='g', yerr=y1_std, zorder=3)			
	plt.errorbar(index,y2, ls="-.", label='DFS',   color='b', yerr=y2_std, zorder=3)						
	plt.errorbar(index,y3, ls="-.", label='A*1',    color='r', yerr=y3_std, zorder=3)			
	plt.errorbar(index,y4, ls="-.", label='A*2',   color='black', yerr=y4_std, zorder=3)
	plt.errorbar(index,y5, ls="-.", label='LBS',   color='y', yerr=y5_std, zorder=3)
			
	if im == 'times':
		rx = 'Time (s)'
		metrica = 'Time'
	elif im == 'nodes':
		rx = 'Number of Nodes'
		metrica = 'Nodes'
	elif im == 'pont':
		rx = 'Number of Points'
		metrica = 'Points'
	else:
		rx = 'Number of left points'
		metrica = 'Left Points'

	titlex = "Metric: " + metrica	
	plt.ylabel(rx, fontweight="bold")	
	plt.title(titlex, fontweight="bold")
	plt.legend(numpoints=1,loc="upper left", ncol=1)
	plt.xlabel('Scenarios', fontweight="bold") # mudar
	#plt.show()
	fig.savefig(nameFile+'.png', format='png', dpi=600, bbox_inches='tight')   # save the figure to file
	plt.close(fig) 			

# Usar "-." ou ":" em vez da reta
# Traduzir tudo para inglês
# Colocar título e labels em negrito
# Acho que pode normalizar os dados para deixar mais fácil ver os dados (gerar as duas formas)
# Colocar todos os xticks no eixo X (todos os números dos experimentos)