# Cortex

## What Is Cortex?

Via Foundry is designed to simplify the design, development, and execution of pipelines. But data doesn't always stop at the pipeline output. Often, the next step is analysis, prediction, or reporting. That's where Cortex comes in.

Cortex is Via Foundry's AI layer. It lets you connect to AI platforms, call models, and generate reports, all without leaving your workflow.

## What Can You Do With Cortex?

With Cortex, you can integrate AI processes directly into your pipelines. Currently supported platforms:

- **Vertex AI**: Google Cloud's managed AI platform
- **Tamarind AI**: Specialized models for biological data

Support for **Amazon SageMaker** is coming soon.

## Who Is Cortex For?

If you're a researcher or data scientist who wants to go from raw pipeline output to AI-powered insights in one place, Cortex is for you. No separate tooling. No switching between platforms.

---

## Getting Started

Before using Cortex, you need to connect your AI platform credentials to Via Foundry. This is a one-time setup per platform.

### Tamarind AI

1. Go to **Profile > Integration Tokens**
2. Click **New Token** and select Tamarind as the platform
3. Enter your Tamarind API key and save

> 📷 *Screenshot placeholder*

### Vertex AI

Via Foundry supports two ways to connect your Vertex AI account.

**Option 1: Service Account JSON**

If you have a GCP service account credentials file:

1. Go to **Profile > Credentials**
2. Upload your service account JSON file
3. Save your credentials

> 📷 *Screenshot placeholder*

**Option 2: GCP Cloud Integration**

If you don't have a service account JSON file, Via Foundry can integrate directly with your GCP account. Contact our support team to get this set up.

---

## Creating an AI Process

An AI process works just like a regular process in Via Foundry. You create it once, then use it inside any pipeline.

When you create an AI process, Via Foundry sets it up with a default script and injects the required credentials automatically. From there, the process can make REST API calls to the selected platform. If you want to go further, you can customize the script using your preferred programming language and SDK.

### Step 1: Open Cortex

Navigate to **Cortex** from the main menu. This is your hub for all AI processes.

> 📷 *Screenshot placeholder*

### Step 2: Create a New Process

Click **New AI Process**. You will be prompted to give it a name and description.

### Step 3: Select a Platform

Choose the AI platform you want to use. Currently available options are:

- **Vertex AI**
- **Tamarind AI**

### Step 4: Choose a Model

Once you select a platform, you will see a list of available models. Pick the one that fits your use case.

> 📷 *Screenshot placeholder*

### Step 5: Add It to a Pipeline

Your AI process is now ready to use. Head to the pipeline builder and add it just like any other process.