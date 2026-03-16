# Frontend

Aceasta este **partea de frontend** a aplicației, construită folosind framework-ul **React + TypeScript + Vite**.

## Cerințe

Pentru a rula aplicația, trebuie să ai instalat:

- **Node.js** (v25.7.0 sau o versiune mai mare)
- **npm** (v11.11.1 sau o versiune mai mare)

## Instalare

1. Asigură-te că te afli în directorul `frontend`

2. Creează un fișier `.env` și adaugă următoarea linie:

```bash
VITE_CHAT_API=http://<IP_BACKEND>:<PORT_BACKEND>
```

_Note: Înlocuiește `<IP_BACKEND>` și `<PORT_BACKEND>` cu valorile corespunzătoare pe care le obții de la backend._

### Optional: rularea fără Docker

1. Instalează dependențele folosind comanda:

```bash
npm install
```

2. Rulează proiectul folosind comanda:

```bash
npm run dev
```
