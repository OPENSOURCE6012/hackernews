FROM debian:bookworm-slim

WORKDIR /app

# Fix for BigQuery TLS certificate verification error
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY toolbox .
COPY tools.yaml .

RUN chmod +x toolbox

ENV PORT=8080

EXPOSE 8080

CMD ["sh", "-c", "./toolbox --tools-file=tools.yaml --address=0.0.0.0 --port=$PORT"]