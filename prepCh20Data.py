import os
import pandas as p

# Read file obtained via custom download from ensembl biomart
# Custom download:
# Filters: Chromosome/scaffold: 20
#          With HGNC Symbol ID(s): Only
# Attrib.: Gene stable ID
#          Gene start (bp)
#          Gene end (bp)
#          Strand
#          GOSlim GOA Accession(s)
#          GOSlim GOA Description
#          HGNC symbol


def prepare_gene(raw_data: p.DataFrame, trait_list: list, sym_list: list) -> None:
    """Return all values under """

    for column in raw_data.columns:
        if column == "trait":
            trait_list = raw_data[column].values.tolist()
        elif column == "sym":
            sym_list = raw_data[column].values.tolist()


def countTissues():
    # Get Trait info.
    rawFile = os.path.abspath("Chr20GWAStraits.tsv")
    rawData = p.read_table(rawFile, header=0)

    # Get Expression info on where the genes are expressed(eg. duodenum).
    rawFile2 = os.path.abspath("Chr20GeneData.tsv")
    rawData2 = p.read_table(rawFile2, header=0)


    # Create a list to first keep the values under the column "HPAspecificExpr".
    expression_list = []
    # Create a list to keep the values under the column "trait".
    traits_list = []
    # Create a list to keep the sym names from Chr20GWAStraits.
    sym_list = []
    # Create a list to keep the sym names from Chr20GeneData. Note that this list will not contain any duplicate syms
    # while sym_list does due to the nature of how differently the values are stored in
    # Chr20GeneData and Chr20GWAStraits.
    sym_list2 = []

    # Retrieve all values under "trait" into result1, from Chr20GWAStraits.
    for column in rawData.columns:
        if column == "trait":
            # print(rawData[column])
            traits_list = rawData[column].values.tolist()
            # print(rawData[column].values.tolist())
        elif column == "sym":
            sym_list = rawData[column].values.tolist()

    # Retrieve all values under "HPAspecificExpr" into result2, from Chr20GeneData.
    for column in rawData2.columns:
        if column == "HPAspecificExpr":
            expression_list = rawData2[column].values.tolist()
        elif column == "sym":
            sym_list2 = rawData2[column].values.tolist()


    # Create a dictionary that maps HPAspecificExpr to a list of syms that are expressed at high levels at
    # that HPAspecificExpr.
    expression_to_sym = {}

    # Gets a list of indices of sym that have no trait (ie. '-'). The resuting list will have
    # indices of sym that have no trait while considering the duplicated syms as one sym so that we can calibrate it
    # to the indices in sym_list2. For example, if there is one sym that has many different traits, we just consider
    # this sym as just one instead of multiple of the same sym.
    i = 0
    index_list = []
    tracker = []
    j = 0
    for i in range(len(traits_list)):
        if sym_list[i] not in tracker and sym_list[i] in sym_list2:
            tracker.append(sym_list[i])
            if traits_list[i] == '-':
                index_list.append(j)
            j += 1


    for index in index_list:
        expression = expression_list[index]
        if expression in expression_to_sym:
            expression_to_sym[expression].append(sym_list2[index])
        else:
            expression_to_sym[expression] = [sym_list2[index]]

    print(len(expression_to_sym.keys()))
    #
    # trimmed_sym = []
    # # Map an HPAspecificExpr to all of the gene sym that corresponds to that HPAspecificExpr.
    # for i in range(len(traits_list)):
    #     if traits_list[i] == '-':
    #         trimmed_sym = sym_list[i]  # The gene sym with unidentified trait '-'.
    #         expression = expression_list[i]  # The HPAspecificExpr of that gene sym.
    #         if expression in expression_to_sym:
    #             expression_to_sym[expression].append(sym)
    #         else:
    #             expression_to_sym[expression] = [sym]

    print(expression_to_sym)









    # # Create another list to append all values that are not NaN.
    # result2 = []
    # for value in result1:
    #     # Check to see if value is NaN. NaN != NaN is always true.
    #     if value == value:
    #         result2.append(value)
    # print(result2)
    #
    # For each item in result2, extract the tissue name only.
    result3 = []
    for item in expression_list:
        info = item.split(";")
        for tissue in info:
            result3.append(tissue.split(":")[0])

    result4 = []
    for item in result3:
        info = item.split(",")
        for tissue in info:
            result4.append(tissue)
    print(result4)
    #
    # # Count the number of times
    # # print(result3)



def prepData():
    #load the biomart data
    rawFile = os.path.abspath("mart_export.txt")
    rawData = p.read_table(rawFile, header=0)

    #don't need the gene ID column but we do want a chromosome column. We can mutate this in place.
    rawData["Gene stable ID"] = 20

    #rename columns
    rawData = rawData.rename(columns={
                            "Gene stable ID": "chr",
                            "Gene start (bp)": "start",
                            "Gene end (bp)": "end",
                            "Strand": "strand",
                            "GOSlim GOA Accession(s)": "GOAid",
                            "GOSlim GOA Description": "GOAdescr",
                            "HGNC symbol": "sym"})

    #set sym to be the index and remove the sym col
    rawData = rawData.set_index(rawData.sym)
    rawData = rawData.drop("sym", axis=1)

    #make GOA frequency table
    GOAfreq = rawData.GOAid.value_counts()

    #remove duplicate rows
    rawData = rawData.drop_duplicates()

    #choose the most specific (least frequent) GOA
    for symbol in rawData.index.unique():
        #if there are multiple, select row with most specific GOA
        if p.Series(rawData.loc[symbol].GOAid).count() > 1:
            topGOA = GOAfreq[rawData.loc[symbol].GOAid].idxmin()
            #drop all other rows for that symbol -> keep all those that are not the symbol of interest OR have the topGOA
            rawData = rawData[((rawData.index != symbol) | (rawData.GOAid == topGOA))]

    #sort output by HUGO symbol
    rawData = rawData.sort_index()

    #write to tsv
    rawData.to_csv("chr20_data.tsv", sep="\t")

if __name__ == '__main__':
    # prepData()
    countTissues()
