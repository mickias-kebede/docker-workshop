#base Docker image that will be build on
FROM python:3.13.11-slim
#FROM python:3.13.10-slim
#copy the uv binary from the uv image to /bin/ in our image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

#set up our image by installing prerequisites: pandas and pyarrow
#RUN pip install pandas pyarrow

#set up the working directory in the container
WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
#COPY pipeline/pyproject.toml pipeline/

#install dependencies using uv
RUN uv sync --locked

#copy the script from the current directory or source to the container or destination path 
COPY pipeline.py pipeline.py

#specify the command to run on container startup ie run the script and use ENTRYPOINT open bash
# to avoid using uv run in the entrypoint as
# ENTRYPOINT ["uv", "run", "python", "pipeline.py"] Set the environment path to include the virtual environment binaries
ENTRYPOINT ["python", "pipeline.py"]
