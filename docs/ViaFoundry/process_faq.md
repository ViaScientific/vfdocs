# Process FAQs

This guide will walk you through some frequently asked questions pertaining to the creation and manipulation of processes in Via Foundry. If you don't see your question here, make sure to check out our [Process Creation Guide](process.md), and as always, if you have any questions, please don't hesitate to reach out to support@viascientific.com. 

## **Revision Control and Usage**

Foundry boasts a utility-packed revision control system, granting users effortlessly controllable project autonomy. Here you'll find answers to some frequently asked questions related to this system.

### How can I use existing processes or modules?

Throughout the pipeline creation and execution process, users can simply drag and drop any of Foundry's numerous publicly available processes and modules. In a pipeline's sidebar menu, you can just click on any of the pre-configured process or module menus (for instance, Alignment) and drag the process(es) you want into your workflow.

![image](../images/process_sidebar.png){: width = "30%"}

You can also use the sidebar's `Search` bar to query a process, pipeline, or module by name if you don't know which menu it's under. Just type in a keyword and you'll see all the processes containing that keyword, which you can of course drag and drop into your workflow. See the image below for an example of querying all processes and modules containing "STAR":

![image](../images/star_search.png)

### How can I create a new process revision and use it in a pipeline?

The brief answer is this: Make your desired edits to the process, then save the changes as a new revision, enter the process's page within the pipeline in which it is used, use the dropdown menu to switch revisions, then save changes as a new pipeline revision. For more detail on new revisions and revision control in general, see [How does revision control work in Via Foundry?](developer_faq.md#how-does-revision-control-work-in-via-foundry)

## **Configuring Inputs**

Via Foundry supports a vast breadth of functionality when it comes to defining and fine-tuning your process inputs. Here are some helpful tips to demystify the process.

### When should I use the val, file, and set qualifiers?

As detailed in the [Process Creation Guide](process.md#parameters), Via Foundry has five main types of qualifiers (essentially ways to specify the type of an input), of which three are chiefly used: `val`, `file`, and `set`. You can set a parameter's qualifier while creating the parameter, but if you're using a pre-made parameter, its qualifier will be shown next to its name as the last parenthesized value in the `Add/Edit/Delete Process` page (seen below). Understanding the distinction between these qualifiers will greatly streamline your process and pipeline creation.

![image](../images/sample_inputs_val.png)

Here, you'll see the `set` qualifier is used for the "mapped_reads" parameter, whereas `val` is used for both "sense_antisense" and "mate".

#### `val`
The `val` qualifier, as you may have surmised, should be used when an input or output is of an atomic type: either an integer or a string. Behind the scenes, it enables the value to be called by reference to its name. This qualifier should be used when you want to just pass in one value to or obtain one value from a process, like the minimum number of counts for a read to be processed, or a string with value "single" or "pair" to distinguish whether single- or paired-end read files are being used.


#### `file`
Using the `file` qualifier for a given parameter allows one file to be passed in as the value for that parameter. Though you may encounter scenarios in which you'd like to pass in one file as an input (such as specifying a genome), this is more commonly used to qualify an output parameter, which is often a file containing some necessary/relevant information for the next process or a report file. It's important to understand the distinction between `file` and `set`, because while they are similar (and frequently overlap), they are decidedly not identical.

#### `set`
The most versatile of the qualifiers, `set` acts as a tuple, grouping two different qualifiers together. For instance, in the RSeQC process below, a set of "mapped_reads", expressed as a tuple of [val(name), file(bam)] is taken in. This means that each read ingested has a string representing its name (val(name)), as well as a filepath representing its contents (file(bam)).

![image](../images/abbreviated_rseqc_inputs.png)

As you can imagine, `set` can be incredibly useful when grouping multiple files together (think a whole dataset's worth of read files), which you'll find is a highly generalizable piece of functionality.


### How can I support single- and paired-end reads?

When analyzing mass quantities of omics data, it's important to be able to group paired-end read files together; else, they might be interpreted as unique single-end files, which would disrupt the analysis. To avert such issues, in any process that takes in reads as input, create and attach a "mate" input parameter with the `val` qualifier. You should also have some form of "reads" input parameter, expressed as a `set` (likely a tuple of a string filename and the file's path itself). From here, the precise way to configure your script depends on what you want to achieve with the process, but the general structure of how to account for single- and paired-end reads is as follows:
```
// Concatenate all read names, then split by spaces
nameAll = reads.toString()
nameArray = nameAll.split(' ')
file2 = ""

// Initialize one read file, initialize a second if paired-end reads have been selected
file1 = nameArray[0]
if (mate == "pair") {file2 = nameArray[1]}

...

"""
If ["${mate}" == "pair"]; then
    *Send file 1 and file 2 through some other process/analysis*
else
    *Only iterate over file 1*
"""
```

Once you realize how to integrate these capabilities, they're not at all daunting, and will accelerate your development process.

### How can I define optional input parameters?

Sometimes, you may find it helpful to be able to control whether or not an input parameter is necessary. Foundry easily supports the use of optional input parameters straight from the `Add/Edit/Delete Process` page. Note the "Optional" checkbox in this image:

![image](../dolphinNext/dolphinnext_images/process_inputs.png)

Checking this box ensures that the process will still be executed even in the absence of that input parameter being defined. Take this process, for example:

![image](../dolphinNext/dolphinnext_images/process_optional_input.png)

Since the `genome` parameter is optional, we define a `filter` parameter with the "NO_FILE" prefix; with this safeguard, the script will still run if no value is entered for `genome`. Moreover, if there is a non-empty value for `genome`, the `filter` parameter will be redefined as `"--filter ${genome}"`, running the script with the specified genome. 

### How can I make an *entire* process optional?

It's slightly more difficult to make a whole process optional than it is to simply check a box to make an input parameter optional, but the procedure is not strenuous. To check whether a process can be run or not, you can and should put a `when` condition in the **Script** section, checking if the parameter in question has been initialized to a desired value. For instance, take this image of the beginning of a Hisat2 process:

![image](../images/hisat2_when.png)

Here, the `when` section evaluates to "True", triggering the `script` section, when the "run_HISAT2" parameter is set to "yes". This ensures that the process runs only when it has been requested. Use this logic in your own processes to safeguard against superfluous process execution. 

This functionality does come with a caveat, though; if the `when` condition is not met and the script does not run, the pipeline will exit *if* the process does not have inputs and outputs of the same type and qualifier. As such, true skipping of a process chiefly occurs when the process does some sort of fine-tuning or editing to an input that isn't wholly necessary; in such a case, if the process is skipped, since the output is of the same type as the input, the command flow will simply skip to the next process. If, though, for instance, a `when` condition fails in a process that takes in a BAM file and outputs a .txt file, the process will not run, and the pipeline will exit. Be careful with what processes you make optional to avoid pipelines exiting during runs when you don't wish them to.

## **Configuring Outputs**

There's a myriad of ways in which developers can easily handle input-output relationships that are not 1:1 (i.e. you can send files from different processes, or multiple files from one process, to the input of one process). Here are some solutions to common issues faced.

### How can I collect the outputs of a process?

While creating and running workflows in Via Foundry, you'll frequently find that you want to combine multiple files created by one or more processes into input readable by a different process. Here's how you can do so (note that the files must be of the same extension):

#### Solution
Once you've created several files of the same extension, you can merge them by using an intermediate process and Nextflow's `collect` operator, which accumulates all the files given to it as input and returns them in an aggregated format. For instance, you could connect a process that operates on a list of Fastq files to a process called "merge_tables", represented as such:

#### Sample Solution Process

|                  |                  |
| ---------------- | ---------------- |
| **Process Input**   | **Input Parameter**: txtFile (*txt, file*)<br> **Parameter Name**: txtFiles <br> **Parameter Operator**: collect <br> *Note*: This input represents the .txt output of a previous process |
| **Process Output**   | **Output Parameter**: outFileTSV (*tsv, file*) <br> **Parameter Name**: "counts.tsv"   |
| **Script**           | echo -e 'filename\tcount' > counts.tsv <br> cat $txtFiles >> counts.tsv |
| **Result**           | TSV-formatted table containing filenames and read counts for all input files |


#### More Info
For a visual aid, look at these photos of a pipeline that merges the results of the count_reads process within merge_tables:

![image](../images/merge_pipeline.png)
![image](../images/updated_merge_tables.png)

This cleanly merges the results into one table, counts.tsv. It's a simple example, so to reinforce the point, here's an example of a process used in the RNA-Seq pipeline, which reinforces the usefulness of merging with the `collect` operator. Merge_TSV_Files concatenates multiple TSV files containing the same header into one TSV file, as shown here:

![image](../images/updated_merge_tsv_files.png)

**Important**: Make sure that, when you're using the `collect` operator, the output you wish to `collect` is in a file format; otherwise, the operator will not work properly.



### How can I parallelize the outputs of a process?

Within Foundry, you may have a process that produces multiple files; if you wish to parallelize those outputs so they're handled independently (and simultaneously), you can use Nextflow's `flatten` or `flatMap` operators. The former transforms a nested channel containing multiple channels or a nested collection into a single-level (flat) collection of files, which lets Nextflow send the files to separate instances of a process, enabling parallel execution of those files. Not dissimilarly, the `flatMap` operator applies some function to every item emitted by a channel, returning the outputted items as a new flat channel, which can then be passed into separate instances of a process, permitting parallelization. In fact, you can parallelize in a rather similar fashion to merging; just replace the `collect` operator with `flatten` like so.

#### Sample Solution Process
|                  |                  |
| ---------------- | ---------------- |
| **Process Input**    | **Input Parameter**: txtFile (*txt, file*) <br> **Parameter Name**: txtFiles <br> **Parameter Operator**: flatten <br> *Note*: This input represents the output of a previous process, parallelized by Nextflow's *flatten* operator |
| **Process Output**        | **Output Parameter**: outFileTSV (*tsv, file*) <br> **Parameter Name**: "counts.tsv"    |
| **Script**           | echo -e 'filename\tcount' > counts.tsv <br> Line 2: cat $txtFiles >> counts.tsv |
| **Result**           | Table containing filenames and read counts for all input files |

Again, this is a rather rudimentary process to illustrate the functionality of `flatten`; you'll likely be using it for more complex purposes, so it's best to be able to understand at the ground level first.

## **Defining Process Settings/Resources**

Foundry processes vary in how computationally intensive they are to execute. Users have a fine-grained level of control over how to configure process settings, in addition to how many resources are allocated to a process's execution.

### How can I define process settings/options?

Click [here](process.md#process-options).

### How can I manually allocate resources to my processes?

In the `Advanced` tab of the runpage, you can specify exactly how all processes or individual processes will be queued, along with how much memory, how many CPUs, and how long they will take. By clicking the **Executor Settings for Each Process** button, you can then customize the resources allocated to each process by clicking on a process's checkbox and manipulating the desired values. For more of a brute-force approach, you can check off **Executor Settings for All Processes**, which will let you configure a group of settings that will apply to every process in the pipeline. For more information, click [here](faq.md#how-should-i-configure-my-executor-settings).






