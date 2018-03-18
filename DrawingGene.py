# Importing libraries to draw gene graph
import matplotlib.pyplot as plt
import Tissue
import Gene
from matplotlib.gridspec import GridSpec
from random import randint

# The colors used to representing pie charts
graph_colours = ("#3498db", "#bdc3c7", "#1abc9c", "#9b59b6", "#f1c40f",
                 "#7f8c8d", "#34495e", "#446cb3", "#d24d57", "#27ae60",
                 "#663399", "#f7ca18", "#3498db", "#2c3e50", "#d35400",
                 "#9b59b6", "#ecf0f1", "#ecef57", "#9a9a00", "#8a6b0e",
                 "#0278AE", "#A40A3C", "#F12B6B", "#BCFFA8", "#D7EEF2",
                 "#EA8F79", "#5628B4", "#4A772F", "#17139C", "#F5E9FF",
                 "#4EF037", "#FD2E2E", "#FBA746", "#A1D9FF", "#FEFF89",
                 "#7A9EB1", "#FFE1B6", "#FFBDD4", "#BC5148")

#####################################################################
# Displaying Main Circle representing gene starting from here
#####################################################################

def return_trait_ratio(index):
    num_trait_genes = 0
    num_untrait_genes = 0

    tissue = all_tissue_list[index]

    for gene in tissue.genes:
        if gene.has_trait:
            num_trait_genes += 1
        else:
            num_untrait_genes += 1

    return num_trait_genes / (num_untrait_genes+num_trait_genes)


def organize_gene_info(all_tissue_list):
    all_tissue_list[0].gene_num = 90

    temp_tissue = all_tissue_list[0]

    all_tissue_list[0] = all_tissue_list[1]

    all_tissue_list[1] = temp_tissue

all_tissue_list = Gene.return_tissue_info()
organize_gene_info(all_tissue_list)


# list of genes which lable on the main gene pie chart
gene_label = list()

# number of different kind of cells in tissue
gene_values = list()


# Appending gean number information of each tissue
for i in range(len(all_tissue_list)):
    gene_values.append(all_tissue_list[i].gene_num)


# Set window size for displaying the graph
plt.figure(figsize=(12, 7))

# Set window grid for drawing graph
the_grid = GridSpec(12, 12)



# Set main graph to be drown at center of the display
plt.subplot(the_grid[5, 5], aspect=1)

# The parameters of main_gene_chart.pie below-
# .pie(value, lable, colours, wedgeprops, pctdistance, statangle, counterclock, autopct)

plt.pie(gene_values,

        # lable of pie chart
        labels=None,

        # colours of each piece in pie chart
        colors=graph_colours,

        # radius size for pie chart
        radius=11.0,

        # Draw edge of the piece of chart with white colour and widthe 2
        wedgeprops={'linewidth': 2, 'edgecolor': "white"},

        # Set colour of text to white and bold
        textprops={'color': "white", 'weight': "light"},

        # Displaying piece counter clockwise
        counterclock=False,

        # Removing the lable from the window
        pctdistance=(-3.0),

        # Change the angle of the graph by 90 degree
        startangle=15,

        )


plt.text(-3.55, -0.48, "Chromosome20")
plt.text(18.1, 16.68, "Heart")
plt.text(25, -12, "Testis")
plt.text(-24, -17, "Epididymis")
plt.text(-26, 11, "Skin")
plt.text(-22, 18, "Celebral Cortex")

plt.pie(gene_values,

        # lable of pie chart
        labels=None,

        # colours of each piece in pie chart
        colors=["#FFFFFF"],

        # radius size for pie chart
        radius=9.25,

        # Draw edge of the piece of chart with white colour and widthe 2
        wedgeprops={'linewidth': 10, 'edgecolor': "white"},

        # Set colour of text to white and bold
        textprops={'color': "black", 'weight': "light"},

        # Displaying piece counter clockwise
        counterclock=False,

        # Removing the lable from the window
        pctdistance=(100.0)

        )



def draw_chart(colours, index, chart_radius):

    gean_values = []

    for i in all_tissue_list[index].genes:
        gean_values.append(i.length)

    gean_colours = colours

    plt.pie(gean_values,

            # lable of pie chart
            labels=None,

            # colours of each piece in pie chart
            colors=gean_colours,

            # radius size for pie chart
            radius=chart_radius,

            # Draw edge of the piece of chart with white colour and widthe 2
            wedgeprops={'linewidth': 1, 'edgecolor': "white"},

            # Set colour of text to white and bold
            textprops={'color': "white", 'weight': "light"},

            # Displaying piece counter clockwise
            counterclock=False,

            # Removing the lable from the window
            pctdistance=(-30.0),

            # Removing dicimal place of gene values in chart
            autopct=lambda p: '{:.1f}%'.format(p) if p >= 2.5 else '',

            )


def draw_inner_chart(colours, index, chart_radius):
    ratio = return_trait_ratio(index)

    ratio_values = [ratio, 1-ratio]

    gean_colours = [colours, "#FFFFFF"]

    plt.pie(ratio_values,

            # lable of pie chart
            labels=None,

            # colours of each piece in pie chart
            colors=gean_colours,

            # radius size for pie chart
            radius=chart_radius,

            # Draw edge of the piece of chart with white colour and widthe 2
            wedgeprops={'linewidth': 2, 'edgecolor': "white"},

            # Set colour of text to white and bold
            textprops={'color': "white", 'weight': "light"},

            # Displaying piece counter clockwise
            counterclock=False,

            # Removing the lable from the window
            pctdistance=(-30.0),

            # Change the angle of the graph by 90 degree
            startangle=90,

            # Removing dicimal place of gene values in chart
            autopct=lambda p: '{:.1f}%'.format(p) if p >= 2.5 else '',

            )

def draw_white_circle(chart_radius):
    pass
    # plt.pie([1],

    #     # lable of pie chart
    #     labels=None,

    #     # colours of each piece in pie chart
    #     colors=["#FFFFFF"],

    #     # radius size for pie chart
    #     radius=chart_radius,

    #     # Draw edge of the piece of chart with white colour and widthe 2
    #     wedgeprops={'linewidth': 10, 'edgecolor': "white"},

    #     # Set colour of text to white and bold
    #     textprops={'color': "black", 'weight': "light"},

    #     # Displaying piece counter clockwise
    #     counterclock=False,

    #     # Removing the lable from the window
    #     #pctdistance=(100.0)

        # )



"""
Drawing pie chart for Heart
"""

# Set the postion of the heart chart
plt.subplot(the_grid[0, 8], aspect=1)

# The clours used to represent genes in Heart
heart_colours=("#0278AE", "#A40A3C", "#F12B6B", "#BCFFA8")

# Draw outer circle of heart pie chart
draw_chart(heart_colours, 25, 2.2)

# Draw inner circle of heaer chart
draw_inner_chart("#D7EEF2", 25, 1.7)

# Draw the white circle to make chart donut
draw_white_circle(0.9)


"""
Drawing pie chart for Testis
"""

# Set the postion of the Testis chart
plt.subplot(the_grid[7, 9], aspect=1)


# The clours used to represent genes in Heart
testis_colours = ("#3498db", "#bdc3c7", "#1abc9c", "#9b59b6", "#f1c40f",
                 "#7f8c8d", "#34495e", "#446cb3", "#d24d57", "#27ae60",
                 "#663399", "#f7ca18", "#3498db", "#2c3e50", "#d35400",
                 "#9b59b6", "#ecf0f1", "#ecef57", "#9a9a00", "#8a6b0e",
                 "#0278AE", "#A40A3C", "#F12B6B", "#BCFFA8", "#D7EEF2",
                 "#EA8F79", "#5628B4", "#4A772F", "#17139C", "#F5E9FF",
                 "#4EF037", "#FD2E2E", "#FBA746", "#A1D9FF", "#FEFF89",
                 "#7A9EB1", "#FFE1B6", "#FFBDD4", "#BC5148", "#3498db",
                 "#7f8c8d", "#34495e", "#446cb3", "#d24d57", "#27ae60",
                 "#663399", "#f7ca18", "#3498db", "#2c3e50", "#d35400",
                 "#9b59b6", "#ecf0f1", "#ecef57", "#9a9a00"
                 )


# Draw outer circle of Testis pie chart
draw_chart(testis_colours, 0, 5.5)


# Draw inner circle of Testis chart
draw_inner_chart("#3498db", 0, 4.87)


# Draw the white circle to make chart donut
draw_white_circle(4.0)




# Drawing outer, inner, white circle is continued until all charts are drawn


"""
Drawing pie chart for Epi

Drawing outer, inner, white circle is continued until all charts are drawn
"""

# Set main pie chart at center of the window
plt.subplot(the_grid[9, 2], aspect=1)


Epi_colours = ("#3498db", "#bdc3c7", "#1abc9c", "#9b59b6", "#f1c40f",
                "#7f8c8d", "#34495e", "#446cb3", "#d24d57", "#27ae60",
                "#663399", "#f7ca18", "#3498db", "#2c3e50", "#d35400",
                "#9b59b6", "#ecf0f1", "#ecef57", "#9a9a00", "#8a6b0e",
                "#0278AE", "#A40A3C", "#F12B6B", "#BCFFA8", "#D7EEF2",
                "#EA8F79")


draw_chart(Epi_colours, 3, 4.5)


draw_inner_chart("#9b59b6", 3, 4.0)


draw_white_circle(3.0)

"""
Drawing pie chart for Skin
"""

plt.subplot(the_grid[2, 1], aspect=1)
#plt.subplot(the_grid[5, 0], aspect=1)

skin_colours =  ("#3498db", "#bdc3c7", "#1abc9c", "#9b59b6", "#f1c40f",
                "#7f8c8d", "#34495e", "#446cb3", "#d24d57", "#27ae60")


draw_chart(skin_colours, 12, 3)


draw_inner_chart("#f7ca18", 12, 2.4)


draw_white_circle(0.5)

"""
Drawing pie chart for Cerebral Cortex
"""

plt.subplot(the_grid[0, 3], aspect=1)


cortex_colours = ("#3498db", "#bdc3c7", "#1abc9c", "#9b59b6", "#f1c40f",
                 "#7f8c8d", "#34495e", "#446cb3", "#d24d57", "#27ae60",
                 "#663399", "#f7ca18", "#3498db", "#2c3e50", "#d35400",
                 "#9b59b6", "#ecf0f1", "#ecef57", "#9a9a00", "#8a6b0e",
                 "#0278AE", "#A40A3C", "#F12B6B", "#BCFFA8", "#D7EEF2",
                 "#EA8F79", "#5628B4", "#4A772F", "#17139C", "#F5E9FF",
                 "#4EF037", "#FD2E2E", "#FBA746", "#A1D9FF", "#FEFF89",
                 "#7A9EB1", "#FFE1B6", "#FFBDD4", "#BC5148", "#3498db",
                 "#7f8c8d", "#34495e")


draw_chart(cortex_colours, 14, 5)

draw_inner_chart("#d35400", 14, 4.38)

# Finished drawing all charts in image

# Display the Graph
plt.show()
