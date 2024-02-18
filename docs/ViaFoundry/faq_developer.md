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
Another reason for unexpected behavior is the use of the expression `((k++))` in a bash script:

```
k=0
((k++))
```

Instead, use the command `k=$((k + 1))` in the bash script.

