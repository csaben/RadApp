# RadApp
Code base for front end, backend, and rest of related docs

[Demo](https://devpost.com/software/radiology-application-radapp?ref_content=user-portfolio&ref_feature=in_progress) Presentation for Fall Chainlink Hackathon 2021
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
- Oasis Parcel set-up (current progress not included for private key leak concerns)
<!-- .slide vertical=true -->

## Developer To Do List

<!-- .slide vertical=true -->
- Update white paper for most accurate architecture
- Complete Oasis file handling architecture
<!-- .slide vertical=true -->
