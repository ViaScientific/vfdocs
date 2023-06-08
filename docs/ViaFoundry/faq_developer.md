## Frequently Asked Questions for Developers

### Process Guide

1. we cannot run another docker command inside the script block since it is already running inside docker. We can change the docker that the process will use.

#### Syntax Errors

1. We need to escape dollar characters with slash \ . 

```
So this part star_w_chimeric_helper($library, $star_index, $genome, $file, $name) needs to be star_w_chimeric_helper(\$library, \$star_index, \$genome, \$file, \$name)
```

2. We need to escape \ characters with another slash \ . 
