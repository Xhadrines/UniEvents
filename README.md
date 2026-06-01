# UniEvents

UniEvents este o platformă centralizată pentru gestionarea și descoperirea evenimentelor universitare organizate în cadrul facultății.

## Funcționalități principale:

### Utilizatori studenți

- Autentificare folosind Google OAuth (@student.usv.ro);
- Vizualizare evenimente în format listă și calendar interactiv;
- Filtrare și căutare evenimente după:
  - categorie;
  - locație;
  - organizator;
  - tip participare;
  - perioadă;
  - filtre suplimentare;
- Sortare evenimente;
- Combinare filtre folosind operatori AND și OR;
- Vizualizare detalii complete ale evenimentelor;
- Înscriere la evenimente;
- Listă de așteptare pentru evenimentele fără locuri disponibile;
- Anulare înscriere;
- Adăugare evenimente la favorite;
- Notificări și remindere pentru evenimente favorite;
- Export evenimente în Google Calendar și format .ics;
- Vizualizare și descărcare materiale publice;
- Oferire feedback și rating după finalizarea evenimentelor.

### Organizatori evenimente

- Creare, editare și ștergere evenimente;
- Gestionare sponsori și materiale pentru evenimente;
- Încărcare fișiere și materiale publice/private;
- Setare limite pentru numărul și dimensiunea fișierelor;
- Gestionare participanți și liste de înscrieri;
- Vizualizare feedback pentru evenimente;
- Configurare:
  - capacitate participanți;
  - deadline înscriere;
  - acces liber / înscriere / bilet.

### Administratori

- Gestionare utilizatori și profiluri;
- Gestionare organizatori;
- Validare și respingere evenimente;
- Panou CRUD pentru administrarea tuturor entităților;
- Gestionare notificări, categorii, locații și statusuri;
- Vizualizare evenimente aflate în așteptare.

## Scop

Scopul proiectului UniEvents este dezvoltarea unei platforme moderne pentru gestionarea și promovarea evenimentelor universitare, oferind un spațiu centralizat unde studenții pot descoperi rapid activități relevante, iar organizatorii și administratorii pot administra eficient evenimentele și participanții.

Platforma urmărește:

- digitalizarea procesului de organizare a evenimentelor universitare;
- centralizarea informațiilor despre evenimente;
- îmbunătățirea comunicării dintre studenți și organizatori;
- automatizarea proceselor de înscriere, validare și notificare;
- oferirea unei experiențe interactive și moderne pentru utilizatori.

## Tehnologii

- **Backend**: Django
- **Frontend**: React + TypeScript + Vite
- **Database:** SQLite

## Instalare

Urmează pașii de mai jos pentru a instala și configura proiectul.

1. Clonează repository-ul folosind comanda:

```bash
git clone https://github.com/Xhadrines/UniEvents.git
```

2. Pentru a configura backend-ul, accesează [backend/README.md](backend/README.md), unde vei găsi informațiile necesare.

3. Pentru a configura frontend-ul, accesează [frontend/README.md](frontend/README.md), unde vei găsi informațiile necesare.

4. Construiește imaginile Docker folosind comanda:

```bash
docker compose build
```

5. Pornește containerele folosind comanda:

```bash
docker compose up
```

_EXTRA: Opreste containerele folosind comanda:_

```bash
docker compose down
```

## Alte informații

**Documentație:** WIP
