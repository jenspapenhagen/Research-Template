FROM bitnami/jax AS devcontainer
# more infos: https://github.com/bitnami/containers/tree/main/bitnami/jax

# Additional cleanup if necessary
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

USER jax 

# Install requirements
COPY requirements.txt requirements.txt

RUN pip3 --disable-pip-version-check --no-cache-dir install -r requirements.txt


FROM devcontainer AS production

COPY main.py /app/main.py
CMD ["python", "/app/main.py"]
