import pickle


class ComplaintClassifierService(object):

    @staticmethod
    def make_classification(text):
        classifier = pickle.load(open('C:/Users/mworthin/gitrepos/mongo-django-question-answer/machine_learning_api/consumer_complaints/serialized_model.pkl', 'rb'))
        vectorizer = pickle.load(open('C:/Users/mworthin/gitrepos/mongo-django-question-answer/machine_learning_api/consumer_complaints/serialized_vectorizer.pkl','rb'))
        features = vectorizer.transform([text])
        return classifier.predict(features)
