# Tutorial: Run Submission through API

In this tutorial, we will guide you through the process of submitting runs using the provided Python scripts `triggerRun.py` and `getRuns.py`. These scripts interact with the ViaFoundry API to trigger a pipeline run and retrieve the list of runs, respectively.

## Prerequisites

Before you start, make sure you have the following:

- Python installed on your machine (version 3.6 or later).
- ViaFoundry account credentials (email and password).

## Step 1: Download the Scripts

Download the following Python scripts from the provided links:

- [triggerRun.py](../files/triggerRun.py)
- [getRuns.py](../files/getRuns.py)

Save these files to your local machine.

## Step 2: Set Environment Variables

Open a terminal and set the required environment variables for ViaFoundry credentials:

```bash
export VIAFOUNDRY_EMAIL=your_email@example.com
export VIAFOUNDRY_PASSWORD=your_password
```

Replace `your_email@example.com` and `your_password` with your ViaFoundry account credentials.

## Step 3: Update `triggerRun.py` with Run Details

Open the `triggerRun.py` file and update the `run_settings` dictionary with your specific run details:

```python
run_settings = {
    "doc": {
        "name": "New Run Name",
        "tmplt_id": 861,
        "in": {
            "testFile": "s3://viafoundry/run_data/test_data/models/data/AmpC_screen_table_subset_10K.csv",
            "numLine": "3000",
            "Header": "smiles"
        }
    }
}
```

Replace the values in the `run_settings` dictionary with the specific configuration for your run. In this context, the term `tmplt_id` refers to the template run ID. The global pipeline inputs include parameters such as `testFile`, `numLine`, and `Header`. Generally, the remaining pipeline parameters will be automatically derived from the template run parameters.

## Step 4: Run `triggerRun.py`

Execute the following command in the terminal to trigger the pipeline run:

```bash
python triggerRun.py
```

This will log in to ViaFoundry, obtain an access token, and trigger the specified pipeline run.

## Step 5: Run `getRuns.py`

Execute the following command in the terminal to retrieve the list of runs:

```bash
python getRuns.py
```

This will log in to ViaFoundry, obtain an access token, and print the list of runs.

Congratulations! You have successfully triggered a pipeline run and retrieved the list of runs using the ViaFoundry API.
