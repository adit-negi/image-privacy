import casbin
import pandas as pd

# Load the CSV file
file_path = '/Users/aditnegi/Downloads/ImgPrivacyStudyResponses.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Identifying scenario columns
# Replace with the actual names or indices of your scenario columns
scenario_columns = data.columns[10:len(data.columns)-2]
print(scenario_columns)

print(scenario_columns)
for idx, col in enumerate(scenario_columns):
    print(idx, col)
non_sensitive = ["wedding", "conference", "sports game", "university", "parade"]
sensitive = ["hospital", "religious", "kid"]
e = casbin.Enforcer("model.conf", "policy_rules.csv")
actions = ["post", "comment", "download"]
name_column = data.columns[1]
pvt_column = data.columns[4]
correctly_predicted = 0
total = 0

non_senstive_total = 0
non_sensitive_cnt = 0

sensitive_total = 0
sensitive_cnt = 0

background_total = 0
background = 0

relationship_total = 0
relationship = 0

temporal_total = 0
temporal = 0
cnt =0
for idx, col in enumerate(scenario_columns):
    for row_idx, response in enumerate(data[col]):
        cnt+=1
        name = data[name_column][row_idx]
        pvt = True if data[pvt_column][row_idx] == "Yes" else False
        actual, predict = "", ""
        actual = response
        if idx in [0,1,2,3,4,5,6,7,8,9,10,11,18,19,20]:

            allowed = False
            if "Post/View" in col:
                allowed = e.enforce(name, "spatial_nonsensitive", "view")
            if "Download" in col:
                allowed = e.enforce(name, "spatial_nonsensitive", "download")
            if "Comment" in col:
                allowed = e.enforce(name, "spatial_nonsensitive", "comment")
            if allowed:
                if pvt:
                    predict = "A"
                else:
                    predict = "E"
            else:
                predict = "F"
            
            if predict == "F":
                if actual == "F" or actual == "A" or actual == "G":
                    correctly_predicted += 1
                    non_sensitive_cnt += 1
            else:
                if actual == predict:
                    correctly_predicted += 1
                    non_sensitive_cnt += 1
            print("actual", actual, "predict", predict)
            total += 1
            non_senstive_total += 1


        if idx in [12,13,14,15,16,17]:

            allowed = False
            if "Post/View" in col:
                allowed = e.enforce(name, "spatial_sensitive", "view")
            if "Download" in col:
                allowed = e.enforce(name, "spatial_sensitive", "download")
            if "Comment" in col:
                allowed = e.enforce(name, "spatial_sensitive", "comment")
            if allowed:
                if pvt:
                    predict = "A"
                else:
                    predict = "E"
            else:
                predict = "F"
        
            if predict == "F":
                if actual == "F" or actual == "A" or actual == "G":
                    correctly_predicted += 1
                    sensitive_cnt += 1
            else:
                if actual == predict:
                    correctly_predicted += 1
                    sensitive_cnt += 1
            total += 1
            sensitive_total += 1



        if idx in [33,34,35,36,37,38]:
            allowed = False
            if "Post/View" in col:
                allowed = e.enforce(name, "background", "view")
            if "Download" in col:
                allowed = e.enforce(name, "background", "download")
            if "Comment" in col:
                allowed = e.enforce(name, "background", "comment")
            if allowed:
                if pvt:
                    predict = "A"
                else:
                    predict = "E"
            else:
                predict = "F"
        
            if predict == "F":
                if actual == "F" or actual == "A" or actual == "G":
                    correctly_predicted += 1
                    background += 1
            else:
                if actual == predict:
                    correctly_predicted += 1
                    background += 1
            total += 1
            background_total += 1


        
        if idx in [45,46,47]:
            allowed = False
            if "Post/View" in col:
                allowed = e.enforce(name, "relationship_friend", "view")
            if "Download" in col:
                allowed = e.enforce(name, "relationship_friend", "download")
            if "Comment" in col:
                allowed = e.enforce(name, "relationship_friend", "comment")
            if allowed:
             
                predict = "E"
            else:
                predict = "F"
        
            if predict == "F":
                if actual == "F" or actual == "A" or actual == "G":
                    correctly_predicted += 1
                    relationship += 1
            else:
                if actual == predict:
                    correctly_predicted += 1
                    relationship += 1
            total += 1
            relationship_total += 1


        if "mutual" in [42, 43, 44]:
            allowed = False
            if "Post/View" in col:
                allowed = e.enforce(name, "relationship_mutual", "view")
            if "Download" in col:
                allowed = e.enforce(name, "relationship_mutual", "download")
            if "Comment" in col:
                allowed = e.enforce(name, "relationship_mutual", "comment")
            if allowed:
                if pvt:
                    predict = "A"
                else:
                    predict = "E"
            else:
                predict = "F"
        
            if predict == "F":
                if actual == "F" or actual == "A" or actual == "G":
                    correctly_predicted += 1
                    relationship += 1
            else:
                if actual == predict:
                    correctly_predicted += 1
                    relationship += 1
            total += 1
            relationship_total += 1



        if idx in [39,40,41]:
            allowed = False
            if "Post/View" in col:
                allowed = e.enforce(name, "relationship_random", "view")
            if "Download" in col:
                allowed = e.enforce(name, "relationship_random", "download")
            if "Comment" in col:
                allowed = e.enforce(name, "relationship_random", "comment")
            if allowed:
                if pvt:
                    predict = "A"
                else:
                    predict = "E"
            else:
                predict = "F"
            actual = response
            if predict == "F":
                if actual == "F" or actual == "A" or actual == "G":
                    correctly_predicted += 1
                    relationship += 1
            else:
                if actual == predict:
                    correctly_predicted += 1
                    relationship += 1
            total += 1
            relationship_total += 1

        if idx in [21,22,23,24,25,26,27,28,29,30,31,32]:
            allowed = False
            if "Post/View" in col:
                allowed = e.enforce(name, "temporal_weekend", "view")
            if "Download" in col:
                allowed = e.enforce(name, "temporal_weekend", "download")
            if "Comment" in col:
                allowed = e.enforce(name, "temporal_weekend", "comment")
            if allowed:
                if pvt:
                    predict = "A"
                else:
                    predict = "E"
            else:
                predict = "F"
        
            if predict == "F":
                if actual == "F" or actual == "A" or actual == "G":
                    correctly_predicted += 1
                    temporal += 1
            else:
                if actual == predict:
                    correctly_predicted += 1
                    temporal += 1
            total += 1
            temporal_total += 1


        #print(actual, predict)
print(total, correctly_predicted)
print("Non-sensitive", non_sensitive_cnt, non_senstive_total)
print("Sensitive", sensitive_cnt, sensitive_total)
print("Background", background, background_total)
print("Relationship", relationship, relationship_total)
print("Temporal", temporal, temporal_total)
print(cnt)


# A - Allow if the photo is going to be private

# B - Photo can be reshared

# C - Person is going to be tagged in the photo

# D - Location of the photo is going to be available

# E - Okay with posting regardless of conditions.

# F - Okay if photo is ephemeral(Will be auto-deleted after a week)

# G - Not okay with any action

# 50 * 20 * 3 