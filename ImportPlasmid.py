from Bio import SeqIO
mito_record = SeqIO.read(open("NC_006581.gbk"), "genbank")
print mito_record.format("fasta")