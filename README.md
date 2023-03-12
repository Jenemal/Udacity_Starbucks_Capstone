# Udacity_Disaster_Response_Pipeline

## Motivation

Combining three datasets provided by Starbucks, I have created a ML model to identify whether or <br> 
not an offer provided by Starbucks will be successful or not. This will hopefully provide them with <br>
insight as to how better target offers.

## Analysis
This project includes datafiles provided by Starbucks on users, offers, and transcripts recording <br> 
user/offer interactions. Jupyter Notebook is used to preprocess the data for a heuristic analysis. The <br>
pre-processed data was also used to create a logistic regression ML model to help predict whether or <br>
not an offer would be successful or not.

### Medium Article
A brief blog describing the results of the analysis can be found here:
https://medium.com/@jmalik.87.osu/7c4fc55fefa5

## Files
#### portfolio.json contains the information on the offers
- id (string) - offer id
- offer_type (string) - type of offer ie BOGO, discount, informational
- difficulty (int) - minimum required spend to complete an offer
- reward (int) - reward given for completing an offer
- duration (int) - time for offer to be open, in days
- channels (list of strings)
#### profile.json contains the information for Starbucks members
- age (int) - age of the customer
- became_member_on (int) - date when customer created an app account
- gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
- id (str) - customer id
- income (float) - customer's income
#### transcript.json contains the transaction information
- event (str) - record description (ie transaction, offer received, offer viewed, etc.)
- person (str) - customer id
- time (int) - time in hours since start of test. The data begins at time t=0
- value - (dict of strings) - either an offer id or transaction amount depending on the record
#### Starbucks_Capstone_Project.ipynb is the Jupyter Notebook file to process the data

## To Run
#### Starbucks_Capstone_Project.ipynb
- Open the Jupyter notebook file.
- In the Pre-Preproccessing section check to make sure that the filepath for loading the <br>
json files matches where the files are stored on your local machine. They are currently set <br>
to './data/portfolio.json'
- Click "Run All"

## Contact Information
Created by Jen E. Malik 03/12/23
