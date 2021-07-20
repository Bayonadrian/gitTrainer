En este paso te voy a enseñar a usar gitHub, git y github parecen lo mismo pero no lo son, git es un versionador, que inicialmente es local, mientras que github es un repositorio en la nube, para crear una cuenta y crear tu primer repositorio te recmiendo iniciar con el. Para poder subir tu repositorio en local a github, usa el formato:

- git remote add origin <url>

El lugar de <url>, emplea el url del repositorio brindado por github. Una vez esto hecho si empleas el comando:

- git remote

Recibes origin como respuesta, lo cual hace referencia a tu repositorio local, luego de esto puedes emplear el comando:

- git remote -v

Lo cual te retornara:

- origin <url> (fetch)
- origin <url> (push)

Lo cual significa que puedes traer informacion de github mediante "fetch" o llevar informacion a github mediante "push". Otro comando bastante util y mas usado que "fetch" es el comando "pull", el cual se usa de la siguiente forma:

- git pull origin master

En caso de devolver un mensaje diciendo "fatal: refusing to merge unrelated stories"(esto indica que hay dos tipos de informacion diferentes entre el repositorio local y el repositorio de github), emplea el comando:

- git pull origin master --allow-unrelated-stories

Para llevar informacion al repositorio de github te recomiendo emplear el comando:

- git push origin master

Nota: En este inicio rapido no te mostrare como generar llaves SSH pero te recomiendo ver ese tema para mejorar la seguridad de tu proyecto.

