import pandas as pd
import os
import sys


def csvcombiner(self, argv: list):

        chunk_list = []

        if self.validate_file_paths(argv):
            filelist = argv[1:]

            for file_path in filelist:

                for chunk in pd.read_csv(file_path, chunksize=100000):
                    
                    filename = os.path.basename(file_path) #retieving file name 

                    chunk['filename'] = filename
                    chunk_list.append(chunk)

            header = True

            for chunk in chunk_list:
                print(chunk.to_csv(index=False, header=header, line_terminator='\n', chunksize=chunksize), end='')
                header = False
        else:
            return


csvcombiner(sys.argv)


