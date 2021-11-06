#Sample Universal File Sorter Script


#import ID_library || define relevant variable
#ID_LIBRARY = sample_region_metadata.csv

#function receives the dicom files and label

  #parses the dcm file for the dcm region meta data
  
  #loops through region metadata id types
  
    #given equivalence, grab the matching label and inference file name(inference file names have the pathology type)
    #return the file location of the given inference script || run the inference script from here using the inputted dcm and label
