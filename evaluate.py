import numpy as np

# fill in the output file name
with open("evaluate/.txt") as f:
    lines = f.readlines()

graspPush = []
list_of_outcomes = []
pushes = []
graspsPushes = []
for line in lines:
    if 'Grasp successful:' in line:
        graspPush.append(line)
    if 'Push successful:' in line:
        graspPush.append(line)
for line in graspPush:
    words = line.split()
    list_of_outcomes.append(words)
    if words[0] == "Grasp" and words[-1] == "True":
        graspsPushes.append(1)
    if words[0] == "Grasp" and words[-1] == "False":
        graspsPushes.append(2)
    if words[0] == "Push" and words[-1] == "True":
        graspsPushes.append(3)
    if words[0] == "Push" and words[-1] == "False":
        graspsPushes.append(4)

max_attempts = 5
completion = []
GraspsuccessCountTotal = []
grasp_success_rate = []
efeciencyList = []
motion_numberTotal = []
GraspFailCount = 0
PushCount = 0
counter = 0
GraspsuccessCount = 0
GraspFailCountTotal  = 0
start_flag = True
total_grasp = 0
old_PushCount = float('NaN')
PushCountOld = 0
for state in graspsPushes:
    counter += 1

    if state == 2: # grasp false
        start_flag = False
        GraspFailCountTotal += 1
        GraspFailCount += 1
        total_grasp += 1
        GraspsuccessCountTotal.append(0)

    if state == 1: # grasp true
        start_flag = True
        GraspsuccessCount += 1
        total_grasp += 1

        if GraspFailCount < max_attempts:
            completion.append(1)
            GraspsuccessCountTotal.append(1)
            motion_numberTotal.append(PushCount - PushCountOld)
            PushCountOld = PushCount
        else:
            completion.append(0)
            GraspsuccessCountTotal.append(0)
        GraspFailCount = 0

    if state == 3 or state == 4: # push true or false
        start_flag = False
        PushCount += 1

final_completion = (sum(completion)/len(completion))*100
SE_final_completion = np.std(completion, ddof=1) / np.sqrt(np.size(completion))
print("final_completion %", final_completion)
print("SE completion", SE_final_completion * 100)
print()
final_GraspSuccessRate = (GraspsuccessCount/(GraspsuccessCount+GraspFailCountTotal))*100
SE_GraspsuccessCountTotal = np.std(GraspsuccessCountTotal, ddof=1) / np.sqrt(np.size(GraspsuccessCountTotal))
print("final_GraspSuccessRate %", final_GraspSuccessRate)
print("SE final_GraspSuccessRate", SE_GraspsuccessCountTotal * 100)
print()
motion_number = (len(graspsPushes)-(total_grasp))/GraspsuccessCount
SE_motion_numberTotal = np.std(motion_numberTotal, ddof=1) / np.sqrt(np.size(motion_numberTotal))
print("motion_number", motion_number)
print("SE_motion_numberTotal", SE_motion_numberTotal)
print()

