FROM python:3.9-slim-bullseye AS build
# Make sure we use the virtualenv:
ENV PATH="/app/venv/bin:$PATH" APP_ENV="development" SUPABASE_URL="" SUPABASE_API_KEY="" SUPABASE_TABLE=""

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc make


WORKDIR /app
COPY . .
RUN make linux_venv

RUN pip install --upgrade pip
COPY requirements.txt .
RUN make install


FROM python:3.9-slim-bullseye AS compile
FROM build
ENV PATH=${PATH} APP_ENV=${APP_ENV} SUPABASE_URL=${SUPABASE_URL} SUPABASE_API_KEY=${SUPABASE_API_KEY} SUPABASE_TABLE=${SUPABASE_TABLE}

WORKDIR /app
COPY --from=build /app/venv /app/venv

COPY . .

CMD ["python3","/app/app.py"]





