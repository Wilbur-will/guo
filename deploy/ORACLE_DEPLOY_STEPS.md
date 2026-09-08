# Oracle Cloud Always Free 部署步骤

## 1. 创建 Oracle VM

在 Oracle Cloud 里创建一台 Always Free VM：

- Image: Ubuntu 22.04 或 Ubuntu 24.04
- Shape: Ampere A1 Always Free 优先，抢不到就先用 AMD Micro
- Public IP: 需要启用
- SSH key: 使用本项目的 `oracle_guo_chuang_key.pub`

创建后，在安全列表或 NSG 里放行：

- TCP 22
- TCP 80

## 2. 初始化服务器

拿到公网 IP 后，从本机运行：

```bash
cd /Users/william/Desktop/guo_chuang
ssh -i oracle_guo_chuang_key ubuntu@你的服务器公网IP
```

第一次连上确认没问题后，退出服务器，在本机运行：

```bash
cd /Users/william/Desktop/guo_chuang
ssh -i oracle_guo_chuang_key ubuntu@你的服务器公网IP 'bash -s' < deploy/oracle_setup_server.sh
```

如果你让 Codex 继续操作，只要给公网 IP，我会替你跑初始化和部署。

## 3. 上传并启动网站

```bash
cd /Users/william/Desktop/guo_chuang
bash deploy/oracle_deploy_app.sh ubuntu@你的服务器公网IP
```

成功后访问：

```text
http://你的服务器公网IP
```

二维码只需要根据这个公网 IP 地址生成一次。
