# Iriscot Frontpage

A personal frontpage showcasing my projects.

## Build


Build an image
```
cd src
docker build -t frontpage .
```

Run the container
```
docker run -d -p 4888:4888 --name=frontpage --restart=unless-stopped <id-from-command-above>
```

Reverse proxy from port 4888

????

PROFIT!!!
