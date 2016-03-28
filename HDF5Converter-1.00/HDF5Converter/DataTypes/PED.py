from DataType import DataType
from tables import StringCol


class PED(DataType):
    def __init__(self, p, collength=16, writing=False, verbose=False):
        """
        Instantiates a PED object corresponding to MAP files.

        See MAP.py for data_format explanation.
        :param p: The full file path.
        """
        self.input = p
        self.data_format = {"family": (0, StringCol(collength)), "sample": (1, StringCol(collength)),
                            "paternal": (2, StringCol(collength)), "maternal": (3, StringCol(collength)),
                            "sex": (4, StringCol(collength)), "affection": (5, StringCol(collength))}
        if not writing:
            self.geno_length = self.get_geno_length()
            self.data_format["genotype"] = (6, StringCol(self.geno_length))
        else:
            self.data_format["genotype"] = (6, StringCol(4))
        DataType.__init__(self, p, "ped", verbose)

    def __str__(self):
        return self.file_name

    def __repr__(self):
        return self.__str__()

    def write(self, table):
        """
        Overrides the write function in DataType. For formats that are not as easily processed (i.e. MAP is simply
        separated by white space) a special function must be written. In this case, the genotype column is manipulated
        prior to writing to the file.

        :param table: HDF5 table that is being read.
        """
        f = []
        for k in self.data_format:
            f.append((k, self.data_format[k][0]))
        a = sorted(f, key=lambda x: x[1])
        with open(self.input, "w") as f:
            for r in table:
                s = ""
                geno = " ".join(r["genotype"])
                for each in a:
                    if not each[0] == "genotype":
                        s += r[each[0]]+"\t"
                    else:
                        s += geno
                s.strip()
                f.write(s+"\n")

    def formatted_line(self, split_line):
        """
        Overrides the formatted_line function in DataType. Similar to write, while reading the PED file, the genotype
        column is manipulated prior to writing to the HDF5 table.

        :param split_line: the line separated into different data points.
        :return: dictionary matching each data point to their respective column.
        """
        line_dict = {}
        for k in self.data_format.keys():
            if k == "genotype":
                x = self.data_format[k][0]
                geno_string = "".join(split_line[x:])
                line_dict[k] = geno_string.strip()
            else:
                data = split_line[self.data_format[k][0]]
                line_dict[k] = data
        return line_dict

    def get_geno_length(self):
        """
        In PED files, the last column is of variable length (from file to file) in order to define the correct size
        while writing the tables, the first row is read to determine the length to use.

        :return: the length of the last column after being formatted correctly.
        """
        with open(self.input) as f:
            line = f.readline().rsplit()
            length_string = "".join(line[6:])
            length_string = length_string.rstrip()
            max_glength = len(length_string)
        return max_glength

