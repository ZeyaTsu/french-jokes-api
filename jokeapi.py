import random
import json

jokes = ["Que dit une noisette quand elle tombe dans l’eau ? Je me noix.", 
        "Comment est-ce que les abeilles communiquent entre elles ? Par -miel.", 
        "Qu’est-ce qu’une frite enceinte ? Une patate sautée.",
        "Que dit une mère à son fils geek quand le dîner est servi ? Alt Tab !", 
        "Quelle est la différence entre les bières et les chasseurs ? Les bières, on arrive à en faire des sans alcool.",
        "Quel est le point commun entre un gynécologue myope et un chien en bonne santé ? Ils ont tous les deux le nez mouillé.", 
        "Pour un chasseur, qu’elle est la différence entre son chien et sa femme ? Le prix du collier.",
        "Pourquoi les Ch’tis aiment les fins de vacances au camping ? Parce que c’est le moment où ils peuvent démonter leur tente.", 
        "Qu’est-ce qui est pire qu’un bébé dans une poubelle ? Un bébé dans deux poubelles.",
        "Quelle partie du légume ne passe pas dans le mixer ? La chaise roulante.", 
        "Qu’est-ce qui est mieux que gagner une médaille d’or aux Jeux Paralympiques ? Marcher.",
        "Quelle mamie fait peur aux voleurs ? Mamie Traillette.", 
        "Pourquoi est-ce qu'on dit que les bretons sont tous frères et sœurs ? Parce qu’ils n’ont Quimper",
        "Pourquoi dit-on que les poissons travaillent illégalement ? Parce qu’ils n’ont pas de FISH de paie.", 
        "Quel est le bar préféré des espagnols ? Le Bar-celone",
        "Pourquoi la France et les USA ne peuvent pas jouer aux échecs ? Les USA ont perdu les 2 tours et la France notre Dame.", 
        "Qu'est-ce qu'un tennisman adore faire ? Rendre des services",
        "Tu veux une blague courte?........ t'en veux une autre ?", 
        "Quel fruit est assez fort pour couper des arbres? Le ci-tron",
        "Quel est le jambon que tout le monde déteste ? Le sale ami", 
        "Que dit une imprimante dans l'eau ? J’ai papier"]


def all():
    
    random.shuffle(jokes)
    x = jokes[0]
    jso1n = {
        "type": "onepart", 
        "response": x,
        "lang": "fr"
    }

    with open('jokeapi.json', 'w') as f:
        json.dump(jso1n, f)
    
    
    #f.write("yes")
