import wfdb

def main():
    data_dir = 'data/raw/'
    wfdb.dl_database('gaitndd', data_dir)

if __name__ == "__main__":
    main()