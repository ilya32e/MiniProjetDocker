
FROM ubuntu:latest

LABEL description="Client mysql + outils reseau (exo 9)"


RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-mysql-client \
        iputils-ping \
        dnsutils \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*


CMD ["bash"]
