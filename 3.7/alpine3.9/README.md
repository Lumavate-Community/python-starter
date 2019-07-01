# Python Starter Kit

Use this project as a starting point for creating a new Lumavate python project.

To build the image in Dev mode with the Editor API, run:

```
docker build --no-cache --rm -f Dockerfile_Dev -t python-starter:1.0
```

To run the container outside of Lumavate, run:

```
./launch-standalone
```

To build the image in Prod mode without the Editor API, run:

```
docker build --no-cache --rm -f Dockerfile_Prod -t python-starter:prod-1.0
```
