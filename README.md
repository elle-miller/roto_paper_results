# roto_paper_results
This repo contains the training logs, checkpoints, and plots for "Enhancing Tactile-based RL for Robotic Control", with instructions for how to playback the agents

## Reproducing the paper results

First, find optimal hyperparameters within a given budget. Second, run optimal hyperparameters for each environment x ssl combo for 5 seeds.

### Sweeping
Same setup as `train.py`, but with an additional `--study` name argument.
```
python sweep.py --task Find --num_envs 4196 --headless --seed 1234 --agent_cfg rl_only_pt --study find_rl_only_pt
python sweep.py --task Find --num_envs 4196 --headless --seed 1234 --agent_cfg full_recon --study find_full_recon
python sweep.py --task Find --num_envs 4196 --headless --seed 1234 --agent_cfg tac_recon --study find_tac_recon
python sweep.py --task Find --num_envs 4196 --headless --seed 1234 --agent_cfg forward_dynamics --study find_forward_dynamics
python sweep.py --task Find --num_envs 4196 --headless --seed 1234 --agent_cfg tac_dynamics --study find_tac_dynamics

python sweep.py --task Bounce --num_envs 4196 --headless --seed 1234 --agent_cfg rl_only_pt --study bounce_rl_only_pt
python sweep.py --task Bounce --num_envs 4196 --headless --seed 1234 --agent_cfg full_recon --study bounce_full_recon
python sweep.py --task Bounce --num_envs 4196 --headless --seed 1234 --agent_cfg tac_recon --study bounce_tac_recon
python sweep.py --task Bounce --num_envs 4196 --headless --seed 1234 --agent_cfg forward_dynamics --study bounce_forward_dynamics
python sweep.py --task Bounce --num_envs 4196 --headless --seed 1234 --agent_cfg tac_dynamics --study bounce_tac_dynamics

python sweep.py --task Baoding --num_envs 4196 --headless --seed 1234 --agent_cfg rl_only_pt --study baoding_rl_only_pt
python sweep.py --task Baoding --num_envs 4196 --headless --seed 1234 --agent_cfg full_recon --study baoding_full_recon
python sweep.py --task Baoding --num_envs 4196 --headless --seed 1234 --agent_cfg tac_recon --study baoding_tac_recon
python sweep.py --task Baoding --num_envs 4196 --headless --seed 1234 --agent_cfg forward_dynamics --study baoding_forward_dynamics
python sweep.py --task Baoding --num_envs 4196 --headless --seed 1234 --agent_cfg tac_dynamics --study baoding_tac_dynamics
```

