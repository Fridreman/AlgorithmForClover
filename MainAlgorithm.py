# File to make functions:
# initData(q, a1, a2, a2): void
# algorithmSelection(): void #функция выбирает нужный алгоритм и вызывает
# после формирования данных из файла HttpRequests будет вызвана функция инициализации данных(initData),
# после вызывается algoritmSelection(), который в свою очередь вызывет нужный алгоритм из файла Algorithms.
# пока алгоритмов нету, соотвественно выбора нету, а значит и выбирать нечего, значит просто вызывает "существующий"
# алгоритм из файла Algorithms

# Рома, Желательно сделать функцию initDataTest() в которой просто вручную проинициализируй какие нибудь данные, чтобы
# было что послать в алгоритм для разработки и отладки его.