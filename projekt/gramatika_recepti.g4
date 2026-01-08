grammar gramatika_recepti;

ulaz: pozdrav EOF | sastojciInput EOF | zahtjevRecept EOF | pomoc EOF | izlaz EOF;

pozdrav: POZDRAV INTERPUNKCIJA?;

sastojciInput: (IMAM | SASTOJCI) DVOTOCKA? listaSastojaka INTERPUNKCIJA?;

listaSastojaka: SASTOJAK ( (I | ZAREZ) SASTOJAK )*;

zahtjevRecept : (DAJ | PREDLOZI) MI? RECEPT (S | OD)? listaSastojaka? INTERPUNKCIJA?
                | STO MOGU (KUHATI | SKUHATI) (S | OD)? listaSastojaka? INTERPUNKCIJA?;

pomoc: POMOC INTERPUNKCIJA?;

izlaz: (IZLAZ | DOVIDJENJA) INTERPUNKCIJA?;

POZDRAV: 'pozdrav' | 'bok' | 'hej';

IMAM        : 'imam' ;
SASTOJCI : 'sastojci' ;
POMOC       : 'pomoc' ;

DAJ      : 'daj' ;
PREDLOZI : 'predlozi' ;
MI       : 'mi' ;
RECEPT   : 'recept' ;

STO     : 'sto';
MOGU    : 'mogu' ;
KUHATI  : 'kuhati' ;
SKUHATI : 'skuhati' ;

S  : 's' ;
OD : 'od' ;

I     : 'i' ;
ZAREZ : ',' ;

DVOTOCKA : ':' ;

INTERPUNKCIJA : [.!?]+ ;

SASTOJAK: 'jaja' | 'sir' | 'mlijeko' | 'krumpir' | 'piletina' | 'tjestenina' | 'riza' | 'luk'
    | 'rajcica' | 'kvasac' | 'secer' | 'brasno' | 'sol' | 'ulje' | 'maslac' | 'margarin' 
    | 'mljeveno meso' | 'parmezan' | 'prsut' | 'vegeta' | 'cesnjak' | 'krusne mrvice'
    | 'voda' | 'hrenovke' | 'secerac' | 'paprika' | 'limun' | 'umak od soje' | 'papar'
    | 'sezam' | 'tuna' | 'kiselo vrhnje' | 'senf' | 'masline' | 'sunka' | 'persin'
    | 'kupus' | 'mrkva' | 'dumbir' | 'svjezi sir' | 'tortilje' | 'zelena salata' | 'majoneza'
    | 'tikvice' | 'grah' | 'umak od rajcice' | 'origano' | 'vrhnje za kuhanje' | 'avokado'; 

IZLAZ      : 'izlaz' ;
DOVIDJENJA : 'dovidenja' ;

WS : [ \t\r\n]+ -> skip ;