import datetime

class CampaignManager:
    def __init__(self):
        self.campaigns = []

    def add_campaign(self, campaign_id, name, end_date_str):
        """Adds a new campaign with a specified end date string."""
        try:
            # Parse the end date string into a datetime object
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
            self.campaigns.append({
                "id": campaign_id,
                "name": name,
                "end_date": end_date
            })
            print(f"Added campaign '{name}' (ID: {campaign_id}) ending on {end_date.strftime('%Y-%m-%d')}")
        except ValueError:
            print(f"Error: Invalid date format for campaign '{name}'. Use YYYY-MM-DD.")

    def is_campaign_active(self, campaign):
        """Checks if a campaign is currently active based on its end date."""
        # A campaign is active if its end date is in the future relative to now
        return campaign["end_date"] >= datetime.datetime.now()

    def extend_campaign_duration(self, campaign_id, new_end_date_str):
        """
        Extends the end date of a specified campaign.
        This directly illustrates the article's core concept of extending campaign durations.
        """
        for campaign in self.campaigns:
            if campaign["id"] == campaign_id:
                try:
                    new_end_date = datetime.datetime.strptime(new_end_date_str, "%Y-%m-%d")
                    
                    # Optional: Prevent extending to a date that's already in the past
                    if new_end_date < datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0):
                         print(f"Warning: New end date {new_end_date_str} for '{campaign['name']}' is in the past. Extension not applied.")
                         return False

                    old_end_date = campaign["end_date"]
                    campaign["end_date"] = new_end_date # Update the campaign's end date
                    print(f"\n--- Campaign '{campaign['name']}' (ID: {campaign_id}) extended ---")
                    print(f"Old end date: {old_end_date.strftime('%Y-%m-%d')}")
                    print(f"New end date: {new_end_date.strftime('%Y-%m-%d')}")
                    return True
                except ValueError:
                    print(f"Error: Invalid new end date format '{new_end_date_str}'. Use YYYY-MM-DD.")
                    return False
        print(f"Campaign with ID {campaign_id} not found.")
        return False

    def display_campaign_status(self):
        """Displays the current status of all campaigns."""
        print("\n--- Current Campaign Status ---")
        for campaign in self.campaigns:
            status = "Active" if self.is_campaign_active(campaign) else "Expired"
            print(f"ID: {campaign['id']}, Name: '{campaign['name']}', Ends: {campaign['end_date'].strftime('%Y-%m-%d')}, Status: {status}")
        print("-----------------------------\n")

# --- Main execution ---
if __name__ == "__main__":
    manager = CampaignManager()

    # Add some initial campaigns
    manager.add_campaign(101, "Early Bird Discount", "2023-12-31") # Initially expired
    manager.add_campaign(102, "Summer Sale", "2024-08-15") # Active
    manager.add_campaign(103, "New Product Launch", "2024-07-01") # Active
    manager.add_campaign(104, "Winter Clearance", "2025-01-31") # Active

    manager.display_campaign_status()

    # Simulate extending a campaign duration
    print("\n--- Simulating Campaign Extension ---")
    # This call directly demonstrates the article's main technical concept: extending a campaign's end date.
    manager.extend_campaign_duration(101, "2025-06-30") # Extend the expired 'Early Bird Discount'
    manager.extend_campaign_duration(103, "2024-09-30") # Extend 'New Product Launch'

    manager.display_campaign_status()

    # Try to extend with a past date (should show warning)
    manager.extend_campaign_duration(102, "2024-01-01")

    manager.display_campaign_status()

    # Show only active campaigns after extensions
    print("\n--- Currently Active Campaigns ---")
    for campaign in manager.campaigns:
        if manager.is_campaign_active(campaign):
            print(f"ID: {campaign['id']}, Name: '{campaign['name']}', Ends: {campaign['end_date'].strftime('%Y-%m-%d')}")
    print("----------------------------------")