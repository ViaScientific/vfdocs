# Frequently Asked Questions


## Installation Guide

### How can I install Singularity?

Follow this link to install [Singularity (Version
3)](https://sylabs.io/guides/3.0/user-guide/installation.html#install-on-linux)
for your pipelines. For your convenience, attached below are the
commands needed to download the newest version in a Linux environment:

    ## Remove old version of Singularity
    # sudo rm -rf /usr/local/libexec/singularity /usr/local/var/singularity /usr/local/etc/singularity /usr/local/bin/singularity /usr/local/bin/run-singularity /usr/local/etc/bash_completion.d/singularity

    ## Install Singularity Version 3
    apt-get install -y build-essential libssl-dev uuid-dev libgpgme11-dev libseccomp-dev pkg-config squashfs-tools
    wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz
    tar -C /usr/local -xzf go1.12.7.linux-amd64.tar.gz
    export PATH=$PATH:/usr/local/go/bin
    export VERSION=3.2.1 
    wget https://github.com/sylabs/singularity/releases/download/v${VERSION}/singularity-${VERSION}.tar.gz
    tar -xzf singularity-${VERSION}.tar.gz
    cd singularity
    ./mconfig && make -C ./builddir 
    sudo make -C ./builddir install

### How can I install Docker?

Follow this link to install
[Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) for
pipelines, or follow the commands below:

    ## Uninstall Old Versions of Docker
    # sudo apt-get remove docker docker-engine docker.io

    ## Install Docker
    sudo apt install docker.io

### How can I install JAVA?

Installing [Java
v8+](https://www.java.com/en/download/help/linux_x64_install.xml#install)
for Nextflow:

    apt-get install -y openjdk-8-jdk && 
    apt-get install -y ant && 
    apt-get clean;

    # Fix certificate issues
    apt-get update && 
    apt-get install ca-certificates-java && 
    apt-get clean && 
    update-ca-certificates -f;
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

### How can I install Nextflow?

[JAVA (v8+)](faq.md#how-can-i-install-java) should be installed before
installing Nextflow. Once Java has been successfully installed, click
this link to install [Nextflow](https://www.nextflow.io/) or use the
commands below:

    ## To install to your ~/bin directory:
    mkdir ~/bin
    cd ~/bin
    curl -fsSL get.nextflow.io | bash

    # Add Nextflow binary to your bin PATH or any accessible path in your environment:
    chmod 755 nextflow
    mv nextflow ~/bin/
    # OR system-wide installation:
    # sudo mv nextflow /usr/local/bin

## Connection Issues

### Why can't I validate my SSH Keys?

If you're having trouble validating your SSH keys, here are a few
things to check:

> 1.  Make sure you copy the entire key, including the initial part
>     (e.g. "ssh-rsa"). The key should span the entire file, like in
>     the following example:
>
>         ssh-rsa
>         AA1AB3N4nX3a....................
>         ................................
>         ................................
>         ...............b9Rj @viafoundry
>
> 2.  The SSH protocol requires specific permissions for files and
>     directories to establish secure connections. Please execute the
>     following commands to make sure your SSH-related files are
>     properly secured:
>
>         chmod 700 ~/.ssh
>         chmod 600 ~/.ssh/authorized_keys
>
> 3.  Ensure that your **home directory** is not writable by other
>     users. Setting the permissions of your home directory to 777 can
>     create security issues and block SSH connections. Instead, set the
>     permissions to more secure options such as 750, 755 or 754.

### How can I create SSH keys in my computer?

You can find your SSH key pairs on your local machine at their default
location: `~/.ssh/id_rsa` for private and `~/.ssh/id_rsa.pub` for public
key. If no keys exist there or you want to create new ones, then on the
command line, enter:

    ssh-keygen -t rsa

You will be prompted to supply a filename and a password. If you want to
accept the default filename (and location) for your key pair, just press
Enter without entering a filename. Your SSH keys will be generated using
the default filename (`id_rsa` and `id_rsa.pub`), and they will be saved
in the "~/.ssh/" directory in your machine.

## Run Questions

### I can't reach my files in the file window

There might be a connection issue. Please check to make sure you've
followed these steps:

> 1.  The SSH protocol requires specific permissions for files and
>     directories to establish secure connections. Please execute the
>     following commands to make sure your SSH-related files are
>     properly secured:
>
>         chmod 700 ~/.ssh
>         chmod 600 ~/.ssh/authorized_keys
>
> 2.  Ensure that your **home directory** is not writable by other
>     users. Setting the permissions of your home directory to 777 can
>     create security issues and block SSH connections. Instead, set the
>     permissions to more secure options such as 750, 755 or 754.

### Error: Run directory cannot be created

It's possible that there's an issue with your connection. Please check
the [Why can't I validate my SSH
Keys](faq.md#why-can-t-i-validate-my-ssh-keys) section to ensure
you've followed all the necessary steps.

## Profile Questions

### How should I configure my executor settings?

In Via Foundry, there are four different sections to control executor
settings: the first two are defined in **Profile** -> **Run
Environment**, and the remaining two are adjusted in the **Advanced**
tab of the run page. If you select an executor other than "Local" or
"Ignite", Via Foundry prompts you to enter additional settings, such
as the queue/partition, memory, CPU, and time.

> **1. Executor of Nextflow (navigate to Profile -> Run
> Environments)**:
>
> > This setting controls how Via Foundry initiates Nextflow. Currently,
> > Via Foundry supports the Local, SGE, SLURM, and LSF executors to
> > initiate Nextflow. For the SGE, SLURM, and LSF executors, Via
> > Foundry only uses them to run Nextflow itself, so the time limit
> > should be long enough to execute all processes in the pipeline. For
> > local execution, Via Foundry limits the total amount of memory and
> > CPU that can be used, so these values should be close to the maximum
> > capacity of your computer.
> >
> > -   Suggested parameters for SGE/SLURM/LSF: long (queue) 8 (GB
> >     Memory) 1 (CPU) 5000-8000 (min, Time)
> > -   Suggested parameters for Local: 100 (GB Memory) 8 (CPU)
>
> **2. Executor of Nextflow Jobs (navigate to Profile -> Run
> Environments)**:
>
> > This setting will be used as the default setting for submitted jobs
> > by Nextflow if you don't set any parameters in the **Advanced**
> > section of your run page.
> >
> > -   Suggested parameters for SGE/SLURM/LSF: short (queue) 20 (GB
> >     Memory) 1 (CPU) 240 (min, Time)
> > -   Suggested parameters for Local: 20 (GB Memory) 1 (CPU)
>
> **3. Executor Settings for All Processes (in the advanced tab of run
> page)**:
>
> > These settings will overwrite those in **Executor of Nextflow Jobs**
> > and set default parameters for all Nextflow Jobs.
> >
> > -   Suggested parameters for SGE/SLURM/LSF: short (queue) 20 (GB
> >     Memory) 1 (CPU) 240 (min, Time)
> > -   Suggested parameters for Local: 20 (GB Memory) 1 (CPU)
>
> **4. Executor Settings for Each Process (in the advanced tab of run
> page)**:
>
> > If a particular process requires different parameters than the
> > defaults (which are defined in the **Executor Settings for All
> > Processes** or **Executor of Nextflow Jobs** sections), you can
> > overwrite the general settings by clicking the checkbox of the
> > process that you want to change. This will only affect the settings
> > of the selected process and keep the original settings for the rest
> > of the processes.
> >
> > -   Suggested parameters for SGE/SLURM/LSF: long (queue) 20 (GB
> >     Memory) 4 (CPU) 1000-5000 (min, Time)
> > -   Suggested parameters for Local: 20 (GB Memory) 4 (CPU)
>
>**Note:** 
> If non-standard resources or settings are required for the executor,
> then you can specify these parameters by using **Other Options** box.
> For instance, to submit an SGE job with 3 CPU using parallel
> environments, you can enter `-pe orte 3` (to use MPI for
> distributed-memory machines) or `-pe smp 3` (to use OpenMP for
> shared-memory machines) in the **Other Options** box, leaving the CPU
> box empty.

