
NOTA: Antes de correr el código, asegúrese de tener instalado Python en su equipo y la librería PyGame.
Para instalar la libreria, abra un comando del sistema: CMD y digite el comando -pip install pygame

-El juego es un juego de memoria en el que el objetivo es encontrar todas las parejas de cartas idénticas. El juego presenta una cuadrícula de cartas boca abajo y el jugador debe voltearlas de a pares, tratando de recordar la ubicación de cada carta para encontrar sus parejas correspondientes.

-Al inicio del juego, se generan cartas aleatorias y se distribuyen en la cuadrícula. Cada carta tiene una imagen asociada. El número de filas y columnas en la cuadrícula puede ser configurado.

-El jugador puede voltear las cartas haciendo clic en ellas con el mouse. Si dos cartas volteadas coinciden, se mantienen boca arriba y se consideran una pareja encontrada. En caso de que las cartas no coincidan, se voltean de nuevo boca abajo después de un breve período de tiempo, permitiendo al jugador recordar su ubicación para futuros intentos.

-El juego lleva un registro del número de coincidencias encontradas y de los errores cometidos por el jugador. El tiempo transcurrido desde el inicio del juego también se muestra en la pantalla.

-El juego continúa hasta que todas las parejas de cartas hayan sido encontradas. En ese momento, se muestra un mensaje de felicitación junto con el tiempo transcurrido y el número de errores cometidos. El jugador puede cerrar la ventana del juego para finalizarlo.
