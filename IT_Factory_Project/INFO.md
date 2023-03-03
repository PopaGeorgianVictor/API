
## Detalii API testat

API-ul testat este unul public (denumit și deschis) care poate fi accesat și folosit în mod liber de oriunde.
Un API deschis poartă denumirea de  <strong><i>Web Services</i></strong>.



### Tipuri de API

 <strong>SOAP</strong> - Simple Object Access Protocol 
 
 <strong>REST</strong> - Representational State Transfer
 
<strong><i> ! ambele sunt servicii web atâta timp cât sunt publice !  </strong></i> 

În cadrul proiectului s-a folosit REST (acesta a fost conceput special pentru a lucra cu componente media, fișiere. Orice serviciu web care este definit pe principiile REST poate fi numit <strong><i>RestFul</i></strong>. Acesta folosește metodele http precum  <strong><i>GET,PUT,POST,DELETE</i></strong> pentru a interacționa cu componentele.

Pentru a se folosi metodele http s-a construit un <strong><i>URL(Uniform Resource Locator)</i></strong> format dintr-un <strong><i>HOST</i></strong>  și un <strong><i>PATH</i></strong> :


<strong>HOST:</strong>

      https://reqres.in

<strong>PATH:</strong> 

<i>GET:

      /api/users?page={page_number}

PUT: 
 
     /api/users/{id}
 
POST: 
 
    /api/users
    /api/register
    /api/login
 
DELETE:
 
    /api/users/{id}

</i>
 

 
 ## Detalii rulare proiect  <img src = "https://media.tenor.com/cBA9HTwt38QAAAAM/work-in.gif" width = "5%"> 
 
 Proiectul poate fi rulat folosind fie fișierul <strong><i>all_tests.py</strong></i> (pentru a rula toate testele odată) sau individual folosind celelalte fișiere <strong><i>get.py, post.py, put.py,delete.py</i></strong>
   
 Putem să folosim pictograma ▶️ din dreptul clasei create pentru a rula întreaga colecție de teste din aceea clasă sau rulăm individul fiecare test folosind acceiași pictogramă din dreptul testului respectiv.
 
 <img src = "https://i.postimg.cc/MHQNg7g2/run.png" width = "80%"> 
 
 <img src = "https://i.postimg.cc/j2k7GN0T/alltest.png" width = "80%"> 
 
 Desigur libraria pytest ne stă la dispoziție : <strong><i>pip install pytest</strong></i>
 
 Cu ajutorul unui terminal scriem comanda : <strong><i>pytest nume_test.py</strong></i> 
 
 <strong><i> ! comanda pytest va executa toate fișierele de format test_* sau *_test din directorul și subdirectoarele curente!  </strong></i> 
 
  <img src = "https://i.postimg.cc/sg4L7Dpz/delete.png" width = "80%"> 
 
