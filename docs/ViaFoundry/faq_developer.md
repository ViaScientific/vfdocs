## Frequently Asked Questions for Developers

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

Using `command 2>/dev/null` will cause the process to exit without providing the reason for the error. Instead use the following pattern: ```my_command 2>/dev/null || true```