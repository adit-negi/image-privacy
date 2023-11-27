class UserPreferences:
    def __init__(self, group_setting_photos, public_private, tag_comment_permissions, time_bound, work_photos, family_photos, social_events, travel_photos, background_in_others_photos, photos_by_friends):
        self.group_setting_photos = group_setting_photos
        self.public_private = public_private
        self.tag_comment_permissions = tag_comment_permissions
        self.time_bound = time_bound
        self.work_photos = work_photos
        self.family_photos = family_photos
        self.social_events = social_events
        self.travel_photos = travel_photos
        self.background_in_others_photos = background_in_others_photos
        self.photos_by_friends = photos_by_friends


import pandas as pd

# Load the CSV file
file_path = '/Users/aditnegi/Downloads/ImgPrivacyStudyResponses.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# read from csv and construct policy.csv 
preference_columns = data.columns[5:10]
name_column = data.columns[1]
action_preferences = {}
cols_dict = {0:"action", 1:"backgroud", 2:"relationship", 3:"temporal", 4:"spatial"}
policy_arr = []
for idx, col in enumerate(preference_columns):
    col_name = cols_dict[idx]
  
    for row_idx, response in enumerate(data[col]):
        name = data[name_column][row_idx]
        policy = (name, col_name, response.split())
        if col_name == "action":
            action_preferences[name] = response.split()
        if col_name == "backgroud":
      
            
            if response == "Yes":
                if 'Comments' in action_preferences[name]:
                    policy_arr.append(["p", name, "background", "comment"])
                    policy_arr.append(["p", name, "background", "view"])
                if 'Downloads' in action_preferences[name]:
                    policy_arr.append(["p", name, "background", "download"])
         
        if col_name == "relationship":
            for respo in response.split():
                if respo == "Close":
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "relationship_close", "comment"])
                        policy_arr.append(["p", name, "relationship_friend", "view"])
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "relationship_close", "download"])
                if respo == "Friends":
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "relationship_friend", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "relationship_friend", "comment"])
                        policy_arr.append(["p", name, "relationship_friend", "view"]) 
                
                if respo == "Mutual":
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "relationship_mutual", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "relationship_mutual", "comment"])
                        policy_arr.append(["p", name, "relationship_mutual", "view"])
                if respo == "Random":
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "relationship_random", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "relationship_random", "comment"])
                        policy_arr.append(["p", name, "relationship_random", "view"])
        if col_name == "temporal":
            for respo in response.split():
                if respo == "Holidays":
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "temporal_holidays", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "temporal_holidays", "comment"])
                        policy_arr.append(["p", name, "temporal_holidays", "view"])
                if respo == "Work":
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "temporal_work", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "temporal_work", "comment"])
                        policy_arr.append(["p", name, "temporal_work", "view"])
                if respo == "Night":
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "temporal_night", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "temporal_night", "comment"])
                        policy_arr.append(["p", name, "temporal_night", "view"])
                if respo == "Weekend":
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "temporal_weekend", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "temporal_weekend", "comment"])
                        policy_arr.append(["p", name, "temporal_weekend", "view"])
        if col_name == "spatial":
            for respo in response.split():
                if respo in ['Work/School', "Hospital", "Religous"]:
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "spatial_sensitve", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "spatial_sensitive", "comment"])
                        policy_arr.append(["p", name, "spatial_sensitive", "view"])
                else:
                    if 'Downloads' in action_preferences[name]:
                        policy_arr.append(["p", name, "spatial_nonsensitive", "download"])
                    if 'Comments' in action_preferences[name]:
                        policy_arr.append(["p", name, "spatial_nonsensitive", "comment"])
                        policy_arr.append(["p", name, "spatial_nonsensitive", "view"])
 
                    
print(policy_arr)

# Converting the nested list to a DataFrame
policy_df = pd.DataFrame(policy_arr, columns=['Prefix', 'Name', 'Condition', 'Action'])

# Define the path where you want to save the CSV file
csv_file_path = 'policy_rules.csv'

# Saving the DataFrame as a CSV file
policy_df.to_csv(csv_file_path, index=False)
