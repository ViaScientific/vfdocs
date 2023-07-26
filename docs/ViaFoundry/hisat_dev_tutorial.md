# Developer Tutorial - Advanced Pipeline Creation

Welcome to the second of Via Foundry's pipeline creation tutorials! If you missed the first one, you can go [right here](demo_developer_tutorial.md) to give yourself a crash course in pipeline creation in Foundry. This tutorial will be decidedly more complex than its predecessor, as we'll be going through the process of replicating our Hisat2 module, which maps next-generation sequencing reads against the general human population or a reference genome. Along the way, we'll address some frequently asked questions about Foundry pipelines, processes, and more as they come up. You'll see a more concise answer to each question on this page, but each question will be linked to a more elaborated-upon answer.

## Before you start

Go to the [Via Foundry homepage](https://viafoundry.com) and log into your account. If you don't have an account or otherwise experience issues logging in, please let us know about it at support@viascientific.com, and we'll be happy to set up an account for you.

## Set-up: Creating a new project and pipeline

Once you're logged in, click the `Projects` tab in the top menu and select `Add a New Project`. After entering whatever name you'd like, you'll be directed to the project's dashboard, which contains space for a description of the project, as well as its pending and completed runs, reports, and embedded apps. From here, you'll want to click on the `Pipelines` tab to the right of `Dashboard`. To access the pipeline builder page, just click the `Pipelines` tab and then click the `Create Pipeline` button. 

![image](../images/build0-builderpage.png)


Now you can write a descripton about your pipeline using the `Description` tab, start developing your pipeline with the `Workflow` tab, and add extra files or set some extra parameters using the `Advanced` tab.

![image](../images/build1-builderpage.png)

*A brief note on processes:*

If you're attempting this tutorial, you're likely already familiar with Foundry processes. However, if you're not (or if you'd simply like to reacquaint yourself), check [this link](demo_developer_tutorial.md#what-is-a-process) from our first developer tutorial to deepen your understanding of processes. Once you've done so, if you'd like, we can move on to actually creating the processes we'll need for the Hisat2 module. Before that, here's how you can use publicly available Foundry modules and processes.

#### FAQ: How can I use pre-existing, publicly available Foundry processes or modules in a pipeline?

With a few minor revisions, this entire exercise could be expedited and carried out in a few seconds. This is because we're replicating Foundry's Hisat2 module, which is ready-made and available for off-the-shelf use by Foundry users. It's quite simple to use the Hisat2 module in its entirety, or to use a process that's already been made (available): just click the appropriate **Pipelines** or **Processes** dropdown menu (or search a module/process by name) and drag the item you want into your workflow in the **Workflow** tab. Just like that, any process or module made for public use can be in your workflow. For more, check out [this FAQ](process_faq.md#how-can-i-use-existing-processes-or-modules).

## Exercise 1 - Creating processes

Throughout this tutorial, we'll be creating six processes: Check_Build_Hisat2_Index, Check_Hisat2_Files, Map_Hisat2, Merge_Bam, Hisat2_Summary, and Merge_TSV_Files. Since the scripts we'll be dealing with in this tutorial will be much longer than those in our [previous tutorial](demo_developer_tutorial.md#1-fastqc-process), the scripts won't be housed on this page. Instead, each process will be linked to its relevant scripts [here](hisat_scripts.md) so as not to clutter this guide.

*Note*: Make sure you're in the **Description**, **Workflow**, or **Advanced** tab of your pipeline's page.

### **Check_Build_Hisat2_Index**

This process builds a HISAT2 index using a provided genome FASTA file and GTF file. It extracts splice sites and exons from the GTF file and creates the HISAT2 index in a designated directory. 

You can find all the relevant inputs, outputs, and scripts for this process [here](hisat_scripts.md#check_build_hisat2_index).

Now that you've entered in all the appropriate values, it's a good time to discuss best practices for scope control in Foundry processes. 

#### FAQ: Which variables are global, and which are local, within a process?

Within the Check_Build_Hisat2_Index process, you'll see variables defined in the script's `script:` block (e.g. basename, basenameGTF, index_dir) that are then invoked in the section enclosed by triple quotes. This stands in contrast with the Header Script, in which the only variable declared (build_hisat2_index) defines and styles an input form on the runpage. These examples exemplify best practices for Foundry scope control, as the following properties are true of process variables:

- Defining variables in the Header Script or Footer script creates them in a global scope, meaning accidental overloading can later occur if a different variable of the same name is defined. For this reason, the only variables that should be defined in these sections are those that configure the appearance of input fields on the runpage; for instance, build_hisat2_index instantiates a checkbox field on the runpage, and is not used in any scripts.
- Defining variables in the **Script** section creates them within a local scope, meaning such variables only exist within their host processes, and you can have different variables of the same name in other processes. Define such variables under the `script:` header, as is done in this process. Here, "basename", "basenameGTF", and "index_dir" only exist in Check_Build_Hisat2_Index, so you're able to define other identically-named variables in other processes.
- Manipulating an existing input variable in the **Script** section overwrites its value. Take care to avoid doing so.
