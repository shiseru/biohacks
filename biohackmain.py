# Importing libraries to draw gene graph
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.gridspec import GridSpec


# Sample dict(data) used in graph.

data={
      "cluster": 1,
      "member_cnt": 21343,
      "generation": {"11-15": 284, "81-85": 216, "0-5": 10,
                     "76-80": 486, "16-20": 840, "56-60": 1938,
                     "unknown": 558, "61-65": 1561, "86-90": 51,
                     "51-55": 2504, "46-50": 2639, "6-10": 18,
                     "31-35": 1501, "41-45": 2410, "36-40": 1954,
                     "66-70": 1486, "91 over": 23, "26-30": 989,
                     "21-25": 976, "71-75": 899},
      "gender": {"M": 11652, "F": 9691}
     }


# data={
#       "cluster": [1],
#       "member_cnt": [21343],
#       "generation": {"11-15": [284], "81-85": [216], "0-5": [10],
#                      "76-80": [486], "16-20": [840], "56-60": [1938],
#                      "unknown": [558], "61-65": [1561], "86-90": [51],
#                      "51-55": [2504], "46-50": [2639], "6-10": [18],
#                      "31-35": [1501], "41-45": [2410], "36-40": [1954],
#                      "66-70": [1486], "91 over": [23], "26-30": [989],
#                      "21-25": [976], "71-75": [899]},
#       "gender": {"M": [11652], "F": [9691]}
#      }



#colours used in representing 
graph_colours =("#3498db","#51a62d","#1abc9c","#9b59b6","#f1c40f",
         		"#7f8c8d","#34495e","#446cb3","#d24d57","#27ae60",
         		"#663399","#f7ca18","#bdc3c7","#2c3e50","#d35400",
         		"#9b59b6","#ecf0f1","#ecef57","#9a9a00","#8a6b0e")



#####################################################################
#Displaying Main Circle representing gene starting from here
#####################################################################


# list of genes which lable on the main gene pie chart
gene_label = list()

# number of different kind of cells in tissue
gene_values = list()


# Appending information in sample data to tisue_label and gene_values
for tissue, gene_numbers in (data['generation'].items()):

	gene_label.append(tissue)
	gene_values.append(gene_numbers)


# Set window size for displaying the graph
plt.figure(figsize=(10, 8))

# Set window grid for drawing graph
the_grid = GridSpec(10, 10)

# Set main graph to be drown at center of the display
plt.subplot(the_grid[5, 5], aspect=1)


# The parameters of main_gene_chart.pie below-
#.pie(value, lable, colours, wedgeprops, pctdistance, statangle, counterclock, autopct)
plt.pie(gene_values,  


		# lable of pie chart
		labels=gene_label, 

		# colours of each piece in pie chart
		colors=graph_colours, 

		# radius size for pie chart
		radius=10.0,

		# Draw edge of the piece of chart with white colour and widthe 2
		wedgeprops={'linewidth': 2,'edgecolor':"white"}, 

		# Set colour of text to white and bold
		textprops={'color': "white", 'weight': "bold"},

		# Displaying piece counter clockwise 
		counterclock=False,

		# Removing dicimal place of gene values in chart
		autopct=lambda p: '{:.1f}%'.format(p) if p >= 2.5 else '',

		)



###############################################################################

# Displaying Chart for tissues

###############################################################################


# Set main pie chart at center of the window
plt.subplot(the_grid[1, 1], aspect=1)


# The parameters of main_gene_chart.pie below-
#.pie(value, lable, colours, wedgeprops, pctdistance, statangle, counterclock, autopct)
plt.pie(gene_values,  

		# lable of pie chart
		labels=gene_label, 

		# colours of each piece in pie chart
		colors=graph_colours, 

		radius=5.0,

		# Draw edge of the piece of chart with white colour and widthe 2
		wedgeprops={'linewidth': 2,'edgecolor':"white"}, 

		# Set colour of text to white and bold
		textprops={'color': "white", 'weight': "bold"},

		pctdistance=0.85,

		startangle=90,

		# Displaying piece counter clockwise 
		counterclock=False,

		# Removing dicimal place of gene values in chart
		autopct=lambda p: '{:.1f}%'.format(p) if p >= 2.5 else ''
		)



# Display graph
plt.show()


