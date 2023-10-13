# App Section Documentation

This documentation provides step-by-step instructions for setting up VTunnel and Kubernetes on your host machine, including installing required dependencies and configuring the environment. VTunnel is a critical component for managing applications on Foundry. 


## Prerequisites

Before you begin, ensure that you have the following prerequisites ready on your host machine:

1. SSL Certificates for foundry-apps (e.g. Let’s Encrypt)

2. Use the following commands to install Node.js and npm:
     ```bash
     sudo apt-get update
     sudo apt-get install -y --no-install-recommends nodejs npm
     sudo npm install pm2 npm@8.19.4 -g
     sudo n 16.20.1
     ```
3. Download and install Minikube from [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/).

## Verify Prerequisites
After installing Node.js and Minikube, verify the versions of Node.js and npm:
```bash
$ npm -v
8.19.4

$ node -v
v16.20.1
```

## Install Node.js PM2 and modules
Assume your vtunnel is install under /opt/viafoundry folder
```bash
cd /opt/viafoundry/vtunnel
sudo npm install pm2 -g
npm install 
```

## Minikube Setup
1. Stop and delete any existing outdated Minikube instance (if previously installed):
   ```bash
   $ minikube stop
   $ minikube delete
   ```
2. Install Minikube with Kubernetes version v1.25.9 and additional configurations:
   ```bash
   $ minikube start --kubernetes-version=v1.25.9 --addons=metrics-server,ingress --container-runtime=docker --cpus=32 --memory=128g --mount --mount-string="/opt:/opt1"
   ```
3. Obtain Minikube's IP address:
   ```bash
   $ minikube ip
   192.168.49.2
   ```

4. Update the server's Apache configuration for VFoundry APP:
   Use minikube IP at below.
   Replace Your_APP_Domain.com with your actual app domain name (e.g. viafoundry-apps.com). 
   ```
   $ vi /etc/apache2/sites-enabled/foundry-app.conf
   
   <IfModule mod_ssl.c>
    <VirtualHost *:443>
    ServerName Your_APP_Domain.com
    RewriteEngine On
    SSLCertificateFile /etc/letsencrypt/live/Your_Domain.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/Your_Domain.com/privkey.pem
    SSLProxyEngine on

    SSLProxyVerify none
    SSLProxyCheckPeerCN off
    SSLProxyCheckPeerName off
    SSLProxyCheckPeerExpire off

    RewriteEngine on
    RewriteCond %{HTTP:Upgrade} =websocket
    RewriteRule /(.*) wss://192.168.49.2/$1 [P,L]
    RewriteRule /(.*) https://192.168.49.2/$1 [P,L]
    <Proxy *>
      Allow from localhost
    </Proxy>
    <Location />
      ProxyPreserveHost on
      ProxyPass         https://192.168.49.2/
      ProxyPassReverse  https://192.168.49.2/
      RequestHeader set X-Forwarded-Port "443"
      RequestHeader set "X-Forwarded-Proto" expr=https
    </Location>

    CustomLog /var/log/apache2/access_vf_apps.log \
          "%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \"%r\" %b"
    ErrorLog /var/log/apache2/error_vf_apps.log
    </VirtualHost>
   </IfModule>

   <VirtualHost *:80>
    ServerName Your_APP_Domain.com
    RewriteEngine On
    RewriteCond %{SERVER_NAME} =Your_APP_Domain.com
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,QSA,R=permanent]
   </VirtualHost>

   ```

## Install VTunnel

1. Using root user change the owner of vtunnel directory.
```
sudo su - root
chown -R viafoundry /opt/vfoundry/vtunnel
```

2. Switch to viafoundry user and install VTunnel
```
sudo su - viafoundry
cd /opt/vfoundry/vtunnel
yarn install & yarn build
pm2 start pm2-process.json
```

## Upgrade VTunnel Config
1. Change the kubectl alias:
   ```bash
   $ alias kubectl='minikube kubectl --'
   ```
2. Navigate to the VTunnel directory:
   ```bash
   $ cd /export/vtunnel
   ```
3. Deploy VTunnel using kustomize:
   ```bash
   $ cd /export/vtunnel/tools/*/docs/deployment/*/1*
   $ kustomize build . | kubectl apply -f - --server-side
   $ # Repeat the command if CRD could not be created on the first attempt
   $ kustomize build . | kubectl apply -f - --server-side
   ```

6. Check the status of pods:
   ```bash
   $ kubectl get pods -n shinyproxy
   ```

## Upgrade VPipe Config
1. Edit the VPipe config file:
   ```
   $ vi /export/vpipe/config/.sec
   ```
2. Update the following APPS section
   ```bash

   [APPS]
   APP_URL=https://YOUR_APP_DOMAIN
   MOUNTED_VOLUME=/opt1/vfoundry
   VTUNNEL_URL=https://YOUR_DOMAIN/vtunnel

   # MOUNTED_VOLUME will be used to mount run reports into app containers. It should be the location of the export directory outside of the container. e.g. /opt1/vfoundry. 
   # If you mounted your drive to minikube on start e.g. minikube start --mount-string="/opt:/opt1"
   # then /opt needs to be replaced with /opt1 on your path. e.g. /opt1/vfoundry. 
   ```

