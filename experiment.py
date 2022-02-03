from pydicom.fileset import FileSet
from pydicom import dcmread
from pydicom.data import get_testdata_file

# relevant install:
# pip install pydicom
# documentation:
# https://pydicom.github.io/

# This reads and shows some sample data that gets auto-installed with pydicom
path = get_testdata_file("DICOMDIR")
ds = dcmread(path)
fs = FileSet(ds)  # or FileSet(path)
print(path)
print(fs)

# replace this with the dir your file is located.
# I haven't figured out how to dynamically do this, yet,
# but strings seem to work fine.
simple_path="/mnt/c/dev/daikon/SIMPLE_FILE.dcm"
print(simple_path)
simple_ds=dcmread(simple_path)
print(simple_ds)