Via Foundry's main server is located at <https://viafoundry.com>. Via Foundry can also be run as a standalone application using a docker container.

## Prerequisites:

- Via Scientific Access Keys
- Via Scientific Docker Hub Access Keys
- SSL Certificates (e.g. Let’s Encrypt)

## Recommended Computer Specifications:

- Hard disk: 100-200GB (root)
- 16-32 CPUs
- 64-128 GB of memory.
- e.g. AWS instance type m6i.4xlarge+, GCP VM type n2-standard-16+
- Operating System: Ubuntu 22.04
- 1-2TB EBS (AWS) / Persistent SSD Disk (GCP) mounted drive

## Preparation Steps

Before you begin, it is recommended to follow these best practices:

1. Create a user named `viafoundry` on the target machine.

2. Configure the directory and perform the installation while logged in as the `viafoundry` user.

3. Ensure that the default shell for the 'viafoundry' user is set to 'bash'. Use `echo $SHELL` to validate the current SHELL, if not, use `chsh` to update the SHELL to `/bin/bash`.
   
## Software Dependencies for Pipeline Execution

In order to execute Via Foundry pipelines, you have to install and validate
certain software dependencies into your host machine.

To enable proper pipeline execution, Nextflow should be installed into
your host environment. Since most of our pipelines isolate their
dependencies within their Docker, please
install Docker or Podman into your machine by following the guidelines
below. If your platform doesn't support the installation of Docker, you
can still use our pipelines with just Singularity.

- Installing
  [Nextflow](https://www.nextflow.io/docs/latest/getstarted.html)
- Java v11+ (for nextflow)
- Installing
  [Docker](https://docs.docker.com/engine/install/)
- Installing [Singularity (Version 3)](https://docs.sylabs.io/guides/3.0/user-guide/installation.html) (required when docker is not available)
- AWS CLI v2 for AWS resources access
- GCloud/GSUtil CLI for GCP resources access

**How to Add Software to Your $PATH Environment:**

- **JAVA Command (optional):** If JAVA is not added to the $PATH
  environment, you can run the command (`module load java/8.0`) to
  manipulate your $PATH environment and gain access to JAVA.
- **Nextflow Path or Command (optional):** If Nextflow is not added
  to the $PATH environment, you can either enter the path of the
  nextflow (eg. `/project/bin`), or run the command
  (`module load nextflow`) to manipulate your $PATH environment and
  gain access to new software.
- **Docker/Singularity Command (optional):** You can run a command
  (eg. `module load docker/1.0.0` or
  `module load singularity/3.0.0`) to manipulate your $PATH
  environment in order to gain access to new software.

## Software Dependencies for Foundry Installation

- Apache2 or NGINX (to redirect the site to selected domain)
- Docker (latest version)

## Installation

1.  We install the database and software outside of the container to be able to keep the changes in the database and software every time you start the container. Therefore, please choose a directory in your machine to mount. Then replace `/path/to/mount` with your path to create a directory. Please remove s permission from the directory for proper installation.

        chmod ug-s /path/to/mount
        mkdir -p /path/to/mount

2.  Use docker to download Foundry container from a private ViaScientific repository.

        docker login
        # username:viasdock
        # password: will be sent with separate email
        docker pull viascientific/vfoundry-docker

3.  Please execute the following command to start the container. Please don't change the target directory(`/export`) in the docker image and bind it to host port 8080.

        docker run -m 10G -p 8080:8080 --name vfoundry -v /path/to/mount:/export -dti viascientific/vfoundry-docker /bin/bash

4.  After you start the container, you need to start the mysql and apache server using the command below:

        startup (if this is for the initial setup time)
        start.sh (if this is continuous maintenance after initial installation)

5.  Verify that foundry and mysql folders located inside of the export folder.

        ls /export

6.  Update software version by executing following commands in docker:

        cd /export/vsso && git pull && yarn install && yarn build && pm2 restart pm2-process.json
        cd /export/vmeta && git pull && yarn install && yarn build && pm2 restart pm2-process.json
        cd /export/vportal && git pull && yarn install && yarn build && pm2 restart pm2-process.json
        cd /export/vfoundry && git pull && yarn install && yarn build && pm2 restart pm2-process.json
        python /export/vpipe/scripts/updateDN.py

7.  Now, you can open your browser to access foundry using the URL below:

        http://localhost:8080
