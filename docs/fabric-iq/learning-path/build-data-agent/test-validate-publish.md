# Test, validate, and publish

With the agent created and configured, you validate its responses, refine instructions when needed, then publish and share it.

## Test with natural-language questions

The chat pane is where users interact with the agent in plain English. Clinical staff might ask:

- *"Which patients are admitted to rooms in the Surgical Services department?"*
- *"How many rooms in the Surgical Services department are currently occupied?"*
- *"Which vital-sign monitors are assigned to rooms in the Surgical Services department?"*

Every response includes a **steps dropdown** — expand it to see how the agent interpreted your question and whether it queried the right entities.

## Examine the steps and generated GQL

Expanding the steps dropdown reveals three things: the **entity types and relationships** the agent identified, the **GQL query** it generated, and the **intermediate reasoning steps** mapping your language to graph concepts.

![The steps dropdown expanded in the chat pane, showing the generated GQL query and reasoning steps.](https://learn.microsoft.com/en-us/training/wwl-data-ai/build-fabric-data-agent-ontology/media/data-agent-steps.png){ .screenshot }

If the steps show the wrong entity types or relationships, there's likely a gap in the instructions. Because the agent shows its work, it's straightforward to identify and correct.

## Refine with instructions

When an ontology is the data source, **instructions** are how you improve accuracy. Microsoft's guidance on iterative improvement identifies four high-impact areas:

- **Terminology** — map the words users say to the entity types and relationships in the ontology.
- **Reasoning steps** — give the agent a logical path for common questions (which entity to start from, which relationships to traverse).
- **Response behaviour** — set expectations for formatting (counts, lists, summaries, level of detail).
- **Scope** — define what the agent should and shouldn't answer.

Re-test the same question after updating instructions to confirm the change helped. This cycle — test, examine steps, refine, repeat — shapes the agent to reliably serve its audience.

## Publish the agent

When testing confirms accurate answers, publishing creates a stable version for colleagues. Publishing requires a **description**, which both guides colleagues on what the agent answers and lets external AI systems (like Copilot Studio) discover and invoke it. A good description explains the agent's scope **and** its limitations.

!!! tip "Let the agent draft its own description"
    Ask the agent *"What can you help me with?"* — it generates a summary from its ontology and instructions, a useful starting point.

After publishing, two versions exist side by side: an editable **draft** (for continued refinement) and the stable **published** version colleagues access via the shared link. A version toggle lets you compare them.

## Share the agent

Sharing generates a link with three permission levels:

- **No extra permission** (default) — query the **published version only**; no access to configurations, instructions, or the draft.
- **View details** — view configurations and instructions of both versions and query both, but not edit or publish.
- **Edit and view details** — full access to view, edit, query, and publish.

![The share dialog showing the permission level options for the data agent.](https://learn.microsoft.com/en-us/training/wwl-data-ai/build-fabric-data-agent-ontology/media/data-agent-share.png){ .screenshot }

!!! warning "Recipients need access to the underlying data"
    For ontology-backed agents, recipients also need read access to the ontology item and the data it's bound to. Without those permissions, queries fail even with a valid link.

With the agent published and shared, clinical staff can ask questions like *"Which patients are admitted to rooms in the Surgical Services department?"* and get answers in seconds — without writing a query.
