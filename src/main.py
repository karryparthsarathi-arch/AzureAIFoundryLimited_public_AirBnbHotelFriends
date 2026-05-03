from hotel_agent_client import OakwoodHotelAgent

agent = OakwoodHotelAgent()
while True:
    q = input('Guest: ')
    if q.lower()=='exit': break
    print(agent.ask(q))
