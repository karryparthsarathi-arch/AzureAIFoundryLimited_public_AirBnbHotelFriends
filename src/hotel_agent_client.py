from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.agents.models import ListSortOrder
from config import FOUNDRY_PROJECT_ENDPOINT, FOUNDRY_AGENT_ID

class OakwoodHotelAgent:
    def __init__(self):
        self.project = AIProjectClient(credential=DefaultAzureCredential(), endpoint=FOUNDRY_PROJECT_ENDPOINT)
        self.agent = self.project.agents.get_agent(FOUNDRY_AGENT_ID)

    def ask(self, question):
        thread = self.project.agents.threads.create()
        self.project.agents.messages.create(thread_id=thread.id, role='user', content=question)
        run = self.project.agents.runs.create_and_process(thread_id=thread.id, agent_id=self.agent.id)
        messages = self.project.agents.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
        for m in messages:
            if m.role == 'assistant' and m.text_messages:
                return m.text_messages[-1].text.value
        return 'No response.'
