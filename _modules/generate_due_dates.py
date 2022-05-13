def create_recurring_dates(start, stop, num_weeks):
    """
    Given the start and stop dates, each a tuple
    in the (M, DD) format.
    num_weeks is an integer indicating for how many
    weeks to generate the schedule. If the `stop` is
    sooner, then the processing ends before num_weeks
    is reached.
    `start` should be the first Monday of the
    start week.
    Prints the Markdown table of the deadlines, which
    can be manually copied wherever necessary.
    Example of running the function:
    create_recurring_dates((3, 28), (6, 10), 9)
    The above function call creates the schedule for 
    9 weeks of the quarter
    starting on March 28 (3, 28) and ending on
    June 10 (6, 10).
    TODO: in the function body, set the correct days
    for when the assignments are due.
    """
    months = {
        1: 31,
        2: 28, # unless it's a leap year
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    month_name = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    days = {
        1: "Mon",
        2: "Tue",
        3: "Wed",
        4: "Thu",
        5: "Fri",
        6: "Sat",
        7: "Sun"
    }
    day_names = ['M', 'T', 'W', 'R', 'F', 'S', 'S']

# TOOD: decide on the days when things are due
    pa_due = 1 # 'M' # Monday
    ca_due = 2 # 'T'
    la_due = 3 # 'W'
    ch_due = 4
    ref_due = 7

    start_month, start_monday = start
    week = 1
    end_month, end_day = stop
    num_days = 7

    pa_header = "**PA**{: .label .label-orange}"
    ca_header = "**CA**{: .label .label-blue}"
    la_header = "**LA**{: .label .label-green}"
    ch_header = "**Chkpt**{: .label .label-green}"
    
    # print the header
    print(f"| Week | {pa_header} ({days[pa_due]}) |"
          f" {ca_header} ({days[ca_due]}) |"
          f" {la_header} ({days[la_due]}) |"
          f" {ch_header} |"
          f" Refl. ({days[ref_due]}) | ")
    print("|--- |" + "--- |" + "--- |" + "--- |" + "--- | ")

    month = start_month
    cur_day = start_monday
    while week <= num_weeks:
        print(f"| [Week {week}](#week-{week}) ", end="|")
        pa_date = ca_date = la_date = ch_date = ref_date = ""
        for day in range(1, num_days+1):
            if cur_day > months[month]:
                cur_day = cur_day - months[month] # e.g., 10/31->11/1
                month += 1
            date_str = month_name[month] + " " + str(cur_day)
            if day == pa_due:
                pa_date = date_str
            elif day == ca_due:
                ca_date = date_str
            elif day == la_due:
                la_date = date_str
            elif day == ch_due:
                ch_date = date_str
            elif day == ref_due:
                ref_date = date_str

            cur_day += 1
        print(f" {pa_date} | {ca_date} | {la_date} | {ch_date} | {ref_date} |")
        week += 1
        if month == end_month and cur_day >= end_day:        
            break # Finish processing
            
            

            

    
        
