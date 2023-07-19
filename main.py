from keybert import KeyBERT
import os

folder_path = "/Users/bryantabalos/PycharmProjects/pythonProject/Internship_Data_ArmyAPI_Pull_06222023"

texts = []

# uploads all the data files and loops through each doucment
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            text = file.read()
            texts.append(text)

# Initalizes KeyBERT model
keybert_Model = KeyBERT()


# Defines and implements KeyBERT extraction method
def extract_keywords_from_document(doc):
    keywords = keybert_Model.extract_keywords([doc])  # extracts the keywords
    return keywords


# Entices the user to run the code and upload the results
document = input("Press Enter to Upload Results")
print("Waiting for Results...")
document_keywords = extract_keywords_from_document(texts[0])  # Extracts Keywords from first document

# ngram range, sets how long the keyword extraction word is (1,1) - (3,3)
ngram_keywords = keybert_Model.extract_keywords(texts, keyphrase_ngram_range=(3, 3), stop_words='english')


# prints the keywords found in 'ngram'
print("Keywords: ")
for keyword in ngram_keywords:
    print(keyword)