from os import listdir
from DataTypes.MAP import MAP
from DataTypes.PED import PED
from DataTypes.HDF5 import HDF5
from tables import open_file
from commandline import initialize_graphics, check_args


class Convert:
    def __init__(self, args):
        """
        Creates a new instance of a Convert object using the runtime arguments.

        :param args: dictionary of arguments
        """
        self.args = args

    def start_converting(self):
        """
        Starts the appropriate conversion function depending on the mode passed through the arguments.

        """
        if self.args["verbose"]:
            print "Starting conversion process"
        if self.args["mode"] == "to":
            self.convert_to()
        elif self.args["mode"] == "from":
            self.convert_from()
        if self.args["verbose"]:
            print "Conversion process complete"

    def convert_to(self):
        """
        Function for converting to HDF5.

        Creates new DataType objects based on file extensions. Creates a new HDF5 file. Creates tables within the
        HDF5 based on the DataType objects.
        """
        input_directory = self.args["dir"]
        output_name = self.args["output"]
        verbose = self.args["verbose"]
        collength = self.args["collength"]
        files = listdir(input_directory)
        dtypes = {}
        for f in files:
            if f.lower().endswith(".map"):
                if "map" not in dtypes:
                    dtypes["map"] = []
                    dtypes["map"].append(MAP(input_directory+f, collength=collength, verbose=verbose))
                else:
                    dtypes["map"].append(MAP(input_directory+f,collength=collength, verbose=verbose))
            elif f.lower().endswith(".ped"):
                if "ped" not in dtypes:
                    dtypes["ped"] = []
                    dtypes["ped"].append(PED(input_directory+f, collength=collength, verbose=verbose))
                else:
                    dtypes["ped"].append(PED(input_directory+f, collength=collength, verbose=verbose))
        h5_file = open_file(output_name+".h5", mode="w", title=output_name)
        for key in dtypes:
            for a in dtypes[key]:
                a.create_table(h5_file)
        print "Closing H5 file:", output_name
        h5_file.close()

    def convert_from(self):
        """
        Function for converting from HDF5 to multiple files.

        """
        input_file = self.args["hdf"]
        output_directory = self.args["dir"]
        verbose = self.args["verbose"]
        h = HDF5(input_file, verbose)
        h.convert(output_directory)


def initialize():
    """
    Displays graphics from commandline.py and loads the runtime arguments to be used while instantiating a
    Convert object.

    """
    initialize_graphics()
    return check_args()


def main():
    """
    Sets the argument dictionary - the runtime parameters - from the initialize function, creates a new Convert
    object using that dictionary, and starts the conversion process.


    """
    arguments = initialize()
    conversion = Convert(arguments)
    conversion.start_converting()


if __name__ == "__main__":
    main()
