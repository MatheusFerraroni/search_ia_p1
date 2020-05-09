import matplotlib.pyplot as plt
import matplotlib.markers as plm
import numpy as np
import json

algoritmos = ["lbs", "dfs", "bfs", "aos", "ats", "hill"]
metricas = ["times", "nodes", "acti", "nodes_per_sec", "expa", "expanded_per_sec"]
vistaMap = ["all", "dense", "nodense"]

for iv in vistaMap:

	if iv is "all":
		cenarios = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
	if iv is "dense":
		cenarios = ["1", "3", "2", "9", "5", "7"]
	if iv is "nodense":
		cenarios = ["4", "10", "11", "12"]

	for im in metricas:									

		maximo = 0
		maxi = 0	

		x1 = []
		x2 = []
		x3 = []
		x4 = []
		x5 = []			
		x6 = []			

		y1 = []
		y2 = []
		y3 = []
		y4 = []
		y5 = []
		y6 = []			
		
		y1_std = []
		y2_std = []
		y3_std = []
		y4_std = []
		y5_std = []
		y6_std = []

		mean1 = 0
		mean1 = 0
		mean3 = 0
		mean4 = 0 
		mean5 = 0
		mean6 = 0


		for iy in algoritmos:					
			
			y = []
			y_std = []
			
			nameFile = iv+"_"+im
			#print(nameFile)
			for ix in cenarios:				

				name = iy + "_map" + ix		
				print(name)		
				f = open("../results/no_points/" + name + ".out", "r")
				dados = json.loads(f.read())
				f.close()

				if im is "nodes_per_sec":
					part_time = dados.get('times')
					media_time = part_time.get("median")
					confianca_time = part_time.get("confidence")
					part_nodes = dados.get('nodes')
					media_nodes = part_nodes.get("median")
					confianca_nodes = part_nodes.get("confidence")
					y.append(float(media_nodes/media_time))
					y_std.append(float(confianca_time))	
					maxi = float(media_nodes/media_time)
					if maxi > maximo:
						maximo = maxi
				elif im is "expanded_per_sec":
					part_time = dados.get('times')
					media_time = part_time.get("median")
					confianca_time = part_time.get("confidence")
					part_exp = dados.get('expa')
					media_exp = part_exp.get('median')
					confianca_exp = part_exp.get('confidence')
					y.append(float(media_exp/media_time))
					y_std.append(float(confianca_time))
					maxi = float(media_exp/media_time)
					if maxi > maximo:
						maximo = maxi
				else:
					part = dados.get(im)
					media = part.get("median")				
					maxi = part.get("max")	
					if maxi > maximo:
						maximo = maxi	
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
			if iy is "hill":
				y6=y
				y6_std=y_std

		mean1= np.mean(y1)
		mean2= np.mean(y2)
		mean3= np.mean(y3)
		mean4= np.mean(y4)
		mean5= np.mean(y5)
		mean6= np.mean(y6)
		
			
		fig = plt.figure(2)
	
		limitesup = maximo + maximo * 0.05
		limiteinf = -1 * maximo * 0.05

		if im is "acti":
			plt.ylim(limiteinf, limitesup)
		elif im is "pont":
			plt.ylim(limiteinf, limitesup)
		else:
			plt.yscale('log')



		if iv is "all":
			plt.xlim(0.65, 12.45)
			index = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
			plt.xticks(index, rotation = "horizontal")

		
		if iv is "dense":
			plt.xlim(0.65, 6.45) 
			index = np.array([1,2,3,4,5,6])	
			x_label  = ['1', '3', '2', '9', '5', '7']
			plt.xticks(index, x_label, rotation = "horizontal")
		
		if iv is "nodense":
			plt.xlim(0.85, 4.25) #FOR PLR
			index = np.array([1,2,3,4])
			x_label  = ['4', '10', '11', '12']
			plt.xticks(index, x_label, rotation = "horizontal")

  
		plt.grid(True, which="both", ls="-", linewidth=0.1, color='0.90', zorder=0)    												
		plt.errorbar(index,y1, ls="solid", label='BFS, avg='+str("{:.1f}".format(mean1)), marker= plm.CARETDOWNBASE, color='g', yerr=y1_std, zorder=3)			
		plt.errorbar(index,y2, ls="dashdot", label='DFS, avg='+str("{:.1f}".format(mean2)), marker= plm.CARETLEFTBASE, color='b', yerr=y2_std, zorder=3)						
		plt.errorbar(index,y3, ls="dotted", label='A*1, avg='+str("{:.1f}".format(mean3)), marker= plm.CARETUPBASE, color='r', yerr=y3_std, zorder=3)			
		plt.errorbar(index,y4, ls="dashed", label='A*2, avg='+str("{:.1f}".format(mean4)), marker= plm.CARETRIGHTBASE, color='m', yerr=y4_std, zorder=3)
		plt.errorbar(index,y5, ls="dotted", label='LBS, avg='+str("{:.1f}".format(mean5)), marker='o', color='c', yerr=y5_std, zorder=3)	
		plt.errorbar(index,y6, ls="dashdot", label='HILL, avg='+str("{:.1f}".format(mean6)), marker='x', color='black', yerr=y6_std, zorder=3)	
			
				
		if im == 'times':
			rx = 'Time (s)'
			metrica = 'Time'
		elif im == 'nodes':
			rx = 'Number of Nodes'
			metrica = 'Nodes'
		elif im == 'pont':
			rx = 'Number of Points'
			metrica = 'Points'
		elif im == 'acti':
			rx = 'Action'
			metrica = 'Actions'
		elif  im == 'left':
			rx = 'Number of left points'
			metrica = 'Left Points'
		elif im == 'expa':
			rx = 'Expanded Nodes'
			metrica = 'Expanded Nodes'
		elif im == 'expanded_per_sec':
			rx = 'Expanded Nodes per Second'
			metrica = 'Expanded Nodes per Second'
		else:
			rx = 'Number of Nodes per Second'
			metrica = 'Nodes per Second'

		titlex = "Metric: " + metrica	
		plt.ylabel(rx, fontweight="bold")	
		#plt.title(titlex, fontweight="bold")
		plt.legend(numpoints=1, loc="upper left", ncol=3, bbox_to_anchor=(-0.02, 1.15))
		plt.xlabel('Scenario', fontweight="bold") # mudar
		#plt.show()
		fig.savefig('../plots/no_points/'+nameFile+'.pdf', format='pdf', dpi=600, bbox_inches='tight')   # save the figure to file
		plt.close(fig) 			

# Usar "-." ou ":" em vez da reta
# Traduzir tudo para inglês
# Colocar título e labels em negrito
# Acho que pode normalizar os dados para deixar mais fácil ver os dados (gerar as duas formas)
# Colocar todos os xticks no eixo X (todos os números dos experimentos)