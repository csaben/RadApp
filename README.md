# RadApp
Code base for front end, backend, and rest of related docs

<!-- .slide -->

## Goal

Provide Radiologists with a tool to double check the pathology labels they make.

### Sub-Goals

- De-identify patient data and store on the Oasis blockchain with labels
- Provide public access to this ever growing database
- Create re-training loop based on new database entries 

<!-- .slide vertical=true -->

<!-- .slide -->

## Achieved Results

<!-- .slide vertical=true -->
- Docker image that takes patient MR data and returns a prediction 
- Initial [database](https://www.kaggle.com/clarksaben/glioma-axial-test-radapp) for MR data (Cancer Imaging Archive and Kaggle 2021 RSNA competition)
- Initial ML training pipeline 

<!-- .slide vertical=true -->

## Aims going forwards

<!-- .slide vertical=true -->
- Complete Oasis-Docker Image interactions
- Connect Front-End to Oasis backend
- Store Oasis data on IPFS 
- Create chainlink external adapter for (IPFS De-Identified Medical Image CID: Label) key value pairs
<!-- .slide vertical=true -->
