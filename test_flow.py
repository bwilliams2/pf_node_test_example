
from promptflow import PFClient

pf = PFClient()
pf.test("flow/flow.dag.yaml", inputs=({"text": "Test text"}))
pf.test("flow/flow.dag.yaml", inputs={"input1": "Hello"}, node="echo_object")
pf.test("flow/flow.dag.yaml", inputs={"echo": "Hello"}, node="echo")