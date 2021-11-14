Archicture for machine learning section:


ipfs cid -> universal sorting script[csv reference] -> inference script [modulated preprocessing] -> return flagged or passing,
                                                                                                    to what % confidence[future; add other 
                                                                                                     posible prognosis' depending on CI threshod]

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[currently only using glioma and control; neglect universal]

Weekend Content(11/5-7) and onwards:


>double checking voxel; do radiologists get more than one segmentation per patient? yes, continue with the following todo:

>hand labeling 20:20 control:MGMT(substituted tumor dcm) from RSNA competition [save locally]

>test upload and download of IPFS dcm file [access using local script; if it doesn't work under 30 minutes of troubleshooting->move on]

>create a csv file containing the dcm id of given region and imaging types (will be used as pseudo database for sorting script)

>universal sort script outline; takes dcm, reads the id, checks the csv for the given id, respective type and points at the appropriate inference scipt(i.e. tumor) and carries the label from radiologist (working under the assumption that they get a dropdown of possible inference script pathologies)

>training script that takes the ipfs dicom(can use local for testing), converts to image and normalizes(if more than one segmentation; find the average image and use that for now, use placehold axial check, creates cross validation test and train splits, and trains with a straightforward cnn(binary clf), and saves the 
corresponding model(bags).

>inference script[title is pathology]; accepts the radiologist label and the dcm file itslef; uses the modulated preprocessing script, evaluates the processed dcm average image and 
  compares with the label, returns CI for agreement or disagreement, returns for yonathan to grab somehow(needs connecting to main)
  
  
  note: all scripts for clf follow this model and compare the control to the given label
  
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  vocab; pathologies = labels
  
  future plans; CID timed retraining sessions, 
                if confusion matrix is doesnt agree with label to given degree, run on other inference scripts to form a different prognosis,
                add voxel based models that might provide better accuracy,
                trade out cnn with a gnn,
                add axial filter (use only axial that we have trained for, make more to cover every possibility)
