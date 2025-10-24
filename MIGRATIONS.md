# Guide des Migrations avec Alembic

## Configuration

Alembic est configuré pour gérer les migrations de base de données du projet SOUTOURA_KS.

## Commandes Principales

### 1. Initialiser Alembic (déjà fait)
\`\`\`bash
alembic init alembic
\`\`\`

### 2. Créer une nouvelle migration
\`\`\`bash
# Génération automatique basée sur les changements de modèles
alembic revision --autogenerate -m "description de la migration"

# Exemples:
alembic revision --autogenerate -m "create products table"
alembic revision --autogenerate -m "add status field to orders"
alembic revision --autogenerate -m "create order_items table"
\`\`\`

### 3. Appliquer les migrations
\`\`\`bash
# Appliquer toutes les migrations en attente
alembic upgrade head

# Appliquer une migration spécifique
alembic upgrade <revision_id>

# Avancer d'une migration
alembic upgrade +1
\`\`\`

### 4. Revenir en arrière (rollback)
\`\`\`bash
# Revenir à la migration précédente
alembic downgrade -1

# Revenir à une migration spécifique
alembic downgrade <revision_id>

# Revenir au début (supprimer toutes les migrations)
alembic downgrade base
\`\`\`

### 5. Voir l'historique des migrations
\`\`\`bash
# Voir l'historique complet
alembic history

# Voir la migration actuelle
alembic current

# Voir les migrations en attente
alembic heads
\`\`\`

## Workflow Typique

### Ajouter un nouveau champ à un modèle

1. Modifier le modèle dans `backend/models/`
\`\`\`python
# backend/models/product.py
class Product(Base):
    __tablename__ = "products"
    # ... existing fields ...
    discount = Column(Float, default=0.0)  # Nouveau champ
\`\`\`

2. Générer la migration
\`\`\`bash
alembic revision --autogenerate -m "add discount field to products"
\`\`\`

3. Vérifier le fichier de migration généré dans `backend/alembic/versions/`

4. Appliquer la migration
\`\`\`bash
alembic upgrade head
\`\`\`

### Créer une nouvelle table

1. Créer le modèle dans `backend/models/`
\`\`\`python
# backend/models/category.py
from backend.database import Base
from sqlalchemy import Column, Integer, String

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
\`\`\`

2. Importer le modèle dans `backend/alembic/env.py`
\`\`\`python
from backend.models.category import Category
\`\`\`

3. Générer et appliquer la migration
\`\`\`bash
alembic revision --autogenerate -m "create categories table"
alembic upgrade head
\`\`\`

## Bonnes Pratiques

1. **Toujours vérifier** les migrations générées automatiquement avant de les appliquer
2. **Tester** les migrations sur un environnement de développement avant la production
3. **Sauvegarder** la base de données avant d'appliquer des migrations en production
4. **Commiter** les fichiers de migration dans le contrôle de version
5. **Ne jamais modifier** une migration déjà appliquée en production

## Structure des Fichiers

\`\`\`
backend/
├── alembic/
│   ├── versions/          # Fichiers de migration
│   ├── env.py            # Configuration de l'environnement
│   └── script.py.mako    # Template pour les migrations
├── alembic.ini           # Configuration Alembic
└── models/               # Modèles SQLAlchemy
\`\`\`

## Dépannage

### Erreur: "Can't locate revision identified by..."
\`\`\`bash
# Réinitialiser l'historique des migrations
alembic stamp head
\`\`\`

### Conflit de migration
\`\`\`bash
# Voir les branches
alembic branches

# Fusionner les branches
alembic merge -m "merge branches" <rev1> <rev2>
\`\`\`

### Base de données désynchronisée
\`\`\`bash
# Marquer la base comme étant à jour sans appliquer les migrations
alembic stamp head
