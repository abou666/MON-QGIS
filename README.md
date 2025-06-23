# SIGLibre

Application SIG libre et modulaire (bureau + serveur), inspirée de QGIS.

## Fonctionnalités (MVP)
- Application de bureau Qt (chargement shapefile)
- Backend Flask prêt à connecter à PostGIS
- Architecture modulaire (plugins)
- Licence open source (GPLv3)

## Roadmap

### v0.1 - Prototype local
- [x] Interface Qt minimaliste
- [x] Upload de Shapefile
- [ ] Table attributaire simple

### v0.2 - SIG backend
- [ ] API REST avec FastAPI/Flask
- [ ] Connexion PostGIS

### v0.3 - SIG Web (optionnel)
- [ ] Visualisation Leaflet/OpenLayers
