from DataType import DataType
from tables import StringCol


class MAP(DataType):
    def __init__(self, p, collength=16, verbose=False):
        """
        Instantiates a MAP object corresponding to MAP files.

        The data_format is how the file is set up for use with reading and writing HDF5 tables. The dictionary
        key represents the name of the column, the first part of the value tuple represents where it is located
        when the line is split and the second part represents the datatype to use within the table.
        :param p: The full file path
        """
        self.data_format = {"chromosome": (0, StringCol(collength)), "identifier": (1, StringCol(collength)),
                            "distance": (2, StringCol(collength)), "position": (3, StringCol(collength))}
        DataType.__init__(self, p, "map", verbose)

    def __str__(self):
        return self.file_name

    def __repr__(self):
        return self.__str__()
