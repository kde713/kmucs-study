import os, glob


def scanfolder(path):
    for path, dirs, files in os.walk(path):
        for d in dirs:
            for f in glob.iglob(os.path.join(path, d, '*.py')):
                print(f)


scanfolder("/Users/kde713/")
