The official repository for the paper: 
# Self-Supervised Learning for Joint Pushing and Grasping Policies in Highly Cluttered Environments

Demo Video: [YouTube](https://www.youtube.com/watch?v=EUrUt9XO7sI&t=1s&ab_channel=KamalMokhtar)

Robots often face situations where grasping a goal object is desirable but not feasible due to other present objects preventing the grasp action. We present a deep  Reinforcement Learning approach to learn grasping and pushing policies for manipulating a goal object in highly cluttered environments to address this problem.
In particular, a dual reinforcement learning model approach is proposed, which presents high resilience in handling complicated scenes, reaching
$98\%$ task completion using primitive objects in a simulation
environment. To evaluate the performance of the proposed
approach, we performed two extensive sets of experiments in packed objects and a pile of objects scenarios. Experimental results
showed that the proposed method worked very well in both scenarios and outperformed the recent state-of-the-art approach.
rained models and source code for the results reproducibility purpose are publicly available.

![Alt Text](images/PushGrasp.gif)

## Installation
### Method 1 (Ubuntu 18.04)
- Python 3.6
- torch 1.2.0
- torchvision 0.4.0
- matplotlib 3.3.4
- numpy 1.19.5
- opencv-python 4.5.4.60
- tensorboardX 2.4.1
- trimesh 3.9.35
- scikit-image 0.17.2
- scipy 1.5.4
- CoppeliaSim_Edu_V4_1_0_Ubuntu18_04

### Method 2 (Ubuntu 20.04)
- Python 3.8
- torch 1.10.1
- torchvision 0.11.2
- matplotlib 3.5.1
- numpy 1.22.1
- opencv-python 4.5.5.62
- tensorboardX 2.4.1
- trimesh 3.9.42
- scikit-image 0.19.1
- scipy 1.7.3
- CoppeliaSim_Edu_V4_2_0_Ubuntu20_04

### Method 3 Singularity Container
We have made a container publicly available which is useful to be used in High Performance Computing (HPC) clusters

singularity .sif image file can be downloaded from [.sif](https://drive.google.com/drive/folders/1KaAugjPULuasGZQbJVwtFDrTRwi36jLD?usp=sharing) 
It contains Ubnutu 20.04 image and all the required packages to run the model training and testing. 

## Train
```
# Grasp Goal agnostic
python main.py --stage grasp_only --num_obj 5 --goal_conditioned --goal_obj_idx 4 --experience_replay --explore_rate_decay --save_visualizations
```

```
# Grasp Goal conditioned
python main.py --stage grasp_only --num_obj 5 --grasp_goal_conditioned --goal_conditioned --goal_obj_idx 4 --experience_replay --explore_rate_decay --save_visualizations --grasp_explore --load_explore_snapshot --explore_snapshot_file '.pth file from the previous training'
```

```
# Push training
python main.py --stage push_only --alternating_training --grasp_goal_conditioned --goal_conditioned --goal_obj_idx 4 --experience_replay --explore_rate_decay --save_visualizations  --load_snapshot --snapshot_file '.pth file from the previous training' 
```

```
# Alternate to grasp training
python main.py --stage push_only --alternating_training --grasp_goal_conditioned --goal_conditioned --goal_obj_idx 4 --experience_replay --explore_rate_decay --save_visualizations  --load_snapshot --snapshot_file '.pth file from the previous training' 
```

```
# Alternate to push training
python main.py --stage push_only --grasp_reward_threshold 1.8 --grasp_goal_conditioned --goal_conditioned --goal_obj_idx 4 --experience_replay --explore_rate_decay --save_visualizations  --load_snapshot --snapshot_file '.pth file from the previous training' 
```
## Test
```
python main.py --stage push_grasp --num_obj 10 --experience_replay --explore_rate_decay --is_testing --test_preset_cases --test_preset_file 'simulation/test-cases/test-10-obj-06.txt' --load_snapshot --snapshot_file '.pth trained model' --save_visualizations --grasp_goal_conditioned --goal_conditioned --goal_obj_idx 1 
```
## Acknowledgment

We made use of the code made by https://github.com/xukechun/Efficient_goal-oriented_push-grasping_synergy 
