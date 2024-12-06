from django.shortcuts import render
import joblib

def symptom_prediction(request):
    prediction = None

    # Modelle und Vektorisierer laden
    model = joblib.load('web/models/symptom_model.pkl')
    vectorizer = joblib.load('web/models/vectorizer.pkl')

    if request.method == "POST":
        # Eingabe vom Benutzer holen
        new_text = request.POST.get('user_input')

        # Text in eine Liste packen
        new_text_list = [new_text]

        # Text in die gleiche numerische Form umwandeln wie beim Training
        new_text_tfidf = vectorizer.transform(new_text_list)

        # Vorhersage treffen
        prediction = model.predict(new_text_tfidf)

    return render(request, 'index.html', {'prediction': prediction[0] if prediction is not None else None})
