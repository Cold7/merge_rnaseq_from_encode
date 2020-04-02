from glob import glob


if __name__ == "__main__":

    geneDict = {}
    geneF = open("gene_coords.tsv","r")
    for line in geneF:
        gene = line[:-1].split("\t")
        geneDict[gene[0]] = {"chr":gene[1],"init":gene[2],"end":gene[3], "strand":gene[4]}

    folders = glob("*/")
    for folder in folders:
        files = glob(folder+"/RNA-seq/*/*.tsv")
        avgRNA = {}
        for file in files:
            f = open(file,"r")
            count = 0
            for line in f:
                if count != 0:
                    data = line.split("\t")
                    id = data[0]
                    rnaCount = float(data[5])
                    if id not in avgRNA:
                        avgRNA[id] =[rnaCount]
                    else:
                        avgRNA[id].append(rnaCount)
                else:
                    count = 1
        finalF = open(folder+"RNA-seq/rnaseq.tsv","w")
        for rna in avgRNA:
            if rna in geneDict:
                score =str( sum(avgRNA[rna])/ len(avgRNA))
                finalF.write(geneDict[rna]["chr"]+"\t"+geneDict[rna]["init"]+"\t"+geneDict[rna]["end"]+"\t"+geneDict[rna]["strand"]+"\t"+score)
        finalF.close()
