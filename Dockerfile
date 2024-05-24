FROM python:3.10.12-slim-bullseye AS build

# Make sure we use the virtualenv:
ENV PATH="/app/venv/bin:$PATH" \
    APP_ENV="${{ env.APP_ENV }}" \
    SECRET_KEY="${{ env.SECRET_KEY }}" \
    SUPABASE_API_KEY="${{ env.SUPABASE_API_KEY }}" \
    SUPABASE_URL="${{ env.SUPABASE_URL }}" \
    SUPABASE_TABLE="${{ env.SUPABASE_TABLE }}" \
    SUPABASE_CONNECTION_STRING="${{ env.SUPABASE_CONNECTION_STRING }}" \
    TIME_OUT_CALL_API="${{ env.TIME_OUT_CALL_API }}" \
    TIME_INTERVAL_CALL_API="${{ env.TIME_INTERVAL_CALL_API }}" \
    UPLOAD_PATH="${{ env.UPLOAD_PATH }}" \
    LOG_PATH="${{ env.LOG_PATH }}"

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
