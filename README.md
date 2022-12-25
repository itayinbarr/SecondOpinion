Second Opinion
==============================

A convolutional neural network model I trained, to classify an MRI scan into one of 3 types of brain tumors, or a healthy scan.

This project demonstrates the process of building and training a dense neural network model.
The model was trained for classification.

Demo video
------------

### Frontend Overview

![Demo](./secondopiniondemo.gif?raw=true)

Getting Started
------------

I recommend storing patient images in

`./patients`

From within the repo directory run

`./MRITumorScanner/runner.py`

You can now load a file (it has to be a supported photo type). For a full list of supported file types, 
go to the bottom of the file.

For analyzing the photo, click Analyze.

When finished, press Exit button.

-----
About Training & Dataset
--

The dataset was derived from public domain pictures, which were verified by a certified doctor for different
machine learning projects. Most of the pictures were found on Kaggle.

Project Organization
------------

    ├── README.md                    <- The top-level README for developers using this project
    ├── LICENSE.md                   <- MIT
    ├── .gitignore                   <- For environment directories
    ├── data                         <- Data directories, .gitignored (recommended to store here)
    │   ├── training                 <- Training images directory
    │   └── testing                  <- Testing images directory
    │
    ├── MRITumorScanner              <- Containing the software itself
    │   ├── BrainModel               <- Directory of trained model
    │   ├── front.py                 <- GUI code
    │   ├── back.py                  <- backend code
    │   └── runner.py                <- Running the software
    │
    └── tests                        <- Tests directory, .gitignored
        └── backend_tests.py         <- Unit tests of backend
 
Dependencies
------------

- Python
- Keras
- TensorFlow
- TKInter
--------
