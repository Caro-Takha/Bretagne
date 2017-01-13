# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:44:24 2017

@author: cecpe
"""
import sqlite3
import csv


conn = sqlite3.connect('hydrometrie.sqlite')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS hydro_debit_histo")
# Create table
c.execute('''CREATE TABLE hydro_debit_histo
             (id INTEGER PRIMARY KEY, code_hydro, date, annee, mois, jour, moyenne_interannuelle REAL, valeur_faible REAL, valeur_tres_faible REAL, valeur_forte REAL, dixieme_module REAL, debit_donnee_provisoire_m3 REAL, debit_donnee_validee_m3 REAL)''')

# Save (commit) the changes
conn.commit()


with open('hydro-debit-histo.csv', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    got_header = False
    for row in spamreader:
        #On ignore la première ligne (ligne d'entête)
        if (not got_header):
            got_header = True
            continue
        annee, mois, jour = row[1].split(sep='-')
        c.execute('INSERT INTO hydro_debit_histo VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?)',tuple(v for v in row[0:2])+(annee,mois,jour)+tuple(v for v in row[2:]))
    conn.commit()
## We can also close the connection if we are done with it.
#conn.close()
#
#
#conn = sqlite3.connect('hydrometrie.sqlite')
#
#c = conn.cursor()

c.execute("DROP TABLE IF EXISTS stations_hydro")
# Create table
c.execute('''CREATE TABLE stations_hydro
             (id INTEGER PRIMARY KEY, CdStationHydro, LbStationHydro, Lng REAL, Lat REAL)''')

# Save (commit) the changes
conn.commit()


with open('stations-hydro.csv', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    got_header = False
    for row in spamreader:
        #On ignore la première ligne (ligne d'entête)
        if (not got_header):
            got_header = True
            continue
        c.execute('INSERT INTO stations_hydro VALUES (NULL, ?, ?, ?, ?)',tuple(v for v in row[0:]))
    conn.commit()




# Extraction du nom de la station, sa latitude et sa longitude

c.execute('SELECT LbStationHydro, Lng, Lat FROM stations_hydro')
r=c.fetchall()   # r est une liste de listes, chacune de ses sous listes contenant le nom de la station, sa latitude et sa longitude


# on suppose que les dates de début et de fin ont été rentrées, ainsi que le code de la station
CodeStation=('I9122020',)

#jourDebut=(05,)
#moisDebut=(09,)
#anneeDebut=(2015,)
#jourFin=(07,)
#moisFin=(09,)
#anneeFin=(2015,)

c.execute('SELECT debit_donnee_validee_m3 FROM hydro_debit_histo WHERE (jour="05" AND (code_hydro=? ',))(CodeStation))
r=c.fetchall()
print(r)
c.execute('SELECT valeur_tres_faible,valeur_faible,valeur_forte,dixieme_module,debit_donnee_provisoire_m3,debit_donnee_validee_m3 FROM hydro_debit_histo WHERE code_hydro=? ',(CodeStation))
r=c.fetchall()
#print(r)
#  AND annee<=anneeFin AND mois<=moisFin AND jour<=jourFin AND annee>=anneeDebut AND mois>=moisDebut AND jour>=dateDebut)valeur_tres_faible,valeur_faible,valeur_forte,dixieme_module,debit_donnee_provisoire_m3
#c.execute('SELECT valeur_tres_faible,valeur_faible,valeur_forte,dixieme_module,debit_donnee_provisoire_m3,debit_donnee_validee_m3 FROM hydro_debit_histo WHERE (code_hydro=?',CodeStation, 'AND annee<=?',anneeFin,' AND mois<=?',moisFin,' AND jour<=?',jourFin', AND annee>=?',anneeDebut,' AND mois>=?',moisFin,' AND jour>=?',jourFin)
# SELECT debit_donnee_validee_m3 FROM hydro_debit_histo WHERE (code_hydro=? AND annee<=? AND mois<=? AND jour<=? AND annee>=? AND mois>=? AND jour>=?',(CodeStation,anneeFin,moisFin,jourFin,anneeDebut,moisDebut,jourDebut)))