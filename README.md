# Nelson-Mandela-Speeches-Sentiment-and-Topic-Modelling-Analysis
This is my MPhil Digital Humanities final dissertation project, applying computational linguistics methods (sentiment analysis and topic modelling) to the transcribed speeches of Nelson Mandela. 
# Data
The dataset has been compiled using 1,577 EAD 2002 XML files containing transcripts of Nelson Mandela's speeches, which have been made available by the Nelson Mandela Foundation's Archive (https://atom.nelsonmandela.org/index.php/za-com-speeches). These transcripts have been taken from various sources, which are noted within the original XML file metadata. 
# The Scripts
This project uses the Python programming language to analyse sentiment and to provide topic modelling of the transcribed speeches. The three scripts being used have been modified from the Charles Stewart Parnell speech analysis project undertaken by Eugenio Biagini, Patrick Geoghegan, Hugh Hanley, Aneirin Jones, and Huw Jones at the University of Cambridge (see, https://github.com/NyeJones/parnell-sentiment-analysis-and-topic-modelling). They are run in the following order:
- mandela_sentiment_analysis.py
- mandela_topic_model.py
- mandela_topic_model_unique_high_low_sentiment.py
# Libraries 
The scripts use several libraries which will need to be installed prior to running:
```
pip install beautifulsoup4
pip install matplotlib
pip install natsort
pip install nltk
pip install pandas
pip install scikit-learn
```
