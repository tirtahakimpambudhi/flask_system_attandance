FROM python:3.10.12-slim-bullseye AS build

# Make sure we use the virtualenv:
ENV PATH="/app/venv/bin:$PATH" \
    APP_ENV="testing" \
    SECRET_KEY="flask_system_attendance" \
    SUPABASE_API_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im14cnpxcWJzbmp5dGd4end4bHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM3NTI1NDgsImV4cCI6MjAyOTMyODU0OH0.xv3Ciws_StrFit7-_QwSfbjK6R5pnPrOfYeV5586lxQ" \
    SUPABASE_URL="https://mxrzqqbsnjytgxzwxlyb.supabase.co" \
    SUPABASE_TABLE="students,absensi" \
    SUPABASE_CONNECTION_STRING="user=postgres.mxrzqqbsnjytgxzwxlyb password=t1rt@h4k1mp@mbudh1 host=aws-0-ap-southeast-1.pooler.supabase.com port=5432 dbname=postgres" \
    TIME_OUT_CALL_API="30000" \
    TIME_INTERVAL_CALL_API="1000" \
    UPLOAD_PATH="./static/upload" \
    LOG_PATH="./log/app.log"

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc make cmake

WORKDIR /app
COPY . .
RUN make linux_venv

RUN pip install --upgrade pip
RUN pip install wheel
COPY requirements.txt .
RUN make install

FROM python:3.10.12-slim-bullseye AS compile
FROM build

ENV PATH=${PATH} \
    APP_ENV=${APP_ENV} \
    SECRET_KEY=${SECRET_KEY} \
    SUPABASE_API_KEY=${SUPABASE_API_KEY} \
    SUPABASE_URL=${SUPABASE_URL} \
    SUPABASE_TABLE=${SUPABASE_TABLE} \
    SUPABASE_CONNECTION_STRING=${SUPABASE_CONNECTION_STRING} \
    TIME_OUT_CALL_API=${TIME_OUT_CALL_API} \
    TIME_INTERVAL_CALL_API=${TIME_INTERVAL_CALL_API} \
    UPLOAD_PATH=${UPLOAD_PATH}

WORKDIR /app
COPY --from=build /app/venv /app/venv
COPY . .

CMD ["python3","/app/app.py"]
