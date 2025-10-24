# SOUTOURA_KS Backend API

Backend API construit avec FastAPI pour la plateforme e-commerce SOUTOURA_KS.

## 🏗️ Architecture

Le backend suit l'architecture MVC avec séparation claire des responsabilités :

- **Models** : Modèles SQLAlchemy pour la base de données
- **Schemas** : Schémas Pydantic pour validation des données
- **Routers** : Routes API avec logique métier

## 📁 Structure du Projet

\`\`\`
backend/
├── main.py              # Point d'entrée FastAPI
├── database.py          # Configuration base de données
├── models/              # Modèles SQLAlchemy
│   ├── __init__.py
│   ├── product.py      # Modèle Produit
│   └── order.py        # Modèles Commande et OrderItem
├── schemas/             # Schémas Pydantic
│   ├── __init__.py
│   ├── product.py      # Schémas Produit
│   ├── order.py        # Schémas Commande
│   └── auth.py         # Schémas Auth
├── routers/             # Routes API
│   ├── products.py     # CRUD Produits
│   ├── orders.py       # Gestion Commandes
│   ├── auth.py         # Authentification
│   └── upload.py       # Upload Images
├── requirements.txt     # Dépendances Python
└── .env.example        # Template variables d'environnement
\`\`\`

## 🚀 Installation

1. **Créer un environnement virtuel**
\`\`\`bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
\`\`\`

2. **Installer les dépendances**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. **Configurer les variables d'environnement**
\`\`\`bash
cp .env.example .env
# Éditer .env avec vos configurations
\`\`\`

Variables requises :
- `DATABASE_URL` : URL de connexion PostgreSQL (Neon)
- `BREVO_API_KEY` : Clé API Brevo pour l'envoi d'emails

4. **Démarrer le serveur**
\`\`\`bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
\`\`\`

Le serveur sera accessible sur `http://localhost:8000`

## 📚 Documentation API

Une fois le serveur démarré, accédez à :
- **Swagger UI** : http://localhost:8000/docs
- **ReDoc** : http://localhost:8000/redoc

## 🔌 Endpoints Principaux

### Produits
- `GET /api/products` - Liste des produits (avec filtres optionnels)
- `GET /api/products/{id}` - Détails d'un produit
- `POST /api/products` - Créer un produit
- `PUT /api/products/{id}` - Mettre à jour un produit
- `DELETE /api/products/{id}` - Supprimer un produit

### Commandes
- `GET /api/orders` - Liste des commandes
- `GET /api/orders/{id}` - Détails d'une commande
- `POST /api/orders` - Créer une commande (+ envoi email)
- `PATCH /api/orders/{id}` - Mettre à jour le statut

### Authentification
- `POST /api/auth/login` - Connexion admin

### Upload
- `POST /api/upload` - Upload d'images (conversion base64)

## 🗄️ Base de Données

Le backend utilise PostgreSQL via Neon avec SQLAlchemy comme ORM.

### Tables
- **products** : Produits avec images (JSON array)
- **orders** : Commandes clients
- **order_items** : Articles de chaque commande

## 📧 Envoi d'Emails

Les emails sont envoyés automatiquement via l'API Brevo lors de la création d'une commande. L'email contient :
- Informations client
- Détails de la commande
- Tableau des articles
- Montant total
- Mode de paiement

## 🔐 Authentification

L'authentification admin utilise des identifiants hardcodés :
- **Email** : test@gmail.com
- **Password** : Test

## 🛠️ Technologies

- **FastAPI** : Framework web moderne et rapide
- **SQLAlchemy** : ORM pour PostgreSQL
- **Pydantic** : Validation de données
- **Uvicorn** : Serveur ASGI
- **psycopg2-binary** : Driver PostgreSQL
- **python-multipart** : Support upload de fichiers
- **requests** : Client HTTP pour Brevo API

## 🔄 Communication avec le Frontend

Le backend expose une API REST consommée par le frontend Next.js. CORS est configuré pour accepter les requêtes depuis `http://localhost:3000`.

## 📝 Notes de Développement

- Les images sont stockées en base64 dans la base de données
- Les commandes déclenchent automatiquement l'envoi d'un email au propriétaire
- Le filtrage des produits supporte la recherche par nom/description et catégorie
- Tous les endpoints sont documentés automatiquement via FastAPI
