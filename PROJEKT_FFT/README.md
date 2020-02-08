Małgorzata Gwinner  |      FFT W JĘZYKU PYTHON       |    Kraków, 21.01.2020 r.
===============================================================================

* Zawartosc:
============
Katalog PROJEKT_FFT zawiera poniższe programy i funkcje:
  I. fft.py
  II. poly.py
  III. numpy_fft.py
  IV. porownanie.py

-------------------------------------------------------------------------------
  
 I. Plik fft.py
 ===============
	Plik fft.py jest implementacją algorytmu Szybkiej Transformaty Fouriera
	(FFT) opisanej w książce "Wprowadzenie do algorytmów" autorstwa
	Cormen Thomas H., Leiserson Charles E., Rivest Ronald L, Clifford Stein.

	Szybka Transformata Fouriera zmniejsza czas mnożenia wielomianów z O(n^2)
	do O(n logn).

	Szybka Transformata Fouriera działa według schematu:
	1. Podwojenie ograniczenia stopnia: rozszerzenie reprezentacji przez
	współczynniki wielomianów do ograniczenia stopnia 2n, dodając do każdej
	zerowych współczynników przy najwyższych potęgach x)

	2. Ewaluacja: Obliczenie reprezentacji przez wartości w punktach,
	stosując dwukrotnie FFT rzędu 2n.

	3. Mnożenie po współrzędnych: Obliczenie reprezentacji przez wartości
	w punktach wielomianu, wymnażając odpowiadające sobie wartości.

	4. Interpolacja: Utworzenie reprezentacji przez współczynniki

	Kroki 1 i 3 realizuje się w czasie O(n), a 2 i 4 w czasie O(n logn),
	dając temu algorytmowi złożoność O(n logn).

-------------------------------------------------------------------------------

 II. Plik poly.py
 =================
	Plik poly.py zawiera implementację wielomianów oraz wszystkich
	najprostszych operacji matematycznych na nich wykonywanych,
	tj. dodawanie, odejmowanie, mnożenie, dzielenie, etc.
	Jest nam potrzebny ze względu na operację mnożenia.

-------------------------------------------------------------------------------

 III. Plik numpy_fft.py
 ======================
 	Plik numpy.py zawiera operację mnożenia wielomianów za pomocą
	wbudowanej funkcji fft() należącej do modułu numpy.

 IV. Plik porownanie.py 
 ========================
 	Plik porownanie.py pokazuje porównanie szybkości działania trzech
	algorytmów - FFT, "tradycyjnego" mnożenia oraz fft wbudowanego
	do modułu numpy. Można w nim ustalić ilość współczynników wielomianu,
	dla jakiej chcielibyśmy przeanalizować szybkość działania wszystkich
	sposobów mnożenia.

	

* Jak uruchomić program:
=========================

Do uruchomienia programu potrzebne jest posiadanie zainstalowanego Pythona
wersji 3.

Aby uruchomić porównanie wszystkich analizowanych sposobów mnożenia, należy
wykonać komendę:
	python3 porownanie.py

* Wyniki uruchomienia programu:
===============================

Po uruchomieniu programu, jako pierwsza wyświetla się informacja o ustalonym
rozmiarze tabel współczynników (obie tabele są takiego rozmiaru).

Jako drugi, wyświetlany jest czas mnożenia wykonywanego w pliku fft.py.

W trzeciej linijce, wyświetlany jest czas mnożenia wykonywanego w pliku poly.py.

W czwartej linijce, wyświetlany jest wynik sprawdzenia, czy powyższe sposoby
mnożenia dały ten sam wynik.

W piątej linijce, wyświetlany jest czas mnożenia wykonywanego w pliku
numpy_fft.py.

W ostatniej linijce, raz jeszcze jest sprawdzana zgodność wyników działania
mnożenia, tym razem pomiędzy mnożeniem za pomocą Szybkiej Transformaty Fouriera
z pliku fft.py, a mnożeniem wykonywanym w pliku numpy_fft.py.

* Wnioski:
==========
Ze wszystkich z analizowanych sposobów, najszybszym jest mnożenie wbudowane
do modułu numpy. Dzieje się tak, gdyż jest interpretowane jako biblioteka
języka C.
Jednakże, widać też, że Szybka Transformata Fouriera jest znacznie szybsza
od tradycyjnej metody mnożenia. Dlatego jest ona wykorzystywana przy wszelkich
rozbudowanych problemach, w których ważna jest szybkość działania nawet
najprostszych operacji matematycznych.
NUMPY PORÓWNAĆ Z FFT Z NUMPY'A I PRZEDSTAWIĆ LISTĘ WSPÓŁCZYNNIKÓW JAKO NUMPY
