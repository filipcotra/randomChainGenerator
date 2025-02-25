# Purpose: To print a given data frame to a file.
# Parameters:
#   df = The data frame to print.
#   fileName = The name of the file.
def printDf(df, fileName):
    outputFile = open(f"/Users/filipcotra/Desktop/contactExtraction/blobSim/{fileName}.tsv", "w");
    outputFile.write(df.to_csv(sep='\t', header=True));
    outputFile.close();