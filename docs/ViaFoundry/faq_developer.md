## Process Guide

1. Inside a Docker container, avoid running additional Docker commands within the script block, as the current process is already running within Docker. Instead, modify the Docker configuration for the desired process.

2. When writing a bash script in the script section, refrain from using `#!/bin/bash` to prevent interference with nextflow's error detection mechanism.

### Syntax Errors

1. Dollar characters `$` should be escaped with a backslash `\` in script blocks.


    ```
    #Change:
    helper($library, $star_index)
    #To:
    helper(\$library, \$star_index)
    ```

2. Backslash characters `\` should be escaped with another backslash `\`.

### Container Directive Usage in Process Definitions

When defining a process, be cautious with the use of the `when:` directive. Specifically, avoid placing the container directive after the `when:` directive, as it may not work as expected.

```
// Avoid placing the `when:` directive before the `container` directive:

when:
params.run_mkfastq == "yes"

container { tool_for_bcl_to_fastq_conversion == 'cellranger' ? 'cellranger:4.0' : 'bclconvert:4.3.6'}

script:
"""	
echo "test"
"""
```

Correct usage:

```
// Place the `container` directive before the `when:` directive.

container { tool_for_bcl_to_fastq_conversion == 'cellranger' ? 'cellranger:4.0' : 'bclconvert:4.3.6'}

when:
params.run_mkfastq == "yes"

script:
"""	
echo "test"
"""

```

### Process Exits with Code 1 without Output

**Case-1:**

```
Caused by:
  Essential container in task exited

Command executed:
  my_command 2>/dev/null

Command exit status:
  1

Command output:
  (empty)
```

Using `my_command 2>/dev/null || true` pattern prevents the process from exiting without providing the reason for the error.

**Case-2:**

```
Caused by:
  Essential container in task exited

Command executed:
  aws s3 ls s3://backup/test.txt

Command exit status:
  1

Command output:
  (empty)
```

Using the `aws s3 ls` command might fail without providing the reason for the error. To prevent the process from exiting when the file does not exist in the S3 bucket, you can use the pattern `aws s3 ls s3://backup/test.txt 2>/dev/null || true`. This command suppresses error messages by redirecting them to `/dev/null` and ensures the process continues by using the `|| true` pattern.

**Case-3:**
Another reason for unexpected behavior is the use of the expression `((k++))` in a bash script:

```
k=0
((k++))
```

Instead, use the command `k=$((k + 1))` in the bash script.

### Process terminated for an unknown reason 

**Case-1:**

```
ERROR ~ Error executing process > 'STAR'

Caused by:
  Process `STAR` terminated for an unknown reason -- Likely it has been terminated by the external system

Command executed:
  my_command

Command exit status:
  -

Command output:
  (empty)


```

Please check .nextflow.log file for clues. For example:

```

DEBUG nextflow.executor.GridTaskHandler - Failed to get exit status for process 
TaskHandler[jobId: 33830839; id: 43; name: STAR; status: RUNNING; exit: -; 
error: -; workDir: /rundir/work/a5/0c31b5e1b0eca2f054d923d509629e started: 1740080252555; exited: -; ] -- exitStatusReadTimeoutMillis: 270000; delta: 270017
Current queue status:
  (empty)

Content of workDir: /rundir/work/a5/0c31b5e1b0eca2f054d923d509629e
null
```

#### **Nextflow Timing Out While Retrieving Job Status**
This error occurs when Nextflow times out while attempting to retrieve the exit status from an executor (e.g., SLURM, LSF, SGE). However, the executor itself has no record of job failure, indicating that the job is likely still running.

#### **Possible Cause: Incorrect Queue/Partition for Job Status Checks**
By default, Nextflow checks job status in SLURM using the following command:

```
squeue --noheader -o '%i %t' -t all -p $PARTITION -u $USERNAME
```
Nextflow assumes that the job is running in the same partition it was submitted to. However, in some clusters, jobs may be assigned to a **different queue or partition**, causing Nextflow to check the wrong queue and fail to retrieve job status.

#### **Solution: Enable Global Queue Status Check**
To ensure that Nextflow retrieves job status correctly across all partitions, add the following directive in the **Run Environment → Profile Variables** section:

```
executor.queueGlobalStatus = true
```
This setting allows Nextflow to check job statuses across **all partitions**, preventing job tracking failures.
