Via Foundry's main server is located at <https://viafoundry.com>. Via Foundry can also be run as a standalone application using a docker container.


## Prerequisites:
- Via Scientific Access Keys
- Via Scientific Docker Hub Access Keys
- SSL Certificates (e.g. Let’s Encrypt)


## Recommended Computer Specifications:

- Hard disk: 50-100GB (root)
- 4-8 CPUs
- 16-32 GB of memory. 
- e.g. AWS instance type  m6i.2xlarge+
- Operating System: Ubuntu 22.04
- 1-2TB EBS mounted drive


## Software Dependencies for Pipeline Execution

In order to execute Via Foundry pipelines, you have to install and validate
certain software dependencies into your host machine.

To enable proper pipeline execution, Nextflow should be installed into
your host environment. Since most of our pipelines isolate their
dependencies within their Docker, please
install Docker or Podman into your machine by following the guidelines
below. If your platform doesn't support the installation of Docker, you
can still use our pipelines with just Singularity.

 -   Installing
     [Nextflow](https://www.nextflow.io/docs/latest/getstarted.html)
 -   Installing
     [Docker](https://docs.docker.com/engine/install/)
 -   Installing [Singularity (Version
     3)](https://docs.sylabs.io/guides/3.0/user-guide/installation.html)
 -   AWS CLI v2 
 -   Java v11+ (for nextflow)


 **How to Add Software to Your $PATH Environment:**

 -   **JAVA Command (optional):** If JAVA is not added to the $PATH
     environment, you can run the command (`module load java/8.0`) to
     manipulate your $PATH environment and gain access to JAVA.
 -   **Nextflow Path or Command (optional):** If Nextflow is not added
     to the $PATH environment, you can either enter the path of the
     nextflow (eg. `/project/bin`), or run the command
     (`module load nextflow`) to manipulate your $PATH environment and
     gain access to new software.
 -   **Docker/Singularity Command (optional):** You can run a command
     (eg. `module load docker/1.0.0` or
     `module load singularity/3.0.0`) to manipulate your $PATH
     environment in order to gain access to new software.

## Software Dependencies for Foundry Installation
- Apache2 or NGINX (to redirect the site to selected domain)
- Docker (latest version)

## Installation

1. We install the database and software outside of the container to be able to keep the changes in the database and software every time you start the container. Therefore, please choose a directory in your machine to mount. Then replace `/path/to/mount` with your path to create a directory.  Please remove s permission from the directory for proper installation.

        chmod ug-s /path/to/mount
        mkdir -p /path/to/mount

2. Use docker to download Foundry container from a private ViaScientific repository.

        docker login 
        # username:viasdock
        # password: will be sent with separate email
        docker pull viascientific/vfoundry-docker

3. Please execute the following command to start the container. Please don't change the target directory(`/export`) in the docker image and bind it to host port 8080.

        docker run -m 10G -p 8080:8080 --name vfoundry -v /path/to/mount:/export -dti viascientific/vfoundry-docker /bin/bash

4. After you start the container, you need to start the mysql and apache server using the command below:
        
        startup (if this is for the initial setup time)
        start.sh (if this is continuous maintenance after initial installation)

5. Verify that foundry and mysql folders located inside of the export folder.
        
        ls /export

6. Update software version by executing following commands in docker:

        cd /export/vsso && git pull && yarn install && yarn build && pm2 restart pm2-process.json
        cd /export/vmeta && git pull && yarn install && yarn build && pm2 restart pm2-process.json
        cd /export/vportal && git pull && yarn install && yarn build && pm2 restart pm2-process.json
        cd /export/vfoundry && git pull && yarn install && yarn build && pm2 restart pm2-process.json
        python /export/vpipe/scripts/updateDN.py

7. Now, you can open your browser to access foundry using the URL below:

        http://localhost:8080



Configuration of the .sec file
------------------------------

This is the main DolphinNext configuration file and located in the ``dolphinnext/config/.sec`` file. 

.. tip:: If you're planing to use DolphinNext on the Amazon or Google Cloud, please check `Running on the Amazon or Google Cloud <admin_faq.html#running-on-the-amazon-or-google-cloud>`_ section.

``.sec`` file contains the following configuration directives, lets start with **Dolphinnext** section::

    [Dolphinnext]
    DB=dolphinnext
    DBUSER=docker
    DBPASS=docker
    DBHOST=localhost
    DBPORT=3306
    SSHPATH=/export/.dolphinnext/.ssh
    AMZPATH=/export/.dolphinnext/.amz
    GOOGPATH=/export/.dolphinnext/.goog
    AMAZON=z7***********
    SALT=23******
    PEPPER=3d******
    MASTER=u7******
    VERIFY=2s******

* **DB:** Database name.
* **DBUSER:** Name for a database user.
* **DBPASS:** Password for a database user.
* **DBHOST:** MySQL Server Hostname.
* **DBPORT:** MySQL Server Port.
* **SSHPATH:** Secure path to save ssh files.
* **AMZPATH:** Secure path to save amazon files.
* **GOOGPATH:** Secure path to save google files.
* **AMAZON:** It is random data (salt) that is used for encrypting Amazon keys.
* **SALT,PEPPER,MASTER,VERIFY:** It is random data that is used for user authentication.

Next section called **CONFIG**.::
    
    [CONFIG]
    ENV_PATH=""
    TIMEZONE=America/New_York
    RUNPATH=../tmp/pub
    TEMPPATH=../tmp
    API_URL = http://localhost/dolphinnext
    BASE_PATH = http://localhost:8080/dolphinnext
    PUBWEB_URL = http://localhost:8080/dolphinnext/tmp/pub
    OCPU_URL = http://localhost
    DEBROWSER_URL = http://localhost
    OCPU_PUBWEB_URL = http://localhost/dolphinnext/tmp/pub
    NEXTFLOW_VERSION = 19.10.0
    LDAP_SERVER=test
    DN_STRING=test
    BIND_USER= SVCLinuxLDAPAuth
    BIND_PASS=test
    EMAIL_SENDER=test@test.edu
    EMAIL_ADMIN=test@test.edu
    

* **ENV_PATH** is an optional profile path to be sourced before executing any commands. (eg. /home/.bashrc)
* **TIMEZONE:** Sets the default timezone used by all date/time functions.
* **RUNPATH:** Relative path to keep run logs.
* **TEMPPATH:** Relative path to keep temporary created files.
* **API_URL** DolphinNext URL inside of the docker container. It will be used when API calls are received.
* **BASE_PATH** DolphinNext URL outside of the docker container. 
* **PUBWEB_URL:** URL to reach public web directory (eg. http://localhost:8080/dolphinnext/tmp/pub for localhost)
* **OCPU_URL:** URL to reach local OCPU server (eg. http://localhost for localhost in which http://localhost/ocpu exist in the server)
* **DEBROWSER_URL:** URL to reach DEBrowser server (eg. http://localhost for localhost in which http://localhost/debrowser exist in the server)
* **OCPU_PUBWEB_URL:** URL to reach local pubweb directory (eg. http://localhost/dolphinnext/tmp/pub for localhost) 
* **NEXTFLOW_VERSION:** NEXTFLOW version to be used.
* **LDAP_SERVER,DN_STRING,BIND_USER,BIND_PASS:** Configuration parameters for LDAP Server.
* **EMAIL_SENDER:** The e-mail of the sender when DolphinNext sends e-mail.
* **EMAIL_ADMIN:** The e-mail(s) of the admin who will receive notification from DolphinNext server.

.. note:: RUNPATH, OCPU_PUBWEB_URL and PUBWEB_URL should end with same directory structure (tmp/pub)


Last section called **UICONFIG**.::

    [UICONFIG]
    COMPANY_NAME=Test Server
    ALLOW_SIGNUP=true
    ALLOW_SIGNUPGOOGLE=true
    SHOW_WIZARD=true
    ; User Preferences for profile page 
    SHOW_AMAZON_KEYS=true
    SHOW_GOOGLE_KEYS=true
    SHOW_SSH_KEYS=true
    SHOW_GROUPS=true
    SHOW_GITHUB=true
    ; User Preferences for run page 
    SHOW_RUN_LOG=true
    SHOW_RUN_TIMELINE=true
    SHOW_RUN_REPORT=true
    SHOW_RUN_DAG=true
    SHOW_RUN_TRACE=true
    SHOW_RUN_NEXTFLOWLOG=true  
    SHOW_RUN_NEXTFLOWNF=true
    SHOW_RUN_NEXTFLOWCONFIG=true
    
    
* **COMPANY_NAME:** Name of the company that will be used in the webpage.
* **ALLOW_SIGNUP:** Toogle the sign-up button in the home page.
* **ALLOW_SIGNUPGOOGLE:** Toogle the google sign-in button in the home page.
* **SHOW_WIZARD:** Toogle wizard in the home page.
* **SHOW_AMAZON_KEYS:** Toogle Amazon Keys tab in the profile section.
* **SHOW_GOOGLE_KEYS:** Toogle Google Keys tab in the profile section.
* **SHOW_SSH_KEYS:** Toogle SSH Keys tab in the profile section.
* **SHOW_GROUPS:** Toogle Groups tab in the profile section.
* **SHOW_GITHUB:** Toogle Github tab in the profile section.
* **SHOW_RUN_LOG:** Toogle Log.txt file in the Log tab of the run page.
* **SHOW_RUN_TIMELINE:** Toogle timeline file in the Log tab of the run page.
* **SHOW_RUN_REPORT:** Toogle report file in the Log tab of the run page.
* **SHOW_RUN_DAG:** Toogle DAG file in the Log tab of the run page.
* **SHOW_RUN_TRACE:** Toogle trace file in the Log tab of the run page.
* **SHOW_RUN_NEXTFLOWLOG:** Toogle .nextflow.log file in the Log tab of the run page. 
* **SHOW_RUN_NEXTFLOWNF:** Toogle nextflow.nf file in the Log tab of the run page.
* **SHOW_RUN_NEXTFLOWCONFIG:** Toogle nextflow.config file in the Log tab of the run page.

