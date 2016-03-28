"""
The main converter program. Handles the command-line arguments and starts the needed conversion depending on them.
"""
import argparse


def initialize_graphics():
    """ Prints introduction graphics """
    print "\n###################################################################"
    print "###                                                            ####"
    print "###                      HDF5 Converter                        ####"
    print "###                                                            ####"
    print "###################################################################"


def usage():
    """ Prints all possible command-line arguments """
    print "\n\n\n"
    print "Command-line usage menu"
    print "--help / -h to see the help menu"
    print "--verbose / -v for verbose mode"
    print "to/from to select mode"
    print "Convert to HDF5 Arguments"
    print "\t--dir / -d to specify the input directory containing the files to convert"
    print "\t--output / -o to specify the name of the output HDF5 file"
    print "Convert from HDF5 Arguments"
    print "\t--hdf / -i to specify the HDF5 file to convert back to the original files"
    print "\t--dir / -d to specify the directory to save the output files to"


def check_args():
    """
    Handles arguments for the conversion

    Creates the argument parser and adds subparsers for to HDF5 and from HDF5 with the needed arguments.
    Parses the given arguments as a dictionary, prints if selected, and returns the dictionary of arguments.
    :return: dictionary of arguments
    """
    parser = argparse.ArgumentParser(description="HDF5 Converter Command Line Interface")
    parser.add_argument("-v", "--verbose", help="Trigger verbose mode", action="store_true", default=False)
    subparsers = parser.add_subparsers(help="Program mode (i.e. to HDF5 or from HDF5", dest="mode")
    add_convert_to_hdf(subparsers)
    add_convert_from_hdf(subparsers)
    args = vars(parser.parse_args())
    if args["verbose"]:
        print_arguments(args)
    return args


def print_arguments(args_dict):
    """
    Prints out the arguments that were passed at run time. This function should only be called after checking for
    the verbose option.

    :param args_dict: the arguments in dictionary form
    """
    print "\nVerbose Mode"
    print "Mode is specified as: Convert", args_dict["mode"], "HDF5"
    if args_dict["mode"] == "to":
        print "The input directory is specified as", args_dict["dir"]
        print "The output file name is specified as", args_dict["output"]+".h5"
        print "Column length is set to", args_dict["collength"]
    elif args_dict["mode"] == "from":
        print "The input HDF5 is specified as", args_dict["hdf"]
        print "The output directory is specified as", args_dict["dir"]


def add_convert_to_hdf(sp):
    """
    Adds the arguments pertaining to converting to HDF5.

    :param sp: the main argument parsers group of subparses
    """
    to_parser = sp.add_parser("to", help="Convert files to a single HDF5 file")
    to_parser.add_argument("-d", "--dir", type=str, required=True,
                           help="Directory containing files to convert to HDF5")
    to_parser.add_argument("-c", "--collength", type=int, required=False, default=16,
                           help="How many characters per column. The length of the longest column excluding the last"
                                "column of the PED file. Default is set to 16 characters")
    to_parser.add_argument("-o", "--output", type=str, required=True, help="HDF5 output file prefix")


def add_convert_from_hdf(sp):
    """
    Adds the arguments pertaining to converting a HDF5 file back to the original set of files.

    :param sp: the main argument parsers group of subparses
    """
    from_parser = sp.add_parser("from", help="Convert from HDF5 file")
    from_parser.add_argument("-i", "--hdf", type=str, required=True, help="HDF5 File to convert to multiple files")
    from_parser.add_argument("-d", "--dir", type=str, required=True, help="Directory to save output files to")

