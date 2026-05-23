import csv

txt_file = "comp_enc_41.txt"
csv_file = "comp_enc_41_merged.csv"




# Change delimiter if needed (e.g., '\t' for tab, '|' for pipe)
delimiter = ","  

with open(txt_file, "r", encoding="utf-8") as infile, open(csv_file, "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile, delimiter=delimiter)
    writer = csv.writer(outfile)
    
    for row in reader:
        writer.writerow(row)

print(f"Converted {txt_file} to {csv_file}")