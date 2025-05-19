# Titanic túlélés előrejelző rendszer

Ez a projekt a Titanic adathalmazon alapuló gépi tanulási rendszert valósít meg, amely előrejelzi az utasok túlélési esélyeit. A rendszer különböző komponensekből épül fel, melyek konténerekben futnak és egy `docker-compose.yml` segítségével könnyen indíthatók.

## Projekt komponensek

### 1. Flask REST API + MLflow
- **REST API**: Lehetőséget biztosít a modell tanítására és az utasok túlélésének predikciójára.
- **MLflow**: Nyomon követi a tanítási folyamatokat és a predikciókat, beleértve a metrikákat és modelleket.

### 2. Apache Airflow
- Lehetőséget biztosít előre ütemezetten vagy manuálisan a modell újratanítására.

### 3. Streamlit + Evidently
- **Streamlit** egy webes dashboard, amely vizualizálja a **Data Drift**-et.
- **Evidently** segítségével az adatok változásai és eltérései könnyen követhetők.

---

## Docker konténerek

A projekt 3 külön konténerre van osztva:

| Konténer neve            | Tartalma                            |
|--------------------------|-------------------------------------|
| `flask_mlflow_container` | Flask REST API + MLflow             |
| `airflow_container`      | Apache Airflow                      |
| `evidently_container`    | Streamlit dashboard + Evidently     |

---

## Indítás

A rendszer indításához használd az alábbi parancsot a projekt gyökérkönyvtárában:

```bash
docker compose up --build -d
```

Ez a parancs felépíti a konténereket és elindítja az összes szolgáltatást a háttérben

## Elérhető Szolgáltatások

- **REST API**        http://localhost:8081
- **MlFlow UI**       http://localhost:5102
- **Airflow UI**      http://localhost:808
- **Streamlit UI**    http://localhost:8501
