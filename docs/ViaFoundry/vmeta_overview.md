# Brief Overview

## What is Vmeta?

Vmeta is a standalone metadata tracking system that integrates
automated data processing pipelines and data analysis and visualization
modules to support a wide variety of use cases from basic to complex,
multi-organization/lab-based projects. It seamlessly communicates with
data processing servers (e.g.
[Via Foundry](https://viafoundry.com)) and analysis and
visualization servers (e.g. ViaPortal)

### Benefits of Vmeta's design

-   **Flexible Design:** Define project collection and fields flexibly
    with a software architecture developed by the MongoDB data management system. MongoDB supports a flexible data field schema where users can efficiently update the data fields of any entry or the information of the associated metadata.
-   **Web APIs:** Vmeta also incorporates extensive and secure
    token-based Web APIs to make the metadata and processed data
    available to its users in accordance with FAIR standards.
-   **Integration with 3rd parties:** Vmeta is fully integrated with
    the data browsing and preprocessing platforms ViaPortal and Via Foundry, but in
    addition to these platforms, can integrate other pipeline management and data
    portal systems for data preprocessing and
    analysis.
-   **Event-based Management:** Events are specific types of insertion,
    deletion and edit operations defined by the project
    administrators to allow internal users to manage multiple specifically permitted fields and collections in an organized manner.
-   **Validation with Ontology Servers:** Data fields are linked to ontology servers or user admin-specified dictionaries, which allows the standardized collection of information from each user.
-   **Share:** Each project, collection, field, and document in Vmeta
    has dynamic permission controls, enabling project admins to update or submit operations to, and limit the access of specified groups or users.

## Who is Vmeta for?

Vmeta is designed for a wide variety of users, from bench biologists to expert bioinformaticians.

-   **Data submission** requires no programming knowledge whatsoever. We've created an intuitive event-based process to simplify and streamline this process.
-   **Metadata setup** only requires basic database knowledge and
    familiarity with MongoDB to effectively use its operators. You
    don't need to learn all of MongoDB's syntax; instead, you can
    easily focus on the field settings. The rest (e.g. creating parent-child relationships with collections,
    delivering data from ontology servers, etc.) is handled by Vmeta.
    
