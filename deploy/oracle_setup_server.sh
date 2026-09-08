#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/opt/guo_chuang/my-app"
APP_USER="${SUDO_USER:-ubuntu}"
SERVICE_NAME="guo-chuang"

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip nginx rsync

sudo mkdir -p "$APP_DIR"
sudo chown -R "$APP_USER":"$APP_USER" /opt/guo_chuang

python3 -m venv /opt/guo_chuang/.venv
/opt/guo_chuang/.venv/bin/python -m pip install --upgrade pip

sudo tee /etc/systemd/system/${SERVICE_NAME}.service >/dev/null <<EOF
[Unit]
Description=Guo Chuang FastAPI app
After=network.target

[Service]
User=$APP_USER
Group=$APP_USER
WorkingDirectory=$APP_DIR
Environment=PYTHONUNBUFFERED=1
ExecStart=/opt/guo_chuang/.venv/bin/python -m uvicorn main:app --host 127.0.0.1 --port 8011
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

sudo tee /etc/nginx/sites-available/${SERVICE_NAME} >/dev/null <<'EOF'
server {
    listen 80;
    server_name _;

    client_max_body_size 50m;

    location / {
        proxy_pass http://127.0.0.1:8011;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF

sudo ln -sf /etc/nginx/sites-available/${SERVICE_NAME} /etc/nginx/sites-enabled/${SERVICE_NAME}
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl daemon-reload
sudo systemctl enable ${SERVICE_NAME}
sudo systemctl restart nginx

echo "Server base setup complete. Upload the app, then restart ${SERVICE_NAME}."
