# AI Chatbot Script

Ce script Python interagit avec l'API d'OpenAI pour créer un chatbot alimenté par l'intelligence artificielle. Le chatbot peut maintenir des conversations simples avec les utilisateurs en générant des réponses basées sur les entrées fournies.

## Configuration

1. Installez la bibliothèque OpenAI en utilisant la commande suivante :

```bash
pip install openai
```

2. Obtenez une clé API OpenAI en suivant les instructions sur le site Web d'OpenAI. Remplacez `"YOUR_API_KEY"` dans le script par votre clé API.

## Fonctionnalités

- Le chatbot accueille l'utilisateur avec un message de salutation et attend les entrées de l'utilisateur.
- Pour mettre fin à la conversation, l'utilisateur peut saisir "exit".
- Le script utilise une boucle pour maintenir la conversation avec l'utilisateur.
- Le chatbot utilise l'API OpenAI pour générer des réponses basées sur les entrées de l'utilisateur.
- Un délai d'une seconde est introduit entre les réponses du chatbot pour simuler un flux de conversation plus naturel.

## Utilisation

1. Exécutez le script en utilisant la commande suivante :

```bash
python chatbot.py
```


2. Le chatbot répondra aux entrées de l'utilisateur en utilisant l'API OpenAI.

3. Pour mettre fin à la conversation, entrez "exit".

## Personnalisation

- Vous pouvez personnaliser les messages de salutation et d'au revoir en modifiant les lignes correspondantes dans le script.
- Vous pouvez également ajuster le délai entre les réponses en modifiant la valeur dans la fonction `time.sleep()`.

## Remarque

Assurez-vous de surveiller l'utilisation de l'API et de respecter les limites de votre plan pour éviter les problèmes de quota.

Pour obtenir de l'aide supplémentaire sur l'utilisation de l'API OpenAI, consultez la documentation officielle d'OpenAI.

---

*Ce script a été créé pour des fins éducatives et de démonstration. Veuillez consulter la documentation d'OpenAI et respecter les conditions d'utilisation de l'API.*


