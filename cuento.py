def imprimir_cuento(opcion):
    """Imprime un cuento según la opción del usuario."""
    cuentos = {
        1: """Érase una vez un pequeño dragón llamado Draco que vivía en un valle escondido. 
Soñaba con volar más allá de las montañas y explorar mundos desconocidos. 
Cada día practicaba su vuelo y, poco a poco, sus alas se hicieron fuertes.""",
        
        2: """Había una niña curiosa llamada Lila que descubrió un bosque mágico detrás de su casa. 
En ese bosque los árboles hablaban y los animales ayudaban a quienes eran valientes y amables. 
Lila hizo amigos increíbles y aprendió lecciones que nunca olvidaría.""",
        
        3: """Un valiente ratón llamado Rafi decidió explorar el mundo más allá de la granja donde vivía. 
Se enfrentó a ríos caudalosos, gatos traviesos y caminos interminables. 
Pero con astucia y coraje, siempre encontraba la manera de seguir adelante y regresar a casa sano y salvo."""
        
        4: """Había una niña llamada Sofía que vivía cerca del mar en Panamá.
Cada día recogía conchas y soñaba con viajar más allá del horizonte.
Un día, el mar le trajo una botella con un mapa... y comenzó la mayor aventura de su vida..."""
    }
    
    print("\n--- CUENTO ---")
    print(cuentos[opcion])
    print("--- FIN DEL CUENTO ---\n")
