# Download-Manga-TuMangaOnline.
Descarga capitulos de TuMangaOnline.

# Requisitos necesarios.
Usar pip3 install -r REQUIREMENTS.txt.

O instalar:

* beautifulsoup4==4.9.3
* bs4==0.0.1
* certifi==2020.12.5
* chardet==3.0.4
* idna==2.8
* lxml==4.5.0
* playsound==1.2.2
* PyQt5==5.15.1
* PyQt5-sip==12.8.1
* requests==2.22.0
* soupsieve==2.2
* urllib3==1.25.11

# Descargar todos los capitulos.
Para esto solo es necesario poner un rango mayor que los capitulos existentes, una vez no haya capitulos para descargar, el programa se detendra.

# Modificar fondo.
Es posible modificar el fondo, para ello se necesita seguir estos pasos.

* Sobreescribir (mismo nombre) la imagen en la carpeta *imgs* (el tamaño debe ser 611x411).
* Eliminar el archivo *source_rc.py*.
* Abrir una terminal (o cmd) y ejecutar *pyrcc5 source.qrc -o source_rc.py*.

# Modificar estilos.
Accediendo al archivo *style.css* podemos cambiar cada parte del diseño actual del programa.

# Modificando sonido final.
Pasos a seguir:

* Sobreescribir (mismo nombre) el fichero *finish-him.mp3* (tiene que ser el mismo formato).
