### Process Guide

1. Inside a Docker container, avoid running additional Docker commands within the script block, as the current process is already running within Docker. Instead, modify the Docker configuration for the desired process.

2. When writing a bash script in the script section, refrain from using `#!/bin/bash` to prevent interference with nextflow's error detection mechanism.

#### Syntax Errors

1. Dollar characters `$` should be escaped with a backslash `\` in script blocks.


    ```
    #Change:
    helper($library, $star_index)
    #To:
    helper(\$library, \$star_index)
    ```

2. Backslash characters `\` should be escaped with another backslash `\`.

#### Container Directive Usage in Process Definitions

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

#### Process Exits with Code 1 without Output

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

