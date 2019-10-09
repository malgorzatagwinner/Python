x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

    #TEN KOD JEST POPRAWNY

for i in "qwerty": if ord(i) < 100: print i

    #TEN KOD JEST NIEPOPRAWNY - warunek if nie może być w tej samej linijce co pętla 'for'

for i in "axby": print ord(i) if ord(i) < 100 else i
    #TEN KOD JEST POPRAWNY W PYTHONIE 2 ALE NIEPOPRAWNY W PYTHONIE 3 - musiały by być postawione nawiasy w następujący sposób:
    for i in "axby": print (ord(i) if ord(i) < 100 else i)
