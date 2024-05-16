import streamlit as st
import time
import tensorflow as tf
import numpy as np


def model_prediction(image_set):
    model = tf.keras.models.load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(image_set, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

def traitement(image_file):
    if not (image_file == None):
        if(st.button("Prédiction")):
            st.markdown("""
            ##### Notre prediction : 
        """)
            with st.spinner("Patientez..."):
                time.sleep(3)
            index = model_prediction(image_file)
            disease = class_name_french[index]
            st.success(disease)
            indice = str(disease).find("sain")
            if(disease[indice : (indice+4)] == "sain"):
                st.balloons()

def capture():
    image_file = st.camera_input(label="Prendre une photo de la fauille", label_visibility="hidden")
    print(image_file)
    traitement(image_file)

def upload():
    image_file = st.file_uploader("Selectionnez une image de plante", type=["jpg", "jpeg", "png"])
    if image_file:
        if(st.button("Voir l'image")):
            st.image(image_file, use_column_width=True)
        traitement(image_file)

class_name_french = [
  'Pomme > Tavelure du pommier',
  'Pomme > Pourriture noire',
  'Pomme > Rouille du pommier de cèdre',
  'Pomme > saine',
  'Myrtille > saine',
  'Cerise (y compris_aigre) > Oïdium',
  'Cerise (y compris_aigre) > saine',
  'Maïs > Tache cercosporéenne Tache grise',
  'Maïs > Rouille commune',
  'Maïs > Brûlure des feuilles du Nord',
  'Maïs > sain',
  'Cépage > Pourriture noire',
  'Cépage > Esca (Rougeole Noire)',
  'Raisin > Brûlure des feuilles (Tache des feuilles Isariopsis)',
  'Raisin > sain',
  'Orange > Haunglongbing (Verdissement des agrumes)',
  'Pêche > Tache bactérienne',
  'Pêche > saine',
  'Poivre > cloche Tache bactérienne',
  'Poivre > cloche saine',
  'Pomme de terre > Mildiou',
  'Pomme de terre > Mildiou',
  'Pomme de terre > saine',
  'Framboise > saine',
  'Soja > sain',
  'Courge > Oïdium',
  'Fraise > Brûlure des feuilles',
  'Fraise > saine',
  'Tomate > Tache bactérienne',
  'Tomate > Mildiou',
  'Tomate > Mildiou',
  'Tomate > Moisissure des Feuilles',
  'Tomate > tache septorienne',
  'Tomate > Acariens Tétranyque à deux points',
  'Tomate > Point Cible',
  'Tomate > Virus de l\'enroulement des feuilles jaunes de la tomate',
  'Tomate > Virus de la mosaïque de la tomate',
  'Tomate > saine'
]

st.title("Sytème De Détection Des Maladies Des Plantes 🇨🇲")
st.sidebar.write("Auteur : TeamsAI_STFN")
st.sidebar.title("Menu")
choix = st.sidebar.selectbox("", ["Acceuil", "Détection", "A propos"])

if(choix == "Acceuil"):

    st.markdown("""
   ## Bienvenue dans notre application 
   - **Une appication de detection des maladie des plantes pour améliorer l'agriculture au Cameroun.**
   - Elle vous permettra de savoir **de quel maldadie peut être atteint vos plantes**
   afin de prendre de facilité les soins et de garentir une culture saine. 🥲
   - Il vous suffira juste importer une image et de laisser **l'intelligence artificielle 🤖** faire tout le reste.
   - Vous ne serrez pas déçu car elle a un exellent taux de prediction et de reconnaissance.
   ## Etapes d'utilisation
   1. **Importer une image :** Allez a la page Detection de importer l'image de la plante que vous suspectez d'être malade
   2. **Analyse :** Notre système va traité l'image en utilisant des algorithmes avancé pour identifier la potentielle maladie
   3. **Résultat :** Visualiser le resultat et prevoyer un traitement en cas de maladie
   ## Pourquoi nous choisir 🤔 ?
   - **Bonne prédiction :** Notre système utilise l'état de l'art des techniques du machine learning avancé 
   pour donner de meilleurs réponses.
   - **Facile a utiliser :** Une interface simple et intuitive pour une meilleur expérience utilisateur
   - **Rapide et efficace :** La réponse est transmis quelque seconde après validation du bouton de décision 
   ## Commencer
   Cliquer sur la page **Detection** du menu puis charger une image de plante afin de connaitre sa maladie 

   """) 

elif(choix == "Détection"):
    st.write("")
    st.subheader("Détection de la maladie")
    choix1 = st.sidebar.selectbox("", ["Utiliser la camera", "Charger une image"])
    if(choix1 == "Utiliser la camera"):
        capture()
    elif (choix1 == "Charger une image"):
        upload()

elif(choix == "A propos"):
    st.subheader("A propos")
    st.markdown("""
    ### Notre équipe
    **TeamsAI_STFN** est une équipe de 4 etudiants passionné par la data science et l'intelligence artifielle. Nous somme tous le temps entrain de chercher et mettre en oeuvre de nouvalle technologie pour ameliorer la vie des citoyen en Afrique et plus precisement au **Cemeroun**
    
    """)
    



