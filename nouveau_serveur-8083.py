# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:29:57 2017

@author: Caro
"""

import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
# définition du nouveau handler
class RequestHandler(http.server.SimpleHTTPRequestHandler):
# sous-répertoire racine des documents statiques
  static_dir= '/client'
  

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
    
    
  def send(self,body):
    # on encode la chaine de caractères à envoyer
    
    # on envoie la ligne de statut
    self.send_response(200)
    # on envoie les lignes d'entête et la ligne vide
    self.end_headers()
    encoded = bytes(body, 'UTF-8')
    # on envoie le corps de la réponse
    self.wfile.write(encoded)
    
# on surcharge la méthode qui traite les requêtes GET
  def do_GET(self):
# on modifie le chemin d'accès en insérant un répertoire préfixe
      #self.path = self.static_dir + self.path
# on traite la requête via la classe parent
      #http.server.SimpleHTTPRequestHandler.do_GET(self)
      
      if self.path[0:8] == "/service":
          self.init_params()
          response= '<!DOCTYPE html><title>hello</title>' + \'<meta charset="utf-8"><p>Bonjour {} {}</p>' \.format(self.params['Prenom'],self.params['Nom'])
          self.send(response)
# on traite le retour de formulaire
     
# on traite la requête vers un document statique
      
      
      
# instanciation et lancement du serveur
httpd = socketserver.TCPServer(("", 8083), RequestHandler)
httpd.serve_forever()