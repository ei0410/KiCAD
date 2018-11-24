import os
import sys
import shutil
import zipfile

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc != 2):
        print("error!")
        print("usage: python pcb.py TARGETDIR")
        sys.exit(1)

    data_path = './' + argv[1]
    save_path = './' + argv[1] + '/' + argv[1]
    
    if os.path.exists(save_path):
        sys.exit(1)
    else:
        os.mkdir(save_path)

    files = os.listdir(argv[1])

    for element in files:
        if element[-3:] == 'gtl':
            shutil.copy(data_path + "/" + element, save_path)
            os.rename(save_path + "/" + element, save_path + "/" + argv[1] + ".GTL")
        if element[-3:] == 'gbl':
            shutil.copy(data_path + "/" + element, save_path)
            os.rename(save_path + "/" + element, save_path + "/" + argv[1] + ".GBL")
        if element[-3:] == 'gto':
            shutil.copy(data_path + "/" + element, save_path)
            os.rename(save_path + "/" + element, save_path + "/" + argv[1] + ".GTO")
        if element[-3:] == 'gbo':
            shutil.copy(data_path + "/" + element, save_path)
            os.rename(save_path + "/" + element, save_path + "/" + argv[1] + ".GBO")
        if element[-3:] == 'gts':
            shutil.copy(data_path + "/" + element, save_path)
            os.rename(save_path + "/" + element, save_path + "/" + argv[1] + ".GTS")
        if element[-3:] == 'gbs':
            shutil.copy(data_path + "/" + element, save_path)
            os.rename(save_path + "/" + element, save_path + "/" + argv[1] + ".GBS")
        if element[-3:] == 'gm1':
            shutil.copy(data_path + "/" + element, save_path)
            os.rename(save_path + "/" + element, save_path + "/" + argv[1] + ".GML")
        if element[-3:] == 'drl':
            shutil.copy(data_path + "/" + element, save_path)
            os.rename(save_path + "/" + element, save_path + "/" + argv[1] + ".TXT")

    shutil.make_archive(save_path, "zip", save_path)

if __name__ == "__main__":
    main()
