# Events Guide

This guide will walk you through the details of creating an event in a
project.

After defining fields, you\'re now ready to create event forms to
insert/update fields from multiple collections. Let\'s go through the
basics of the event section.

## Insert Events

1.  Please click the `admin` button at the top and select your project.
2.  Click the `All Events` tab of your project.
3.  Click the `Insert` button and enter the `Event Name`.
4.  Choose your target collection from the dropdown and choose the
    behavior of the form. Insert, Update, or Multiple (for Multiple
    Insert) options are available.
5.  Choose the field to belong to the selected collection.
6.  Click the \"Plus\" button to insert a new field into the event form
    and choose a new field.
7.  To insert another collection of data, please click the
    `Insert Group` button.
8.  Read/Write permission of this form could be adjusted with the
    Permissions section at the bottom.

![image](images/insert-events.png){.align-center width="99.0%"}

## Insert New Run Event

You can create an `New Run` event to simply run submissions. Here are
the expected values for this event.

-   **Event Name:** New Run
-   **Collection:** Runs

  -----------------------------------------------------------------------
  Fields
  -----------------------------------------------------------------------
  Name (required)

  Server ID (requiredref.)

  Run Environment

  Template Run ID

  Inputs

  Outputs

  Work Directory

  Run URL
  -----------------------------------------------------------------------

Example From from Dmeta User Interface:

![image](images/insert-run-event.png){.align-center width="99.0%"}
