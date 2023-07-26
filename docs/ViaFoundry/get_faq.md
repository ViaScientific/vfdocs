# Frequently Asked Questions


## Via Scientific Capabilities

### What is the primary focus of Via Scientific and Foundry platform?

Via Scientific is primarily a data processing and analytics company that specializes in creating advanced bioinformatics pipelines with seamless metadata integration to feed ML/AI algorithms and other analytical processes in an automatized fashion. The Foundry platform facilitates seamless integration with 3rd party applications enabling automatic data aggregation from various 3rd party sources. By automating the data collection and processing needs, and by further automating the interrogation and exploration of the resultant data through an expanding library of statistical and model / AI driven tool sets we empower scientists and researchers to focus on their core scientific analysis tasks, eliminating tedious manual data handling, dev ops tasks and modeling tasks accelerating their science and while simultaneously eliminating costs and and creating  overall efficiency.

While we are an analytics company, and not  a “data broker” , it is important to note that data is an integral part of our operations. As our Via Foundry platform gathers data from 3rd party platforms for various experiments, we inevitably handle and manage substantial amounts of data. Furthermore we not only process and manage that data, the analytical processes inherent in the various omics workflows will generally expand the data and create additional, richer data prior to it moving into the analytical and reporting steps, Its also important to note that as part of our platform we do manage, and allow our customers to manage various reference data sets (e.g. genome builds etc.)  This data is crucial for driving the analysis processes and generating valuable insights for our customers.  Lastly, customers accumulate data within Foundry  for additional comparative analysis (or they might have us feed a data lake  moving data between Foundry and the data lake environment)

### Via Foundry: AI in omics data analysis, genomics research benefits?

Via foundry platform specializes in the aggregation, analysis, and sharing of vast amounts of genomic and clinical data. Here's a general idea of the kinds of data we aggregate:

**Data Sets:**

**1. Omics Data:** This could include whole genome sequences, exome sequences, genotyping data, transcriptomic data, metagenomic data, epigenomic data, and more. This data is usually obtained from a variety of sources, including individual research studies, larger initiatives like the 1000 Genomes Project, and direct-to-consumer genetic testing companies.

**2. Phenotypic and Clinical Data:** This includes medical histories, lab results, diagnostic images, and other clinical data that can be linked to genomic data to find correlations between genetic variations and health outcomes. This kind of data often comes from electronic health records, clinical trials, and longitudinal cohort studies.

**3. Environmental Data:** Increasingly, genomic studies are integrating data about individuals' environments and lifestyles to better understand how these factors interact with genetic factors to influence health.

**4. Other Metadata:** This is data about the other datasets — where it came from, when it was collected, how it was processed, what type of perturbations done etc. This kind of data is crucial for managing, integrating, and interpreting the other types of data.

The value of aggregating these data sets in Via Platform in omics is multi-fold:

**1. Interdisciplinary Research:** The aggregation of diverse datasets facilitates cross-disciplinary research and accelerates translational development. For instance, researchers can investigate how genomic data interacts with environmental factors to influence health outcomes.  

**2. Scale and Statistical Power:** Aggregated datasets are larger, which provides more statistical power and reliability to detect smaller effects or rare occurrences. 

**3. Data Reuse:** Once data is collected and made available in an aggregated format, other researchers can use it to conduct their own studies without having to collect new data or with having the ability to add new data they can also contextualize the models according to their needs, especially using transfer learning.

**4. Collaboration:** Via Foundry facilitates collaboration and data sharing between researchers and institutions across geographical and organizational boundaries, promoting scientific progress.

**5. Discovery of Novel Insights:** By analyzing different datasets together, researchers can potentially uncover novel insights that would have been impossible to detect in isolated datasets.

**6. Training:** based upon the analytics that customers are doing, the data they feed into Foundry can also become training data (and also operational input data) to customize certain models made available to our customers  inside of Foundry ( this training loop is a new capability being deployed here in 2H-2023.

The usage of such data requires stringent data governance policies and processes to protect privacy and ensure ethical use, especially in the case of genomic and clinical data.

Via platform not only serves as repositories for data but also provides powerful computational resources and tools for analyzing these data, including machine learning (ML) and artificial intelligence (AI) algorithms. 

Running ML and AI on the platform allow researchers to identify patterns, make predictions, and even generate hypotheses for further investigation. Here are some examples of how these technologies are applied in this field:

**1. Genomic Variant Prediction:** ML algorithms are trained on large datasets to predict the potential impact of genomic variants. For example, an algorithm might be trained on known pathogenic (disease-causing) and benign variants to classify novel variants as either benign or likely pathogenic. This can aid in diagnosing genetic disorders and understanding the function of different genes and variants.

**2. Drug Discovery and Personalized Medicine:** AI/ML are also being used to identify potential new drugs or to predict how individual patients will respond to existing drugs based on their genetic and clinical data. For instance, machine learning models identify genomic markers that predict a patient's response to a particular chemotherapy agent, helping to customize treatment plans for each individual patient.

**3. Disease Risk Prediction:** AI/ML models are developed to predict an individual's risk of developing certain diseases based on their genetic and clinical data. Successful outcome of this could allow for early intervention or preventive measures in high-risk individuals.

**4. Phenotype Prediction:** AI is used to predict physical traits or disease phenotypes based on genotypic/transcriptomic data. This can help in identifying individuals who may be at risk for certain diseases even before symptoms appear.

**5. Data Integration and Visualization:** AI can also be useful in integrating different types of data (genomic, clinical, environmental, etc.) and visualizing complex relationships between them. This can provide novel insights and generate new hypotheses for research.

### How does Via Foundry handle noisy genomics data?

In areas like genomics and healthcare, noise can indeed be quite high, meaning they may contain errors, inconsistencies, or irrelevant information. Noise can arise from a variety of sources, including measurement errors, inconsistent data collection methods, missing data, and more. Here are some common strategies Foundry uses to deal with noisy data.  These strategies and capabilities are part of Foundry’s core value as Foundry enables the below methods for our customers based on the pipelines they select or create within Foundry and based on their own sensitivities.

**1. Data Cleaning:** This is the process of identifying and correcting errors in the data. It might involve correcting obvious mistakes, dealing with missing or inconsistent data, and standardizing the data format across the dataset. For example, the same patient in vitiligo project entered the system two times because of using an extra name and two unique IDs were given by human error. Once data processing is done, the system detects that this is the same individual from its genetic information. 

**2. Data Normalization and batch effect correction:** This involves adjusting the values measured on different scales to a common scale. It reduces the distortion due to different scales and helps to manage the noise. Especially different batches coming from different labs usually have batch effect issues. Our systems have built-in modules to deal with this issue using different methods (i.e Combat, Harman). 

**3. Feature Selection:** This process involves identifying the most relevant variables for a particular analysis and discarding the rest. Feature selection can help to reduce noise by eliminating irrelevant or redundant variables using methods like PCA and others.

**4. Outlier Detection:** Outliers are data points that are significantly different from others. They might be due to noise or error, or they might represent genuinely unusual cases. Outlier detection methods can be used to identify these points. Our QC modules have different plots and statistical methods to detect and identify outliers for our customers  by profiling them using existing data. 

**5. Robust Statistical Methods:** These are techniques that are less sensitive to outliers and noise than traditional methods. For instance, median is a more robust measure of central tendency than mean because it's less affected by outliers. Since omics data mostly comes from count based experiments (genomic read counts), the data distribution is based on negative binomial distribution that helps us to remove 0 counts and apply robust differential analysis like DESeq2 or Limma to find differences between cell states. 

**6. Machine Learning Techniques:** Some machine learning techniques are particularly well-suited to dealing with noisy data. For instance, ensemble methods like random forests or boosting can improve prediction accuracy and robustness in the presence of noise. Within Foundry  these methods are often used  for tissue and sub cell type annotation use cases.

**7. Imputation Methods:** When dealing with missing data, imputation methods can be used to fill in the gaps. These methods estimate the missing values based on the information in the rest of the data. 

**8. Validation and Cross-Validation:** These techniques are used to assess the performance of a model on an independent dataset and can help to prevent overfitting to the noise in the training data.

**9. Regularization:** This is a technique used in model fitting that adds a penalty term to the loss function (the function being minimized) that discourages overfitting to the noise in the data.

Data preprocessing is a crucial step in data analysis and needs to be handled carefully to avoid introducing biases. However, if done correctly, it can significantly improve the quality and reliability of the results. 


Via Foundry provides a robust and scalable environment to run complex machine learning and AI algorithms on large genomic and clinical datasets to reduce the noise and complexity of data. However, it's crucial to note that any such predictive models need to be built and evaluated carefully by the users using appropriate metrics and confidence values to ensure their reliability and validity, given the high stakes of medical and genetic data. Foundry is actively simplifying model creations and calculating appropriate metrics to evaluate the models and sharing and recording the underlying code and parameters with the users. The evaluation of the results are made by the users.

### How does Foundry handle versioning for structured and unstructured data?

Our structured and unstructured data supports document differences by automatic versioning.  Foundry follows these general steps:

**1. Data Schema Design:** Platform ensures that the data schema includes fields to store metadata about each document's version, such as a timestamp or and a unique hash for that entry. Metadata of metadata is also kept in the collections in MongoDB as well rather than as static json objects required to be loaded while starting an app.

**2. Store/Backup Complete Versions:** Instead of directly updating documents, Foundry  saves complete copies (snapshots) of the documents. Additionally Foundry does not delete any fields if they are removed, those fields are deprecated to allow supporting continuity and backward compatibility.

**3. Audit Trail:** Foundry creates an "audit trail" in separate log files to store the history of changes made to the documents. The changes are tracked with timestamps, user identifiers, and any other relevant metadata.

**4. Querying the History:** When there is a need to retrieve historical data or show the diff indications, Foundry enables the user to query the audit trail logs to fetch the relevant versions of the document and compare them to identify the differences.

**5. Displaying Diffs:** Currently the Foundry UI does not support  displaying differences, however, in our roadmap, the algorithms such as the "Longest Common Subsequence" (LCS) are going to be used to efficiently compute the differences between two versions of a document. These differences can then be presented as "diff indications" to the users, showing what has been added, deleted, or modified.

**6. Managing Storage:** Foundry manages storage, periodic archival and / or cleanup of older versions. Foundry also has manual two step delete and prune options if the user chooses to remove data.

### How does Foundry enable customizable data ingestion for genomics research needs?

Data from third-party sources is often software-based and is usually ingested in various formats like excel sheets, images, and PDF files, particularly when it originates from hardware with web API support. Foundry, designed for broad data processing and analytics, can also handle standardized industry formats in specific sectors like genomics. Metadata attached to this data is typically sourced from Electronic Lab Notebook software or Research Electronic Data Software using secure, token-based communication. Foundry features a user-friendly interface, facilitating necessary collections and matching fields from APIs to the fields in the collection.

We offer standard normalized metadata tables and ETL pipelines, commonly used by many of our customers. However, we recognize that the unique needs and specific use cases of our customers necessitate customization and configuration. This understanding is where Foundry excels - it's designed with the flexibility and adaptability to meet diverse needs.

Foundry allows users to tailor the metadata and pipelines to align with their individual research goals. It empowers customers to modify metadata, adjust input and output parameters, integrate proprietary algorithms, and adapt workflows to suit specific datasets, thereby truly making the system their own.

To ensure a smooth and efficient customization process, our team of experts is always available to offer guidance and assistance. Moreover, we believe that customer feedback is invaluable, and we use it to continually enhance Foundry's capabilities. As a result, Foundry is constantly evolving and improving based on the changing needs and methods of the user community. This fosters a collaborative and symbiotic relationship between Foundry and its users, promoting shared growth and progress.

### How does Via Foundry handle metadata organization and data normalization?

Foundry’s metadata system ensures compliance with NCBI's GEO submission requirements, which are based on standards developed by the wider genomics research community. These standards enable data sharing and interoperability, and also enhance the reproducibility of scientific research.

**1.** The challenge of metadata organization lies in the complexity and variability of the data. For genomics and other biological research data, there is a need to capture a wide range of metadata including not just the raw data, but also factors such as experimental conditions, processing methods, and other relevant details. This creates a complex matrix of data to manage and organize.

The metadata is not only derived from the user entries. While the majority of metadata comes from the sequencing machinery and associated software, other crucial metadata sources include the biological source material, reagents, lab conditions, and even the researcher's notes and observations. In addition, post-processing of data can also generate its own metadata. Therefore, the metadata can come from a variety of sources, both human and machine-generated.

The propagation of new metadata across all samples is a dynamic process. Our system updates the metadata repository in real time as new data comes in. This helps ensure that the metadata for all samples remains up-to-date and consistent, even as new data is added.

**2.** Regarding normalization, indeed, there are challenges presented by disparate data sources, especially in terms of variability in format, structure, and semantics. Our system uses a combination of automated processes and manual curation to normalize the data across different sources.

Our normalization process typically involves the following steps: 

- First, the data is mapped to a common data model which provides a standard structure for the data. 
- Then, various the data transformation techniques are used to make the data more consistent, such as converting measurements to a standard unit or mapping variable names to a standard nomenclature.
- Lastly, quality checks are pefromed to ensure the consistency and reliability of the data.

To further enhance our data integration capabilities, wcommon normalized template metadata collections are used to serve as a starting point for every project. These templates contain the minimum information required to integrate different omic fields, providing a foundation for future expansion if needed. 

Moreover, to ensure the metadata is both interoperable and accurately interpreted across different systems, ontology support is incorprated into our fields. This means that the terms used in the metadata fields are linked to controlled vocabularies and standards used in the broader scientific community. This also allows users to add additional, specialized metadata fields to the system to meet their specific needs, while ensuring that this new data remains compliant with the established standards.

### How does Foundry enhance pipeline development and support interoperability in bioinformatics?

We have implemented specialized training sessions for developers, enabling scientists and bioinformaticians to seamlessly learn the art of pipeline development. By showcasing best-case scenarios and fostering the creation of reusable processes, we have significantly increased the efficiency of pipeline development. This optimization not only saves valuable time but also translates into tangible cost reductions for our clients.

A game-changer in our approach has been the removal of dependencies on pipeline managers. By standardizing the process development with clear input, output, and script sections, our platform empowers users to concentrate solely on the scientific analysis required, bypassing the typical challenges associated with pipeline management. As a result, our customers experience a dramatic boost in productivity and can focus on what truly matters – advancing groundbreaking research and discoveries.

Furthermore, Foundry is committed to interoperability. Foundry supports third-party pipelines such as nf-core and other nextflow pipelines.  Accordingly, our customers can also readily incorporate into Foundry historical pipelines they have created, or that they have  harnessed from the open source scientific community while simultaneously tapping into Foundry’s larger capabilities and powers.  
Lastly, other protocols used in the bioinformatic and computational biology communities, such as snakemake and WDL, are actively being incorporated into Foundry making Foundry a  /the  universal bioinformatic abstraction layer - eliminating pipeline and metadata complexity, accelerating data, analytical and multi-omics fusion and opening up deeper analytical possibilities that accelerates insights and their mission to advance therapeutic development.