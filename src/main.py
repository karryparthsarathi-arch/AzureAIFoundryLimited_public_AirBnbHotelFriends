from hotel_agent_client import AirBnbOurFriendsHotelAgent

agent = AirBnbOurFriendsHotelAgent()
while True:
    q = input('Guest: ')
    if q.lower()=='exit': break
    print(agent.ask(q))
