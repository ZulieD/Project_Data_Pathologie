import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

### Sidebar ####
with st.sidebar:
    st.title('Auteur du projet :')
    st.write("")
    st.write("Julie DANIEL")
    st.write("21 ans ")
    st.write("Sexe féminin")
    github_url = "https://github.com/ZulieD/Project_Data_Pathologie/tree/main"
    st.markdown(f"[Lien vers le GitHub]( {github_url} )")
    st.write("")
    st.subheader('Comment me contacter :')
    st.write("")
    linkedin_url = "https://www.linkedin.com/in/julie-daniel-9003961b6/"
    st.markdown(f"[LinkedIn]( {linkedin_url} )")
    email_address = "julie.daniel@efrei.net"
    st.markdown(f"[Par e-mail](mailto:{email_address})")
    st.write("")
    st.subheader("Votre avis sur le projet :")
    color = st.select_slider(
        '',
        options=['médiocre', 'moyen', 'passable', 'correct', 'satisfaisant', 'excellent', 'remarquable'])
    st.write('Vous pensez que mon projet est ', color)
    
    ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
        background: rgb(99 1 1 / 0%); } </style>''', unsafe_allow_html = True)


    Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
        background-color: rgb(14, 38, 74); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)

    
    Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                { color: rgb(14, 38, 74); } </style>''', unsafe_allow_html = True)
    

    col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
        background: linear-gradient(to right, rgb(1, 183, 158) 0%, 
                                rgb(99, 183, 195), 
                                rgba(99, 166, 195), 
                                rgba(14, 38, 74) 100%); }} </style>'''

    ColorSlider = st.markdown(col, unsafe_allow_html = True)
    
### 

### Introduction ###

st.markdown("<h1 style='text-align: center; color: black;'>Analyse des pathologies dans les hôpitaux Français</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: black;'>Projet Data Visualization </h3>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write(''' Nos hôpitaux sont actuellement surchargés, et le personnel hospitalier est débordé.
Il est impératif de réformer le fonctionnement des hôpitaux pour assurer une gestion plus efficace des patients
et des ressources. Aujourd'hui, dans notre étude, nous examinerons de près les hospitalisations,
leurs causes, et réfléchirons à des moyens d'améliorer la situation.    ''')
st.write('')
st.image('hopital.png')
st.write('')
### 

### donnée ###

df=pd.read_csv("echantillons_trie2.csv")
if st.checkbox('Voir nos données'):
    st.write(df)
    
df['niveau_prioritaire'] = df['niveau_prioritaire'].str.replace(',', '|')
df['niveau_prioritaire'] = df['niveau_prioritaire'].str.extract(r'(\d+)$')
df['niveau_prioritaire'] = df['niveau_prioritaire'].fillna(0)
df['niveau_prioritaire'] = df['niveau_prioritaire'].astype(int)

with st.expander("Voir explication"):
    st.write(''' Nous avons un dataframe provenant des données officiels de l'assurance maladie (AMELIE) entre 2015 et 2021.
Nous avons procédé à une selection de 1% des données, gardant ainsi un dataframe de 40 000 lignes.''')
    st.write('Notre dataframe est composé de 16 colonnes :')
    st.write('''année *(année de la pathologie enregistrée)*, patho_niv1, patho_niv2,
patho_niv3 *(différents niveaux de pathologies)*, top *(libellé technique de la pathologie)*,
cla_age_5 *(classe d’âge [5 ans])*, sexe, région, dept *(département)*,
Ntop *(effectif de patients pris en charge pour la pathologie dans l'hôpital en question)*,
Npop *(population de référence qui est celle de la cartographie des pathologies et des dépenses de l'Assurance Maladie)*,
prev *(prévalence de patients pris en charge pour la pathologie)*, Niveau prioritaire *(en fonction de la pathologie)*,
libellé_classe_age, libellé_sexe, tri.''')

st.header('Problématique :')
st.subheader('Comment pouvons-nous améliorer la prise en charge des hospitalisations en France ?') 

####

### Exploration donnée ###

st.write('')
st.write("Nombre moyen d'hospitalisation en fonction des différentes niveau de pathologie :")
col1, col2, col3 = st.columns(3)
col1.metric("Pathologie de niveau 1", "12041")
col2.metric("Pathologie de niveau 2", "2158")
col3.metric("Pathologie de niveau 3", "1999")

with st.expander("Voir explication"):
    st.write(''' Les pathologies de niveau 1 correspondent aux pathologies de faible niveau prioritaire tel qu'une hospitalisation ponctuelle ou pas de pathologie''')
    st.write(" Les pathologies de niveau 2 correspondent aux pathologies de niveau intermediaire regroupant des traitements antihypertenseurs ou encore des diabètes de type 2")
    st.write(" Les pathologies de niveau 3 correspondent aux pathologies de fort niveau prioritaire correspondant à des cancers ou des troubles névrotiques de l'humeur")

st.write("On remarque que les patients vont à l'hopital majoritairement pour des pathologies de niveau 1")

code_1='''
    df_1 = df[df['niveau_prioritaire'] == 1]
    mean_by_pathology = df_1.groupby('patho_niv1')['ntop'].mean()
    mean_by_pathology_sorted = mean_by_pathology.sort_values(ascending=False)
    top_3_pathologies = mean_by_pathology_sorted.head(3)

    top_3_pathologies
    '''
st.code(code_1, language='python')

# Code pathologie 1 majoritaire
st.write(" Les trois pathologies majoritaires de niveau 1 :")
df_1 = df[df['niveau_prioritaire'] == 1]
mean_by_pathology = df_1.groupby('patho_niv1')['ntop'].mean()
mean_by_pathology_sorted = mean_by_pathology.sort_values(ascending=False)
top_3_pathologies = mean_by_pathology_sorted.head(3)

st.write(top_3_pathologies)

st.write("On remarque qu'en moyenne, en France, plus de 68 000 patients viennent tous les ans pour aucune pathologie repérée.")

st.write("On peut alors se poser la question si cette dispersion est homogène dans tous les hôpitaux de France")

code_2='''
import matplotlib.pyplot as plt

df_dep=pd.read_csv("dep_pop2.csv")

# Créez une figure et des sous-graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Premier ensemble de données
mean_by_dept = df.groupby('dept')['ntop'].mean()

# Créez le premier graphique à barres
hist1 = mean_by_dept.plot(kind='bar', title="Moyenne par département des hospitalisations", ax=ax1)
spacing1 = 5
ticks1 = range(0, len(mean_by_dept.index), spacing1)
ax1.set_xticks(ticks1)
ax1.set_xticklabels(mean_by_dept.index[ticks1], rotation=45, ha='right')
ax1.set_xlabel('Département')
ax1.set_ylabel("Moyenne d'hospitalisation")

# Deuxième ensemble de données
plt.sca(ax2)  # Définissez le sous-graphique actuel sur ax2
plt.bar(df_dep['Numéro du Département'], df_dep['Habitants'])
plt.xlabel('Département')
plt.ylabel('Habitants')
plt.title('Nombre d\'habitants par département en France')

# Ajustez la mise en page
plt.tight_layout()

# Affichez le graphique
plt.show()
'''
st.code(code_2, language='python')

# Code graph
df_dep = pd.read_csv("dep_pop2.csv")

def generate_plots():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    mean_by_dept = df.groupby('dept')['ntop'].mean()

    hist1 = mean_by_dept.plot(kind='bar', title="Moyenne par département des hospitalisations", ax=ax1)
    spacing1 = 5
    ticks1 = range(0, len(mean_by_dept.index), spacing1)
    ax1.set_xticks(ticks1)
    ax1.set_xticklabels(mean_by_dept.index[ticks1], rotation=45, ha='right')
    ax1.set_xlabel('Département')
    ax1.set_ylabel("Moyenne d'hospitalisation")

    plt.sca(ax2)
    plt.bar(df_dep['Numéro du Département'], df_dep['Habitants'])
    plt.xlabel('Département')
    plt.ylabel('Habitants')
    plt.title('Nombre d\'habitants par département en France')
    plt.tight_layout()

    return fig

if __name__ == "__main__":
    st.write("Comparaison des données par département :")
    st.pyplot(generate_plots())


st.write("On remarque que les départements où il y a le plus d'hospitalisation correspond aux départements qui ont le plus d'habitant")
st.write('''On peut donc en conclure que le nombre d'hospitalisations varie en fonction de la population ;
ainsi, plus l'hôpital est situé dans une grande ville, plus il est nécessaire de mettre en place une gestion efficace des patients.
''')


####


## Conclusion ###
st.subheader('Notre solution : ')
st.write('''La principale raison des hospitalisations en France est
         *Pas de pathologies repérées, traitements, maternité, hospitalisations ni traitement antalgique ou anti-inflammatoire*. 
         Cela signifie que la majorité des patients qui se rendent à l'hôpital n'ont besoin d'aucun traitement spécifique.
         Malgré cela, ils sont accueillis et traités par des médecins qui pourraient être disponibles pour des patients atteints de pathologies plus graves.
         Cela a pour conséquence de ralentir le fonctionnement des établissements hospitaliers et de réduire la qualité des soins,
         car les médecins doivent agir rapidement pour traiter un plus grand nombre de patients.''')
st.write(''' Pour réduire le nombre de patients sans pathologie à l'hôpital, il est nécessaire de proposer davantage de médecins disponibles en journée.
Il nous est tous arrivé d'éprouver une douleur intense ou simplement d'être inquiets, et la seule façon d'obtenir un diagnostic rapide est de se rendre à l'hôpital.
Il est impératif de changer cette habitude et d'encourager les patients à consulter un médecin en premier lieu. Cependant, si les médecins ne sont disponibles que
dans une semaine, cela ne motivera pas les patients à changer leurs comportements.''')

st.write (''' De plus, nous avons observé que le nombre de patients à l'hôpital est fortement corrélé avec le nombre d'habitants.
Ainsi, plus la ville est grande, plus nous devons mettre en place des médecins disponibles à tout instant.''')

st.header(" Pour conclure : ")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Nombre de medecin", "","++++++++")
col2.metric("Nombre patient hôpital", "", "----")
col3.metric("Temps personnel hospitalié", "", "++++")
col4.metric("Qualité soin hôpital", "", "+++++++")
###

### Pour aller plus loins ###
st.header(" Pour aller plus loins : ")

st.write('''Nous pouvons pousser notre analyse de données encore plus loin, en exploitant toutes les colonnes dont nous disposons.
Dans une étude préliminaire que vous pouvez consulter sur mon GitHub,
j'ai conclu que les colonnes département, région, âge et année n'avaient aucun impact sur la nature des pathologies.
''')

st.write ("Concentrons-nous alors sur la colonne restante : *sexe*")


def generate_plot2(df):
    fig, ax = plt.subplots(figsize=(12, 10))  # Utilisez plt.subplots pour obtenir à la fois la figure et l'axe

    # Filtrez le DataFrame avant de créer le graphique
    subset = df[df['niveau_prioritaire'].isin([1, 2, 3])]

    # Définissez la palette de couleurs
    palette = {1: 'blue', 2: 'pink', 9: 'purple'}  # Supprimez 9.0 car il n'est pas dans les données filtrées

    # Utilisez sns.barplot pour créer le graphique à barres
    sns.barplot(x='niveau_prioritaire', y='ntop', hue='sexe', data=subset, palette=palette)

    plt.title("Moyenne de patient par niveau_prioritaire avec distinction de sexe")
    plt.xlabel('Niveau Prioritaire')
    plt.ylabel("Moyenne de la colonne 'ntop'")
    plt.xticks(rotation=0)

    plt.legend(title='Sexe')
    return fig

if __name__ == "__main__":
    st.pyplot(generate_plot2(df))
    
with st.expander("Voir explication"):
    st.write("1 correspond aux Hommes")
    st.write("2 correspond aux Femmes")
    st.write("9 correspond à tous les sexes *aucune différenciation faite lors de l'enregistrement dans la base de donnée, soit car le sexe n'a aucun impact dans la pathologie soit pour des raisons de confidentialité*")

st.write(''' On remarque que les hommes vont beaucoup plus à l'hôpital pour des pathologies de niveau 1 comparé aux femmes''')

df_1 = df[df['niveau_prioritaire'] == 1]
df_1_H = df_1[df_1['sexe'] == 1]
mean_by_pathology = df_1_H.groupby('patho_niv1')['ntop'].mean()
mean_by_pathology_sorted = mean_by_pathology.sort_values(ascending=False)
top_3_pathologies = mean_by_pathology_sorted.head(3)

st.write("La principale raison pour laquelle les hommes se rendent à l'hôpital pour les pathologies de niveau 1", top_3_pathologies)

df_1_F = df_1[df_1['sexe'] == 2]
mean_by_pathology = df_1_F.groupby('patho_niv1')['ntop'].mean()
mean_by_pathology_sorted = mean_by_pathology.sort_values(ascending=False)
top_3_pathologies = mean_by_pathology_sorted.head(3)

st.write("La principale raison pour laquelle les femmes se rendent à l'hôpital pour les pathologies de niveau 1", top_3_pathologies)

st.write('''La différence observée entre les deux sexes pour les hospitalisations sans pathologie identifiée ne peut pas être négligée.
En France, la majorité de ces hospitalisations sans motif médical sont des hommes.''')

st.write("")
st.subheader(''' Cela soulève de nombreuse question :''')
st.write("")
st.write('''Pourquoi les hommes vont-ils plus à l'hôpital pour aucune raison médicale comparé aux femmes ?''')
st.write("Retrouvons-nous une différence aussi importante dans d'autre pathologie ?")
st.write("Est-ce que cette disparité reflète un déséquilibre social ou simplement des différences physiologiques entre les sexes ? ")

st.subheader("Regardons alors cela de plus pret pour différente pathologie")


