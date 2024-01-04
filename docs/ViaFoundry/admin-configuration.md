# Configuration

## Configuration of Amazon RDS/Cloud SQL for MySQL (optional):

Create `vpipe` database and load initial database file with following commands:

```
mysql -h hostname -u root -p -e 'CREATE DATABASE IF NOT EXISTS vpipe;'
mysql -h hostname -u root -p vpipe < /export/vpipe/db/db.sql
mysql -h hostname -u root -p -e "CREATE USER 'viafoundry'@'%' IDENTIFIED BY 'change_password';"
mysql -h hostname -u root -p -e "GRANT ALL PRIVILEGES ON vpipe.* TO 'viafoundry'@'%';"
```

After that please update DBUSER, DBPASS, DBHOST and DBPORT parameters in `/export/vpipe/config/.sec` file  and then execute the following command:

```
cd /export/vpipe/scripts && python updateDN.py
```


## Configuration of Vpipe:

Vpipe configuration file found in /export/vpipe/config/.sec file.

By default, localhost:8080 is used for domain name. Please use static IP address or domain name and please update BASE_PATH and PUBWEB_URL as follows:

```
BASE_PATH=http://localhost:8080/vpipe
PUBWEB_URL=http://localhost:8080/vpipe/tmp/pub
```

to

```
BASE_PATH=https://your_domain/vpipe
PUBWEB_URL=https://your_domain/vpipe/tmp/pub
```

Other important parameters:
```
[CONFIG]
AUTH_RUN_FILES=true
AUTH_RUN_FILES_ALLOWED_DOMAINS=your_domain

```

All of the configuration directive details can be found [here](../admin-configuration/#vpipe-config-file-details)

**Note:** If you were using Standalone Vpipe (or DolphinNext) before, please check the SALT and PEPPER config parameters in /export/vpipe/config/.sec file. These values should be the same for /export/vsso/config.env. So, you need to update /export/vsso/config.env with Vpipe parameters.

## Configuration of Vsso:

Vmeta configuration file found in /export/vsso/config.env.

By default, localhost:3000 is used for domain name. Please use static IP address or domain name and please update BASE_URL as follows:

```
BASE_URL=http://localhost:3000/vsso
```

to

```
BASE_URL=https://your_domain/vsso
```

All of the configuration directive details can be found [here](../admin-configuration/#vsso-config-file-details)

## Configuration of Vmeta:

Vmeta configuration file found in /export/vmeta/config.env.

By default, localhost:4000 is used for domain name. Please use static IP address or domain name and please update BASE_URL, SSO_REDIRECT_URL, SSO_USER_INFO_URL and SSO_URL as follows:

```
BASE_URL=http://localhost:4000/vmeta
SSO_URL=http://localhost:3000/vsso
SSO_REDIRECT_URL="http://localhost:4000/vmeta/receivetoken"
SSO_USER_INFO_URL="http://localhost:3000/vsso/api/v1/users/info"
```

to

```
BASE_URL=https://your_domain/vmeta
SSO_URL=https://your_domain/vsso
SSO_REDIRECT_URL="https://your_domain/vmeta/receivetoken"
SSO_USER_INFO_URL="https://your_domain/vsso/api/v1/users/info"
```

All of the configuration directive details can be found [here](../admin-configuration/#vmetavportalvfoundry-config-file-details)

## Configuration of Vfoundry:

Vfoundry configuration file found in /export/vfoundry/config.env.

By default, localhost:9000 is used for domain name. Please use static IP address or domain name and please update BASE_URL, SSO_REDIRECT_URL, SSO_USER_INFO_URL and SSO_URL as follows:

```
BASE_URL=http://localhost:9000
SSO_URL=http://localhost:3000/vsso
SSO_REDIRECT_URL="http://localhost:9000/receivetoken"
SSO_USER_INFO_URL="http://localhost:3000/vsso/api/v1/users/info"
```

to

```
BASE_URL=https://your_domain
SSO_URL=https://your_domain/vsso
SSO_REDIRECT_URL="https://your_domain/receivetoken"
SSO_USER_INFO_URL="https://your_domain/vsso/api/v1/users/info"
```

All of the configuration directive details can be found [here](../admin-configuration/#vmetavportalvfoundry-config-file-details)

## Configuration of Vportal:

Vportal configuration file found in /export/vportal/config.env.

By default, localhost:8000 is used for domain name. Please use static IP address or domain name and please update BASE_URL, SSO_REDIRECT_URL, SSO_USER_INFO_URL and SSO_URL as follows:

```
BASE_URL=http://localhost:8000
SSO_URL=http://localhost:3000/vsso
SSO_REDIRECT_URL="http://localhost:8000/receivetoken"
SSO_USER_INFO_URL="http://localhost:3000/vsso/api/v1/users/info"
```

to

```
BASE_URL=https://your_domain/vportal
SSO_URL=https://your_domain/vsso
SSO_REDIRECT_URL="https://your_domain/vportal/receivetoken"
SSO_USER_INFO_URL="https://your_domain/vsso/api/v1/users/info"
```

All of the configuration directive details can be found [here](../admin-configuration/#vmetavportalvfoundry-config-file-details)


## Configuration of OKTA:

If you're integrating OKTA for user authentication, you can use the SAML method. Below are the URLs and settings you'll need to input in your OKTA configuration:

```
Single Sign-On URL: https://viafoundry.{hostname}/vsso/auth/saml/callback
Recipient URL: https://viafoundry.{hostname}/vsso/auth/saml/callback
Destination URL: https://viafoundry.{hostname}/vsso/auth/saml/callback
Audience Restriction: https://viafoundry.{hostname}/vsso/auth/saml/callback
Default Relay State: https://viafoundry.{hostname}/vsso/auth/saml
```

Make sure to replace `{hostname}` with your actual server's hostname.

### Sending User Attributes

In your OKTA setup, configure it to send the user's first name (`firstName`) and last name (`lastName`) when they log in.

### Metadata File

Download the `metadata.xml` file from OKTA and place it in the specified location `SSO_SAML_METADATA`.

### Configuration File for OKTA

Finally, update your configuration file located at `/export/vsso/config.env` with the following parameters:

```
OKTA_SAML_LOGIN=true
SSO_ISSUER=http://www.okta.com/{ISSUER_ID} 
SSO_SAML_METADATA=/export/vsso/certs/metadata.xml
SSO_SAML_DESTINATION_URL=https://viafoundry.{hostname}
```

Here, `{ISSUER_ID}` should be replaced with the actual issuer ID provided by OKTA, and `{hostname}` with your server's hostname.


## Configuration of Microsoft Active Directory:

If you're integrating Microsoft Active Directory for user authentication, you can use the SAML method. Below are the URLs and settings you'll need to input in your Microsoft Active Directory configuration:

```
Indentifier(Entity ID): https://viafoundry.{hostname}/vsso/auth/saml/callback
Reply URL: https://viafoundry.{hostname}/vsso/auth/saml/callback
Sign On URL: https://viafoundry.{hostname}/vsso/auth/saml/callback
Relay State (Optional): https://viafoundry.{hostname}
Logout Url (Optional):
```

Make sure to replace `{hostname}` with your actual server's hostname.

### Metadata File

Download the `metadata.xml` file from Microsoft Entra and place it in the specified location `SSO_SAML_METADATA`.

### Configuration File for Microsoft Active Directory 

Finally, update your configuration file located at `/export/vsso/config.env` with the following parameters:

```
OKTA_SAML_LOGIN=true
SSO_ISSUER=https://viafoundry.{hostname}/vsso/auth/saml/callback
SSO_SAML_METADATA=/export/vsso/certs/metadata.xml
SSO_SAML_DESTINATION_URL=https://viafoundry.{hostname}
SSO_SAML_WANT_AUTHN_RESPONSE_SIGNED=false
```


## Apache Configuration for the Foundry Server:

To configure Apache, you need to enable the mod_ssl and mod_proxy modules. Please follow the instructions below:

1. Create certificate files (SSLCertificateFile and SSLCertificateKeyFile) in PEM format. SSLCertificateChainFile file is optional.

2. Save the following text into /etc/apache2/sites-enabled/viafoundry.conf file
```
<IfModule mod_ssl.c>
    <VirtualHost *:443>
        ServerAdmin Your_Email
        ServerName Your_Domain.com
        ServerAlias Your_Domain.com
        RewriteEngine On

        # Some rewrite rules in this file were disabled on your HTTPS site,
        # because they have the potential to create redirection loops.
        SSLCertificateFile /etc/letsencrypt/live/Your_Domain.com/cert.pem
        SSLCertificateKeyFile /etc/letsencrypt/live/Your_Domain.com/privkey.pem
        SSLCertificateChainFile /etc/letsencrypt/live/Your_Domain.com/chain.pem
        SSLProxyEngine on

        <Proxy *>
            Allow from localhost
        </Proxy>

        ProxyPass /vtunnel http://localhost:6000/vtunnel
        ProxyPassReverse /vtunnel http://localhost:6000/vtunnel
        ProxyPass / http://localhost:8080/
        ProxyPassReverse / http://localhost:8080/

        ProxyRequests Off

        CustomLog /var/log/apache2/access_vf.log "%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \"%r\" %b"
    </VirtualHost>


    ErrorLog /var/log/apache2/error_vf.log
</IfModule>
```

3.  Enable mod_ssl: You need to make sure that the mod_ssl module is enabled in your Apache configuration. This module provides support for SSL/TLS encryption.
    Enable mod_proxy: You also need to enable the mod_proxy module in your Apache configuration. This module allows Apache to act as a proxy server.
```
a2enmod ssl rewrite proxy requestheader headers proxy_http
```

4. Replace "Your_Domain.com", "Your_Email", ProxyPass and ProxyPassReverse: In the Apache configuration, you need to replace "Your_Domain.com" with your actual domain name. 

5. Adjust SSL certificate locations: You need to specify the correct SSL certificate locations for the subdomain used by the apps. 

6. Check the apache config syntax.
```
apache2ctl configtest
```

7. Restart Apache 2 web server,
```
/etc/init.d/apache2 restart
or 
sudo /etc/init.d/apache2 restart
or 
sudo service apache2 restart
```




## After Configuration

1. After changing the configurations, please restart vfoundry, vmeta, vportal and vsso.

   ```
   pm2 restart all
   ```

2. Enter Vsso (https://your_domain/vsso) and login with any username and password. The first user will be assigned as admin.
3. Enter Vmeta (https://your_domain/vmeta). Click the profile button at the top right and click the Servers tab. Here you can insert multiple foundry servers after clicking the “add a server” button. Enter any name for your vpipe server and select type as “vpipe”.
   - URL Client: https://your_domain/vpipe
   - URL Server: https://your_domain/vpipe
   - Type: vpipe
   - Main Server: checked

## Advanced Configuration:

### Vpipe Config File Details

All of the configuration directive details can be found below:

**[Vpipe] Section:**

- **DB**: This is the name of the database used by Vpipe.
- **DBUSER**: It is the name of a database user who has access to the Vpipe database.
- **DBPASS**: This is the password for the specified database user.
- **DBHOST**: It represents the hostname or IP address of the MySQL server where the Vpipe database is hosted.
- **DBPORT**: This specifies the port number used to connect to the MySQL server.

- **SSHPATH**: It denotes the secure path on the system where SSH files are saved. This path is used for SSH-related operations in Vpipe.
- **AMZPATH**: This is the secure path on the system where Amazon files are saved. It is used for storing files related to Amazon integration in Vpipe.
- **GOOGPATH**: Similarly, this is the secure path where Google files are saved. It is used for storing files related to Google integration in Vpipe.

- **AMAZON**: It is a randomly generated string or salt used for encrypting Amazon keys. This salt adds an extra layer of security to the encryption process.

- **SALT, PEPPER, MASTER, VERIFY**: These are randomly generated strings used for user authentication. They enhance the security of the authentication process by adding unique elements.

- **JWT_SECRET**: This is the secret key used for creating and verifying JSON Web Tokens (JWT) in Vpipe. JWTs are used for authentication and ensuring the integrity of data transmitted between the client and server.

- **JWT_COOKIE_EXPIRES_IN**: This specifies the expiration time for the JWT cookie. Once the specified time period has passed, the cookie will expire, and the user will need to log in again for authentication. The value is usually set in terms of days.

**[CONFIG] Section**:

- **ENV_PATH**: This is an optional file path that can be specified to be sourced before starting the application's run. It could be a file like "/home/.bashrc" and is used to load environment variables or configuration settings.

- **TIMEZONE**: It sets the default timezone used by all date and time functions in the application. It ensures that the application works with the correct time representation based on the specified timezone.

- **RUNPATH**: This is the relative path where run logs are stored.

- **TEMPPATH**: Similarly, this is the relative path where temporary files created during the application's runtime are stored.

- **API_URL**: This is the Vpipe URL used inside the Docker container. It is the endpoint that the application will use to make API calls when it receives requests.

- **BASE_PATH**: This represents the Vpipe URL outside the Docker container. It is the base URL used to access Vpipe from external sources or systems.

- **PUBWEB_URL**: This is the URL that can be used to reach the public web directory. It specifies the address and path to access the directory where public web files are hosted. For example, "http://localhost:8080/vpipe/tmp/pub" can be the URL for accessing the public web directory when running locally.

- **NEXTFLOW_VERSION**: This setting specifies the version of Nextflow that will be used by the application.

- **LDAP_SERVER, DN_STRING, BIND_USER, BIND_PASS**: These configuration parameters are used for the LDAP (Lightweight Directory Access Protocol) server. They include details such as the LDAP server address, DN string, and credentials for binding to the LDAP server.

- **EMAIL_SENDER**: This configuration parameter represents the email address that will be used as the sender when the Vpipe application sends emails. It is the "From" address in the email communication.

- **EMAIL_ADMIN**: This configuration parameter specifies the email address (or multiple email addresses) of the administrator(s) who will receive notifications from the Vpipe server. These email addresses are used for administrative alerts or important notifications.

- **EMAIL_TYPE**: This configuration parameter determines the type of email sending mechanism to be used by the Vpipe application. There are three options:

  - **DEFAULT (sendMail):** This option uses the default email sending method available in the system.
  - **SMTP:** This option utilizes the Simple Mail Transfer Protocol (SMTP) to send emails. It requires additional parameters for SMTP configuration.
  - **HTTP:** This option uses an HTTP-based email sending mechanism. It requires additional parameters for configuring the HTTP endpoint.

- **Required Parameters for EMAIL_TYPE=DEFAULT/SMTP**:

  - **EMAIL_HOST**: This parameter specifies the hostname or IP address of the email server to be used for sending emails.
  - **EMAIL_USERNAME**: This parameter represents the username or account name used for authentication when connecting to the email server.
  - **EMAIL_PASSWORD**: This parameter is the password associated with the email account used for authentication.
  - **EMAIL_PORT**: This parameter indicates the port number used to establish a connection with the email server.

- **Required Parameters for EMAIL_TYPE=HTTP**:
  - **EMAIL_URL**: This parameter represents the URL of the HTTP endpoint used for sending emails.
  - **EMAIL_HEADER_KEY**: This parameter specifies the header key required by the HTTP endpoint for authentication or identification purposes.
  - **EMAIL_HEADER_VALUE**: This parameter represents the value associated with the header key mentioned above. It is provided for successful communication with the HTTP endpoint.

**[UICONFIG] Section:**

- **COMPANY_NAME**: This setting defines the name of the company or organization that will be displayed on the webpage.

- **PASSWORD_LOGIN**: This parameter is used to enable or disable password-based login for users.

- **ALLOW_SIGNUP**: This parameter toggles the sign-up button on the home page. Enabling it allows users to sign up for an account.

- **ALLOW_SIGNUPGOOGLE**: This parameter toggles the Google sign-in button on the home page. To use this feature, you need to provide the `GOOGLE_CLIENT_ID` directive. Enabling this option allows users to sign in using their Google accounts.

- **GOOGLE_CLIENT_ID**: This parameter specifies the client ID required for Google sign-in functionality. It is used to authenticate users through Google services.

- **SHOW_WIZARD**: This parameter toggles the display of a wizard on the home page. Enabling it shows a step-by-step guide or tutorial to assist users.

- **SHOW_AMAZON_KEYS**: This parameter toggles the display of the Amazon Keys tab in the user's profile section.

- **SHOW_GOOGLE_KEYS**: This parameter toggles the display of the Google Keys tab in the user's profile section.

- **SHOW_SSH_KEYS**: This parameter toggles the display of the SSH Keys tab in the user's profile section.

- **SHOW_GROUPS**: This parameter toggles the display of the Groups tab in the user's profile section.

- **SHOW_GITHUB**: This parameter toggles the display of the GitHub tab in the user's profile section.

- **SHOW_RUN_LOG**: This parameter toggles the display of the Log.txt file in the Log tab of the run page.

- **SHOW_RUN_TIMELINE**: This parameter toggles the display of the timeline file in the Log tab of the run page.

- **SHOW_RUN_REPORT**: This parameter toggles the display of the report file in the Log tab of the run page.

- **SHOW_RUN_DAG**: This parameter toggles the display of the DAG (Directed Acyclic Graph) file in the Log tab of the run page.

- **SHOW_RUN_TRACE**: This parameter toggles the display of the trace file in the Log tab of the run page.

- **SHOW_RUN_NEXTFLOWLOG**: This parameter toggles the display of the .nextflow.log file in the Log tab of the run page.

- **SHOW_RUN_NEXTFLOWNF**: This parameter toggles the display of the nextflow.nf file in the Log tab of the run page.

- **SHOW_RUN_NEXTFLOWCONFIG**: This parameter toggles the display of the nextflow.config file in the Log tab of the run page.

- **SHOW_HOMEPAGE**: This parameter toggles the display of the homepage.

- **SHOW_APPS**: This parameter toggles the display of applications on the webpage.

- **ENABLE_SHARE_WITH_EVERYONE_RUN**: This parameter enables or disables the option to share runs with everyone.

- **ENABLE_SHARE_WITH_EVERYONE_PIPELINE**: This parameter enables or disables the option to share pipelines with everyone.

- **CUSTOM_HELP_MESSAGE**: This setting allows the customization of a help message to be displayed in the support section of the webpage.

- **CUSTOM_FILE_LOCATION_MESSAGE**: This setting allows the customization of a message to be displayed in the "add file" window on the run page.

**[SSOCONFIG] Section:**

- **SSO_LOGIN**: This setting determines whether Single Sign-On (SSO) login is enabled or disabled for the application. Set it to `true` to enable SSO login and `false` to disable it.

- **SSO_URL**: This parameter specifies the URL of the SSO server. It is the endpoint where the authentication process takes place.

- **CLIENT_ID, CLIENT_SECRET**: These parameters represent the client credentials required for SSO integration. They are obtained from the SSO server. The `CLIENT_ID` is a unique identifier assigned to the Vpipe application, and the `CLIENT_SECRET` is a secure key used for authentication and authorization purposes.

**[VIACONFIG] Section:**

- **VFOUNDRY_URL**: This parameter represents the URL of the Via Foundry server. The VFOUNDRY_URL setting allows the Vpipe application to connect and interact with the Via Foundry server.

### Vmeta/Vportal/Vfoundry Config File Details

All of the configuration directive details can be found below. By configuring these settings, you can customize various aspects of the application, including the environment, server configuration, database connection, authentication options, email settings, SSO integration, SSL/TLS certificates, and session management.

- **NODE_ENV**: This parameter specifies the environment in which the application is running. The default value is "production".

- **PROTOCOL**: This parameter determines the protocol to be used for communication. It can be either "http" or "https".

- **PORT**: This parameter specifies the port number on which the application will run.

- **BASE_URL**: This parameter represents the base URL of the application. If the application is running under a subfolder of another application, the SUBFOLDER parameter should be defined.

- **SUBFOLDER**: This parameter is used when the application is running under a subfolder of another application. It specifies the subfolder path.

- **DATABASE_LOCAL**: This parameter defines the connection URL for the local MongoDB database. It includes the credentials (username and password), hostname, port, and database name.

- **SESSION_SECRET**: This is a secret key used for session management. It should be a long, secure string.

- **JWT_SECRET**: This is the secret key used for JWT (JSON Web Token) generation and verification. It should also be a long, secure string.

- **JWT_EXPIRES_IN**: This parameter defines the expiration time for JWTs in days.

- **JWT_COOKIE_EXPIRES_IN**: This parameter defines the expiration time for JWT cookies in days.

- **CERTS_PRIVATE_KEY**: This parameter specifies the file path for the private key used for SSL/TLS certificates.

- **CERTS_CERTIFICATE**: This parameter specifies the file path for the SSL/TLS certificate.

- **TIME_TO_CHECK_EXPIRED_TOKENS**: This parameter determines the time interval (in seconds) for checking the database for expired tokens.

- **SSO_LOGIN**: This setting determines whether Single Sign-On (SSO) login is enabled or disabled for the application.

- **SSO_URL**: This parameter represents the URL of the SSO authorization server.

- **SSO_REDIRECT_URL**: This parameter specifies the URL where the user will be redirected after successful SSO authentication.

- **SSO_USER_INFO_URL**: This parameter represents the URL for obtaining user information from the SSO server.

- **CLIENT_ID, CLIENT_SECRET**: These parameters represent the client credentials retrieved from the SSO server for authentication and authorization.

### Vsso Config File Details

All of the configuration directive details can be found below. By configuring these settings, you can customize various aspects of the application, including the environment, server configuration, database connection, authentication options, email settings, SSO integration, SSL/TLS certificates, and session management.

- **NODE_ENV**: This parameter specifies the environment in which the application is running. The default value is "production".

- **PORT**: This parameter specifies the port number on which the application will run. It is set to 3000.

- **PROTOCOL**: This parameter determines the protocol to be used for communication.

- **BASE_URL**: This parameter represents the base URL of the application. If the application is running under a subfolder of another application, the SUBFOLDER parameter should be defined.

- **SUBFOLDER**: This parameter is used when the application is running under a subfolder of another application. It specifies the subfolder path, which is "/vsso" in this case.

- **DATABASE**: This parameter defines the connection URL for the MongoDB database. It includes the credentials (username and password), hostname, port, and database name.

- **SALT, PEPPER**: These parameters are random strings used for user authentication.

- **JWT_SECRET**: This is the secret key used for JWT (JSON Web Token) generation and verification. It should be a long, secure string.

- **JWT_EXPIRES_IN**: This parameter defines the expiration time for JWTs, set to 90 days.

- **JWT_COOKIE_EXPIRES_IN**: This parameter defines the expiration time for JWT cookies, also set to 90 days.

- **COMPANY_NAME**: This parameter specifies the name of the company that will be displayed in the user interface.

- **ALLOW_SIGNUP**: This parameter toggles the sign-up button on the home page. It is set to false, meaning sign-up is not allowed.

- **PASSWORD_LOGIN**: This parameter toggles the password login option. It is set to true, enabling password-based login.

- **EMAIL_FROM, EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_HOST, EMAIL_PORT, EMAIL_ADMIN, EMAIL_ADMIN_NAME**: These parameters configure the email settings, including the sender's email, SMTP credentials, host, port, admin email, and admin name.

- **GOOGLE_LOGIN**: This parameter enables Google login. It is set to true.

- **GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_CALLBACK_URL**: These parameters represent the client credentials and callback URL for Google login.

- **OKTA_SAML_LOGIN**: This parameter enables SAML-based login with Okta. It is set to true.

- **SSO_ISSUER, SSO_SAML_METADATA, SSO_SAML_DESTINATION_URL**: These parameters configure the SAML settings for Okta login, including the issuer, SAML metadata file path, and destination URL after successful login.

- **CERTS_PRIVATE_KEY, CERTS_CERTIFICATE**: These parameters specify the file paths for the private key and SSL/TLS certificate used by the application.

- **SESSION_SECRET**: This is a secret key used for session management. It should be a long, secure string.

- **SESSION_MAXAGE**: This parameter defines the maximum age (in milliseconds) for sessions.

- **TIME_TO_CHECK_EXPIRED_TOKENS**: This parameter determines the time interval (in seconds) for checking the database for expired tokens.

- **ACCESS_TOKEN_EXPIRES_IN**: This parameter defines the expiration time (in milliseconds) for access tokens.

- **CODE_TOKEN_EXPIRES_IN**: This parameter defines the expiration time (in seconds) for code tokens.

- **REFRESH_TOKEN_EXPIRES_IN**: This parameter defines the expiration time (in minutes) for refresh tokens.
