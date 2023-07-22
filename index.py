import sqlite3
import random
import os

# Funktion zum Generieren von 12345678 Zufallszahlen
def generate_random_numbers():
    return [random.randint(10000000, 99999999) for _ in range(4)]

# Funktion zum Einfügen von Daten in die Datenbank
def insert_data(connection, data):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO your_table (id, data, id2, id3, id4) VALUES (?, ?, ?, ?, ?)", data)
    connection.commit()

# Funktion zum Aufteilen einer Datei in 19-MiB-Chunks
def split_file(input_file, chunk_size=19*1024*1024):
    chunks = []
    with open(input_file, 'rb') as f:
        while True:
            chunk_data = f.read(chunk_size)
            if not chunk_data:
                break
            chunks.append(chunk_data)
    return chunks

# Hauptfunktion
def main():
    # Pfad zur großen Datei, die aufgeteilt und hochgeladen werden soll
    input_file_path = '/path/to/large_file.bin'    # Pfade anpassen

    # Pfad zur Datenbankdatei
    db_file = '/path/to/your_database.db'  # Beispiel: 'C:/Users/username/Desktop/your_database.db'

    # Verbindung zur SQLite-Datenbank herstellen
    connection = sqlite3.connect(db_file)

    # Tabelle erstellen (falls sie noch nicht existiert)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS your_table (id INTEGER PRIMARY KEY, data BLOB, id2 INTEGER, id3 INTEGER, id4 INTEGER)")

    # Datei in 19-MiB-Chunks aufteilen
    chunks = split_file(input_file_path)

    # Daten in die Datenbank einfügen
    for chunk_number, chunk_data in enumerate(chunks):
        data_part = []
        for i in range(len(chunk_data)):
            data_part.append((None, chunk_data[i:i+1], *generate_random_numbers()))

        # Daten in die Datenbank einfügen
        insert_data(connection, data_part)

    # Datenbankverbindung schließen
    connection.close()

if __name__ == "__main__":
    main()
