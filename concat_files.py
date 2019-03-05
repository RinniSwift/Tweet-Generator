

def concatenate_files():
    
    # insert file names
    file_names = ['AnnaKerenina.txt', 'AdamBede.txt']

    with open('corpus.txt', 'w') as outfile:
        for filee in file_names:
            with open(filee) as infile:
                for line in infile:
                    outfile.write(line)


if __name__ == '__main__':
    concatenate_file = concatenate_files()