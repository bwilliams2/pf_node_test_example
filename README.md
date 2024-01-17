# pf_node_test_example

This flow example utilizes a property from a node output as a node input value (e.g., `${node.output.property}`).

`test_flow.py` runs a full flow test and a node specific test on the `echo` node that utilizes a node output property as input (`${echo_object.output.echo}`)


# Current state

Running the flow with `python test_flow.py` raises a `promptflow.executor._errors.InvalidReferenceProperty` on line 7.

```
promptflow.executor._errors.InvalidReferenceProperty: Flow execution failed. Invalid property 'echo' when accessing the node 'echo_object'. Please check the property and try again.
```

The full flow test and `echo_object` node test both execute successfully but test for `echo` node does not successfully parse input reference to "echo".

# Desired State

Execution of `python test_flow.py` completes successfully with provided input data.