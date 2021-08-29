# Spark 
Instalación, configuración y ejecución de proyectos con Apache Spark

### Preparación del entorno de trabajo
Para trabajar con Spark, necesitamos instalar los siguientes programas:

Desde Ubuntu:
  ```
  sudo add-apt-repository ppa:openjdk-r/ppa
  sudo apt-get -y update
  sudo apt-get -y upgrade
  sudo apt-get -y install openjdk-8-
  sudo apt-get -y install python3
  sudo apt-get -y install scala
  sudo apt-get -y install python3-pip
  
  sudo pip3 install py4j  
  ```
Vamos a la página de Spark https://spark.apache.org/downloads.html e instalamos los programas que necesitamos (Spark y Hadoop)
  
Una vez descargados los archivos, vamos a la carpeta de descargas desde la termina y usamos el siguiente comando para descomprimir los archivos:
  
```
  tar -xvf spark-3.1.2-bin-hadoop3.2.tgz  
```
  
Cambiamos el nombre del archivo, lo enviamos a la ruta principal y eliminamos el archivo comprimido

```
  mv spark-3.1.2-bin-hadoop3.2 spark
  mv spark ~/
  rm spark-3.1.2-bin-hadoop3.2.tgz
```
  
Instalamos Anaconda en nuestro entorno Linux y la exportamos como variable de entorno
  
```
  wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh  
  sh Anaconda3-2020.02-Linux-x86_64.sh -b
  export PATH=/home/user/anaconda3/bin:$PATH
```
