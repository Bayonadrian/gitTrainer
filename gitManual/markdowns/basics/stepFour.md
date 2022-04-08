En este paso te enseñare como regresar al pasado, esto se da mediante el comando:

- <code>git reset --hard </code>
- <code>git reset --soft </code>

Este comando emplea el codigo del commit que te da el comando "git log" en lugar de "code" y tambien emplea una opcion la cual puede ser "hard" o "soft", hard es mucho mas agresivo y elimina tambien los cambios que puedan estar dentro de "add", por eso te recomiendo emplearlo solo en el caso de querer regresar al pasado ya que tambien este comando elimirara, todos los commits hechos.

Otro comando a emplear para poder ver commits del pasado es el comando:

- <code> git checkout </code>

Donde se emplea el codigo de "git log" en el lugar de las otras opciones, siendo asi este comando muestra el como se encontraba el proyecto en ese "commit", hay que tener bastante cuidado ya que si en ese momento se da un "commit" se perderian los nuevos cambios, por ultimo si deseas volver a como estaba todo antes del "checkout" emplea el comando:

- git checkout master

De este modo puedes "volver al presente".

-> Continua en /stepFive(branch, checkout, merge)