demo_developer_tutorial2.md

Questions to be answered (**bold** means done):
1. **How to support paired and single end reads?**
2. **How to collect process outputs**
3. **How to parallize process outputs.**
4. How to publish files into multiple directories?
5. How to install specific process to docker container we have
6. **How to make process optional? Can I skip one process and continue with the next process?**
7. **How to use existing modules or processes?**
8. How do we use existing index files? How can I add my index file?
9. How to configure autofill section of the pipeline?
10. **When should I use val, file or set?**
11. **How to define optional input parameters? If it is optional file how do we check wheter it is defined or not?
    filter = genome.name.startsWith('NO_FILE') ? "" : "--filter ${genome}"**
12. **How to define process settings?**
13. How to create pipeline inputs? Compare different solutions.
14. How to define global variable vs process specific local variable?
15. How to use my python or R script in (in bash/python or R script) process?
    import subprocess as sp
    functions_py_path = sp.getoutput("which functions.py")
    if you prefer you can copy script to current work folder
    sp.call("cp "+functions_py_path + " .", shell = True)
16. How to convert groovy array into python or R array?
    list to ["",""] list for R and python
    name = name.collect{ '"' + it + '"'}
    println name -> ["a","b"]
    #name = name.toString().replaceAll("\\[", "").replaceAll("\\]","")
    println name -> "a","b"
17. _How to autoscale memory and cpu if process fails?_
18. How to debug it process fails? Compare local vs aws batch env.
19. **How to create process revision and use it in the pipeline**
20. **How to push pipeline to github?**
21. How to set up continuous testing (travis, etc.)?
22. **How to configure process and pipeline resources.(CPU, memory, time)**
