FROM bitnami/jax

ARG USER_ID
ARG GROUP_ID
ARG NAME
RUN groupadd --gid ${GROUP_ID} ${NAME}
RUN useradd \
    --no-log-init \
    --create-home \
    --uid ${USER_ID} \
    --gid ${GROUP_ID} \
    -s /bin/sh ${NAME}

ARG WORKDIR_PATH
WORKDIR ${WORKDIR_PATH}

# Additional cleanup if necessary
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install requirements
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# when building with --target devcontainer, the following will not be executed
FROM devcontainer as production

COPY main.py /app/main.py
CMD ["python", "/app/main.py"]
