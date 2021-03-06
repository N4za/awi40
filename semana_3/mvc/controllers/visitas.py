import web
from datetime import date 
from datetime import datetime 

class Visitas:
  def GET(self, nombre):
    try:
      cookie = web.cookies() 
      visitas = "0" 
      fecha = date.today() 
      now = datetime.now()
      format = now.strftime("Hora: %H, Minutos: %M, Segundos: %S")

      
      if nombre:
        web.setcookie("nombre", nombre, expires = "", domain=None)
      else:
        nombre = "Anonimo"
        web.setcookie("nombre", nombre, expires = "", domain=None) 

      if cookie.get("visitas"):
        visitas = int(cookie.get("visitas"))
        visitas += 1
        web.setcookie("visitas", str(visitas),expires = "",  domain = None)
      else:
        web.setcookie("visitas", str(1), expires = "", domain = None)
        visitas = "1"
        
      if cookie.get("fecha"):
        web.setcookie("fecha", fecha, expires="", domain=None)
      else:
        web.setcookie("fecha", fecha, expires="", domain=None)

      if cookie.get("Hora"):
        web.setcookie("Hora", format, expires="", domain=None)
      else:
        web.setcookie("Hora", format, expires="", domain=None)
      
      return "Numero de visitas: " + str(visitas) + "\nNombre: " + str(nombre) + "\nFecha actual: "+ str(fecha) + "\n" + str(format)
      print(cookie)
    
    except Exception as e:
      return "error "+str(e.args)