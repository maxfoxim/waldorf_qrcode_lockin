# Allgemein
Bei diesem Djangoprojekt wird ein einfaches An- und Abmeldesystem für einen Schulclub implementiert.

# Oberfläche

## Hauptseite

## Schülerliste
Hier befindet sich die Liste aller Schüler. Diese Liste wird über eine Exceltabelle erzeugt.

## Anwesenheitsliste
Eine historische Liste aller Anmeldungen.

## Heutige Anmeldungen
Zeigt alle heutigen angemeldeten Schüler und Schülerinnen.

## Excel Import
Importiert eine Exceltabelle mit den Tabellen Vornamen, Nachname und Klasse der jeweiligen Schüler. Die Exceltabelle muss exakt so formatiert sein.

## Anmeldung korrigieren
Hier können falsche Einträge, zum Beispiel Schüler hat sich bei Anmeldung verklickt, gelöscht werden. Es wird nur der heutige Eintrag gelöscht. 

# Schülerliste hochladen

# Anwesenheitsliste exportieren
Hierfür muss zunächst auf "Excel Datei erstellen" und anschließend auf "Download Exceldokument" geklickt werden. 

# To Do
-   Sicherheit -> Anmeldefenster

# Installation für eigenes Testen
1) Terminal öffnen
2) git clone https://github.com/maxfoxim/waldorf_qrcode_lockin.git
3) Alternativ die Dateien als ZIP herunterladen
4) Im Terminal ausführen: pip install requirements.txt
5) Anschließend: python manage.py runserver


