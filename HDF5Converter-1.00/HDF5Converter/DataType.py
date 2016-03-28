from os import path


class DataType:
    def __init__(self, file_path, t, verbose=False):
        """
        Creates a new instance of DataType.

        :param file_path: Full path to a specific file
        :param t: Type of file (i.e. MAP / PED)
        """
        self.input = file_path
        head, tail = path.split(self.input)
        self.file_name = tail
        self.file_prefix = path.splitext(self.file_name)[0]
        self.type = t
        self.verbose = verbose

    def read(self):
        """
        Generator to open file and yield each line after it is formatted.

        :return: Each line formatted into a dictionary
        """
        if self.verbose:
            print "Reading", self.file_name
        with open(self.input) as f:
            for line in f:
                line = line.rstrip().split()
                yield self.formatted_line(line)

    def write(self, table):
        """
        Writes to a file from a HDF5 table using the data_format found in the child classes.

        :param table: The table containing the data
        """
        if self.verbose:
            print "Writing", self.input
        f = []
        for k in self.data_format:
            f.append((k, self.data_format[k][0]))
        a = sorted(f, key=lambda x: x[1])
        with open(self.input, "w") as f:
            for r in table:
                s = ""
                for each in a:
                    s += r[each[0]]+"\t"
                s.strip()
                f.write(s+"\n")

    def formatted_line(self, split_line):
        """
        Returns a dictionary using a list of the line elements and matching them to their columns depending on
        the given data format.

        :param split_line: the line separated into different data points.
        :return: dictionary matching each data point to their respective column.
        """
        line_dict = {}
        for k in self.data_format.keys():
            data = split_line[self.data_format[k][0]]
            line_dict[k] = data
        return line_dict

    def create_table(self, h5_file):
        """
        Creates and populates a HDF5 table based on the file type. Writes to this table using the given data format.

        :param h5_file: file to add the table to
        """
        if self.verbose:
            print "Creating and populating", self.file_prefix, self.type, "table"
        group_exists = False
        for x in h5_file:
            if x._v_name == self.file_prefix:
                group_exists = True
                group = x
        if not group_exists:
            group = h5_file.create_group("/", self.file_prefix, self.file_prefix)
        table_def = {}
        for k in self.data_format:
            table_def[k] = self.data_format[k][1]
        table = h5_file.create_table(group, self.type, table_def)
        individual = table.row
        for x in self.read():
            for y in x:
                individual[y] = x[y]
            individual.append()
        table.flush()
