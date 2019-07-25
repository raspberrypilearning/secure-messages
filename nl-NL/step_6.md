## Hele berichten versleutelen

In plaats van het per teken versleutelen van berichten, kunnen we het programma zo aanpassen dat het hele bericht wordt gecodeerd.

+ Kijk eerst of de code er zo uitziet:
    
    ![screenshot](images/messages-character-finished.png)

+ Maak een variabele waarin het nieuwe gecodeerde bericht wordt opgeslagen.
    
    ![screenshot](images/messages-newmessage.png)

+ Wijzig de code om het hele bericht van de gebruiker op te slaan en niet slechts één teken.
    
    ![screenshot](images/messages-message.png)

+ Voeg een `for` -lus toe aan de code en laat de rest van de code inspringen zodat die wordt herhaald voor elk teken in het bericht.
    
    ![screenshot](images/messages-loop.png)

+ Test de code. Je zou moeten zien dat elk teken in het bericht is gecodeerd en één voor één wordt weergegeven.
    
    ![screenshot](images/messages-loop-test.png)

+ We gaan elk gecodeerd teken toevoegen aan de variabele `nieuwBericht`.
    
    ![screenshot](images/messges-message-add-character.png)

+ Je kunt `nieuwBericht` `printen` terwijl die wordt versleuteld.
    
    ![screenshot](images/messages-print-message-characters.png)

+ Als je de spaties vóór de `print` -instructie verwijdert, wordt het gecodeerde bericht slechts eenmaal weergegeven aan het einde. Je kunt ook de code om de tekenposities af te drukken verwijderen.
    
    ![screenshot](images/messages-print-message-comment.png)