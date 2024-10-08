from datetime import datetime

def find_latest_timestamp(data):
    """Find the latest timestamp in a list of dictionaries"""
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S') for entry in data]
    
    latest_timestamp = max(timestamps)
    latest_index = timestamps.index(latest_timestamp)
    
    
    return latest_timestamp.strftime('%Y-%m-%d %H:%M:%S'), latest_index