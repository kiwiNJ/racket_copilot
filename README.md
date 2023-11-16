# racket_copilot
Ein Skript, das Racketcode für Testfälle automatisch erzeugt.

_Dieses Projekt ist für die Vorlesung Informatik I an der Universität Münster gedacht, darf aber auch für andere Zwecke genutzt werden._

## Installation
### Ausfühbare Datei
Unter Microsoft Windows können Sie die Datei [racket_copilot.exe](racket_copilot.exe) herunterladen.  

_Getestet unter Microsoft Windows 10 Home._

### Python Skript
Wenn Sie ein anderes Betriebssystem nutzen oder den Code verändern wollen, müssen Sie zunächst einen Python 3 Interpreter installieren, z.B. [von der offizielen Python Webseite](https://www.python.org/downloads/). 

Anschließend können Sie die Datei [racket_copilot.py](racket_copilot.py) herunterladen und mit dem Python Interpreter ausführen. Doppelklicken Sie dazu auf die Datei bzw. öffnen Sie den Ordner mit der heruntergeladenen racket_copilot.py Datei in einer Konsole und führen Sie `py racket_copilot.py` aus.  

_Getestet mit Python Version 3.10.1 und 3.12.0._ 

## Verwendung
Wenn Sie das Programm starten, sollte sich ein Eingabefenster öffnen.  

Um zu einer Racketfunktion die Testfälle zu erzeugen, kopieren Sie den Kommentar in dem Sie die Beispiele zu der Funktion beschreiben in das Eingabefenster. Drücken Sie die ENTER-Taste (evtl. zweimal) und das Programm gibt Ihnen den Racketcode aus, der diese Beispiele testet.

### Eingabeformat
Die Eingabe sollte das folgende Format haben (stark angelehnt an die Schreibweise der Vorlesung):

- Ein Beispiel wird durch einen Satz `;; ... sollte ... ergeben` beschrieben. Der erste Platzhalter steht für das, was getestet werden soll. Der zweite Platzhalter steht für das erwartete Ergebnis.
- Für Tests, die mit atomaren Werten (Zahlen, Wahrheitswerte, Symbole, Zeichenketten) arbeiten, können Sie Eingabeparameter und Ausgabe direkt hinschreiben. Beispiel: `;; (pow 2.5 3) sollte 15.625 ergeben.`
- Für Tests, die zusammengesetzte Daten als Eingabe verwenden, können Sie diese in der Konstruktorschreibweise hinschreiben. Beispiel: `;; (perimeter (make-square (make-posn 2 3) 4)) sollte 16 ergeben.`
- Für Tests, die zusammengesetzte Daten als Ausgabe haben, können Sie die gleiche Schreibweise für das Ergebnis verwenden. Beispiel: `(scale (make-square (make-posn 2 3) 4) 2) sollte (make-square (make-posn -2 -1) 8) ergeben.`
- Für Tests, bei denen näherungsweise Ergebnisse geprüft werden sollen (check-within), können Sie am Ende der Zeile die maximale Fehlerschranke angeben, im Format `(+- ...)`. Beispiel: `;; (sqrt 2) sollte 1.41 ergeben (+- 0.01).`
- Für Tests, bei denen ein Fehler auftreten soll (check-error), können Sie die Schreibweise `;; ... sollte einen Fehler "..." ergeben` verwenden. Beispiel: `;; (sqrt -2) sollte einen Fehler "sqrt: negative Eingabe" ergeben.`
- Jedes Beispiel muss in einer eigenen Zeile beschrieben werden. Beispiele dürfen nicht über mehrere Zeilen gehen.
- Die Eingabe darf weitere Kommentarzeilen enthalten, die keine Beispiele sind. Diese werden unverändert an der gleichen Stelle in die Ausgabe eingefügt. Beispiel: `;; Das nächste Beispiel ist wichtig, da es xy prüft.`
- Einzige Ausnahme: Wenn die Beschreibung der Beispiele mit der Überschrift `;; Beispiele:` beginnt, so wird diese in der Ausgabe durch die Überschrift `;; Tests:` ersetzt.
- In der Eingabe dürfen am Ende jeder Zeile weitere Erklärungen stehen, diese werden allerdings in der Ausgabe gelöscht. Beispiel: `;; (sqrt 0) sollte 0 ergeben [Randfall prüfen]` ergibt `(check-expect (sqrt 0) 0)` 


### Ausgabe
Wenn Sie mit der Eingabe fertig sind, drücken Sie die ENTER-Taste (evtl. zweimal) und das Programm gibt Ihnen den Racketcode aus, der diese Beispiele testet. Sie können die Ausgabe anschließend markieren, kopieren, und in Ihr Racketprogramm einfügen.

Wenn Sie bei der Installation die Option _Ausführbare Datei_ gewählt haben, kopiert das Programm die Ausgabe außerdem von alleine in die Zwischenablage. In diesem Fall wird zusätzlich die Meldung `(Die Ausgabe wurde in Ihre Zwischenablage kopiert.)` ausgeben. Wenn Sie bei der Installation die Option _Pythonskript_ gewählt haben, müssen Sie gegebenenfalls das Pythonmodul pyperclip in der Version 1.8.2 installieren, damit die Ausgabe automatisch kopiert wird. (Verwenden Sie dazu den Befehl `py -m pip install pyperclip==1.8.2`)

Nach der Ausgabe beginnt das Programm von vorne und Sie kÖnnen eine neue Eingabe einfügen.

Falls das Programm eine Zeile in Ihrer Eingabe nicht versteht, so lässt es diese als Kommentar in der Ausgabe stehen. Sie sollten dies also spätestens durch die farbige Hervorhebung von Kommentaren in DrRacket sehen und die Zeile manuell anpassen können.


### Beispiele
Versuchen Sie als Beispiel, die vom Programm vorgeschlagene Beispieleingabe auszuführen. Die Ausgabe sollte wie folgt aussehen: 

(Hierbei sollten Sie als Nutzer*in die Zeilen unterhalb vom `Eingabe (Kommentar, der die Beispiele beschreibt):` einfügen.)
```
Willkommen zu dem Programm, dass Ihnen hoffentlich mehrere Stunden Lebenszeit sparen wird.

Kopieren Sie in dieses Fenster den Kommentar Ihrer Racket Funktion, in dem Sie die Beispiele beschreiben.
Dann drücken Sie auf ENTER (im Zweifel mehrfach), und das Programm gibt Ihnen den vollständigen Racket-Code aus, der diese Beispiele testet._

Das erwartete Eingabeformat ist wie folgt:
;; Beispiele:
;; (pow 2.5 3)  sollte 15.625  ergeben. ;; Format fuer numerische Tests
;; (perimeter (make-square (make-posn 2 3) 4))  sollte 16 ergeben ;; Format fuer Tests mit structs als Eingabe
;; (scale (make-square (make-posn 2 3) 4) 2)  sollte (make-square (make-posn -2 -1) 8) ergeben ;; Format fuer Tests mit structs als Ausgabe
;; (sqrt -2) sollte einen Fehler "sqrt: negative Eingabe" ergeben ;; Format fuer Tests mit Fehlermeldungen
;; (sqrt 2) sollte 1.41 ergeben (+- 0.01) ;; Format fuer naeherungsweises pruefen (check-within)
;; Ein Kommentar darf auch Zeilen enthalten, die keinen Test beschreiben. Diese werden ignoriert.
;; Beispiele duerfen nicht ueber mehrere Zeilen gehen. Jedes Beispiel muss in einer eigenen Zeile stehen.

Eingabe (Kommentar, der die Beispiele beschreibt):
;; Beispiele:
;; (pow 2.5 3)  sollte 15.625  ergeben. ;; Format fuer numerische Tests
;; (perimeter (make-square (make-posn 2 3) 4))  sollte 16 ergeben ;; Format fuer Tests mit structs als Eingabe
;; (scale (make-square (make-posn 2 3) 4) 2)  sollte (make-square (make-posn -2 -1) 8) ergeben ;; Format fuer Tests mit structs als Ausgabe
;; (sqrt -2) sollte einen Fehler "sqrt: negative Eingabe" ergeben ;; Format fuer Tests mit Fehlermeldungen
;; (sqrt 2) sollte 1.41 ergeben (+- 0.01) ;; Format fuer naeherungsweises pruefen (check-within)
;; Ein Kommentar darf auch Zeilen enthalten, die keinen Test beschreiben. Diese werden ignoriert.
;; Beispiele duerfen nicht ueber mehrere Zeilen gehen. Jedes Beispiel muss in einer eigenen Zeile stehen.==

Ausgabe (Racket code, der diese Beispiele testet):
;; Tests:
(check-expect (pow 2.5 3) 15.625)
(check-expect (perimeter (make-square (make-posn 2 3) 4)) 16)
(check-expect (scale (make-square (make-posn 2 3) 4) 2) (make-square (make-posn -2 -1) 8))
(check-error (sqrt -2) "sqrt: negative Eingabe")
(check-within (sqrt 2)             1.41 0.01)
;; Ein Kommentar darf auch Zeilen enthalten, die keinen Test beschreiben. Diese werden ignoriert.
;; Beispiele duerfen nicht ueber mehrere Zeilen gehen. Jedes Beispiel muss in einer eigenen Zeile stehen.


(Die Ausgabe wurde in Ihre Zwischenablage kopiert.)
```

### Fehler, was nun?
Prüfen Sie zunächst, ob Sie sich an das richtige [Eingabeformat](#eingabeformat) gehalten haben. 

Bei allen weiteren Fragen können Sie im [Learnweb Forum](https://sso.uni-muenster.de/LearnWeb/learnweb2/mod/moodleoverflow/discussion.php?d=3275) nachfragen. 

Falls das Programm die folgende Fehlermeldung anzeigt, so ist es abgestürzt. Schritt 1: Schließen Sie das Fenster und starten Sie das Programm erneut. Schritt 2: Falls das Problem bestehen bleibt, stellen Sie eine Frage im Learnweb Forum. Fügen Sie Ihrem Post bitte die Fehlermeldung hinzu, die das Programm unterhalb der Nachricht anzeigt.

Fehlermeldung bei Programmabsturz:
```
################################################################################
################################################################################
Bei der Ausfuehrung des Programms ist leider ein Fehler aufgetreten.
Druecken Sie ENTER um das Programm zu schliessen und starten Sie es dann erneut.
################################################################################
################################################################################
```

## Copyright
Alle von mir geschaffenen Inhalte dürfen Sie unter der [Lizenz CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.de) verwenden. Das heißt, für alle nicht-kommerzielle Zwecke dürfen Sie das Programm nutzen, verändern, und weiterverbreiten, solange Sie dabei mich als ursprüngliche Quelle angeben.

Das Icon des Programms basiert auf dem frei verfügbaren Logo von [racket-lang](https://racket-lang.org/).

Autor: Nikolai Jenki
Datum: 16.11.2023
Version: 1.0
