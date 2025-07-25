

# Drakos CLI - Commandes disponibles

| Commande      | Description                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------|
| `birth`       | Charge le dataset dans le cache                                                                          |
| `detect-lair` | Vérifie si le fichier de configuration existe                                                            |
| `first-fly`   | Affiche les statistiques de base du dataset                                                              |
| `inspect`     | Charge le dataset du cache et affiche les informations                                                    |
| `lair`        | Crée le fichier de configuration avec le chemin du projet dans `drk_stgs` (Drakos Settings)              |

---

## Description détaillée des commandes

### `birth`
Charge un dataset depuis un fichier CSV et le sauvegarde dans le cache pour une utilisation ultérieure.


### `detect-lair`
Vérifie la présence du fichier de configuration (`config.json`) dans le dossier `drk_stgs`.  
Utile pour s'assurer que la configuration est en place avant d'exécuter d'autres commandes.

### `first-fly`
Affiche les statistiques descriptives de base du dataset chargé en cache, incluant notamment la moyenne, l'écart-type, les valeurs minimales et maximales, etc.

### `inspect`
Permet d’afficher un aperçu des données stockées en cache.  
Par défaut, affiche les premières lignes (`head`) ou peut afficher les dernières (`tail`) selon l’argument passé.

### `lair`
Crée ou met à jour le fichier de configuration `config.json` contenant le chemin du projet, dans le dossier `drk_stgs`.  
Ce dossier `drk_stgs` signifie **Drakos Settings** et sert à centraliser les fichiers de configuration et cache.

---

Cette CLI est pensée pour faciliter la gestion et l'exploration rapide de datasets CSV dans un workflow structuré, tout en centralisant la configuration et le cache pour optimiser les opérations répétées.


