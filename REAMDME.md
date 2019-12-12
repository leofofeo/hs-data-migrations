# HubSpot Data Migrations 2.0

## A more OOP-focused, reworked version of the previous HubSpot migration script

I previously wrote [a script](https://github.com/leofofeo/migrations-sample) for migrating data out of one HubSpot portal and into another using HubSpot's APIs. While the script is sufficient for getting most relevant data in and out cleanly, it lacks structure and heavily violates the DRY principle. The goal of rewriting it is to use class-based approach for the sake of reusability, along with unit tests to help with the integrity of the code. In addition, there were some functions and logic tied to specific endpoints like lists and workflows that fell short of the full automation goal. The plan is to flesh those out so that this program truly is a one-click data migration process.

The longer term vision for the more robust program outlined above is to add a simple front-end, using either React or Flask's own templating engine. This will allow users to navigate to the program in the form of a web ui and input the two critical pieces of data necessary for the program to run: the two API keys (one for each of the portals involved in the data migration.)

Even beyond that, there's a good use case for the app to be used as the intermediary between the two HubSpot portals once it's got the necessary server-side logic. Some of HubSpot's more sophisiticated endpoints require OAuth rather than simple API keys; adding this functionality to this program would allow for the export or import of that data, as well as create a pathway for webhooks and polling if one wanted to create a steady stream of data from one to the other (e.g., an integration to keep a sandbox portal up-to-date and mirroring the real portal).
