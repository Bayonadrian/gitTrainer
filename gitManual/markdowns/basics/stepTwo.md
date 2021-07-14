Una vez tengas el repositorio inicializado, emplea el comando:

- git status

Este comando te retornara el status del repositorio.

Luego puedes emplear el comando:

- git add <file>

para poder añadir documentos a tu repositorio, en el lugar de <file> debes poner el nombre del documento que desees añadir o en caso de que desees añadir todos los documentos de la carpeta, puedes emplear un ., de la siguiente forma:

- git add .

En este punto puedes volver a usar el comando:

- git status

Este te dira el status del proceso, ahora no debes olvidar comentar este cambio para poder hacerlo efectivo, con el comando:

- git commit -m <commend>

En lugar de <commend> debes registrar un comentario, jamas envies un commit sin un comentario. Una vez mas puedes ver el status:

- git status

Si se guardaron cambios te dara un resultado como este:

- "nothing to commit, working tree clean"

Hasta aqui ya aprendiste a guardar documentos en un repositorio de git.

-> Continua en /stepTree(show, log, diff)