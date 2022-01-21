# BE Intégration - Mineure Interaction Avancée

Le but de ce BE est d'imaginer et développer une preuve de concept 
d'un  assistant  dédié  à  l’aide  à  la  gestion  d’une  maison  intelligente  dans  ses 
aspects domotiques (chauffage, stores, ...), domestiques (liste de courses, ...) 
et familiaux (laisser un message aux membres de la famille : aller chercher du pain, ...).

Le chatbot a été fait avec [RASA](https://rasa.com/).

Pour plus de détails, consultez le rapport présent dans le répertoire.

## Comment utiliser l'application :
Dans un premier terminal, démarrer l'écoute de l'utilisateur:
```
cd PATH\interaction_chatbot\rasa_chatbot\actions\
python stt_tts.py
```
Dans un deuxième terminal, démarrer le serveur des CustomsActions:
```
cd PATH\interaction_chatbot\rasa_chatbot\
rasa run actions
```
Dans un troisième terminal, démarrer le chatbot Rasa:
```
cd PATH\interaction_chatbot\rasa_chatbot\
rasa run
```
(Optionnel) Dans un dernier terminal, démarrer l'interface de démo:
```
cd PATH\interaction_chatbot\
python home.py
```

Commencer ensuite l'intéraction en disant "ok google".
Les scénarios d'intéractions possibles sont décrit dans le rapport.

## Requirements :

- L'app ne fonctionne pas offline, vous devez être connecté à Internet
- Python 3.6.2
- RASA
```
pip3 install rasa==2.8
```
- PyAudio
```
pip install PyAudio
```
- SpeechRecognition 3.8.1
```
pip install SpeechRecognition
```
- ivy-python
```
pip install ivy-python
```
- pygame
```
pip install pygame
```
- python text to speech
```
pip install pyttsx3
```
- requests
```
pip install requests
```