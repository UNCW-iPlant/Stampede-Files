from tables import open_file
from MAP import MAP
from PED import PED
from os import path, mkdir


class HDF5:
    def __init__(self, name, verbose=False):
        """
        Instantiates HDF5 object with a given file name. Then opens this file for reading.

        :param name: The full path of the .h5 file
        """
        self.verbose = verbose
        if self.verbose:
            print "Opening HDF5 file", name
        self.h5_file = open_file(name, mode="r")

    def convert(self, directory):
        """
        Starts the conversion process from HDF5 back to the original file types.

        :param directory: full path of the directory to save converted files to.
        """
        if not path.exists(directory):
            if self.verbose:
                print "Output directory does not exist"
                print "Creating output directory", directory
            mkdir(directory)
        if self.verbose:
            print "Writing tables to files"
        for x in self.h5_file.root:
            prefix = x._v_name
            for y in x:
                x = directory+prefix+"."+y._v_name
                if x.lower().endswith(".map"):
                    if self.verbose:
                        print "Writing", x
                    m = MAP(x)
                    m.write(y)
                elif x.lower().endswith(".ped"):
                    if self.verbose:
                        print "Writing", x
                    m = PED(x, writing=True)
                    m.write(y)
        if self.verbose:
            print "Closing HDF5 file"
        self.h5_file.close()
