ARG PYTHON_VERSION=3.7

FROM python:${PYTHON_VERSION}
RUN apt-get update && apt-get -y install \
    gnupg2 \
    pass \
    curl

COPY ./tests/gpg-keys /gpg-keys
RUN gpg2 --import gpg-keys/secret
RUN gpg2 --import-ownertrust gpg-keys/ownertrust
RUN yes | pass init $(gpg2 --no-auto-check-trustdb --list-secret-key | awk '/^sec/{getline; $1=$1; print}')
RUN gpg2 --check-trustdb

ARG VERSION=v0.6.0
RUN curl -sSL -o /opt/docker-credential-pass.tar.gz \
    https://github.com/docker/docker-credential-helpers/releases/download/$VERSION/docker-credential-pass-$VERSION-amd64.tar.gz && \
    tar -xf /opt/docker-credential-pass.tar.gz -O > /usr/local/bin/docker-credential-pass && \
    rm -rf /opt/docker-credential-pass.tar.gz && \
    chmod +x /usr/local/bin/docker-credential-pass
WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY test-requirements.txt .
RUN pip install -r test-requirements.txt

COPY . /src
RUN python setup.py develop
CMD pytest -v ./tests
