from datetime import datetime, timedelta


def calculate_time_difference(start_time, end_time):
    # Convert input strings to datetime objects
    start_time = datetime.strptime(start_time, "%H:%M:%S")
    end_time = datetime.strptime(end_time, "%H:%M:%S")

    # Calculate the difference
    time_difference = end_time - start_time

    # Extract components of the time difference
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60
    seconds = time_difference.seconds % 60

    # Print the results
    print(
        f"Time difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

    # Return total seconds for further calculations
    return time_difference.total_seconds()


# Example usage
start_time = "09:00:00"
end_time = "17:30:45"

difference_in_seconds = calculate_time_difference(start_time, end_time)
print(f"\nTotal seconds: {difference_in_seconds}")
