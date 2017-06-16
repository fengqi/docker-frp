# docker-frp

Docker 封装的 frp

## 服务端使用方法

```
docker run --restart \
    always -d \
    --name frps \
    -p 80:80 \
    -p 443:443 \
    -p 7000:7000 \
    -p 10000-50000:10000-50000 \
    -v /docker-frp:/data \
    fengqi/frp:server
```

运行后会自动在 `/docker-frp` 下生成 frps.ini 和 log 文件.
如需调整配置, 可以修改 `/docker-frp/frps.ini` 然后重启容器.

## 客户端使用方法


```
docker run --restart \
    always -d \
    --name frpc \
    -v /docker-frp:/data \
    fengqi/frp:client
```

运行后会自动在 `/docker-frp` 下生成 frpc.ini 和 log 文件.
如需调整配置, 可以修改 `/docker-frp/frpc.ini` 然后重启容器.

## 提示

如果频繁构建导致 github 提示 api 请求限制, 请设置 `DOCKER_FRP_BUILD_TOKEN`,
方法: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/