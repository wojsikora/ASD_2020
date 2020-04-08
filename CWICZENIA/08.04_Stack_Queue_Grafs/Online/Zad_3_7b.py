""" 
Mówimy,  że  wierzchołek t w  grafie  skierowanym  jest  uniwersalnym ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź wychodząca z t. Proszę podać algorytm znajdujący ujście (jeśli istnieje) przy reprezentacji macierzowej grafu.
 """

""" 
Szukam podejrzanego wierzchołku DFSem w nast sposób:
1) Zwykły DFS, ale przed tym jak się cofnąć dodaje do ostatniego elementu +1 do jakiegos .odw
2) Mam zawsze na tym elemencie konczyc rekurencje, jak .odw tego elementu (ostatniego) będzie się równać ilości wywołanych rekurencji, to:
    1) Sprawdzam warunki na ujście dla tego el
Jak nie, to:
    1) return false

 """