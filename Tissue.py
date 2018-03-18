import Gene


class Tissue:
    """Keeps track of the name and the genes that are highly expressed in this Tissue."""

    def __init__(self, name: str, genes: list) -> None:
        """Initialize a new Tissue object."""
        if name != name:
            self.name = "unidentified"
        else:
            self.name = name
        self.genes = genes

        self.gene_num = 0



    def add_gene(self, gene: Gene) -> None:
        """Add a new Gene to the existing list of Genes."""
        self.genes.append(gene)
        self.gene_num += 1

    