# pydicom installation; https://pydicom.github.io/pydicom/dev/tutorials/virtualenvs.html

from pydicom.data import get_testdata_file
fpath = get_testdata_file("CT_small.dcm")
import pydicom
from pydicom import dcmread


# print(pydicom.__version__)   2.2.2

ds = dcmread(fpath)
print(ds)

#to force a read from the dcm file if you are getting errors
# ds = dcmread(no_meta, force=True)
