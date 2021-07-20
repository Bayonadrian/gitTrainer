En este paso te mostrare a crear ramas dentro de git, normalmente cuando trabajas con otros programadores necesitas hacerlo en linea, mediante el repositorio de github y mediante ramas para que cada desarrollador pueda trabajar en su propia rama sin alterar constantemente la rama principal y por lo tanto el proyecto completo. Las ramas se crean mediante el comando:

- git branch <name>

En el espacio de "name" debe entrar el nombre de tu rama. Posteriormente si deseas emplear esta rama debes usar el comando:

- git checkout <name>

Una vez mas en el espacio "name", se debe emplear el nombre de la rama. Si quieres ver en que rama te encuentras, puedes emplear el comando:

- git branch

Si deseas unir llevar el contenido de las ramas a la rama master debes emplear el comando:

- git merge <branch>

Empleando el nombre de la rama en lugar de <branch>, de este modo lo recomendado es jalar la informacion de la otra rama dentro de la rama "master", de este modo lo recomendado es seguir estos pasos:

- git checkout master

Entonces dentro de la rama "master" hacer lo siguiente:

- git merge <branch>

Si el procedimiento fuese al reves, dentro de la rama <branch>, jalando informacion de la rama "master", entonces se dejaria del lado la rama "master".

-> Continua en /stepSix(remote, push, pull)