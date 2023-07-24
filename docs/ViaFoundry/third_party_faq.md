# Third Party Software FAQs

This document will walk you through some common questions related to integrating the functionality of various third-party services (e.g. Docker, GitHub, travis.io) into your Via Foundry pipelines and runs.

## **Docker**

### How can I build a Docker container/image for my project?

Like [this](developer_faq#how-can-i-build-a-docker-containerimage-for-my-project)!

### How can I install a specific script to a pre-existing Docker container?

There are two main strategies you can utilize to integrate a third-party script into your run environment: importing it into a **bin** folder and adding the path to your Dockerfile. Below, we'll expound upon both of these tactics:

#### **Importing into a bin folder**

For a slightly easier experience importing your own scripts into a run, navigate to the **Advanced** tab of the pipeline in which you'd like to include the scripts. If a folder called **bin** does not already exist in the **Pipeline Files** field, create one by clicking on the folder icon, then naming the newly created folder "**bin**". From there, simply import your scripts by clicking the plus sign in the top left to create as many files as you have scripts, then pasting each script into its own file. Make sure to drag all your newly created files into the **bin** folder, as this creates a shortcut to the files behind the scenes. To actually invoke a script, all you need to do is type its name into the portion of a process script that's enclosed by triple quotes. For instance, say you have a Python script called run_GSEA.py that runs GSEA analysis. You'd create a **bin** folder in the relevant pipeline, then add a file called run_GSEA.py with the script's contents to that folder. Within the process in which you'd like to call the script, you'd use the following syntax:
```
when:
// Conditions that must be met to run the script

script:
// Define whatever variables you need to

"""
run_GSEA.py
// Add any additional flags required by run_GSEA.py
"""
```

This will call your script by referencing its name, and since it is located in the **bin** folder, its contents are made accessible by the process, rendering it usable within your pipeline.

To visually demonstrate what placing script files into a **bin** folder looks like, here's an image of the **Advanced** tab in a pipeline containing a script called prepare_DESeq2.py:

![image](../images/prepare_deseq_bin_folder.png)

#### **Adding to a Dockerfile**

To achieve the same results as outlined above, you can also add the directory containing your script(s) to your pipeline's Dockerfile. For example's sake, let's say you have a directory of RMarkdown scripts, called RMD_scripts, for interactive data analysis. You'd navigate to your Dockerfile, then add the line ```ADD RMD_scripts /RMD_scripts/```. This copies the full directory into the container, enabling access to its contents in the pipeline. Alternatively, if you'd like to only add one script in this fashion, you can include only the path to that one script (instead of its entire parent directory). Either way, now that you have the location of your script stored in the pipeline's container, you need to invoke it in a process script. The overall structure of such a script is similar to that of the [previous example](third_party_faq.md#importing-into-a-bin-folder), but instead of just calling the name of a script, you need to call its entire path so Foundry knows where to look:

```
when:
// Conditions that must be met to run the script

script:
// Define whatever variables you need to

"""
// Script filepath
C:\Users\12345\Documents\RMD_scripts\run_GSEA_explorer.Rmd

// Add any additional flags required by run_GSEA_explorer.Rmd
"""
```

Overall, the two techniques outlined above are fairly similar, so choosing between them is a matter of preference (and, to a lesser degree, familiarity with [Dockerfiles](developer_faq.md#how-can-i-build-a-docker-containerimage-for-my-project)).

## **GitHub**

Via Foundry enables effortless integration with GitHub, the world's leading open-source development platform. To link your GitHub account, navigate to the **Repositories** section of your Foundry profile, then click `Add Account`. From here, select "GitHub" from the **Account Type** dropdown menu, then enter in your username and e-mail in the appropriate fields. You'll have to enter an access token, which you can obtain by following the directions at [this link](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token). Once you've gotten the access token, enter it in, press `Submit`, and voila - your account has been linked! From here, you can enjoy access to GitHub from within your Foundry account.

### How can I push a pipeline to GitHub?

If you'd like to add a pipeline you've created to GitHub, the process is quite simple. Navigate to your pipeline's page. In the top bar, next to your pipeline's name, you'll see a series of icons. Click the `Repository Management` button, represented by a cloud with an upward arrow, and you'll be taken to this screen:

![image](../images/repo_management_console.png)

Select your GitHub account from the **Account** dropdown menu, then enter in your repository and the appropriate branch, and hit `Push Pipeline`. Refresh your GitHub repository, and you should see the pipeline with all its dependencies and source files.

## **Support**

For any questions or help, please reach out to
<support@viascientific.com> with your name and question.