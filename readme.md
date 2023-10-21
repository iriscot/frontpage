# Iriscot Frontpage

A personal frontpage showcasing my projects.

## Build

```
docker build -t frontpage .
```

```
docker run -d -p 4888:4888 --name=frontpage --restart=unless-stopped <id-from-command-above>
```
