from haystack.telemetry import tutorial_running

tutorial_running(24)

from getpass import getpass

model_api_key = getpass("Enter model provider API key:")

from haystack.nodes import PromptNode

model_name = "OpenAssistant/oasst-sft-1-pythia-12b"
prompt_node = PromptNode(model_name, api_key=model_api_key, max_length=256)

from haystack.agents.memory import ConversationSummaryMemory

summary_memory = ConversationSummaryMemory(prompt_node)

from haystack.agents.conversational import ConversationalAgent

conversational_agent = ConversationalAgent(prompt_node=prompt_node, memory=summary_memory)
