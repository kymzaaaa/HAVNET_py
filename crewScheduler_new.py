class ActivityImpl:
    def __init__(self, activity_id, location, duration):
        self.activity_id = activity_id
        self.location = location
        self.duration = duration

def crew_scheduler_new(mission_duration_in_hours, location):
    number_of_days = mission_duration_in_hours // 24
    # No laundry
    standard_day_schedule = [
        ActivityImpl(1, location, 1),
        ActivityImpl(2, location, 1),
        ActivityImpl(3, location, 1),
        ActivityImpl(4, location, 1),
        ActivityImpl(5, location, 1),
        ActivityImpl(6, location, 10),
        ActivityImpl(7, location, 1),
        ActivityImpl(8, location, 8)
    ]
    # Laundry
    laundry_days = range(7, number_of_days + 1, 7)  # Starting from day 7 and every 7 days thereafter
    laundry_day_schedule = [
        ActivityImpl(1, location, 1),
        ActivityImpl(2, location, 1),
        ActivityImpl(3, location, 1),
        ActivityImpl(4, location, 1),
        ActivityImpl(5, location, 1),
        ActivityImpl(6, location, 9),  # Shorter IVA by 1 hr to accommodate laundry
        ActivityImpl(7, location, 1),
        ActivityImpl(8, location, 8),
        ActivityImpl(9, location, 1)
    ]
    # Make crew schedule
    crew_schedule = []
    for day in range(1, number_of_days + 1):
        if day in laundry_days:
            crew_schedule.extend(laundry_day_schedule)
        else:
            crew_schedule.extend(standard_day_schedule)
    
    return crew_schedule, [activity.activity_id for activity in crew_schedule]

# Example usage:
location = "Mars Habitat"
mission_duration = 24 * 30  # 30 days mission
crew_schedule, activity_index_vec = crew_scheduler_new(mission_duration, location)
print("Crew Schedule:", crew_schedule)
print("Activity Index Vector:", activity_index_vec)
