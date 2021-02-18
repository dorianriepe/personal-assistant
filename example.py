from wrapper.google_calendar import Calendar

calendar = Calendar("DHBW - Projekte")

print("> Calendar ID: \t"+calendar.calendar_id+"\n")
print("> Todays Events: \n"+str(calendar.get_events_today())+"\n")
print("> First Event Tomorrow: \n"+str(calendar.get_first_event_tomorrow())+"\n")