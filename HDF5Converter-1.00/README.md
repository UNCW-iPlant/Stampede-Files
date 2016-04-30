#HDF5 Converter
###Stampede Setup
#####Modules
To determine which modules are already loaded enter the command `module list`.
The HDF5 Converter requires the hdf5 module which depends on the intel/13.0.2.146 module.

Enter `module load intel/13.0.2.146` followed by `module load hdf5/1.8.9`. 

In order to save this configuration (otherwise you would need to enter this everytime you log into Stampede) enter `module save`
#####Python
PyTables can be installed on Stampede by entering `pip install --user tables`
