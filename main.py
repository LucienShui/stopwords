import glob


if __name__ == "__main__":
    stopwords = set()

    # 将 source 目录下的 txt 取并集，写至 stopwords.txt 中
    for file_name in glob.glob("source/*.txt"):
        if file_name != "stopwords.txt":
            for line in open(file_name):
                stopwords.add(line)
    
    with open("stopwords.txt", "w") as file:
        file.write("".join(stopwords))
