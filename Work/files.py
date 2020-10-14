# with open("Data/portfolio.csv", "rt") as f:
#     for line in f:
#         print(line, end="")

import gzip
with gzip.open("Data/portfolio.csv.gz", "rt") as f:
    for line in f:
        print(line, end="")
