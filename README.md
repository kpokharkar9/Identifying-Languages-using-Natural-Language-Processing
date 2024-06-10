# Identifying-Languages-using-Natural-Language-Processing

#1. Introduction
Language detection is a crucial task in natural language processing (NLP), involving the automatic identification of the language of a given piece of text. This project focuses on language classification using text data from the Europarl dataset. The aim is to preprocess the data and build machine learning models to classify text into different European languages.

#2. Dataset
The dataset consists of parallel corpora from the European Parliament proceedings, which includes multiple languages such as English, Bulgarian, Czech, Danish, German, Spanish, Finnish, French, Hungarian, Italian, Latvian, Dutch, Polish, Portuguese, Romanian, Slovenian, and Swedish. Each language's text data is stored in separate files. For this project, a balanced dataset with an equal number of samples from each language is created to ensure unbiased model training.

#3. Preprocessing
Text preprocessing is crucial for text analysis as it involves cleaning and transforming raw text data into a format suitable for analysis.

* process_chunk: This function processes each chunk of text data, applies the preprocess_text function, and appends the cleaned text with its corresponding language label to a list.
* preprocess_text: This function converts text to lowercase, removes digits, and translates punctuation characters to whitespace.

#4. Batch Preprocessing
Text data is read in chunks from the specified filepaths, preprocessed, and the cleaned data is appended to a list. This approach is memory efficient and helps in handling large datasets.

#5. Creating a Balanced Dataset
A balanced dataset ensures that each language is equally represented, which is crucial for training an unbiased model. The first 10,000 rows for each language are selected to create a new dataframe.

#6. Modeling

The modeling section involves building and training the classifiers:

+ Feature Extraction using TF-IDF
TF-IDF (Term Frequency-Inverse Document Frequency) is used to transform the text data into numerical features:

* char_vectorizer: Generates TF-IDF features based on character n-grams (2 to 4 characters).
* word_vectorizer: Generates TF-IDF features based on word n-grams (1 to 2 words).
* FeatureUnion: Combines both character and word TF-IDF features.

+ Multinomial Naive Bayes (MNB)
A pipeline is created to streamline the process:

* Vectorizer: Combines character and word TF-IDF features.
* Classifier: Multinomial Naive Bayes classifier.
* Training and Prediction: The model is trained on the training data and used to predict the language of the test data.
* Accuracy Calculation: Accuracy of predictions is calculated.

+ Logistic Regression (LR)
Similar to MNB, a pipeline is created for Logistic Regression:

* Vectorizer: Combines character and word TF-IDF features.
* Dimensionality Reduction: TruncatedSVD is used to reduce feature dimensionality.
* Classifier: Logistic Regression.
* Training and Prediction: The model is trained and used for prediction.

+ Results

The performance of the models is evaluated using various metrics:

* Classification Report
Provides precision, recall, and F1-score for each language. Reports are generated for both training and testing data to evaluate the model's performance.

* Confusion Matrix
Visualizes the performance by showing the true positives, true negatives, false positives, and false negatives for each language. This helps understand misclassifications.

+ Dependencies

The project requires the following libraries:

string: For string manipulation.
pandas: For data manipulation and analysis.
numpy: For numerical operations.
re: For regular expressions.
requests: For sending HTTP requests.
io: For working with streams.
seaborn: For data visualization.
matplotlib: For plotting.
sklearn: For machine learning tools.

+ Usage

To use the models for language detection:

* Preprocess the Text Data: Ensure text data is cleaned and transformed as described.
* Feature Extraction: Apply TF-IDF vectorization using character and word n-grams.
* Train the Model: Train either the MNB or LR model using the processed data.
* Predict: Use the trained model to predict the language of new text data.
* Evaluate: Check the accuracy, classification report, and confusion matrix to evaluate the model's performance.
