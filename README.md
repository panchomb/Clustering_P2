# Proyecto de Clustering - Machine Learning (CS3061)

Este proyecto explora técnicas de agrupamiento aplicadas al reconocimiento de acciones humanas en videos, utilizando métodos de reducción de dimensionalidad y algoritmos de clustering.

## 📊 Metodología
1. **Extracción de características** con *R(2+1)D* (modelo preentrenado).
2. **Reducción de dimensionalidad** con *UMAP* y *t-SNE* para visualización.
3. **Agrupamiento** con *K-means++* y *DBSCAN*.
4. **Evaluación** con métricas como *Silhouette Score*, *Rand Index* e *Información Mutua*.

## 🔬 Resultados
- *UMAP* ofrece mejor separación de clusters que *t-SNE*.
- *K-means++* funciona mejor con *k=9* (debido a similitudes semánticas en clases).
- *DBSCAN* es menos efectivo en datos con variabilidad en densidad.
- Mejor combinación: *UMAP + K-means++*.

## 👥 Contribuciones
- **Jean Pier Angeles**: Desarrollo teórico.
- **Francisco Calle**: Extracción de características y modelos *DBSCAN* y *K-means++*.
- **Francisco Magot**: Extracción y experimentación de modelos.