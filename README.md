# PhishShield
A Phishing Detection Chrome Extention powered by Machine Learning 
Phishing involves fraudulently obtaining sensitive information through deceptive websites. Detecting phishing sites is challenging due to their short-lived nature. Machine learning, particularly the random forest classifier, shows promise in improving detection. Implementing a browser plugin for real-time detection is effective for end users. Existing plugins face limitations in language and resource access. To address privacy concerns and reduce latency, a Chrome browser plugin is being developed to classify phishing sites locally without relying on external servers.

# Installation
1) Download Extentions and Unzip it
2) After installing run those command

    step - 1
   
          cd ./Phishshield/Master/backend/dataset
   
      . Run Preprocessing file
   
              python preprocess.py

     step - 2
   
           cd ./Phishshield/Master/backend/classifier
   
      . Run training file
   
           python training.py
   
4) Go to extention menu and turn on "Developer Mode"
5) Select "Load Unpacked" and load "Frontend" folder.
6) Your are ready to go





