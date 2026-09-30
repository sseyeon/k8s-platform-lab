# Kubernetes Platform Lab

Python/FastAPI 애플리케이션을 기반으로 Kubernetes 환경에서
CI/CD, 모니터링 및 장애 대응 과정을 실습하는 프로젝트입니다.

## Project Goal

- FastAPI 애플리케이션 컨테이너화
- Kubernetes 기반 애플리케이션 배포
- Jenkins 기반 CI/CD Pipeline 구축
- Prometheus / Grafana 모니터링
- Kubernetes 장애 상황 재현 및 분석

## Tech Stack

- Python
- FastAPI
- Docker
- Jenkins
- Kubernetes
- Prometheus
- Grafana

## API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | 애플리케이션 상태 |
| GET | `/api/info` | 애플리케이션 정보 |
| GET | `/health/live` | Liveness Check |
| GET | `/health/ready` | Readiness Check |

## Local Development

### 1. Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
``` 

### 2. Install Dependencies
```bash
pip install -r requirements.txt
``` 


### 3. Run Application
```bash
uvicorn app.main:app --reload
``` 

Application:
http://localhost:8000

Swagger:
http://localhost:8000/docs

### 4. Test
```bash
pytest
```

