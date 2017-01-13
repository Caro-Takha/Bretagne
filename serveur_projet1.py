# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:37:24 2017

@author: Marine
"""
#Projet INF TC3
#Création d'un serveur


# ProjetD_Hydrometrie/serveur_projet.py

# Application exemple : affichage des rivières bretonnes

import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import json

# définition du handler
class RequestHandler(http.server.SimpleHTTPRequestHandler):

  # sous-répertoire racine des documents statiques
<<<<<<< HEAD
  static_dir = '/clients'

  # version du serveur
  server_version = 'ProjetD_hydrometrie/serveur_projet.py/0.1'
=======
  static_dir = '/client'

  # version du serveur
  server_version = '/Serveur_projet/serveur_projet.py/0.1'
>>>>>>> origin/master

  # on surcharge la méthode qui traite les requêtes GET
  def do_GET(self):
    self.init_params()
    print('iiiiiiiiiiiiiiii',self.path_info)

    # requete location - retourne la liste des stations et leurs coordonnées géographiques
    if self.path_info[0] == "location":
        data=[]
        for i in range(175):
<<<<<<< HEAD
            data.append({'id':i,'name': lieu[i][0] ,'lat':lieu[i][2],'lon':lieu[i][1]}) #importer code cécile
        self.send_json(data)
#On ferra ça quand ça marchera ! (c'est le blabla écrit en dessous de la carte)
#    # requete description - retourne la description du lieu dont on passe l'id en paramètre dans l'URL
    elif self.path_info[0] == "description":
        print('laaaaaa', self.path_info)
        data=[]
        for i in range(175):
            data.append({'id':i,'name':lieu[i][0],'valeur forte':y[i]})
        for c in data:
            if c['id'] == int(self.path_info[1]):
                self.send_json(c)
                break
=======
            data.append({'id':i, 'name': r[i][0] ,'lat':r[i][2],'lon':r[i][1]}) #importer code cécile
        self.send_json(data)
#On ferra ça quand ça marchera ! (c'est le blabla écrit en dessous de la carte)
    # requete description - retourne la description du lieu dont on passe l'id en paramètre dans l'URL
    elif self.path_info[0] == "description":
        data2=[]        
        for i in range(175):
            data2.append({'id':i,'desc':'a'})
        for c in data2:
            if c['id'] == int(self.path_info[1]):
                self.send_json(c)
                break
      
          
>>>>>>> origin/master

    # requête générique
    elif self.path_info[0] == "service":
        self.send_html('<p>Path info : <code>{}</p><p>Chaîne de requête : <code>{}</code></p>' \
        .format('/'.join(self.path_info),self.query_string));

    else:
      self.send_static()


  # méthode pour traiter les requêtes HEAD
  def do_HEAD(self):
      self.send_static()


  # méthode pour traiter les requêtes POST - non utilisée dans l'exemple
  def do_POST(self):
    self.init_params()

    # requête générique
    if self.path_info[0] == "service":
      self.send_html(('<p>Path info : <code>{}</code></p><p>Chaîne de requête : <code>{}</code></p>' \
          + '<p>Corps :</p><pre>{}</pre>').format('/'.join(self.path_info),self.query_string,self.body));

    else:
      self.send_error(405)


  # on envoie le document statique demandé
  def send_static(self):

    # on modifie le chemin d'accès en insérant le répertoire préfixe
    self.path = self.static_dir + self.path

    # on calcule le nom de la méthode parent à appeler (do_GET ou do_HEAD)
    # à partir du verbe HTTP (GET ou HEAD)
    method = 'do_{}'.format(self.command)

    # on traite la requête via la classe parent
    getattr(http.server.SimpleHTTPRequestHandler,method)(self)


  # on envoie un document html dynamique
  def send_html(self,content):
     headers = [('Content-Type','text/html;charset=utf-8')]
     html = '<!DOCTYPE html><title>{}</title><meta charset="utf-8">{}' \
         .format(self.path_info[0],content)
     self.send(html,headers)

  # on envoie un contenu encodé en json
  def send_json(self,data,headers=[]):
    body = bytes(json.dumps(data),'utf-8') # encodage en json et UTF-8
    self.send_response(200)
    self.send_header('Content-Type','application/json')
    self.send_header('Content-Length',int(len(body)))
    [self.send_header(*t) for t in headers]
    self.end_headers()
    self.wfile.write(body) 

  # on envoie la réponse
  def send(self,body,headers=[]):
     encoded = bytes(body, 'UTF-8')

     self.send_response(200)

     [self.send_header(*t) for t in headers]
     self.send_header('Content-Length',int(len(encoded)))
     self.end_headers()

     self.wfile.write(encoded)


  # on analyse la requête pour initialiser nos paramètres
  def init_params(self):
    # analyse de l'adresse
    info = urlparse(self.path)
    self.path_info = info.path.split('/')[1:]
    self.query_string = info.query
    self.params = parse_qs(info.query)

    # récupération du corps
    length = self.headers.get('Content-Length')
    ctype = self.headers.get('Content-Type')
    if length:
      self.body = str(self.rfile.read(int(length)),'utf-8')
      if ctype == 'application/x-www-form-urlencoded' : 
        self.params = parse_qs(self.body)
    else:
      self.body = ''

    print(length,ctype,self.body, self.params)


# instanciation et lancement du serveur
<<<<<<< HEAD
httpd = socketserver.TCPServer(("", 8095), RequestHandler)
=======
httpd = socketserver.TCPServer(("", 8100), RequestHandler)
>>>>>>> origin/master
httpd.serve_forever()