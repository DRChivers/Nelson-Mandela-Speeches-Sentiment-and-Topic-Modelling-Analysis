# Nelson Mandela Speeches Sentiment and Topic Modelling Analysis
This is a repository for my MPhil Digital Humanities final dissertation project, which applies computational linguistics methods (sentiment analysis and topic modelling) to the speech transcriptions of Nelson Mandela. 
# Data
The dataset has been compiled using 1,577 EAD 2002 XML files containing transcripts of Nelson Mandela's speeches, which have been made available by the Nelson Mandela Foundation's Archive (https://atom.nelsonmandela.org/index.php/za-com-speeches). These transcripts have been taken from various sources, which are noted within the original XML file metadata. 
# Data Cleaning Process and Scripts
To make a corpus of machine-readable transcripts ready for my analysis, I have created scripts using ChatGPT and my own knowledge to extract the relevant data from the XML files. This project uses the Python programming language via the Jupyter Notebooks IDE. The following is an outline of the steps and scripts used to clean the data (in order): 
- Deploy the custom webscraper to extract the XML files from the archive to my computer (mandela_xml_files_web_scraping.ipynb)
- Use the data extraction script to grab the filename and speech date and write it to a spreadsheet file (extract_xml_filename_and_date.ipynb)
- Use the XML file renaming script to write the speech dates into the filename to make future computational analysis of the speeches easier (rename_xml_files.ipynb) 
- Download OpenRefine, and upload the renamed XML files for further data cleaning (to manualy extract the transcripts which where originally tagged as a generic note rather than a transcript specifically - a barrier which could have been avoided if the creator of the XML files tagged them explicitly) 
- Export the cleaned data from OpenRefine into a spreadsheet file 
- Use the merging script to merge all the transcript data into a single cell, as every paragraph of each transcript is exported as an individual data cell (merging_transcipts_in_excel.ipynb) 
- Read through the new merged spreadsheet database and complete final data cleaning operations (remove undated transcripts, etc.)
- Then run the Excel to XML converter script to create new XML files which contain just the text of each transcript and uses the new file names we created earlier (excel_to_xml_converter.ipynb)

Of the 1,577 XML files available in the archive, after data cleaning only 1,500 are usable after removing files which had no date, files which conatain no speeches, files which had non-English language speeches and no official translation, and so on. 
# Sentiment and Topic Modelling Scripts
This project uses the Python programming language via the Jupyter Notebooks IDE to analyse sentiment and to provide topic modelling of the transcribed speeches. The three scripts being used have been modified from the Charles Stewart Parnell speech analysis project undertaken by Eugenio Biagini, Patrick Geoghegan, Hugh Hanley, Aneirin Jones, and Huw Jones at the University of Cambridge (see, https://github.com/NyeJones/parnell-sentiment-analysis-and-topic-modelling). They should be run in the following order:
- mandela_sentiment_analysis.py
- mandela_topic_model.py
- mandela_topic_model_unique_high_low_sentiment.py
# Libraries 
The scripts for data cleaning use several libraries which will need to be installed prior to running (some may already be installed if using a distribution like Anaconda):
```
pip install pandas
pip install requests
pip install os
pip install elementpath
```
The scripts for sentiment analysis and topic modelling use several libraries which will need to be installed prior to running:
```
pip install beautifulsoup4
pip install matplotlib
pip install natsort
pip install nltk
pip install pandas
pip install scikit-learn
```
