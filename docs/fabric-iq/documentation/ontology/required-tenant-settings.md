# Required tenant settings

Before you can use all ontology (preview) features, a [Fabric administrator](https://learn.microsoft.com/en-us/fabric/admin/roles) must enable certain settings in the **admin portal → tenant settings**.

| Setting | Required for | If not enabled |
| --- | --- | --- |
| **Enable Ontology item (preview)** | Creating ontology items | Errors when creating a new ontology. |
| **User can create Graph (preview)** | The graph associated with an ontology | Errors when accessing a newly created ontology (e.g. *"Unable to create the Ontology (preview) item"*). |
| **Data agent tenant settings** | Using ontology with a Fabric data agent | Errors when creating a data agent. |
| **Operations agent tenant settings** | Using ontology with an operations agent | Errors when creating an operations agent. |

## Enabling the settings

**Enable Ontology item (preview)** — required to create ontology items.

![Enabling the Ontology item setting in the Fabric admin portal.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/overview-tenant-settings/prerequisite-ontology.png){ .screenshot }

**User can create Graph (preview)** — required for the graph associated with an ontology.

![Enabling the Graph setting in the Fabric admin portal.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/overview-tenant-settings/prerequisite-graph.png){ .screenshot }

If the Graph setting isn't enabled, accessing a newly created ontology fails with an error such as *"Unable to create the Ontology (preview) item."*

![Error shown when graph permissions are missing.](https://learn.microsoft.com/en-us/fabric/iq/ontology/media/overview-tenant-settings/graph-error.png){ .screenshot }

## Next steps

Once your tenant is ready, start the [ontology tutorial](tutorial.md).

*Curated from [Microsoft Learn](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview-tenant-settings) · Updated 2026-04-30*
