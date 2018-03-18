import Tissue
import pandas as p
import os

class Gene:
    """Keeps track of the name, whether or not this gene has a trait, and the tissue_location.

    === Public Attributes ===
    name:
        The gene symbol of this gene (eg. AAR2)
    has_trait:
        Whether or not this gene's trait has been identified in Genome-wide Association Study results.
    tissue_location:
        The tissue in which this gene is highly expressed.
    length:
        The length of this gene in nucleotides (from start to end).
    """
    name: str
    has_trait: bool
    tissue_location: Tissue
    length: int

    def __init__(self, name: str, has_trait: bool, tissue_location: Tissue, length: int) -> None:
        """Initialize a new Gene object. name is the gene symbol, trait is a boolean representing whether or not
        this gene has a trait (derived from GWAS data), and tissue_location is where this gene is highly expressed."""

        self.name = name
        self.has_trait = has_trait
        self.tissue_location = tissue_location
        self.length = length


def prepare_data_list(data: p.DataFrame, column: str) -> list:
    """Prepare a list of data values obtained under the column <column> from data.
    """

    return data[column].values.tolist()


def get_lengths_list(start_list: list, end_list: list) -> list:
    """Return a list of the length of each gene by utilizing the lists containing start and end positions."""

    result = []
    for i in range(len(start_list)):
        result.append(int(end_list[i]) - int(start_list[i]))

    return result


def gene_exists(gene_name: str, gene_list: list) -> bool:
    """Return whether or not gene_list has a Gene with the same name as gene_name.
    """

    for _gene in gene_list:
        if gene_name == _gene.name:
            return True
    return False


def search_tissue(tissue_name: str, tissue_list: list) -> Tissue:
    """Return the Tissue from tissue_list that has the same name as tissue_name. If it does not exist, return None.
    """

    for _tissue in tissue_list:
        if tissue_name == _tissue.name:
            return _tissue
    return None


def process_tissue_names(tissues: str) -> list:
    """Return a list containing stripped organ names from organs. Argument organs may have unnecessary float values
    or multiple organ names concatenated together.
    """

    # Split and store the individual organ names separately into a list to return.
    # Splitting is done according to how the Chr20GeneData.tsv data is organized.
    first_separation = tissues.split(";")
    tissue_names = []

    for data in first_separation:
        # data.split(":")[0] is where the name of tissues reside. However, there may be one or multiple, so it has to
        # be further split in the next for loop.

        name = data.split(":")[0]
        tissue_names.append(name)

    # result will keep track of the individual tissue names stored in each cell under the HPAspecificExpr column of
    # Chr20GeneData.tsv
    result = []

    # Further split the names inside tissue_names into individual names if it has to be.
    for names in tissue_names:
        individual_names = names.split(",")
        for name in individual_names:
            result.append(name.strip())
    return result


def add_tissue(tissue_name: str, tissue_list: list, gene: Gene) -> None:
    """If a Tissue called <tissue_name> already exists in <tissue_list>, insert gene into Tissue.genes. Otherwise,
    create a new Tissue called <tissue_name> and with <gene> inside Tissue.genes, and append it to <tissue_list>.
    """

    for individual_organ in process_tissue_names(tissue_name):
        if tissue_exists(individual_organ, tissue_list):
            tissue = search_tissue(individual_organ, tissue_list)
            tissue.add_gene(gene)
        else:
            tissue_list.append(Tissue.Tissue(individual_organ, [gene]))


def tissue_exists(tissue_name: str, tissue_list: list) -> bool:
    """Return whether or not a Tissue called <tissue_name> exists in tissue_list.
    """

    for tissue in tissue_list:
        if tissue.name == tissue_name:
            return True
    return False


def prepare_tissues(traits: list, syms_duplicate: list, syms: list, tissues: list, lengths: list) -> list:
    """Return the list containing all Tissues created using Chr20GeneData.tsv, without any duplicates. traits is a list
    containing all the traits of a Gene, corresponding to the gene symbols at the same index in syms.
    syms_duplicate contains the same gene symbols as in syms but are duplicated due to the possibility of multiple
    traits present for a single gene from GWAS. tissues is a list of all the tissue names corresponding to the gene
    symbol at the parallel index in syms. lengths contains all of the nucleotide lengths of the gene.
    """

    i = 0

    # We will iterate over every Gene in gene_list to create Tissue objects using those.
    gene_list = []

    # j tracks the index of each Gene, ignoring
    # duplicates. This enables to calibrate the indices so that we ignore duplicate gene symbols.
    j = 0
    for i in range(len(traits)):
        gene_name = syms_duplicate[i]

        # We only want to create Gene objects if that Gene is not yet in gene_list and if the gene symbols from
        # sym_duplicate also appears in syms.
        if not gene_exists(gene_name, gene_list) and gene_name in syms:
            tissue_name = tissues[j]
            gene_length = lengths[j]

            # ie. if there are no traits identified yet.
            if traits[i] == '-':

                # This condition checks for NaN values. The first condition is satisfied if tissue_name is not NaN.
                if tissue_name == tissue_name:
                    gene = Gene(gene_name, False, tissue_name, gene_length)
                else:
                    gene = Gene(gene_name, False, "unidentified", gene_length)
            else:
                if tissue_name == tissue_name:
                    gene = Gene(gene_name, True, tissue_name, gene_length)
                else:
                    gene = Gene(gene_name, True, "unidentified", gene_length)
            gene_list.append(gene)
            j += 1

    tissue_list = []
    for gene in gene_list:
        add_tissue(gene.tissue_location, tissue_list, gene)
    return tissue_list


def return_tissue_info():
    # Reads from the file Chr20GWAStraits.tsv.
    raw_file = os.path.abspath("Chr20GWAStraits.tsv")
    raw_data = p.read_table(raw_file, header=0)

    # Reads from the file Chr20GeneData.tsv
    raw_file2 = os.path.abspath("Chr20GeneData.tsv")
    raw_data2 = p.read_table(raw_file2, header=0)

    # List of all the tissues, prepared from the column "HPAspecificExp".
    expression_list = prepare_data_list(raw_data2, "HPAspecificExpr")

    # List of all the start and end positions of the gene sequence.
    start_list = prepare_data_list(raw_data2, "start")
    end_list = prepare_data_list(raw_data2, "end")

    # List of all the lengths of the gene.
    lengths_list = get_lengths_list(start_list, end_list)

    # Create a list to keep the values under the column "trait".
    traits_list = prepare_data_list(raw_data, "trait")

    # Create a list to keep the sym names from Chr20GWAStraits.
    sym_list = prepare_data_list(raw_data, "sym")

    # Create a list to keep the sym names from Chr20GeneData. Note that this list will not contain any duplicate syms
    # while sym_list does due to the nature of how differently the values are stored in
    # Chr20GeneData and Chr20GWAStraits.
    sym_list2 = prepare_data_list(raw_data2, "sym")

    all_tissues = prepare_tissues(traits_list, sym_list, sym_list2, expression_list, lengths_list)

    return all_tissues
